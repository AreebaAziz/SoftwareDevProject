import pickle
from tkinter import *
import os
from PIL import ImageTk, Image
# from GUIHelper import GUIHelper

class Parameters:

    def pacingModeList(self):
        pacingModes = ["AAT", 
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
        return pacingModes

    def displayParams(self, gui, pacingMode):
        possibleParams = ["Lower Rate Limit",
        "Upper Rate Limit",
        "Maximum Sensor Rate",
        "Fixed AV Delay",
        "Dynamic AV Delay",
        "Sensed AV Delay",
        "Atrial Amplitude",
        "Ventricular Amplitude",
        "Atrial Pulse Width",
        "Ventricular Pulse Width",
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
        gui.showParam(possibleParams)
        print(pacingMode.get())
        self.checkPacingMode(gui, possibleParams, pacingMode.get())
        

    def checkPacingMode(self, gui, possible, pacingMode):
        print(pacingMode)
        if pacingMode == "AAT":
            programmableParameters = ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Ventricular Amplitude", "Atrial Sensitivity", "ARP", "PVARP"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "VVT":
            programmableParameters = ["Lower Rate Limit", "Upper Rate Limit", "Ventricular Amplitude", "Ventricular Pulse Width", "Ventricular Sensitivity", "VRP"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "AOO":
            programmableParameters = ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "AAI":
            programmableParameters = ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width", "Atrial Sensitivity", "ARP", "PVARP", "Hysteresis", "Rate Smoothing"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "VOO":
            programmableParameters = ["Lower Rate Limit", "Upper Rate Limit", "Ventricular Amplitude", "Ventricular Pulse Width"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "VVI":
            programmableParameters = ["Lower Rate Limit", "Upper Rate Limit", "Ventricular Amplitude", "Ventricular Pulse Width", "Ventricular Sensitivity", "VRP", "Hysteresis", "Rate Smoothing"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "VDD":
            programmableParameters = ["Lower Rate Limit", "Upper Rate Limit", "Fixed AV Delay", "Dynamic AV Delay", "Ventricular Amplitude", "Ventricular Pulse Width","Ventricular Sensitivity", "VRP", "PVARP Extension", "Rate Smoothing", "ATR Duration", "ATR Fallback Mode", "ATR Fallback Time"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "DOO":
            programmableParameters = ["Lower Rate Limit","Upper Rate Limit","Fixed AV Delay","Atrial Amplitude","Ventricular Amplitude","Atrial Pulse Width","Ventricular Pulse Width"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "DDI":
            programmableParameters = ["Lower Rate Limit","Upper Rate Limit","Fixed AV Delay","Atrial Amplitude","Ventricular Amplitude","Atrial Pulse Width","Ventricular Pulse Width","Atrial Sensitivity","Ventricular Sensitivity","VRP","ARP","PVARP"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "DDD":
            programmableParameters = ["Lower Rate Limit", "Upper Rate Limit", "Fixed AV Delay", "Dynamic AV Delay", "Sensed AV Delay Offset", "Atrial Amplitude", "Ventricular Amplitude", "Atrial Pulse Width", "Ventricular Pulse Width", "Atrial Sensitivity", "Ventricular Sensitivity", "VRP", "ARP", "PVARP", "PVARP Extension", "Hysteresis", "Rate Smoothing", "ATR Duration", "ATR Fallback Mode", "ATR Fallback Time"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "AAOR":
            programmableParameters = ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Atrial Amplitude", "Atrial Pulse Width", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "AAIR":
            programmableParameters = ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Atrial Amplitude", "Atrial Pulse Width", "Atrial Sensitivity", "ARP", "Hysteresis", "Rate Smoothing", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"]
            gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "VOOR":
            programmableParameters = ["Lower Rate Limit","Upper Rate Limit","Maximum Sensor Rate","Ventricular Amplitude","Ventricular Pulse Width","Activity Threshold","Reaction Time","Response Factor","Recovery Time"]
            gui.showEntryParam(programmableParameters, possible)
        
        elif pacingMode == "VVIR":
            programmableParameters = ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Ventricular Amplitude", "Ventricular Pulse Width", "Ventricular Sensitivity", "VRP", "Hysteresis", "Rate Smoothing", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"]
            gui.showEntryParam(programmableParameters, possible)
        else:
            print ('NOPE')

    def checkParamValid(self, gui, entryid, enteredVal):
        if entryid == "Lower Rate Limit":
            if (enteredVal):
                lowerRateLimit = float(enteredVal)
                if (lowerRateLimit < 57.0 or lowerRateLimit > 73.0):
                    error = str(lowerRateLimit)
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(lowerRateLimit)

        elif entryid == "Upper Rate Limit":
            if (enteredVal):
                upperRateLim = float(enteredVal)
                if (upperRateLim < 112 or upperRateLim > 128):
                    error = str(upperRateLim)
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(upperRateLim)

        elif entryid == "Maximum Sensor Rate":
            if (enteredVal):
                maxSensorRate = float(enteredVal)
                if (maxSensorRate < 116 or maxSensorRate > 124):
                    error = str(maxSensorRate)
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(maxSensorRate)

        elif entryid == "Fixed AV Delay":
            if (enteredVal):
                fixedAVDelay = float(enteredVal)
                if (fixedAVDelay < 142 or fixedAVDelay > 158):
                    error = str(fixedAVDelay)
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(fixedAVDelay)

        elif entryid == "Dynamic AV Delay":
            if (enteredVal):
                if (enteredVal == "ON" or enteredVal == "on" or enteredVal == "On"):
                    # 1 means on 
                    gui.acceptOrRejectParam(1)
                elif(enteredVal == "OFF" or enteredVal =="Off" or enteredVal == "off"):
                    # 0 means off
                    gui.acceptOrRejectParam(0)
                else:
                    error = "error"
                    gui.acceptOrRejectParam(error)

        elif entryid == "Sensed AV Delay Offset":
            if (enteredVal):
                sensedAVDelayOffset = float(enteredVal)
                if (sensedAVDelayOffset < 142 or sensedAVDelayOffset > 158):
                    error = str(sensedAVDelayOffset)
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(sensedAVDelayOffset)

        elif entryid == "Atrial Amplitude":
            pass
        elif entryid == "Ventricular Amplitude":
            pass
        elif entryid == "Atrial Pulse Width":
            pass
        elif entryid == "Ventricular Pulse Width":
            pass
        elif entryid == "Atrial Sensitivity":
            pass
        elif entryid == "Ventricular Sensitivity":
            pass
        elif entryid == "VRP":
            pass
        elif entryid == "ARP":
            pass
        elif entryid == "PVARP":
            pass
        elif entryid == "PVARP Extension":
            pass
        elif entryid == "Hysteresis":
            pass
        elif entryid == "Rate Smoothing":
            pass
        elif entryid == "ATR Duration":
            pass
        elif entryid == "ATR Fallback Mode":
            pass
        elif entryid == "ATR Fallback Time":
            pass
        elif entryid == "Activity Threshold":
            pass
        elif entryid == "Reaction Time":
            pass
        elif entryid == "Response Factor":
            pass
        elif entryid == "Recovery Time":
            pass
        else:
            print ('NOPE')
