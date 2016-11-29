import os #needed for the looping through of the logs
import time # needed for pausing, to make sure program is working alright when debugging.
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

time.sleep(5) #only used for debugging purposes. Want to make sure execution is occurring correctly.

for index, values in enumerate(input_lines):
	#print(values) #I know this was occurring correctly, so no longer need it
	#input_words.append([index, values.split()])
	for word in values.split(): #splitting by the space
		for specific_word in word.split('='): #splitting by equal sign
			input_words.append([index,specific_word])
	print(input_words)


