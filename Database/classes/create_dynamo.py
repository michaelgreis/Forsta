import boto3

def create_landing_table():
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    landing_table = dynamodb.create_table(
        TableName='landing_table',
        KeySchema=[
            {
            'AttributeName': 'uuid',
            'KeyType': 'HASH'
            },
            {
            'AttributeName': 'upload_date',
            'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'uuid',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'upload_date',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits':10,
            'WriteCapacityUnits':10
        }
    )

    print('Table Status: ',landing_table.table_status)