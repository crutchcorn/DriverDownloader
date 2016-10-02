from setuptools import setup, find_packages

setup(
    name='DriverDownloader',
    version="0.1",
    description="A download manager pointed towards downloading drivers.",
    url='https://github.com/crutchcorn/DriverDownloader',
    author="Corbin Crutchley",
    author_email='crutchcorn@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
        [driverdl.plugin]
        lenovoHandle=plugins.lenovo:handleExt
        lenovoExt=plugins.lenovo:getExt
        driverpackHandle=plugins.driverpacksolution:handleExt
        driverpackExt=plugins.driverpacksolution:getExt
    """,
)