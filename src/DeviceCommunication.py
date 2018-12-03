'''
	- Connect to device, return true if successful connection
	- send parameter data (see chart Geoff sent)
	- receive egram data and display it (using a separate graph class)
'''
import serial
from GraphEGram import GraphEGram

class DeviceCommunication:
	def __init__(self):
		self.ser = serial.Serial(timeout=10)
		self.connected = False

	def connectToDevice(self): 
	    self.ser.port = 'COM5'
	    self.ser.baudrate = 115200
	    try:
	    	self.ser.open()
	    	self.connected = True
	    	return True
	    except:
	    	return False

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
		temp_byte = b'\x00'	
		if ('hysteresis' in paramData and paramData['hysteresis']):
				temp_byte = b'\x01'

		serialData += temp_byte

		# byte indices 4:9
		# 4:5 - hysteresis level in 2 bytes
		temp_bytes = b'\x00\x00'
		if ('hysteresisLevel' in paramData):
			if (paramData['hysteresisLevel'] < 65536):
				temp_bytes = paramData['hysteresisLevel'].to_bytes(2, byteorder='big')
			else:
				temp_bytes = b'\x00'
		serialData += temp_bytes

		# 6:7 - lowrate interval in 2 bytes
		temp_bytes = b'\x00\x00'
		if ('Low Rate Interval' in paramData):
			if (paramData['Low Rate Interval'] < 65536):
				temp_bytes = paramData['Low Rate Interval'].to_bytes(2, byteorder='big')
			else:
				temp_bytes = b'\x00'
		serialData += temp_bytes

		# 8:9 - Ventricular Amplitude (mV) in 2 bytes
		temp_bytes = b'\x00\x00'
		if ('Ventricular Amplitude (mV)' in paramData):
			if (paramData['Ventricular Amplitude (mV)'] < 65536):
				temp_bytes = paramData['Ventricular Amplitude (mV)'].to_bytes(2, byteorder='big')
			else:
				temp_bytes = b'\x00'
		serialData += temp_bytes

		# 10 - Ventricular Pace Width (10 ms) in 1 byte
		temp_bytes = b'\x00'
		if ('Ventricular Pace Width (10 ms)' in paramData):
			if (paramData['Ventricular Pace Width (10 ms)'] < 256):
				temp_bytes = paramData['Ventricular Pace Width (10 ms)'].to_bytes(2, byteorder='big')
			else:
				temp_bytes = b'\x00'
		serialData += temp_bytes

		# 11:12 - VRP in 2 bytes
		temp_bytes = b'\x00\x00'
		if ('VRP (ms)' in paramData):
			if (paramData['VRP (ms)'] < 65536):
				temp_bytes = paramData['VRP (ms)'].to_bytes(2, byteorder='big')
			else:
				temp_bytes = b'\x00'
		serialData += temp_bytes

		return serialData

	'''
		paramData is a dict: {'paramName': value, 'paramName2': value}
		verbose is a boolean determining whether to log info on standard output
		returns True upon success, False upon failure
	'''
	def sendAllDataToDevice(self, paramData: dict, verbose: bool):
		# assume data is transmitted high-byte first
		serialData = b'\x01\x00'		# sync - x01 code to indicate start of package transmission
									# header - 0 to signify we're transmitting data

		serialData += self.convertDataIntoBytes(paramData)

		if (verbose):
			print("Successfully converted all data into bytes.")
			print("Attempting to send data to device...")

		return self.sendDataToDevice(serialData)

		#if (self.sendDataToDevice(serialData)):
		#	serialData = b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
		# 	self.sendDataToDevice(serialData)
		# 	return self.receiveDataFromDevice(12)

	'''
		Sends a request to the hardware to send over one byte of egram data. 
		returns the byte read, or None if failed
	'''
	def requestEGramData(self):
		serialData = b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
		self.sendDataToDevice(serialData)
		data = self.receiveDataFromDevice(2)
		try:
			print("v: ", str(data[0]), ", a: ", str(data[1]))
			return {'v': data[0], 'a': data[1]}
		except:
			return None

	def receiveDataFromDevice(self, numOfBytes: int):
		try:
			return self.ser.read(size=numOfBytes)	# read one byte
		except serial.SerialException:
			return None

	def sendDataToDevice(self, serialData):
		try:
			res = self.ser.write(serialData)
		except serial.SerialException:
			res = 0

		if (res == 0):	# no data sent
			print("Failed to send data to device:")
			print(serialData)
			return False
		else:
			print("Successfully sent data to device:")
			print(serialData)
			return True

	def plotEgramData(self):
		return GraphEGram().plotEgramData(self)