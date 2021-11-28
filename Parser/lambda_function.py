#from tests import test_parser
from classes import ingester as ing
from classes import forstaparser as fp

def lambda_handler(event, context):
 bucket_name = event['Records'][0]['s3']['bucket']['name']
 file_name = event['Records'][0]['s3']['object']['key']
 target_bucket = 'landing-bucket-11.15.2021'
 upload_table = 'landing_table'
 source_type = 's3'

 if bucket_name == target_bucket:
  upload_file_name = ing.ingester.convert_object(None,bucket_name,file_name)
  raw_logs = fp.parser.read_logs(None,source_type,target_bucket,upload_file_name)
  fp.parser.dynamo_landing_load(None,upload_table,raw_logs,file_name)
 else:
  landing_ingester = ingester.ingester()
  landing_ingester.copy_bucket(bucket_name,target_bucket)
  #test_parser.t_parser()
 print("Completed")