import os #needed for os function read_logs
import datetime
from collections import Counter
import json
import uuid
from itertools import islice
import boto3
import io
import re

class parser:
 #initalizing
 def __init__(self):
  self.clean_logs = []
  self.dedup_logs = {}
  pass


 #This function is used to read the logs in from a specific directory.
 def read_logs(self,source_type,target_bucket,target_key):
  input = []
  if source_type == 'local':
    for filename in os.listdir(filepath): #read all files in directory
     with open(filepath+filename,'r') as file:
      for line in file: #read in all lines for a file 
       self.input.append(line)
     print(filename + ' in directory ' + filepath + ' has been recorded successfully brother.') # message for log
    return (input)
  elif source_type == 's3':
    s3_client = boto3.client('s3')
    read_object = s3_client.get_object(Bucket=target_bucket,Key=target_key)
    output = io.BytesIO(read_object['Body'].read())
    output = io.TextIOWrapper(output,'utf-8')
    return output
  else:
    print(source_type + ' is invalid. Must be source_type = \'local\' or \'s3\'.') 

 def dynamo_landing_load(self,table_name,data,source):
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    load_table = dynamodb.Table(table_name)
    #In order for this to work, the data must be the right format
    for line in data.readlines():
      j_line = json.loads(line)
      #added the UID for PK
      j_line.update({'uuid': str(uuid.uuid4())})
      response = load_table.put_item(
        TableName = table_name,
        Item={
          'uuid': str(j_line['uuid']),
          'upload_date': str(datetime.date.today()),
          'data': str(j_line),
          'source': source
        }
      )

      print(response)

 #This function accepts a list of strings (cleaning_values) to filter out irrelevant data from another list of strings (list_to_clean)
 #Specifically, you pass the values you WANT to filter out
 #Split value = the value you want to grab everything after. AKA don't preserver all the standard gobbly gook before the SQL statement.
 #def clean_input_logs(self,cleaning_values,split_value):
 # total_line_count = 0
 # clean_count = 0
 # for line in : #iterating through the lines
 #  if any(word in line for word in cleaning_values) == True: # iterating through the cleaning list
 #   line = line.upper().partition(split_value.upper())[2]
 #   self.clean_logs.append(line)
 #   clean_count+=1 # count of lines cleaned
 #  total_line_count+=1 #count of total lines read
 # print('List of ' + str(total_line_count) + ' has been cleaned to ' + str(clean_count) + ' for lines containing the following values: ' + str(cleaning_values)) # outputs log

#The purpose of this counter is to load the dictionary along with the line count.
 def dedupe_input_logs(self):
  if len(self.clean_logs) > 0: 
   self.dedup_logs = dict(Counter(self.clean_logs))
   print('clean_list has been loaded into the dedup_list.')
  else:
   self.dedup_logs = dict(Counter(self.input))
   print ('input has been loaded into the dedup_list.')

#this function is used to return the data in a JSON format.
 def extract_JSON(self,output_lines=-1):
  output_json = [] #this is the final list that contains the data to be output
  output_counter = 0

  if output_lines==-1:
   for key,value in self.dedup_logs.items():
    output_json.append({'SQL': key ,'Count':value})
   return json.dumps(output_json)
  else:
   for key,value in self.dedup_logs.items():
    output_counter+=1
    if output_counter <= output_lines:
     output_json.append({'SQL': key ,'Count':value})
   return json.dumps(output_json)
