import boto3

region = 'us-east-1'
accessKeyId = 'AKIAUJMWPD3MC3WRJI7H'
secretAccessKey = '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'

#Create an SNS client
sns = boto3.client('sns',region_name=region,aws_access_key_id=accessKeyId,
         aws_secret_access_key=secretAccessKey)

sns_topic_ARN = '<Add Topic ARN here>'
email = '<Provide a valid email address here>'

#Subscribe to a topic
response = sns.subscribe(
                TopicArn=sns_topic_ARN,
                Protocol='email',
                Endpoint=email,
                ReturnSubscriptionArn=True
            )
            
print(response)