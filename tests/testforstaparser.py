import unittest

from parser.forstaparser import ForstaParser

class TestForstaParser(unittest.TestCase):

	def setUp(self):
		self.forstaParser = ForstaParser()

	def test_simple_select(self):
		stmt = "SELECT country FROM kill_floor.aiddata3_0;"
		# forstaParser = ForstaParser()
		query_info = self.forstaParser.parse(stmt)

		output_schema = { 'queryid':1, 'tables':['kill_floor.aiddata3_0'],'joins':[]}
		
		assert query_info['tables'] == ['kill_floor.aiddata3_0']
		# assert query_info == output_schema

	def test_join_with_alias(self):
		stmt = "SELECT * FROM kill_floor.aiddata3_0 aid_data INNER JOIN kill_floor.nytimeslocations location_count on aid_data.recipient_iso2 = location_count.country;"
		query_info = self.forstaParser.parse(stmt)
		tables = ['kill_floor.aiddata3_0','kill_floor.nytimeslocations']
		assert query_info['tables'] == tables
		#assert query_info['joins'] == {'type':'INNER','left':'kill_floor.aiddata3_0','right':'kill_floor.nytimeslocations'}	
