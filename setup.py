#################

# https://python-packaging.readthedocs.io/en/latest/minimal.html
# For a fuller example see: https://github.com/CGATOxford/UMI-tools/blob/master/setup.py
# Or: https://github.com/CGATOxford/cgat/blob/master/setup.py

# TO DO: update with further options such as include README.rst and others when ready

# TO DO: to add tests see https://python-packaging.readthedocs.io/en/latest/testing.html

# See also this example: https://github.com/pypa/sampleproject/blob/master/setup.py

# This may be a better way, based on Py3: http://www.diveintopython3.net/packaging.html

# To package, check setup.py first:
# python setup.py check
# Then create a source distribution:
# python setup.py sdist
# which will create a dist/ directory and a compressed file inside with your package.
# For uploading to PyPi see http://www.diveintopython3.net/packaging.html#pypi

#################

from distutils.core import setup
#from setuptools import setup # Py2


setup(name = 'project_quickstart',
      packages = ['project_quickstart'],
#      install_requires=[
#            'cgat',
#            'CGATPipelines',
#      ],
      version = '0.2',
      url = 'https://github.com/AntonioJBT/project_quickstart/',
      download_url = 'https://github.com/AntonioJBT/project_quickstart',
      author = 'Antonio J Berlanga-Taylor',
      author_email = 'a.berlanga at imperial.ac.uk',
      license = 'GPL-3.0',
      classifiers = ["Programming Language :: Python", # see https://pypi.python.org/pypi?:action=list_classifiers
                     "Programming Language :: Python :: 3",
                     "Development Status :: 2- Pre-Alpha",
                     "Environment :: Other Environment",
                     "Intended Audience :: Science/Research",
                     "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
                     "Operating System :: OS Independent",
                     "Topic :: Utilities",
                     "Topic :: Scientific/Engineering :: Bio-Informatics"
                    ],
      description = 'Data science Python project quickstart',
      keywords = ['data science', ''],
      long_description = 'Utility tool to create skeleton structure and file templates for Python based data analysis project'
     )
#################


