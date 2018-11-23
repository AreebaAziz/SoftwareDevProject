import pickle
from tkinter import *
import os
from PIL import ImageTk, Image

class Parameters:
    def pacingModeList(self):
        pacingModes = [
        "AAT", 
        "VVT", 
        "AOO",
        "AAI",
        "VOO",
        "VVI",
        "VDD",
        "DOO",
        "DDI",
        "DDD",
        "AOOR",
        "AAIR",
        "VOOR",
        "VVIR",
        "VDDR",
        "DOOR",
        "DDIR",
        "DDDR"]
        # call on function createMenu to create the option list
        #selectedMode = gui.CreateMenu(20, 20, pacingModes)
        #gui.CreateButton(40, 30, 'OK', self.checkPacingMode(selectedMode))


    def checkPacingMode(self,pacingMode):
        possibleParams = ["Lower Rate Limit",
        "Upper Rate Limit",
        "Maximum Sensor Rate",
        "Fixed AV Delay",
        "Dynamic AV Delay",
        "Sensed AV Delay",
        "Atrial Amplitude",
        "Ventricular Amplitude",
        "Atrial Pulse Width",
        "Atrial Sensitivity",
        "Ventricular Sensitivity",
        "VRP",
        "ARP",
        "PVARP",
        "PVARP Extension",
        "Hysteresis", 
        "Rate Smoothing",
        "ATR Duration",
        "ATR Fallback Mode",
        "ATR Fallback Time",
        "Activity Threshold",
        "Reaction Time",
        "Response Factor",
        "Recovery Time"]

        yvalue = 30
        for i in possibleParams:
            #gui.CreateParameter(i, yvalue)
            yvalue += 30

        def createInputBoxes(programmable):
            for j in programmable:
                if j in possibleParams:
                    yvalue = (j+1)*30
                   # gui.CreateEntryParam(yvalue)
                    #gui.CreateButton(85, yvalue, 20, 'Check', checkParams)
                    ##where x=85, 20=width
                    # getParam is a function that tells you which param needs to be checked

        if pacingMode == "AAT":
            programmableParameters = [0, 1, 6, 8, 10, 13, 14]
            createInputBoxes(programmableParameters)

        if pacingMode == "VVT":
            programmableParameters = [0, 1, 7, 9, 11, 12]
            createInputBoxes(programmableParameters)

        if pacingMode == "AOO":
            programmableParameters = [0, 1, 6, 8]
            createInputBoxes(programmableParameters)

        if pacingMode == "AAI":
            programmableParameters = [0, 1, 6, 8, 10, 13, 14, 16, 17]
            createInputBoxes(programmableParameters)

        if pacingMode == "VOO":
            programmableParameters = [0, 1, 7, 9]
            createInputBoxes(programmableParameters)

        if pacingMode == "VVI":
            programmableParameters = [0, 1, 7, 9, 11, 12, 16, 17]
            createInputBoxes(programmableParameters)

        if pacingMode == "VDD":
            programmableParameters = [0, 1, 3, 4, 7, 9, 11, 12, 15, 17, 18, 19, 20]
            createInputBoxes(programmableParameters)

        if pacingMode == "DOO":
            programmableParameters = [0, 1, 3, 6, 7, 8, 9]
            createInputBoxes(programmableParameters)

        if pacingMode == "DDI":
            programmableParameters = [0, 1, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            createInputBoxes(programmableParameters)

        if pacingMode == "DDD":
            programmableParameters = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
            createInputBoxes(programmableParameters)

        if pacingMode == "AAOR":
            programmableParameters = [0, 1, 2, 6, 8, 21, 22, 23, 24]
            createInputBoxes(programmableParameters)

        if pacingMode == "AAIR":
            programmableParameters = [0, 1, 2, 6, 8, 10, 13, 16, 17, 21, 22, 23, 24]
            createInputBoxes(programmableParameters)

        if pacingMode == "VOOR":
            programmableParameters = [0, 1, 2, 7, 9, 21, 22, 23, 24]
            createInputBoxes(programmableParameters)
        
        if pacingMode == "VVIR":
            programmableParameters = [0, 1, 2, 7, 9, 11, 12, 16, 17, 21, 22, 23, 24]
            createInputBoxes(programmableParameters)