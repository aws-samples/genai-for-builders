# Temporary preprocess step (to be changed with new dataset)
import boto3
from sagemaker.s3_utils import parse_s3_url
import subprocess

def preprocess(evaluation_data_path, output_data_path):

    # This is a very simple example, you can add your own data processing code here

    s3 = boto3.client("s3")

    bucket, object_key = parse_s3_url(evaluation_data_path)
    s3.download_file(bucket, object_key, "dataset.jsonl")

    # Some preprocessing
    output_processed_evaluation_data_path = output_data_path + "/processed-dataset.jsonl"
    s3.upload_file("dataset.jsonl", *parse_s3_url(output_processed_evaluation_data_path))

    return {"output_data_path": output_data_path, "output_dataset_path": output_processed_evaluation_data_path}
