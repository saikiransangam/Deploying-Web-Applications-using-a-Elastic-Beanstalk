import boto3

region = 'us-east-1'
accessKeyId = 'AKIAUJMWPD3MC3WRJI7H'
secretAccessKey = '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'
username = '<Provide a username here>'
email = '<Provide a valid email address here>'
password = '<Provide a password here>'

#DynamoDB resource
dynamodb = boto3.resource('dynamodb',region_name=region,aws_access_key_id=accessKeyId,
         aws_secret_access_key=secretAccessKey)
table = dynamodb.Table('MyTable')

#Add item to the table
response = table.put_item(
                Item={
                    'Username': username,
                    'EmailID': email,
                    'Password': password,
                }
            )

print(response)