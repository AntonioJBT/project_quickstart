'''
Utilities for project_quickstart.py

:Author: Antonio J Berlanga-Taylor
:Date:


Boilerplate tools for quickstarting a data analysis project:

https://github.com/AntonioJBT/project_quickstart

'''

# Get locations of source code
    # os.path.join note: a subsequent argument with an '/' discards anything
    # before it
    # For function to search path see: 
    # http://stackoverflow.com/questions/4519127/setuptools-package-data-folder-location
    # __init__.py has the getDir() function
# MANIFEST.in file instructs the project_quickstart/templates folder to be included in installation

import os

prog_version = '0.2'

_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..'))
def getDir(path):
    ''' Get the absolute path for the package directory '''
    return os.path.join(_ROOT, f'project_quickstart-{prog_version}', path)

#print(getDir('templates'))


# Load arguments for docopt from an INI file 
# Modified from:
# https://github.com/docopt/docopt/blob/master/examples/config_file_example.py
# See also (which includes reading from json):
# http://stackoverflow.com/questions/8884188/how-to-read-and-write-ini-file-with-python
# https://wiki.python.org/moin/ConfigParserExamples
# CGAT tools do a better job, using argparser.

def load_ini_config():
    ''' Loads an *.ini file if present in the current directory and prepares it
    for use with docopt'''

    try:  # Python 2
        from ConfigParser import ConfigParser
        from StringIO import StringIO
    except ImportError:  # Python 3
        from configparser import ConfigParser
        from io import StringIO

    import sys
    import os
    import glob

    # By using `allow_no_value=True` we are allowed to
    # write `--force` instead of `--force=true` below.
    config = ConfigParser(allow_no_value=True)

    # Check if there's an INI file present:
    if len(glob.glob('*.ini')) == 0:
        return 'No configuration file (e.g. xxx.ini) present in the directory'
    elif len(glob.glob('*.ini')) > 1:
        return ''' More than one configuration file present
        (several files ending in ".ini" files") present in the directory')
        '''
    else:
        INI_file = glob.glob('*.ini')

    # ConfigParser requires a file-like object and
    # no leading whitespace.
    with open(INI_file, 'r') as f:
        config_file = f.StringIO('\n'.join(INI_file.split()))
        config_file = config.read_file(config_file)
        config_file = config.read(config_file)

        for section, key, value in config_file:
            print(section, key, value)

    # ConfigParsers sets keys which have no value
    # (like `--force`) to `None`. Thus we
    # need to substitute all `None` with `True` for docopt:
    return dict((key, True if value is None else value)
                for key, value in config_file)


    ini_config = load_ini_config()

    # Arguments take priority over INI, INI takes priority over JSON:
    result = arguments, ini_config

    from pprint import pprint

    print('\nINI config:')
    pprint(ini_config)
    print('\nResult:')

    pprint(result)
    
    return(result)

