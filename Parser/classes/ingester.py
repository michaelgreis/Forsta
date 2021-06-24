import boto3
import time as time

class ingester():
 #def __init__(self):
 #print the name of all the buckets the configured account has access to
 def s3_list_buckets(self):
  for bucket in boto3.resource('s3').buckets.all():
   print(bucket.name)
   response_dict = boto3.client('s3').list_objects(Bucket=bucket.name)
   print(response_dict.keys())
   #ensures bucket has content before trying to pull content info out
   try:
    response_dict['Contents']
   except:
    print('No objects in ' + bucket.name + ' exist.')
   else:
    print(response_dict['Contents']) 
    objs_contents = response_dict['Contents']
    print(objs_contents)
    #unnecessary, good for reference
    #for i in range(len(objs_contents)):
    # file_name = objs_contents[i]['Key']
    # print(file_name)

#download all the files in the s3 bucket - Deprecated
# def s3_read(self,bucket_name,object_name,file_name):
#  print(time.time())
#  s3 = boto3.client('s3')

# Read data file from S3 location
# Unpack/Unzip into JSON
# Load to landing bucket location
 def copy_load(self,source_bucket,object_key,target_bucket):
   copy_source = {
    'Bucket' : source_bucket,
    'Key' : object_key
   }
   #!!!!!!!!!!!!ISSUE HERE. S3 DOESN'T EXIST!!!!
   s3 = boto3.resource('s3')
   landing_bucket = s3.Bucket(target_bucket)
   try:
    landing_bucket.copy(copy_source, object_key + str(time.time()))
   except Exception as ex:
    print(ex)
   else:
    print('Success!')