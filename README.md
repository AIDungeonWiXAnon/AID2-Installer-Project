# AI Dungeon 2: Clover Edition Installer (.exe)

This repo's main focus is providing an easy-to-use, intuitive, and comprehensive installer for AI Dungeon 2: Clover Edition. It will handle install of the Github repo, CUDA, cuDNN, Python, and all related packages, plus any configuration options that need to be made (such as downloading the torrent.)

Currently the system is manually updated by me to whatever the latest release of Clover Edition is when I have the time, but in the future, it will be an automated web-based installer that will automatically pull the latest version for you.

It does, however, currently automatically pull the latest versions of Python 3.7, CUDA, cuDNN, and their related packages (such as transformers).

## Getting Started

These instructions will get you a copy of the project up so that you can fiddle around with it. If you'd rather just download an exe and install the game, [see deployment](https://github.com/AIDungeonWiXAnon/AID2-Installer-Project#deployment) for notes on that.

### Prerequisites

What things you need to install the software and how to install them:

```
Visual Studio (VS) - Download the community edition and register it to an MS account.
WiX v3 - Download the VS extension for your version of VS
```

### Installing

A step by step series of instructions that'll tell you how to get a development env running:

Install Visual Studio

```
Launch the Visual Studio Installer
Update Visual Studio Community to the latest version for that edition (2019 16.4.2 recommended)
```

Add the WiX extension

```
Just run the downloaded extension file and VS Installer should take care of the rest for you
```

And import the .sln project

```
Download and extract this Github repo somewhere you'd like
Select "Open a project" in VS and select the .sln
```

Congrats, that's it! From there you should be able to compile the project.  
If you run into any issues, it's likely references being in new locations: make sure to update the references to WixUIExtension & WixUtilExtension for the .msi installer, and WixBalExtension & WixUtilExtension for the .exe bootstrapper.

## Deployment

In the near future, you'll be able to check the [releases tab for this repo](https://github.com/AIDungeonWiXAnon/AID2-Installer-Project/releases) and you'll have a nice, fancy download button to click that'll give you the latest version of the installer. For now, though, you can get the installer here:
* [64-bit .exe installer for Clover Edition c74ba69](https://mega.nz/#!G5lTxIyD!DFb6LBiwtVzxCfOwEgTPyG0W8B-oRXWx-yxA_aKOjak)

## Built With

* [Visual Studio](https://visualstudio.microsoft.com/) - The IDE used for source code development
* [WiX v3](https://wixtoolset.org/) - The toolset used to create the .exe bootstrapper and .msi installer
* [Anaconda](https://www.anaconda.com/) - Used to download and install CUDA, cuDNN, Python, and related Python packages
* [CUDA](https://developer.nvidia.com/cuda-zone) - API used for giving the AI something useable to compute with
* [cuDNN](https://developer.nvidia.com/cudnn) - Library used to improve GPU-based AI computation performance
* [Python v3.7](https://www.python.org/) - Language used to tie all of the various systems of the AI together

## Contributing

Feel free to submit issues, create forks, make pull requests, and help out with whatever you like; I work on this in my increasingly sparse spare time and extra codemonkeys (especially if they know XML) are always appreciated.  
Localization files (.xwl) would be especially nice for anons out there who don't speak the English. [See WiX documentation for how to make one of those.](https://wixtoolset.org/documentation/manual/v3/howtos/ui_and_localization/build_a_localized_version.html)

## Versioning

Currently I'm leaving versioning at 0.0.0.0 until out of beta (probably once a web-based installer is finished, so that I don't have to maintain the versioning manually).  
The application GUID, however, will be edited for each version (every commit will get a generated GUID) and upgrade code GUIDs will be changed per-branch (local-based and web-based, for instance) for the installer/bootstrapper themselves.

## Authors

* **Cloveranon** - *Dev of the Clover Edition that this installer uses* - [AID2 Clover Edition](https://github.com/cloveranon/Clover-Edition)
* **Friendly /vp/oreon** - *Me, dev of this installer and its related bootstrapper*

## Acknowledgments

* The /vp/ anon who pointed me to this game in the first place, and for directing me to the /v/ (now /vg/) threads

