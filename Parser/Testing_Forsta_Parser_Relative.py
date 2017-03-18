from classes import forstaparser as fp
#from classes import forstaalgorithm as fa

print('LOADED BRO')

# this is used to define the cleaning values we are looking for.
cleaning_values = []
cleaning_values.append('select')
cleaning_values.append(':LOG:  statement: ')

#this defines the split value that is used in clean_input_list
sql_log_split = ':LOG:  statement: '

logs = fp.parser()

logs.read_logs('Sample_Data_Generation/Sample_Data/')

#print(logs_input)

print('Logs Read.')

logs.clean_input_list(cleaning_values,sql_log_split)

print('Logs Cleaned.')


print(logs.clean_list)

#dataframe = fp.parser.reading_into_dataframe(logs_input)


#dataframe_count = fa.word2vec.wordcount(dataframe)

#print(dataframe_count)

#dataframe_pivot = fa.word2vec.pivot_data(dataframe_count)

#print(dataframe_pivot)

#fa.word2vec.word_relationship(dataframe_pivot)