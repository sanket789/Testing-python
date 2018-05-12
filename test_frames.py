import frames as fr 	#module to be tested
import unittest	#testing library
import numpy as np
from ddt import ddt,file_data,unpack,data
from math import sin,cos
@ddt
class TestLatLon(unittest.TestCase):
	@file_data("test-data/test_latlon.json")
	@unpack
	def test_cases_file(self,value):
		given,expected = np.asarray(value[0]),value[1]	#asarray to convert list to array
		result = fr.latlon(given)
		self.assertTrue(np.allclose([result[0],result[1]],expected))	
		self.assertEqual(type(result),tuple)
	@data(1,2,3,4,6,-6.8,1.1)
	def test_z_symmetry_lat(self,value):
		#self.assertEqual(2,2)
		x1 = np.array([sin(value),cos(value),13.])
		self.assertAlmostEqual(fr.latlon(x1)[0],fr.latlon(np.array([1.,0.,13.]))[0])
	@data(7e3,7.1e3,7.2e3,7.3e3,7.4e3)
	def test_independnt_of_radius(self,radius):
		x1 = np.array([1.,2.,-03.0])
		self.assertAlmostEqual(fr.latlon(radius*x1)[0],fr.latlon(x1)[0])
		self.assertAlmostEqual(fr.latlon(radius*x1)[1],fr.latlon(x1)[1])

if __name__=='__main__':
	unittest.main(verbosity=2)
