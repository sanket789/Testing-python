import frames as fr 	#module to be tested
import unittest	#testing library
import numpy as np
from ddt import ddt,file_data,unpack,data



@ddt	#ddt package repeats the test for each data points in file_data or data
		#check documentation of @ddt, file_data and data in ddt package
class TestAdd(unittest.TestCase):
	@file_data("test-data/test_add.json")	#File can contain nested list 
	#first and second number in each sub-list are numbers to be added and third number is expected result
	def test_cases_file(self,value):
		given_num1 = value[0]	
		given_num2 = value[1]
		expected = value[2]
		result = fr.add(given_num1,given_num2)
		self.assertTrue(np.allclose(result,expected))	
		

if __name__=='__main__':
	unittest.main(verbosity=2)
