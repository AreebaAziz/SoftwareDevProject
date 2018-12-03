import pickle
from tkinter import *
import os
from PIL import ImageTk, Image
# from GUIHelper import GUIHelper

class Parameters:

    def __init__(self):
        self.pacingMode = None

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
        possibleParams = [
        "Low Rate Interval",
        "Upper Rate Limit",
        "Maximum Sensor Rate",
        "Fixed AV Delay",
        "Dynamic AV Delay",
        "Sensed AV Delay",
        "Atrial Amplitude",
        "Ventricular Amplitude (mV)",
        "Atrial Pulse Width",
        "Ventricular Pace Width (10 ms)",
        "Atrial Sensitivity",
        "Ventricular Sensitivity",
        "VRP (ms)",
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
        self.pacingMode = pacingMode

        if pacingMode == "AAT":
            programmableParameters = ["Low Rate Interval", "Upper Rate Limit", "Atrial Amplitude", "Ventricular Amplitude (mV)", "Atrial Sensitivity", "ARP", "PVARP"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "VVT":
            programmableParameters = ["Low Rate Interval", "Upper Rate Limit", "Ventricular Amplitude (mV)", "Ventricular Pace Width (10 ms)", "Ventricular Sensitivity", "VRP (ms)"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "AOO":
            programmableParameters = ["Low Rate Interval", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "AAI":
            programmableParameters = ["Low Rate Interval", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width", "Atrial Sensitivity", "ARP", "PVARP", "Hysteresis", "Rate Smoothing"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "VOO":
            programmableParameters = ["Low Rate Interval", "Upper Rate Limit", "Ventricular Amplitude (mV)", "Ventricular Pace Width (10 ms)"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "VVI":
            programmableParameters = ["Low Rate Interval", "Upper Rate Limit", "Ventricular Amplitude (mV)", "Ventricular Pace Width (10 ms)", "Ventricular Sensitivity", "VRP (ms)", "Hysteresis", "Rate Smoothing"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "VDD":
            programmableParameters = ["Low Rate Interval", "Upper Rate Limit", "Fixed AV Delay", "Dynamic AV Delay", "Ventricular Amplitude (mV)", "Ventricular Pace Width (10 ms)","Ventricular Sensitivity", "VRP (ms)", "PVARP Extension", "Rate Smoothing", "ATR Duration", "ATR Fallback Mode", "ATR Fallback Time"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "DOO":
            programmableParameters = ["Low Rate Interval","Upper Rate Limit","Fixed AV Delay","Atrial Amplitude","Ventricular Amplitude (mV)","Atrial Pulse Width","Ventricular Pace Width (10 ms)"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "DDI":
            programmableParameters = ["Low Rate Interval","Upper Rate Limit","Fixed AV Delay","Atrial Amplitude","Ventricular Amplitude (mV)","Atrial Pulse Width","Ventricular Pace Width (10 ms)","Atrial Sensitivity","Ventricular Sensitivity","VRP (ms)","ARP","PVARP"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "DDD":
            programmableParameters = ["Low Rate Interval", "Upper Rate Limit", "Fixed AV Delay", "Dynamic AV Delay", "Sensed AV Delay Offset", "Atrial Amplitude", "Ventricular Amplitude (mV)", "Atrial Pulse Width", "Ventricular Pace Width (10 ms)", "Atrial Sensitivity", "Ventricular Sensitivity", "VRP (ms)", "ARP", "PVARP", "PVARP Extension", "Hysteresis", "Rate Smoothing", "ATR Duration", "ATR Fallback Mode", "ATR Fallback Time"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "AAOR":
            programmableParameters = ["Low Rate Interval", "Upper Rate Limit", "Maximum Sensor Rate", "Atrial Amplitude", "Atrial Pulse Width", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "AAIR":
            programmableParameters = ["Low Rate Interval", "Upper Rate Limit", "Maximum Sensor Rate", "Atrial Amplitude", "Atrial Pulse Width", "Atrial Sensitivity", "ARP", "Hysteresis", "Rate Smoothing", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)

        elif pacingMode == "VOOR":
            programmableParameters = ["Low Rate Interval","Upper Rate Limit","Maximum Sensor Rate","Ventricular Amplitude (mV)","Ventricular Pace Width (10 ms)","Activity Threshold","Reaction Time","Response Factor","Recovery Time"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)
        
        elif pacingMode == "VVIR":
            programmableParameters = ["Low Rate Interval", "Upper Rate Limit", "Maximum Sensor Rate", "Ventricular Amplitude (mV)", "Ventricular Pace Width (10 ms)", "Ventricular Sensitivity", "VRP (ms)", "Hysteresis", "Rate Smoothing", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"]
            self.paramaterEntryObjects = gui.showEntryParam(programmableParameters, possible)
        else:
            print ('NOPE')

    def checkParamValid(self, gui, entryid, enteredVal):
        if entryid == "Low Rate Interval":
            if (enteredVal):
                try:
                    lowerRateLimit = float(enteredVal)
                except:
                    gui.acceptOrRejectParam("error")
                if (lowerRateLimit < 57.0 or lowerRateLimit > 73.0):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(lowerRateLimit)

        elif entryid == "Upper Rate Limit":
            if (enteredVal):
                upperRateLim = float(enteredVal)
                if (upperRateLim < 112 or upperRateLim > 128):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(upperRateLim)

        elif entryid == "Maximum Sensor Rate":
            if (enteredVal):
                maxSensorRate = float(enteredVal)
                if (maxSensorRate < 116 or maxSensorRate > 124):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(maxSensorRate)

        elif entryid == "Fixed AV Delay":
            if (enteredVal):
                fixedAVDelay = float(enteredVal)
                if (fixedAVDelay < 142 or fixedAVDelay > 158):
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
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(sensedAVDelayOffset)

        elif entryid == "Atrial Amplitude":
            if (enteredVal):
                atrialAmp = float(enteredVal)
                if (atrialAmp < 0.5 or atrialAmp > 5.0):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(atrialAmp)

        elif entryid == "Ventricular Amplitude (mV)":
            if (enteredVal):
                VentricularAmp = float(enteredVal)
                if (VentricularAmp < 500 or VentricularAmp > 7000):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(VentricularAmp)

        elif entryid == "Atrial Pulse Width":
            if (enteredVal):
                atrialPulseWidth = float(enteredVal)
                if (atrialPulseWidth < 0.2 or atrialPulseWidth > 0.6):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(atrialPulseWidth)
                    
        elif entryid == "Ventricular Pace Width (10 ms)":
            if (enteredVal):
                ventricularPulseWidth = float(enteredVal)
                if (ventricularPulseWidth < 1 or ventricularPulseWidth > 19):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(ventricularPulseWidth)

        elif entryid == "Atrial Sensitivity":
            if (enteredVal):
                atrialSensitivity = float(enteredVal)
                if (atrialSensitivity < 0.6 or atrialSensitivity > 0.9):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(atrialSensitivity)

        elif entryid == "Ventricular Sensitivity":
            if (enteredVal):
                ventricularSensitivity = float(enteredVal)
                if (ventricularSensitivity < 2 or ventricularSensitivity > 3):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(ventricularSensitivity)

        elif entryid == "VRP (ms)":
            if (enteredVal):
                VRP = float(enteredVal)
                if (VRP < 150 or VRP > 500):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(VRP)

        elif entryid == "ARP":
            if (enteredVal):
                arp = float(enteredVal)
                if (arp < 242 or arp > 258):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(arp)

        elif entryid == "PVARP":
            if (enteredVal):
                pvarp = float(enteredVal)
                if (pvarp < 242 or pvarp > 258):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(pvarp)

        elif entryid == "PVARP Extension":
            if (enteredVal):
                if (enteredVal == "OFF" or enteredVal =="Off" or enteredVal == "off"):
                    # 0 means off
                    gui.acceptOrRejectParam(0)
                elif(float(enteredVal) < 50 or float(enteredVal) > 400):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(float(enteredVal))

        elif entryid == "Hysteresis":
            if(enteredVal):
                if(enteredVal == "True" or enteredVal == "TRUE" or enteredVal == "true"):
                    # 1 means true
                    gui.acceptOrRejectParam(1)
                elif(enteredVal == "False" or enteredVal == "FALSE" or enteredVal == "false"):
                    # 0 means false
                    gui.acceptOrRejectParam(0)
                else:
                    error = "error"
                    gui.acceptOrRejectParam(error)

        elif entryid == "Rate Smoothing":
            if(enteredVal):
                if(enteredVal == "OFF" or enteredVal == "Off" or enteredVal == "off"):
                    gui.acceptOrRejectParam(0)
                elif(int(enteredVal)%3 == 0 and int(enteredVal) < 21):
                    gui.acceptOrRejectParam(int(enteredVal))
                else:
                    error = "error"
                    gui.acceptOrRejectParam(error)
        
        elif entryid == "ATR Duration":
            if(enteredVal):
                atrDuration = float(enteredVal)
                if(atrDuration < 20 or atrDuration > 80):
                    gui.acceptOrRejectParam(atrDuration)
                else:
                    error = "error"
                    gui.acceptOrRejectParam(error)

        elif entryid == "ATR Fallback Mode":
            if (enteredVal):
                if(enteredVal == "OFF" or enteredVal == "Off" or enteredVal == "off"):
                    gui.acceptOrRejectParam(0)
                elif(enteredVal == "ON" or enteredVal == "On" or enteredVal == "on"):
                    gui.acceptOrRejectParam(1)
                else:
                    error = "error"
                    gui.acceptOrRejectParam(error)

        elif entryid == "ATR Fallback Time":
            if(enteredVal):
                atrFallbackTime = float(enteredVal)
                if(atrFallbackTime < 1 or atrFallbackTime > 5):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(atrFallbackTime)

        elif entryid == "Activity Threshold":
            if(enteredVal):
                if (enteredVal == "high" or enteredVal == "HIGH" or enteredVal == "High"):
                    # 1 is HIGH
                    gui.acceptOrRejectParam(1)
                elif (enteredVal == "low" or enteredVal == "LOW" or enteredVal == "Low"):
                    # 0 is LOW
                    gui.acceptOrRejectParam(0)
                elif (enteredVal == "med" or enteredVal == "MED" or enteredVal == "Med"):
                    # 0.5 is MEDIUM
                    gui.acceptOrRejectParam(0.5)
                else:
                    error = "error"
                    gui.acceptOrRejectParam(error)
            
        elif entryid == "Reaction Time":
            if(enteredVal):
                reactionTime = float(enteredVal)
                if(reactionTime < 10 or reactionTime > 50):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(reactionTime)
            
        elif entryid == "Response Factor":
            if(enteredVal):
                responseFactor = float(enteredVal)
                if(responseFactor < 1 or responseFactor > 16):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(responseFactor)

        elif entryid == "Recovery Time":
            if(enteredVal):
                recoveryTime = float(enteredVal)
                if(recoveryTime < 2 or recoveryTime > 16):
                    error = "error"
                    gui.acceptOrRejectParam(error)
                else:
                    gui.acceptOrRejectParam(recoveryTime)

        else:
            print ('NOPE')

    def getCurrentParamData(self):
        paramDict = {'pacingMode': self.pacingMode}
        for paramName, entryObject in self.paramaterEntryObjects.items():
            if (entryObject.get() is not ''):
                paramDict[paramName] = entryObject.get()

        if 'hysteresis' in paramDict:
            if(paramDict['hysteresis'] == "True" or paramDict['hysteresis'] == "TRUE" or paramDict['hysteresis'] == "true"):
                paramDict['hysteresis'] = True
            else:
                paramDict['hysteresis'] = False

        if 'hysteresisLevel' in paramDict:
            paramDict['hysteresisLevel'] = int(paramDict['hysteresisLevel'])

        if 'Low Rate Interval' in paramDict:
            print(paramDict['Low Rate Interval'])
            paramDict['Low Rate Interval'] = int(paramDict['Low Rate Interval'])

        if 'Ventricular Amplitude (mV)' in paramDict:
            paramDict['Ventricular Amplitude (mV)'] = int(paramDict['Ventricular Amplitude (mV)'])

        if 'Ventricular Pace Width (10 ms)' in paramDict:
            paramDict['Ventricular Pace Width (10 ms)'] = int(paramDict['Ventricular Pace Width (10 ms)'])

        if 'VRP' in paramDict:
            paramDict['Ventricular Pace Width (10 ms)'] = int(paramDict['Ventricular Pace Width (10 ms)'])

        return paramDict