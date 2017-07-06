#!/usr/bin/python3.5
import sys
import os
print(sys.argv[1])
newfile=open(("/home/trump/Desktop/rshit/results/newfile"+sys.argv[1]+".txt"),"w")
with open(("/home/trump/Desktop/rshit/prepython/test"+str(sys.argv[1])+".txt"), "r") as f:
	for line in f:
		for a in line:
			if a!="\"":
				if a!=";":
					newfile.write(a)
				else:
					newfile.write(",")
		newfile.write("\n")		
			



