import boto3
import os

# AWS credentials and S3 bucket details
AWS_ACCESS_KEY_ID = 'your_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'
AWS_BUCKET_NAME = 'your_bucket_name'

# Function to upload files from a folder to S3 and delete them from the local folder
def upload_and_delete_files(folder_path):
    # Connect to S3
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp4'):
            # Get the full file path
            file_path = os.path.join(folder_path, filename)

            # Upload file to S3
            s3.upload_file(file_path, AWS_BUCKET_NAME, filename)
            print(f'File {filename} uploaded to S3')

            # Delete the file from the local folder
            os.remove(file_path)
            print(f'File {filename} deleted from local folder')

# Path to the folder containing videos
folder_path = '/toBeUploaded'

while True:
  # Upload videos from the folder to S3 and delete them from the local folder
  upload_and_delete_files(folder_path)
