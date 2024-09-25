
    <h1>How to build a Python library<h2>

    <h2>First time<h2>

    Open a command line, in command line, type:

    cd to path/want to save
    python3 -m venv venv
    source venv/bin/activate
    pip install wheel
    pip install setuptools
    pip install twine #  pip install [-r requirements.txt] --use-deprecated=legacy-resolver
    touch setup.py
    mkdir pythonUtility
    cd pythonUtility
    touch __init__.py
    touch myfunction.py # copy some valid function you want to be included in the library
    cd ..
    mkdir test_myfunctions.py
    touch __init__.py
    pip install pytest
    pip install pytest-runner
    touch test_myfunctions.py
    touch setup.py<p>

    <p># in setup.py, input(quotation marks not included):<p>

    <p>"""
    from setuptools import find_packages, setup
    setup(
        name='mypythonlib',
        packages=find_packages(include=['mypythonlib']),
        version='0.1.0',
        description='My first Python library',
        author='Lizzie Zhou',
        license='lizziedev team',
        install_requires=[],
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        test_suite='tests',
    )
    """<p>

    python setup.py pytest
    python setup.py bdist_wheel # wheel file is stored in the 'dist' folder
    pip install /path/to/wheelfile.whl

    <h1>Rebuild<h1>

    cd to/path/where/the/libary/is, my case: /Users/lizziez/projects/pythonUtility
    ls -la 
    source venv/bin/activate
    pip install wheel
    pip install setuptools
    pip install twine
    python setup.py pytest
    python setup.py bdist_wheel
    pip install /Users/lizziez/projects/pythonUtility/dist/pythonUtilitylib-0.1.0-py3-none-any.whl 

    <h2> The functions in this lib including:
    redshift connection
    db utility
    csv file utility(read, write)
    s3 upload, download
    googlesheet reading
    file utility
    datetime

    <h2> Importing in your new project<h2>
    import mypythonlib
    from mypythonlib import myfunctions