from classes import forstaparser as fp
import uuid
import json

source_type = 's3'
target_bucket = 'forsta-processing-6.24.2021' 
target_key = 'data_0_0_0.json.gz1624645957.03699661624645957.9166074.txt'

raw_logs = fp.parser.read_logs(None,source_type,target_bucket,target_key)
#print(raw_logs.readlines())

#how to generate the UUID for the upload...should be part of the Lambda function likely.
for line in raw_logs.readlines():
    j_line = json.loads(line)
    print(j_line)
    print(type(j_line))
    j_line.update({'uuid': uuid.uuid4()})
    print(j_line)
    print(j_line["uuid"])