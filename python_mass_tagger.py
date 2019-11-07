#!/usr/bin/env python3
"""
Quick and dirty (for now)
Reads file with tag names, sets title tag and track number of files in directory _en mass_
They are set to the contents of the lines inside a file ("taglist" file)
If necessary add numeric prefix to the names of the files so they sort correctly and align with the file

DON'T RUN THIS IN THE SAME DIRECTORY, AND KEEP THE TAGLIST FILE IN ANOTHER DIRECTORY ALSO

Requitements: 
Debian/Ubuntu id3 package

Argument 1: Directory
Argument 2: Filename that contains titles ("taglist")
Argument 3: If anything is provided it will execute, otherwise it will preview
"""

import os
import sys

taglist =  [line.rstrip('\n') for line in open(sys.argv[2])]
index = 0

for fichier in sorted(os.listdir(sys.argv[1])):
    command_string  = 'id3 -T ' + str(index+1) + ' -t "' + str(taglist[index:index+1][0]) +  '" ' + '"' + str(sys.argv[1]) + fichier + '"'
    if len(sys.argv) > 3:
        print("executing " + str(command_string) + ":")
        os.system(command_string)
    else:
        print("command preview:  " + command_string)
    index += 1
