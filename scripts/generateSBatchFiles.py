#!/usr/bin/python3

##################################################
## Python script to generate 
#
## $ python3 generateSBatchFiles.py -h
#
##################################################
## Author: RoiArthurB
## Copyright: Copyright 2020, COMOKIT, COMO-TK
## Licence: LGPL 3.0
## Version: 1.0.0
## Maintainer: RoiArthurB
##################################################

import os
import argparse

#
#	MAIN
#
if __name__ == '__main__':

	# 0 _ Get/Set parameters
	# 
	parser = argparse.ArgumentParser()

	#	SLURM settings
	parser.add_argument('-n', '--node', metavar='', help="Number of nodes to dispatch your exploration on", default=1, type=int)
	parser.add_argument('-c', '--core', metavar='', help="Number of cores per node", default=-1, type=int)
	#	GAMA Headless settings
	parser.add_argument('-f', '--folder', metavar='', help="Path to folder where your XML are stored (will gather EVERY! XML file)", type=str, required=False)
	parser.add_argument('-x', '--xml', metavar="", help = 'Path to your XML (/path/to/your/headlessExplo.xml)', type=str, required=False)
	parser.add_argument('-g', '--gama', metavar="", help = 'Path to GAMA headless script (/path/to/your/gama/headless/gama-headless.sh)', type=str, required=True)
	parser.add_argument('-F', '--outputFolder', metavar="", help='Path to folder where GAMA will write simulation\'s console output', type=str, default="/tmp/.gama-output")
	#	Script settings
	parser.add_argument('-o', '--output', metavar="", help='Path to your saved conf file (default: "./gama-headless.conf")', type=str, default="./gama-headless.conf")

	args = parser.parse_args()

	# 1 _ Setup environment to be sure to launch
	#
	print("=== Prepare everything")
	# Make gama executable
	os.chmod(args.gama, 0o665)

	# Gather XML in a list
	if args.folder != None:
		if os.path.isdir(args.folder):
			for fname in os.listdir(args.folder)[::-1]:
				if fname.endswith('.xml'):
					xmlList.append( os.path.abspath(args.folder + "/" + fname) )
			if len(xmlList) == 0:
				raise ValueError('The folder doesn\'t contain any XML file.')
		else: 
			raise ValueError('The folder doesn\'t exist.')
	elif args.xml != None:
		if os.path.isfile(args.xml) and args.xml.endswith('.xml'):
			xmlList.append( os.path.abspath(args.xml) )
		else: 
			raise ValueError('The XML file do not exist or is not an XML file.')
	else:
		raise ValueError('You should specify a folder with XML (w/ `-f`) or an XML (w/ `-x`) in your command.\nTry to launch the script with `-h` for full help options.')
