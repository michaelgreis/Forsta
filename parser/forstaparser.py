from . import select_parser as sp

class ForstaParser():

	def parse(self,query):
		query_record = {}
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