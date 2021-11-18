import boto3
import time as time
import gzip
import json
from io import BytesIO

class ingester():
 #def __init__(self):
 #print the name of all the buckets the configured account has access to
 def s3_list_buckets(self):
  for bucket in boto3.resource('s3').buckets.all():
   print(bucket.name)
   response_dict = boto3.client('s3').list_objects(Bucket=bucket.name)
   #print(response_dict.keys())
   #ensures bucket has content before trying to pull content info out
   try:
    for s3_item in response_dict['Contents']:
     print(s3_item['Key'])
    #print(response_dict['Name'])
   except:
    print('No objects in ' + bucket.name + ' exist.')
   #else:
   # print(response_dict['Contents']) 
   # objs_contents = response_dict['Contents']
   # print(objs_contents)
    #unnecessary, good for reference
    #for i in range(len(objs_contents)):
    # file_name = objs_contents[i]['Key']
    # print(file_name)

# Read data file from S3 location
# Load to landing bucket location
 def copy_object(self,source_bucket,object_key,target_bucket):
   target_object = object_key + str(time.time())
   copy_source = {
    'Bucket' : source_bucket,
    'Key' : object_key
   }
   s3 = boto3.resource('s3')
   landing_bucket = s3.Bucket(target_bucket)
   try:
    landing_bucket.copy(copy_source, target_object)
   except Exception as ex:
    print(ex)
   else:
    print('Success! Object loaded to: ' + target_object)
    return (target_object)

# Read all files from S3 bucket
# Load all files to landing bucket location
 def copy_bucket(self,source_bucket,target_bucket):
   #setup target location
   s3 = boto3.resource('s3')
   landing_bucket = s3.Bucket(target_bucket)

   response_dict = boto3.client('s3').list_objects(Bucket=source_bucket)
   try:
     for s3_item in response_dict['Contents']:
       copy_source = {
         'Bucket' : source_bucket,
         'Key' : s3_item['Key']
       }
       #only copy non-0 byte files
       if s3_item['Size'] != 0:
        landing_bucket.copy(copy_source,(s3_item['Key'] + str(time.time())).replace('/','.'))
        print('Object ' + s3_item['Key'] + ' copied to ' + target_bucket)
   except Exception as ex:
     print(ex)


# turns the data contained in the s3 gzip compressed file to text document
 def convert_object(self,target_bucket,target_key):
   data = []
   s3_client = boto3.client('s3')
   read_object = s3_client.get_object(
     Bucket = target_bucket,
     Key = target_key
   )
   read_byte_object = BytesIO(read_object['Body'].read()) 
   raw_data = gzip.GzipFile(None, 'rb', fileobj=read_byte_object).read().decode('ASCII') #.decode('utf-8')
   s3_client.put_object(Body=raw_data, Bucket=target_bucket,Key=target_key[target_key.rindex('/')+1:] + str(time.time())+'.txt')
