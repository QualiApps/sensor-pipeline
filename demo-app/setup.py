"""
A demo temp checker
-------------

It app uploads rules and handlers to the Sensor Pipeline.
And checks an input stream

"""
from setuptools import setup

setup(
    name="smartapp",
    version="0.1",
    license="MIT",
    author="Yury Kavaliou",
    author_email="qualiapps@gmail.com",
    description="It controlls a temp of smart teapot",
    long_description=__doc__,
    packages=["smartapp"],
    zip_safe=False,
    platforms="any",
    install_requires=[
        "requests>=2.7.0"
    ],
    entry_points={
        'console_scripts':
            ['smartapp = smartapp.main:run']
    },
    keywords=['handlers', 'rules', "Apache Nifi", "stream", "flow data"],
)
