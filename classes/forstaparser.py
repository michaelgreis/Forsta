import os #needed for os function read_logs
import pandas as pd #needed for the dataframe read in


class parser():
	def __init__(self):
		self.x = 'Hello'

	#This function is used to read the logs in from a specific directory.
	def read_logs(filepath):
		input_lines=[]

		for filename in os.listdir(filepath): #read all files in directory
			file=open(filepath+filename,'r')
			for line in file: #read in all lines for a file 
				input_lines.append(line)
			file.close()
			print(filename + ' in directory ' + filepath + ' has been recorded successfully brother.') # message for log
		return input_lines

	#This function accepts a list of strings (cleaning_values) to filter out irrelevant data from another list of strings (list_to_clean)
	# Specifically, you pass the values you WANT to include
	def clean_input_list(cleaning_values,list_to_clean):
		clean_list = [] #this is the output list
		for line in list_to_clean: #iterating through the lines
			for sterilization_values in cleaning_values: # iterating through the cleaning list
				if line.str.find(sterilization_values,beg=0,end=len(line))>=0: #this checks if there is a sterilization value in the string.
					clean_list.append(line)
					clean_count+=1 # count of lines cleaned
					break # if one of the values is found, it returns the line.
			total_line_count+=1 #count of total lines read
		print('List of ' + total_line_count + ' has been cleaned to ' + clean_count + ' for lines containing the following values: ' + cleaning_values) # outputs log
		return clean_list

	def reading_into_dataframe(input_array):
		input_words = [] # this is used to input all of the words that are codes
		for index, values in enumerate(input_array):
			for word in values.split(): #splitting by the space
				for specific_word in word.split('='): #splitting by equal sign
					input_word.append([index,specific_word]) #appending to the input word with the index for the word
		df_input_words = pd.DataFrame(input_words,columns=list(['log_entry', 'word']))
		return(df_input_words)
