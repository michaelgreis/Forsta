import sys
sys.path.append('../')
from classes import forstaparser as fp
from classes import ingester as ing

source_type = 's3'
target_bucket = 'landing-bucket-11.15.2021' 
target_key = 'Snow_Log.data_0_0_0.json.gz1637201489.66063671637964465.613458'
upload_table = 'landing_table'

def t_parser():
    upload_file_name = ing.ingester.convert_object(None,target_bucket,target_key)
    raw_logs = fp.parser.read_logs(None,source_type,target_bucket,upload_file_name)
    print(raw_logs)
    fp.parser.dynamo_landing_load(None,upload_table,raw_logs,upload_file_name)


t_parser()