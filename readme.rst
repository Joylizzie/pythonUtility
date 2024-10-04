    
    .. inclusion-marker-do-not-remove
    
    *************
    pythonUtility 
    *************

    These are utility code for a project, including database connection, csv file processing, path creation.

    .. note.. More functions will be added

    How to build a Python library
    #############################

    First time
    ##########

    Open a command line, in command line, type::

        cd to path/want to save
        python3 -m venv venv
        source venv/bin/activate
        pip install wheel
        pip install setuptools
        pip install twine
        mkdir pythonutility
        cd pythonutility
        touch __init__.py
        touch myfunction.py # copy some valid function you want to be included in the library
        cd ..
        mkdir tests
        touch __init__.py
        pip install pytest
        pip install pytest-runner
        touch test_myfunctions.py

    In setup.py, input(quotation marks not included)::

        from setuptools import find_packages, setup
        setup(
            name='pythonutilitylib',
            packages=find_packages(include=['pythonUtility']),
            version='0.1.0',
            description='Python utility library',
            author='Lizzie',
            license='lizziedev team',
            install_requires=[],
            setup_requires=['pytest-runner'],
            tests_require=['pytest'],
            test_suite='tests',
        )
    
    In command line, type::

        python setup.py pytest
        python setup.py bdist_wheel # wheel file is stored in the 'dist' folder
        pip install /path/to/wheelfile.whl

    Rebuild
    ###############

    In a terminal, type::
        cd to/path/where/the/libary/is, my case: /Users/lizziez/projects/pythonUtility
        ls -la 
        source venv/bin/activate
        pip install wheel
        pip install setuptools
        pip install twine
        python setup.py pytest
        python setup.py bdist_wheel
        pip install /Users/lizziez/projects/pythonUtility/dist/pythonUtilitylib-0.1.0-py3-none-any.whl 

    How to install
    ##############

        If the libary is in local computer::
            pip install /path/to/wheelfile.whl
        
        If published in Pypy repository::
            Importing in your new project
            import pythonUtility
            from pythonUtilitylib import [desired functions]


    The functions in this lib including:
    ####################################
            #.redshift connection
            #.db utility
            #.csv file utility(read, write)
            #.s3 upload, download
            #.file utility
            #.datetime


