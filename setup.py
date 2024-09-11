
from setuptools import find_packages, setup
setup(
    name='pythonUtilitylib',
    packages=find_packages(include=['pythonUtilitylib']),
    version='0.1.0',
    description='Python untility library',
    author='Lizzie Zhou',
    license='lizziedev team',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)