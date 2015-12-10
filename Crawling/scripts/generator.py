import os
import shutil
import random

"""
@author Nils Bouchardon
"""


file = open("testSet.txt",'w')

for i in range(1,2000):
	
	file.write('show'+str(i)+'\t'+str(random.uniform(0,1))+'\t'+str(random.uniform(0,1))+'\t'+str(random.uniform(0,1))+'\t'+str(random.uniform(0,1)) +'\n')


file.close()