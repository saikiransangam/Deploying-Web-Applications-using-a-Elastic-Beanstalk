import boto3

region = 'us-east-1'
accessKeyId = 'AKIAUJMWPD3MC3WRJI7H'
secretAccessKey = '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'

#Create an SNS client
sns = boto3.client('sns',region_name=region,aws_access_key_id=accessKeyId,
         aws_secret_access_key=secretAccessKey)

sns_topic_ARN = '<Add Topic ARN here>'

#Publish a message
response = sns.publish(
            TopicArn=sns_topic_ARN, 
            Message='This is a message', 
            Subject='Hello World!'
          )            

print(response)