    
.. inclusion-marker-do-not-remove

*************
pythonUtility 
*************

These are utility modules for a project written in Python programming language , including database connection, csv file processing, path creation.

.. note.. More functions will be added

How to build a Python library
#############################

First time
##########

Open a command line, in command line, type::

    cd to path/want to save
    python3 -m venv venv # create an virtual environment
    source venv/bin/activate # activate the virtual environment
    pip install --upgrade  wheel # for source build
    pip install --upgrade setuptools[core]
    pip install --upgrade build
    pip install --upgrade twine# package distribution
    mkdir src # use src-layout `Link text <https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout>`_
    mkdir pythonUtility
    cd pythonUtility
    touch __init__.py
    # adding some valid functions to be included in the library
    cd ..
    mkdir tests
    touch __init__.py
    touch function_test.py # using unittest to test all the functions added in pythonUtility

In project root folder, add file pyproject.toml for building configuration 

.. important::
    .. _src-layout: https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout
    Using src-layout, Setuptools will automatically scan the project directory looking for these layouts 
    and try to guess the correct values for the packages and py_modules configuration.

Now you can build the package. In command line, type::
    python3 -m build

In project root folder, two new folder 'build' and 'dist' generatted, 
for source build and distribution respectively. 'pythonUtility.egg-info' in src folder 


Development mode
----------------

``setuptools`` allows you to install a package without copying any files
to your interpreter directory (e.g. the ``site-packages`` directory).
This allows you to modify your source code and have the changes take
effect without you having to rebuild and reinstall.
Here's how to do it::

    pip install --editable .

How to install
##############

    If the libary is in local computer::
        pip install /path/to/wheelfile.whl
    
    If published in Pypy repository::
        Importing in your new project
        import pythonUtility
        from pythonUtilitylib import [desired functions]