#!/usr/bin/python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages
import sys
import os
import os.path as path


os.chdir(path.realpath(path.dirname(__file__)))
sys.path.insert(1, 'src')
from gerbmerge.gerbmerge import VERSION_MAJOR, VERSION_MINOR

setup(
    name             = 'gerbmerge',
    version          = "%s.%s" % (VERSION_MAJOR, VERSION_MINOR),
    author           = 'Rugged Circuits LLC',
    author_email     = 'support@ruggedcircuits.com',
    description      = 'Merge multiple Gerber/Excellon files',
    long_description = \
r"""GerbMerge is a program that combines several Gerber
(i.e., RS274-X) and Excellon files into a single set
of files. This program is useful for combining multiple
printed circuit board layout files into a single job.

To run the program, invoke the Python interpreter on the
gerbmerge.py file. On Windows, if you installed GerbMerge in
C:/Python24, for example, open a command window (DOS box)
and type:
    C:/Python24/gerbmerge.bat

For more details on installation or running GerbMerge, see the
URL below.
""",
    url              = 'https://github.com/MLAB-project/gerbmerge',
    
    packages    = find_packages("src"),
    package_dir = {'': 'src'},
    provides    = ['gerbmerge'],
    keywords = ['gerber', 'kicad'],
    license     = 'Lesser General Public License v3',
    download_url = 'https://github.com/MLAB-project/MLAB-I2c-modules/archive/0.3.tar.gz',
        
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: Czech',
        # 'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    scripts=['bin/gerbmerge', ]
)

