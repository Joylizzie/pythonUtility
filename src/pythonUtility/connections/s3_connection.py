from os import listdir, remove
from os.path import isfile, join, basename
import logging
from pathlib import Path, PurePath
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

# Connect to s3 with credetials either saved in environment or from credential system
s3_client = boto3.client("s3")

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    If S3 object_name was not specified, use file_name

    :param file_name: File to upload
    :param bucket: Bucket to upload to s3
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    if object_name is None:
        object_name = Path.resolve().parent(file_name)

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_recusive(local_dir, s3_bucket, s3_dir):
    """Upload local_dir files recusively to s3_dir under s3 bucket with the same
    folder names and file names in s3

    :param local_dir: local directory where files need to be uploaded
    :type local_dir: string
    :param s3_bucket: the files need to be in s3 bucket
    :type s3_bucket: string
    :param s3_dir: object name under s3 bucket
    :type s3_dir: string
    :return: True or False
    :rtype: Boolean
    """
    for f in Path.iterdir(local_dir):
        try:
            if f.startswith("."):
                continue
            if Path.is_file(PurePath.joinpath((local_dir,f))):
                upload_file(local_dir + f, s3_bucket, s3_dir + f)
                logging.info(f"{f} uploaded")
                remove(local_dir + f) # remove the file after uploaded
                logging.info(f'file {f} is removed after uploded to s3')

            else:
                upload_recusive(local_dir + f"{f}/", s3_bucket, s3_dir + f"{f}/")
        except ClientError as e:
            logging.error(e)
            return False
    return True