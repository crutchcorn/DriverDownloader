from pkg_resources import iter_entry_points
from os import rename
from wget import download

available_methods = []
for entry_point in iter_entry_points(group='driverdl.plugin', name=None):
    available_methods.append(entry_point.load())

drivers = available_methods[0]()

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