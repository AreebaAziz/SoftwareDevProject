import os, sys
sys.path.insert(0, '../src')

class SimpleTestSuite:
	def __init__(self):
		self.__num_asserts = 0
		self.__num_asserts_failed = 0
		self.__verbose = True

	def setVerbose(self, val: bool):
		self.__verbose = val

	def assertIs(self, expected, actual):
		try:
			self.__num_asserts += 1
			assert expected is actual
		except AssertionError as e:
			if (self.__verbose is True):
				print("assertIs failed.\nExpected:\n" + str(expected))
				print("Actual:\n" + str(actual))
			self.__num_asserts_failed += 1

	def assertIsNot(self, expected, actual):
		try:
			self.__num_asserts += 1
			assert expected is not actual
		except AssertionError as e:
			if (self.__verbose is True):
				print("assertIsNot failed.\nExpected:\n" + str(expected))
				print("Actual:\n" + str(actual))
			self.__num_asserts_failed += 1

	def assertEqual(self, expected, actual):
		try:
			self.__num_asserts += 1
			assert expected == actual
		except AssertionError as e:
			if (self.__verbose is True):
				print("assertEqual failed.\nExpected:\n" + str(expected))
				print("Actual:\n" + str(actual))
			self.__num_asserts_failed += 1

	def assertNotEqual(self, expected, actual):
		try:
			self.__num_asserts += 1
			assert expected != actual
		except AssertionError as e:
			if (self.__verbose is True):
				print("assertNotEqual failed.\nExpected:\n" + str(expected))
				print("Actual:\n" + str(actual))
			self.__num_asserts_failed += 1

	def finishTest(self):
		print("\n" + str(self.__num_asserts_failed) + " failed asserts out of "
			+ str(self.__num_asserts) + " total asserts")
		print("")

	@classmethod
	def runAllTests(cls):
		for root, dirs, files in os.walk("."):
			for filename in files:
				if (filename.endswith(".py") and filename != __file__):
					print("Running " + filename + "-----------------------------------")
					os.system('python ' + filename)

if __name__ == "__main__":
    SimpleTestSuite.runAllTests()