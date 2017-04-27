import unittest
import os
from seds import get_data
from seds import remove_data

class TestPrimeChecker(unittest.TestCase):

	# Test get_data
	def testGetDataFileDoesNotExist(self):
		# Case: Validate that file is downloaded if it does not exist.
		# Ensure file is not present locally
		if os.path.exists('4xy5-26gy.csv'):
			os.remove('4xy5-26gy.csv')
		# Run the function
		returnValue = get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
		# Validate that the file is now present
		self.assertTrue(os.path.exists('4xy5-26gy.csv'))
		self.assertTrue(returnValue == 200)
		
	def testGetDataFileExists(self):
		# Case: Validate that file is NOT downloaded if it exists.
		# Ensure file is present locally
		get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
		self.assertTrue(os.path.exists('4xy5-26gy.csv'))
		# Run the function
		returnValue = get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
		# Validate that the file is now present
		self.assertTrue(os.path.exists('4xy5-26gy.csv'))
		self.assertTrue(returnValue == 100)

	def testGetDataInvalidFilePath(self):
		# Case 3: Validate appropriate code is returned if file does not exist.
		# Run the function with invalid filepath
		returnValue = get_data('https://data.seattle.gov/resource/GameOfThrones.csv')
		# Validate that the file is now present
		self.assertFalse(os.path.exists('GameOfThrones.csv'))
		self.assertTrue(returnValue == 404)		

	def testRemoveData(self):
		# Case: Validate that file is remove.
		# Ensure file is present locally
		get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
		self.assertTrue(os.path.exists('4xy5-26gy.csv'))
		# Run the function
		returnValue = remove_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
		# Validate that the file is now present
		self.assertFalse(os.path.exists('4xy5-26gy.csv'))


if __name__ == '__main__':
	unittest.main()