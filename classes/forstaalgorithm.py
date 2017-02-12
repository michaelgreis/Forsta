import pandas as pd #needed for the pandas dataframe input
import numpy as np


class word2vec():
	def __init__(self):
		self.x = 'Hello'

	def wordcount(df_input): #this function expects to receive a datframe with "log_entry" and "word" columns
		print('Counting Words.')
		df_input = df_input[['log_entry','word']].groupby(['log_entry','word']).size().reset_index(name="mentions")
		print('Words Counted.')
		return df_input

	def pivot_data(df_input):
		print('Data pivoting.')
		df_input = df_input.pivot(index='log_entry',columns='word',values='mentions').fillna(0)
		print('Data pivoted.')
		return df_input

	def word_relationship(df_input):
		word_matrix = df_input.as_matrix()
		print(word_matrix)

		for column in word_matrix:
			if column