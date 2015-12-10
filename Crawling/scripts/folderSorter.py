import os
import shutil

"""
@author Nils Bouchardon
"""


currentPath = os.getcwd()
listOfDir = os.listdir(currentPath)

for dir in listOfDir:
	if os.path.isdir(dir):
		splitedDir = dir.split(' - ')
		destDir = splitedDir[0]
		
		if not os.path.exists(destDir):
			os.makedirs(destDir)
		
		os.rename(dir,destDir+'/'+splitedDir[1].split('.')[0])	
