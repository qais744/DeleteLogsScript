#coded by Qais Temeiza

import os
from datetime import date
import math

noOfDays = 1 #number of days
currentDate = date.today()
directory = "/PATH TO LOG FILES/"
f = open(directory+"ScriptLogs.txt", "a")
f.write("Date of deletion " + str(date.today()) + ":\n")

for fileName in os.listdir(directory):
	if fileName.endswith(".log"):
		noExtFileName = os.path.splitext(fileName)[0]

		try:
			year = noExtFileName[:4]
			month = noExtFileName[4:-2]
			day = noExtFileName[6:]

			fileDate = date(int(year),int(month),int(day))
			dateDiff = (currentDate - fileDate).days

			if dateDiff >= noOfDays:
				f.write(fileName + "\n")
				os.remove(directory+fileName)

		except Exception, e:
			f.write("An error has occured:" + str(e)+"\n")
			continue