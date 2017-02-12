from classes import forstaparser as fp
print('LOADED BRO')

# this is used to define the cleaning values we are looking for.
cleaning_values = []

cleaning_values.append('select')

logs_input = fp.parser.read_logs('Sample_Data_Generation/Sample_Data/')

print('Logs Read.')

logs_input = fp.parser.clean_input_list(cleaning_values,logs_input)

print('Logs Cleaned.')

dataframe = fp.parser.reading_into_dataframe(logs_input)

print(dataframe)