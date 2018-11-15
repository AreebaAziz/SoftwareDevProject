import os

class SimpleTest:
	def __init__(self):
		self.num_asserts = 0
		self.num_asserts_failed = 0

	def assertIs(self, obj_a, obj_b):
		try:
			assert obj_a is obj_b
		except AssertionError as e:
			self.num_asserts_failed += 1

	@classmethod
	def runAllTests(cls):
		for root, dirs, files in os.walk("."):
			for filename in files:
				if (filename.endswith(".py") and filename != __file__):
					os.system('python ' + filename)
					#print(filename)

SimpleTest.runAllTests()