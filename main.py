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
from os import rename
from wget import download
from re import sub
from uniprez import getExtensions

arguments = docopt(__doc__, version='DriverDownloader 0.0.1')

group = "driverdl.plugin"
extensions = getExtensions(group)
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
