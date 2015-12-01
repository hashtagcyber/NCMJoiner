#!/usr/bin/python
from sys import argv
import glob
targetdir=argv[1]
endswith=argv[2]

#Create an Array listing all files in the target directory
almosthost=glob.glob(targetdir+"*"+endswith)
hostlist=[]
# Strip the 
for i in almosthost:
	hostlist.append(i.rstrip(endswith))
for host in hostlist:
	hostfiles=[]
	hostfiles.append(host+"showversion")
	hostfiles.append(host+"showrun")
	hostfiles.append(host+"showcdpneighboor")
	with open(host + "results.txt",'w') as outfile:
		for fname in hostfiles:
			with open(fname) as infile:
				outfile.write(infile.read())
