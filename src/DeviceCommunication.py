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
	    self.ser.port = 'COM5'
	    self.ser.baudrate = 115200
	    self.ser.open()

	def convertDataIntoBytes(self, paramData: dict):
		serialData = b''

		# byte index 2 and 3 - pacing mode and hysteresis
		temp_byte = b'\x03' 		# default mode is VVI
		if ('pacingMode' in paramData):
			if (paramData['pacingMode'] == 'VOO'):
				temp_byte = b'\x01'
			elif (paramData['pacingMode'] == 'AOO'):
				temp_byte = b'\x02'
			elif (paramData['pacingMode'] == 'VVI'):
				temp_byte = b'\x03'
			elif (paramData['pacingMode'] == 'AAI'):
				temp_byte = b'\x04'

		serialData += temp_byte

		# hysteresis
		temp_byte = b'\x00'		# @TODO: default hysteresis ??
		if ('hysteresis' in paramData and paramData['hysteresis']):
				temp_byte = b'\x01'

		serialData += temp_byte

		# byte indices 4:9
		# 4:5 - hysteresis level in 2 bytes
		temp_bytes = '\x00'
		if ('hysteresisLevel' in paramData):
			if (paramData['hysteresisLevel'] < 65536):
				temp_bytes = paramData['hysteresisLevel'].to_bytes(2, byteorder='big')
			else:
				temp_bytes = '\x00'
		serialData += temp_bytes

		# 6:7 - lowrate interval in 2 bytes
		temp_bytes = '\x00'
		if ('lowrateInterval' in paramData):
			if (paramData['lowrateInterval'] < 65536):
				temp_bytes = paramData['lowrateInterval'].to_bytes(2, byteorder='big')
			else:
				temp_bytes = '\x00'
		serialData += temp_bytes

		# 8:9 - vPaceAmp in 2 bytes
		temp_bytes = '\x00'
		if ('vPaceAmp' in paramData):
			if (paramData['vPaceAmp'] < 65536):
				temp_bytes = paramData['vPaceAmp'].to_bytes(2, byteorder='big')
			else:
				temp_bytes = '\x00'
		serialData += temp_bytes

		# 10 - vPaceWidth in 1 byte
		temp_bytes = '\x00'
		if ('vPaceWidth' in paramData):
			if (paramData['vPaceWidth'] < 256):
				temp_bytes = paramData['vPaceWidth'].to_bytes(2, byteorder='big')
			else:
				temp_bytes = '\x00'
		serialData += temp_bytes

		# 11:12 - VRP in 2 bytes
		temp_bytes = '\x00'
		if ('VRP' in paramData):
			if (paramData['VRP'] < 65536):
				temp_bytes = paramData['VRP'].to_bytes(2, byteorder='big')
			else:
				temp_bytes = '\x00'
		serialData += temp_bytes

		return serialData

	'''
		paramData is a dict: {'paramName': value, 'paramName2': value}
		verbose is a boolean determining whether to log info on standard output
		returns True upon success, False upon failure
	'''
	def sendAllDataToDevice(self, paramData: dict, verbose: bool):
		# assume data is transmitted high-byte first
		serialData = b'\x11\x00'		# sync - x11 code to indicate start of package transmission
									# header - 0 to signify we're transmitting data

		serialData += self.convertDataIntoBytes(paramData)

		if (verbose):
			print("Successfully converted all data into bytes.")
			print("Serial data is: ")
			print(serialData)
			print("Attempting to send data to device...")

		return self.sendDataToDevice(serialData)

	'''
		Sends a request to the hardware to send over one byte of egram data. 
		returns the byte read, or None if failed
	'''
	def requestEGramData(self):
		serialData = b'\x16\x01'
		self.sendDataToDevice(serialData)
		try:
			return self.ser.read(size=1)	# read one byte
		except serial.SerialException:
			return None

	def sendDataToDevice(self, serialData):
		try:
			res = self.ser.write(serialData)
		except serial.SerialException:
			res = 0

		if (res == 0):	# no data sent
			print("Failed to send data to device.")
			return False
		else:
			print("Successfully sent data to device.")
			return True

	def displayEGramData(self):
		pass
