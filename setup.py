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
        lenovoHandle=plugins.lenovo:handleExt
        lenovoExt=plugins.lenovo:getExt
        driverpackHandle=plugins.driverpacksolution:handleExt
        driverpackExt=plugins.driverpacksolution:getExt
    """,
)