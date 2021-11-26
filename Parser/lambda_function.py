#from tests import test_parser
from classes import ingester

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    target_bucket = 'landing-bucket-11.15.2021'

    landing_ingester = ingester.ingester()
    landing_ingester.copy_bucket(bucket_name,target_bucket)
    #test_parser.t_parser()
    print("Completed")