import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wport",
    version="0.0.3",
    author="Maxime Beauchamp",
    author_email="<cybersecmax@outlook.com>",
    description="Common ports information fetcher for pentesting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["wport"],
    url="https://github.com/Octomany/wport",
    keywords=['pentesting', 'ports','services'],
    package_data={
      'myapp': ['data/*.json'],
    },
    project_urls={
        "Bug Tracker": "https://github.com/Octomany/wport/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)