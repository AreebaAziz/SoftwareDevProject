import matplotlib.pyplot as plt
import matplotlib.animation as anim 

class GraphEGram:
	#this function returns the analog value of voltage
	def getVoltage(self, rawValue: int):
		return (5.0 * float(rawValue)) / (pow(2, 8) - 1) #convert to analog voltage based on equation

	def plotEgramData(self, deviceCommunication):
		minX = 0
		maxX = 200
		x = [minX] 
		data = deviceCommunication.requestEGramData()
		y_vent = [self.getVoltage(data['v'])]
		y_atr = [self.getVoltage(data['a'])]
    
		fig = plt.figure()
		plt.ion()   #set the plot to be on interactive mode
		minY = 0
		maxY = 300
		plt.axis([minX, maxX, minY, maxY])
		axes = fig.add_subplot(111)
		line_vent, = axes.plot(x, y_vent, 'r-') # Returns a tuple of line objects, thus the comma
		line_atr, = axes.plot(x, y_atr, 'blue')
		axes.set_xlabel("Time (s)")
		axes.set_ylabel("Voltage (V)")

		for i in range(minX, 101):
		    data = deviceCommunication.requestEGramData()
		    y_vent.append(self.getVoltage(data['v']))
		    y_atr.append(self.getVoltage(data['a']))
		    x.append(i/10.0)
		    line_vent.set_data(x, y_vent)
		    line_atr.set_data(x, y_atr)
		    plt.draw()

		plt.tight_layout()

		def update(i):
			data = deviceCommunication.requestEGramData()
			y_vent.append(self.getVoltage(data['v']))
			y_atr.append(self.getVoltage(data['a']))
			x = range(len(y_vent))
			axes.clear()
			axes.grid(True)
			axes.set_xlabel("Time (s)")
			axes.set_ylabel("Voltage (V)")
			axes.plot(x[i:], y_vent[i:])
			axes.plot(x[i:], y_atr[i:])

		a = anim.FuncAnimation(fig, update, frames=maxX, repeat=True)
		plt.show(block=True)
		