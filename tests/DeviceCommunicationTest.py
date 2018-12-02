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
			'hysteresisLevel': 300,		# ms
			'lowrateInterval': 1000, 	# ms
			'vPaceAmp': 5000, 			# mv
			'vPaceWidth': 255, 			# 10 ms
			'VRP': 200 					# ms
		}
		self.dc.sendAllDataToDevice(paramDict, True)

	def test_requestEgramData(self):
		print(self.dc.requestEGramData())

	def test_plotEgramData(self):
		self.dc.plotEgramData()

	def runTests(self):
		self.setUp()
		self.test_connectToDevice()
		self.test_requestEgramData()
		self.test_sendAllDataToDevice()
		self.test_plotEgramData()

DeviceCommunicationTest().runTests()