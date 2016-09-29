#!/usr/bin/env python3
"""DriverDownloader - Remember spending the afternoon downloading those EXEs? Neither do I

Usage:
  DriverDownloader <url>

Options:
  -h --help                  Show this screen.
  -v --version               Show version.
  <url>                      Pick the URL to download the drivers from.

"""
from docopt import docopt
from pkg_resources import iter_entry_points
from os import rename
from wget import download
from re import sub

arguments = docopt(__doc__, version='DriverDownloader 0.0.1')

##### THE FOLLOWING IS CODE IN AN UPCOMING PROJECT. THIS WILL EVENTUALLY BE MOVED INTO A LIBRARY!
extensions = {}
handleExtPlugin = {}
group = "driverdl.plugin"
for entry_point in iter_entry_points(group=group, name=None):
    if entry_point.attrs[0] == "handleExt":
        if extensions:
            for extension in extensions:
                if extensions[extension] == entry_point.module_name: # if extensions["mp3"] == "plugins.lenovo "(this assumes this is second)
                    extensions[extension] = entry_point.load()
        handleExtPlugin[entry_point.module_name] = entry_point.load() # handleExtPlugin["plugins.lenovo"] (this assumes this is first)
    elif entry_point.attrs[0] == "getExt":
        if handleExtPlugin.get(entry_point.module_name, None): # handleExtPlugin["plugins.lenovo"] (this assumes this is second)
            moduleLoad = handleExtPlugin[entry_point.module_name]
        else:
            moduleLoad = entry_point.module_name # This assumed this is first. It allows the extensions to become module_name to be handled by handleExt code
        for extension in entry_point.load()(): # entry_point() would return list of extentions handleExt could handle
            extensions[extension] = moduleLoad # extensions["mp3"]
    elif not entry_point.attrs[0]:
        print("But nobody came")
###### WHEN THAT IS DONE, PLEASE REMOVE THIS CODE AND REPLACE IT WITH THE LIBRARY


urlExt = sub(r'http.*//', '', arguments["<url>"]) # Removes http/https
urlExt = urlExt.split('/')[0].split('.')[-2] # Gets second to last string before /, split by . (support.lenovo.com => lenovo)
drivers = extensions[urlExt](arguments["<url>"]) # it lenovo.com will run lenovo, but www.lenovo.com will run www This should be fixed

for driver in drivers:
    # Download files
    try:
        file_name = download(driver['URL'])
    except: # Error handling needs better implamentation
        pass

    # Rename Downloaded Files
    try:
        rename(file_name, driver['Name'])
    except FileExistsError: # Add option to delete or rename existing file
        rename(file_name, driver['Name']+"ALT") # Should continue to add "ALT" until no longer possible
    except NameError:
        pass

# http://docs.pylonsproject.org/projects/pylons-webframework/en/latest/advanced_pylons/entry_points_and_plugins.html