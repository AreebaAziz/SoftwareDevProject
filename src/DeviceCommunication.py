'''
	- Connect to device, return true if successful connection
	- send parameter data (see chart Geoff sent)
	- receive egram data and display it (using a separate graph class)
'''
import serial
class DeviceCommunication:
	def __init__(self):
		self.ser = serial.Serial()

	def connectToDevice(self): 
	    self.ser.port = 'COM13'
	    self.ser.baudrate = 115200
	    self.ser.open()

	def convertDataIntoBytes(self, param: str, data):
		if (param == 'pacingMode'):
			return b'\x04'
		if (param == 'hysteresis'):
			return b'\x04'
		if (param == 'hysteresisLevel'):
			return b'\x04'
		if (param == 'lowrateInterval'):
			return b'\x04'
		if (param == 'vPaceAmp'):
			return b'\x04'
		if (param == 'vPaceWidth'):
			return b'\x04'
		if (param == 'VRP'):
			return b'\x04'

	'''
		paramData is a dict: {'paramName': value, 'paramName2': value}
		verbose is a boolean determining whether to log info on standard output
		returns True upon success, False upon failure
	'''
	def sendAllDataToDevice(self, paramData: dict, verbose: bool):
		expectedParamsInOrder = [
			'pacingMode',
			'hysteresis',
			'hysteresisLevel',
			'lowrateInterval',
			'vPaceAmp',
			'vPaceWidth',
			'VRP'
		]
		# assume data is transmitted high-byte first
		serialData = b'\x16'		# sync 
		serialData += b'\x00'		# header
		
		for param in expectedParamsInOrder:
			if (param in paramData):
				serialData += self.convertDataIntoBytes(param, paramData[param])
			else:
				serialData += b'\x00'

		if (verbose):
			print("Successfully converted all data into bytes.")
			print("Serial data is: ")
			print(serialData)
			print("Attempting to send data to device...")

		# # @TODO - do this function properly
		# res = self.ser.write(serialData)
		# if (res == None):
		# 	print("Failed to send data to device.")
		# 	return False
		# else:
		# 	print("Successfully sent data to device.")
		# 	return True

	def displayEGramData(self):
		pass
