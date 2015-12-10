import os


"""
@author Nils Bouchardon
"""


currentPath = os.getcwd()
listOfDir = os.listdir(currentPath)

for dir1 in listOfDir:
	if (not dir1.startswith('.')) and  os.path.isdir(dir1):
		
		for dir2 in os.listdir(currentPath+'/'+dir1):
			if (not dir2.startswith('.')) and os.path.isdir(dir1+"/"+dir2):

				for ep in os.listdir(currentPath+'/'+dir1+"/"+dir2):
					
					prefix = currentPath+'/'+dir1+"/"+dir2+"/"
					
					if ep.endswith(".txt"):
						os.remove(prefix+ep)
					else:	
						try:
							os.rename(prefix+ep,prefix+ep.split(' - ')[1]+".srt")
						except:
							os.remove(prefix+ep)