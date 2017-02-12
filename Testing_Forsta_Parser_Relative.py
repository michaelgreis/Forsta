from classes import forstaparser as fp
from classes import forstaalgorithm as fa

print('LOADED BRO')

# this is used to define the cleaning values we are looking for.
cleaning_values = []

cleaning_values.append('select')

logs_input = fp.parser.read_logs('Sample_Data_Generation/Sample_Data/')

print('Logs Read.')

logs_input = fp.parser.clean_input_list(cleaning_values,logs_input)

print('Logs Cleaned.')

dataframe = fp.parser.reading_into_dataframe(logs_input)


dataframe_count = fa.word2vec.wordcount(dataframe)

#print(dataframe_count)

dataframe_pivot = fa.word2vec.pivot_data(dataframe_count)

print(dataframe_pivot)

fa.word2vec.word_relationship(dataframe_pivot)