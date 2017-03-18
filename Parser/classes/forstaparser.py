import os #needed for os function read_logs
import time as time
from collections import Counter
import json
from itertools import islice

class parser():
 #initalizing
 def __init__(self):
  self.input = []
  self.clean_logs = []
  self.dedup_logs = {}


 #This function is used to read the logs in from a specific directory.
 def read_logs(self,filepath):
  input_lines=[]
  print(time.time())
  for filename in os.listdir(filepath): #read all files in directory
   with open(filepath+filename,'r') as file:
    for line in file: #read in all lines for a file 
     self.input.append(line)
   print(filename + ' in directory ' + filepath + ' has been recorded successfully brother.') # message for log
  print(time.time())


 #This function accepts a list of strings (cleaning_values) to filter out irrelevant data from another list of strings (list_to_clean)
 # Specifically, you pass the values you WANT to include
 #Split value = the value you want to grab everything after. AKA don't preserver all the standard gobbly gook before the SQL statement.
 def clean_input_logs(self,cleaning_values,split_value):
  total_line_count = 0
  clean_count = 0

  for line in self.input: #iterating through the lines
   if any(word in line for word in cleaning_values) == True: # iterating through the cleaning list
    line = line.upper().partition(split_value.upper())[2]
    self.clean_logs.append(line)
    clean_count+=1 # count of lines cleaned
   total_line_count+=1 #count of total lines read
  print('List of ' + str(total_line_count) + ' has been cleaned to ' + str(clean_count) + ' for lines containing the following values: ' + str(cleaning_values)) # outputs log

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
