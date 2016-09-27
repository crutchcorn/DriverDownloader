from setuptools import setup, find_packages

setup(
    name='DriverDownloader',
    version="0.0.1",
    description="URL parsing plugins for Driver Downloader",
    author="Corbin Crutchley",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["DriverDownloader>=0.0.1"],
    entry_points="""
        [driverdl.plugin]
        lenovo=plugins.lenovo:getDriverList
    """,
)