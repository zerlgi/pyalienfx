# How To Install #

How to use :
  * install libusb 1.0 : http://www.libusb.org/
  * extract the pyAlienFX-v0.2a.tar.gz file to any folder
  * enter the folder pyalienfx/
  * execute : sudo ./install.py
  * to launch the Configurator : launch pyAlienFX (Alt+F2 pyAlienFX, or in the Unity Dash or in a terminal)
  * To have the Indicator please add the pyAlienFX\_Launcher.sh to the list of Startup software (any help on how to automatize this would be welcome !)

How to DEB :
  * Double click on the deb file !
  * Or "sudo dpkg -i package.deb"

How to Arch Linux:
  * Easy way (using yaourt package manager):
    * yaourt -S pyalienfx

  * Using the Arch Build System:
    * Download the tarball from: https://aur.archlinux.org/packages/pyalienfx/
    * Extract the tarball and cd on directory
    * "makepkg -s"
    * "sudo pacman -U {package}.tar.xz"

Command How To :
  * sudo apt-get update
  * sudo apt-get install libusb-1.0
  * cd
  * cd Download
  * tar zxvf pyAlienFX.tar.gz
  * cd pyalienfx
  * python ./pyAlienFX.py