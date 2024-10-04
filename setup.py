
from setuptools import find_packages, setup
setup(
    name='pythonutilityliblz',
    packages=find_packages(include=['pythonutilityliblz/pathoperation', 'pythonutilityliblz/processcsv']),
    version='0.1.0',
    description='Python untility library',
    author='Lizzie Zhou',
    license='lizziedev team',
    install_requires=['selinux', 'six'],
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest'],
    # test_suite='tests',
)