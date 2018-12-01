class DeviceSettings:
	def __init__(self):
		self.allModes = [
			'AOO',
			'AAI',
			'VOO',
			'VVI'
			# @TODO - complete listing all possible pacing modes
		]
		self.pacingMode = ''
		self.params = {}

	def setPacingMode(self, pacingMode: str):
		if pacingMode in self.allModes:
			self.pacingMode = pacingMode
			return True
		else:
			return False

	# returns list of possible editable parameters given pacing mode
	def getEditableParameters(self):
		# @TODO - Need to fill appropriately
		if (self.pacingMode == ''):
			return None		# no pacing mode set
		if (self.pacingMode == 'AOO'):
			return ['a', 'b']	
		if (self.pacingMode == 'AAI'):
			return ['a', 'c']
		if (self.pacingMode == 'VOO'):
			return ['d', 'e']
		if (self.pacingMode == 'VVI'):
			return ['d', 'f']	

	''' 
	Returns True or False depending on if user-given value
	is within range of parameter requirements.
	If parameter and value are both valid, set it in user settings
	'''
	def setParameter(self, parameter: str, value):
		# @TODO - Need to fill appropriately
		if (parameter == 'a'):
			# validate example:
			if (value > 30 and value < 50):
				self.params[parameter] = value
				return True
			else:
				return False
		elif (parameter == 'b'):
			pass
		else:
			return False	# invalid parameter string