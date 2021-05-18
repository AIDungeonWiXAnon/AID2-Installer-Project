# AI Dungeon 2: Clover Edition Installer (.exe)

This repo's main focus is providing an easy-to-use, intuitive, and comprehensive installer for [AI Dungeon 2: Clover Edition](https://github.com/cloveranon/Clover-Edition). It will handle install of the Github repo, CUDA, cuDNN, Python, and all related packages, plus any configuration options that need to be made (such as downloading the torrent.)

Currently the system is a web-based installer that will pull the latest versions of Clover Edition, Git, Python 3.8, CUDA, cuDNN, and their related packages (such as transformers).

## Getting Started

These instructions will get you a copy of the project up so that you can fiddle around with it. If you'd rather just download an exe and install the game, then please check the [releases tab for this repo](https://github.com/AIDungeonWiXAnon/AID2-Installer-Project/releases/latest) for a nice, fancy download button to click that'll give you the latest version of the installer!

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

## Built With

* [Visual Studio](https://visualstudio.microsoft.com/) - The IDE used for source code development
* [Git](https://git-scm.com/) - The version control software used for pulling the latest version of Clover Edition
* [WiX v3](https://wixtoolset.org/) - The toolset used to create the .exe bootstrapper and .msi installer
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html) - Used to download and install CUDA, cuDNN, Python, and related Python packages
* [CUDA](https://developer.nvidia.com/cuda-zone) - API used for giving the AI something useable to compute with
* [cuDNN](https://developer.nvidia.com/cudnn) - Library used to improve GPU-based AI computation performance
* [Python v3.7](https://www.python.org/) - Language used to tie all of the various systems of the AI together

## Contributing

Feel free to submit issues, create forks, make pull requests, and help out with whatever you like; I work on this in my increasingly sparse spare time and extra codemonkeys (especially if they know XML) are always appreciated.  
Localization files (.xwl) would be especially nice for anons out there who don't speak the English. [See WiX documentation for how to make one of those.](https://wixtoolset.org/documentation/manual/v3/howtos/ui_and_localization/build_a_localized_version.html)

## Versioning

Currently versions are based on an X.Y versioning, where X is the major release version and Y is the patch for that version.
Additionally, the application GUID is edited for each noteable (i.e. released) version of the installer and upgrade code GUIDs will be changed per-branch (local-based and web-based, for instance) for the installer/bootstrapper themselves.

## Authors

* **Cloveranon** - *Author of Clover Edition, the game that this installer configures & installs* - [AID2 Clover Edition](https://github.com/cloveranon/Clover-Edition)
* **Friendly /vp/oreon** - *Me, author of this installer and its related bootstrapper*

## Acknowledgments

* The /vp/ anon who pointed me to this game in the first place, and for directing me to the /v/ (now /vg/) threads

