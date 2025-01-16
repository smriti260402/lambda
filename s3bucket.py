import json
import boto3
import base64
from botocore.exceptions import ClientError

# Initialize the S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Extract the file content and metadata from the event
        file_content = event['body']  # Assuming the file content is sent in the body (Base64 encoded)
        bucket_name = event['bucket_name']  # Bucket name where the file will be stored
        file_name = event['file_name']  # The name of the file to be stored (e.g., 'document.pdf')

        # Decode the file content if it's Base64 encoded
        file_content_decoded = base64.b64decode(file_content)

        # Store the file in the S3 bucket
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content_decoded,
            ContentType='application/pdf'  # Set the MIME type (can be customized for other file types)
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'File {file_name} uploaded successfully to {bucket_name}!'
            })
        }

    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': f'Missing required parameter: {str(e)}'
            })
        }

    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f'Error uploading file to S3: {str(e)}'
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f'An error occurred: {str(e)}'
            })
        }
