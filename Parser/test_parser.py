from classes import forstaparser as fp

source_type = 's3'
target_bucket = 'forsta-processing-6.24.2021' 
target_key = 'data_0_0_0.json.gz1624645957.03699661624645957.9166074.txt'

fp.parser.read_logs(None,source_type,target_bucket,target_key)