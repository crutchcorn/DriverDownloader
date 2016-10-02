# Driver Downloader

Hate downloading driver files one by one from an OEM website when they don't supply a driverpack? Me too!
That's why I made a pluginable program to handle all that wonderful downloading for you.

## Installation
```bash
pip install requirements.txt
python setup.py install
```

## Usage
THIS SECTION IS TO COME. THIS REPOSITORY IS NOT READY YET - COME BACK LATER
Usage:
   <url>

Options:
* `DriverDownloader -h` or `DriverDownloader --help`    - Show program help
* `DriverDownloader -v` or `DriverDownloader --version` - Show version.
* `DriverDownloader <url>`                              - Pick the URL to download the drivers from.
	* *EG: DriverDownloader http://lenovo.com/driverpath.html*

## Pluginability
We implament a library that I created called [Uniprez](https://github.com/crutchcorn/Uniprez). You may follow the direction in that repository to package that plugins that you create. The only standardization we have currently is how the program returns data. We require you to return a list of dictionaries with at least one key per item:
* `URL` allows us to find the URL of the file to download. This is a required key
* `Name` allows us to know what to name the file after downloading. This is an optional key