import sys
sys.path.insert(0, '../src')
from DeviceCommunication import *
from RunTests import SimpleTestSuite

class DeviceCommunicationTest:
	def setUp(self):
		self.sts = SimpleTestSuite()
		self.dc = DeviceCommunication()

	def test_connectToDevice(self):
		self.dc.connectToDevice()

	def test_sendAllDataToDevice(self):
		paramDict = {			
			'pacingMode': 'AOO',
			'hysteresis': True,
			'hysteresisLevel': 500,		# ms
			'lowrateInterval': 2000, 	# ms
			'vPaceAmp': 7000, 			# mv
			'vPaceWidth': 13, 			# 10 ms
			'VRP': 200 					# ms
		}
		self.dc.sendAllDataToDevice(paramDict, True)

	def test_requestEgramData(self):
		res = self.dc.requestEGramData()
		print(res)

	def runTests(self):
		self.setUp()
		self.test_connectToDevice()
		self.test_sendAllDataToDevice()
		#self.test_requestEgramData()
DeviceCommunicationTest().runTests()