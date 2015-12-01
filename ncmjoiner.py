#!/usr/bin/python
from sys import argv
import glob
#directory where files to cat are stored
targetdir=argv[1]
#end of text file to parse against
endswith=argv[2]
#list of endings that files will have
endfile=argv[3]

#Create a python list containing the end of filenames with newlines
mylist = open(endfile).readlines()
#Get ride of the newlines
strippedlist=[]
for i in mylist:
	strippedlist.append(i.strip())
#Create an Array listing all files in the target directory
almosthost=glob.glob(targetdir+"*"+endswith)
hostlist=[]
# Strip the endwith off to get a list of hostnames
for i in almosthost:
	hostlist.append(i.rstrip(endswith))
#iterate through hosts
for host in hostlist:
	hostfiles=[]
#Create a list of hostfiles to concat based on strippedlist from earlier
	for ending in strippedlist:
		hostfiles.append(host+ending)
# Iterate through files in hostlist, concat them
	with open(host + "results.txt",'w') as outfile:
		for fname in hostfiles:
			with open(fname) as infile:
				outfile.write(infile.read())
