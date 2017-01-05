from . import select_parser as sp
import os #needed for os function read_logs

<<<<<<< HEAD
class ForstaParser():
	def parse(self,query):
		query_record = {}
		return query_record

	#This function is used to read the logs in from a specific directory.
	def read_logs(filepath):
		input_lines=[]

		for filename in os.listdir(filepath): #read all files in directory
			file=open(filepath+filename,'r')
			for line in file: #read in all lines for a file 
				input_lines.append(line)
			file.close()
			print(filename + ' in directory ' + filepath + ' has been recorded successfully brother.') # message for log
		return input_lines[]

	#This function accepts a list of strings (cleaning_values) to filter out irrelevant data from another list of strings (list_to_clean)
	# Specifically, you pass the values you WANT to include
	def clean_input_list(cleaning_values,list_to_clean):
		clean_list[] #this is the output list

		for line in list_to_clean: #iterating through the lines
			for sterilization_values in cleaning_values: # iterating through the cleaning list
				if line.str.find(sterilization_values,beg=0,end=len(line)) > -1 #this checks if there is a sterilization value in the string.
					clean_list.append(line)
					clean_count+=1 # count of lines cleaned
					break # if one of the values is found, it returns the line.
			total_line_count+=1 #count of total lines read
		print('List of ' + total_line_count + ' has been cleaned to ' + clean_count + ' for lines containing the following values: ' + cleaning_values) # outputs log
		return clean_list[]
=======
		parseResults = sp.select_stmt.parseString(query)
		# print(parseResults)
		# print(parseResults.dump())
		# print(type(parseResults["from"]))
		print(parseResults.items)
		self.get_tables(parseResults)
		return query_record

	def get_tables(self,parseResults):
		from_clause = parseResults["from"]
		print(from_clause.items)
		for x in from_clause:
			
			print(x)
			print(type(x))
>>>>>>> origin/master
