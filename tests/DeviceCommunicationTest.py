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
			'pacingMode': 'VOO',
			'hysteresis': True,
			'hysteresisLevel': 250,		# ms
			'lowrateInterval': 1000, 	# ms
			'vPaceAmp': 6500, 			# mv
			'vPaceWidth': 13, 			# 10 ms
			'VRP': 200 					# ms
		}
		self.dc.sendAllDataToDevice(paramDict, True)

	def runTests(self):
		self.setUp()
		#self.test_connectToDevice()
		self.test_sendAllDataToDevice()
DeviceCommunicationTest().runTests()