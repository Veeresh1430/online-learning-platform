import boto3
from botocore.exceptions import NoCredentialsError

def upload_video_to_s3(file_name, bucket, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket, object_name)
        print(f"Video uploaded successfully: {file_name}")
    except NoCredentialsError:
        print("Credentials not available")

def generate_cloudfront_url(object_name):
    cloudfront_domain = 'dxxxxxxxxxxxxx.cloudfront.net'
    url = f"https://{cloudfront_domain}/{object_name}"
    return url

# Example Usage
upload_video_to_s3('my_video.mp4', 'my_bucket')
video_url = generate_cloudfront_url('my_video.mp4')
print(video_url)
