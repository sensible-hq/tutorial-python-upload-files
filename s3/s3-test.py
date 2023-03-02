import boto3

# create a new Amazon S3 client
s3 = boto3.client('s3')

# store the name of your S3 bucket
bucket_name = 'my-test-bucket-kh'

# create reference to the file location
target_file = '../samples/sample.pdf'

# store the name of the target file in S3
s3_target_file_name = 'sample.pdf'

# upload the file
s3.upload_file(target_file, bucket_name, s3_target_file_name)

# verify that the file was uploaded
response = s3.list_objects(Bucket=bucket_name)
for content in response.get('Contents', []):
    print(content.get('Key'))