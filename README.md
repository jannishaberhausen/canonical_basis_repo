# CANONICAL_BASIS_REPO

This repo is a collection of useful/convinient files for a quick setup of a new device.


## Gnome Extensions

- [system-monitor](https://extensions.gnome.org/extension/3010/system-monitor-next/): display system information in GNOME Shell status bar, such as CPU and memory usage, and network rates

- [workspace-matrix](https://extensions.gnome.org/extension/1485/workspace-matrix/): arrange workspaces in a two dimensional grid with workspace thumbnails.


## Terminal Customization

### Color Palette

Use [pywal](https://pypi.org/project/pywal/) to customize your terminal based on your desktop wallpaper.
Install pywal:

```pip3 install pywal```

then run:

```wal -i <path_to_wallpaper_file>```

to make the change persistent after closing and opening a terminal add the following line to your ```.bashrc``` script:

```(cat ~/.cache/wal/sequences &)```

to make the changes also persisent after a reboot open "Startup Applications Preferences" and add the new command:

```wal -R```

### Show git Branch

Add the ```.bash_profile``` file to your root directoy, here:

```~/.bash_profile```

and then source it in you ```.bashrc``` file:

```source ~/.bash_profile```



