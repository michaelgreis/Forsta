import os #needed for the looping through of the logs
import time # needed for pausing, to make sure program is working alright when debugging.
import pandas as pd #needed for the dataframe read in
import numpy
import matplotlib.pyplot


import string



path = '../Sample_Data_Generation/Sample_Data/'
input_lines=[]
input_words=[]


for filename in os.listdir(path):	
	file = open(path + filename,'r')
	for line in file:
		#print(filename) #to get the filename associated with the file
		#print(line)
		input_lines.append(line)
	file.close()
	print(filename + ' has been written into array successfully.')

time.sleep(1) #only used for debugging purposes. Want to make sure execution is occurring correctly.

for index, values in enumerate(input_lines):
	#print(values) #I know this was occurring correctly, so no longer need it
	#input_words.append([index, values.split()])
	for word in values.split(): #splitting by the space
		for specific_word in word.split('='): #splitting by equal sign
			input_words.append([index,specific_word])
	#print(input_words) # No longer needed

#print([i[0] for i in input_words])
#print([i[1] for i in input_words])

#this is the start of the use of Pandas

#df_input_words = pd.Series(input_words)

#This is the series populater that works.
#df_input_words = pd.Series([i[1] for i in input_words], index=[i[0] for i in input_words])
#------------

#df_input_words.groupby(df_input_words).count()

#print(df_input_words)

#df = pd.DataFrame(input_words,columns=headers)

df_input_words = pd.DataFrame(input_words, columns=list(['log_entry', 'word']))

#outputting to a test file
f_test = open('../Dev_Space/testing.txt','w')
test_data = df_input_words
f_test.write(str(test_data))
f_test.close()
#end of test file output
