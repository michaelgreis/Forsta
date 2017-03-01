import os #needed for os function read_logs
#import pandas as pd #needed for the dataframe read in
import time as time


class parser():
	def __init__(self):
		self.x = 'Hello'

	#This function is used to read the logs in from a specific directory.
	def read_logs(filepath):
		input_lines=[]
		input_files=[]
		print(time.time())
		for filename in os.listdir(filepath): #read all files in directory
			with open(filepath+filename,'r') as file:
				for line in file: #read in all lines for a file 
					input_lines.append(line)
			print(filename + ' in directory ' + filepath + ' has been recorded successfully brother.') # message for log
		print(time.time())
		return input_lines

	#This function accepts a list of strings (cleaning_values) to filter out irrelevant data from another list of strings (list_to_clean)
	# Specifically, you pass the values you WANT to include
	#Split value = the value you want to grab everything after. AKA don't preserver all the standard gobbly gook before the SQL statement.
	def clean_input_list(cleaning_values,list_to_clean,split_value):
		total_line_count = 0
		clean_count = 0
		clean_list = [] #this is the output list

		for line in list_to_clean: #iterating through the lines
			if any(word in line for word in cleaning_values) == True: # iterating through the cleaning list
				#if line.upper().find(sterilization_values.upper())>=0: #this checks if there is a sterilization value in the string.
				line = line.upper().partition(split_value.upper())[2]
				clean_list.append(line)
				clean_count+=1 # count of lines cleaned
				# break # if one of the values is found, it returns the line.
			total_line_count+=1 #count of total lines read
		print('List of ' + str(total_line_count) + ' has been cleaned to ' + str(clean_count) + ' for lines containing the following values: ' + str(cleaning_values)) # outputs log
		return clean_list

	#def reading_into_dataframe(input_array):
#		input_words = [] # this is used to input all of the words that are codes
#		for index, values in enumerate(input_array):
#			for word in values.split(): #splitting by the space
#				for specific_word in word.split('='): #splitting by equal sign
#					input_words.append([index,specific_word]) #appending to the input word with the index for the word
#		df_input_words = pd.DataFrame(input_words,columns=list(['log_entry', 'word']))
#		return(df_input_words)

#	def wordcount(df_input): #this function expects to receive a datframe with "log_entry" and "word" columns
#		print('Counting Words.')
#		df_input = df_input[['log_entry','word']].groupby(['log_entry','word']).size().reset_index(name="mentions")
#		print('Words Counted.')
#		return df_input

#	def pivot_data(df_input):
#		print('Data pivoting.')
#		df_input = df_input.pivot(index='log_entry',columns='word',values='mentions').fillna(0)
#		print('Data pivoted.')
#		return df_input

#	def word_relationship(df_input):
#		word_matrix = df_input.as_matrix()
#		print(word_matrix)