from classes import forstaparser as fp
import uuid
import json

source_type = 's3'
target_bucket = 'forsta-processing-6.24.2021' 
target_key = 'data_0_0_0.json.gz1624645957.03699661624645957.9166074.txt'
upload_table = 'landing_table'

def t_parser():
    raw_logs = fp.parser.read_logs(None,source_type,target_bucket,target_key)
    fp.parser.dynamo_landing_load(None,upload_table,raw_logs,target_key)

