#!/usr/bin/env python
import fnmatch
import os

#rights_array = "Copyright (C) 2011-2017 Intel Corporation All rights reserved".split()
rights_array = "Copyright (C)".split()
suffixs = ['.C', '.EDL', '.CPP', '.CC', '.SH','.H', 'MAKEFILE']
#suffixs = ['H']

valid_files_array = []
invalid_files_array = []

def check_one_file(fp):
	count = 0
	flag = False
	with open(fp, "r") as f:
		for line in f:
			count = 0
			for x in rights_array:
				if x.upper() not in line.upper():
					count = 0
					break
				else:
					count = count + 1
			if count >= len(rights_array):
				flag = True
				break

	return flag

#recursive to find suffix file
def recursive_glob(rootdir='.', suffix=''):
    return [os.path.join(looproot, filename)
            for looproot, _, filenames in os.walk(rootdir)
            for filename in filenames if fnmatch.fnmatch(filename.upper(), "*"+suffix)]

def check_copy_right(rootdir='.'):
	for suffix in suffixs:
		for fp in recursive_glob(rootdir, suffix):
			ret = False;
			ret = check_one_file(fp)
			if ret:
				valid_files_array.append(fp)
			else:
				invalid_files_array.append(fp)

#find some type file
#open and check.
#if contains, record report_array.
#elif record done_array.
if __name__ == "__main__":
	check_copy_right(os.getcwd())
	print("Invalid File\n")
	for x in invalid_files_array:
		print(x)
