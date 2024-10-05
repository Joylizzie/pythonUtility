
import argparse

def get_args(cmd_args=None):
    """Configure commandline, where to get souce data, qeury dw or existing csv files;
    where to save output files, prod or statging
    :return: namespace

    :param cmd_args: a string, defaults to None
    :type cmd_args: string, optional
    :raises: 
    :return: The value for command line arguments
    :rtype: string   
    """

    commandline_parser = argparse.ArgumentParser(\
        description='Input different arguments in commandline to meet different requirements like use cached data/refresh from database etc.')
    # If it pulls new data from dw. It always queries new data from dw when it runs on Cloud based platform
    commandline_parser.add_argument("--use_cached_data", action='store_true',\
        help="Use stored data, don't refresh from data warehouse")
    commandline_parser.add_argument("--use_cached_test_data", action='store_true', \
        help="Use stored test data")    
    # If it needs to upload results to Cloud storage. It aLways uploads results to Could storage when it runs on Cloud based platform
    commandline_parser.add_argument("--no_uploading_to_cloud", action='store_true',\
        help="When in testing stage, don't upload results to Cloud")
    commandline_parser.add_argument("--uploading_to_cloud", action='store_true',\
        help="Run Automated_Amendments")
    if cmd_args:
        return commandline_parser.parse_args(cmd_args)
    return commandline_parser.parse_args()