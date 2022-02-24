import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wport-OCTOMANY",
    version="0.0.1",
    author="Maxime Beauchamp",
    author_email="cybersecmax@outlook.com",
    description="Common ports information fetcher for pentesting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Octomany/wport",
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