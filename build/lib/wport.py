#!/usr/bin/python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Title : What port? *wport*                                                  #
# Just a simple script to help pentesting the most common ports.              #
#                                                                             #
# By : Octomany, AKA Maxime Beauchamp                                         #
# Last update : 02-22-2022                                                    #
#                                                                             #
# Special thanks to Carlos Polop for letting me use his descriptions & links  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import argparse
from colorama import Fore
import re
import json
import textwrap

parser = argparse.ArgumentParser(description='Search for a port number or service name.')

# Set the argument
parser.add_argument('ARG', metavar='Port or Service', help='Default port number OR service name')

# Get the argument
args = parser.parse_args()
Arg = args.ARG

# Error message if port doesn't exist
ErrorNotFound = Fore.RED + "ERROR: port or service name not found." + Fore.WHITE

# Read the dictionary file
f = open('./src/AllPorts.json')
data = json.load(f)
f.close()

Allports = data['Allports']

def PrintResult(rs):
    # Setup the data
    Title = 'WPORT : RESULTS'
    PortNo = Fore.YELLOW + rs['nb'] + Fore.WHITE
    Service = Fore.RED + rs['name'] + Fore.WHITE
    Description = rs['desc']
    Link = Fore.GREEN + rs['link'] + Fore.WHITE
    TopBottom = '-'
    TitlePort = Fore.YELLOW + "PORT" + Fore.WHITE
    TitleName = Fore.RED + "SERVICE NAME" + Fore.WHITE
    TitleLink = Fore.GREEN + "PENTESTING TIPS" + Fore.WHITE
    # Wrap this text.
    wrapper = textwrap.TextWrapper(width=108)
    WrappedDesc = wrapper.wrap(Description)

    # Show the result
    print("")
    print(TopBottom.center(110,'-'))
    print("|" + Title.center(108) + "|")
    print(TopBottom.center(110,'-'))
    print("|" + TitlePort.center(32) + "|" + TitleName.center(33) + "|" + TitleLink.center(71) + "|")
    print("|" + PortNo.center(32) + "|" + Service.center(33) + "|" + Link.center(71) + "|")
    print(TopBottom.center(110,'-'))
    # Print the wrapped description
    for element in WrappedDesc:
        print("|" + element.center(108) + "|")
    
    print(TopBottom.center(110,'-'))

    # print("   DEFAULT PORT NUMBER: " + rs['nb']+"         Service name: "+rs['name'])

    # print("\n" + Fore.YELLOW + rs['name'] + Fore.WHITE)
    # print("Port " + rs['nb']+"\n")
    # print(rs['desc']+"\n")
    # print(Fore.GREEN + "Pentesting tips : " + rs['link'])
    # exit()

def PortNB(PN):
    PN = int(PN)
    if PN >= 6660 and PN <= 7000: # IRC
        SelectedPort = next((item for item in Allports if item['nb'] == '194, 6667, 6660-7000'), ErrorNotFound)
    elif PN >= 1522 and PN <= 1529: # Oracle TNS Listener
        SelectedPort = next((item for item in Allports if item['nb'] == '1521, 1522-1529'), ErrorNotFound)
    elif PN >= 49152 and PN <= 49160: # GlusterFS
        SelectedPort = next((item for item in Allports if item['nb'] == '124007, 24008, 24009, 49152+'), ErrorNotFound)
    else:
        PN = str(PN)
        SelectedPort = next((item for item in Allports if re.search(r'\b'+PN+r'\b', item['nb'])), ErrorNotFound)
    
    if SelectedPort != ErrorNotFound:
        PrintResult(SelectedPort)

    else:
        print(SelectedPort)

def ServiceN(SN):
    #ServiceNames = [i for i, x in enumerate(Allports) if re.search(r'\b'+SN+r'\b', x['name'])]
    SelectedPort = next((item for item in Allports if re.search(r'(?i)\b'+SN+r'\b', item['name'])), ErrorNotFound)
        
    if SelectedPort != ErrorNotFound:
        PrintResult(SelectedPort)
        
    else:
        print(SelectedPort)

if Arg.isnumeric():
    PortNB(Arg)
elif not Arg.isnumeric():
    ServiceN(Arg)
else:
    print(ErrorNotFound)
    exit()