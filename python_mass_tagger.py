#!/usr/bin/env python3
"""
Quick and dirty (for now)
Reads file with tag names, sets title tag (and maybe artist) and track number of files in directory _en mass_
They are set to the contents of the lines inside a file ("taglist" file)
If necessary add numeric prefix to the names of the files so they sort correctly and align with the file

DON'T KEEP THIS FILE OR THE TAGLIST FILE IN THE SAME DIRECTORY AS THE MUSIC FILES AS IT WILL CONFUSE THE FILE ORDER

Requirements: 
Debian/Ubuntu id3v2 package

Argument 1: Directory which contains mp3 files to be tagged
Argument 2: Filename that contains titles/artist ("taglist"), example of row 

(artist TAB title):
Planxty 	The Raggle Taggle Gypsy

If there isn't a tab then the row is assumed to just be the title. 

There must be the same number of rows as files to be tagged and they must be sorted the same

Argument 3: If anything is provided it will execute, otherwise it will preview
"""

import os
import sys
import pdb

taglist =  [line.rstrip('\n') for line in open(sys.argv[2])]
index = 0

for fichier in sorted(os.listdir(sys.argv[1])):
    tagline = str(taglist[index:index+1][0]).strip()    
    tag_artist = tagline.split('\t')[0].strip()
    try:
        tag_title = tagline.split('\t')[1].strip()
    except IndexError:
        tag_artist = tagline
    
    if tag_artist == tagline:
        command_string  = 'id3v2 -T ' + str(index+1) + ' -t "' + tagline +  '" ' + '"' + str(sys.argv[1]) + fichier + '"'
    else:
        command_string  = 'id3v2 -T ' + str(index+1) + ' -t "' + tag_title + '" -a "' + tag_artist +  '" ' + '"' + str(sys.argv[1]) + fichier + '"'
        
    if len(sys.argv) > 3:
        print("executing " + str(command_string) + ":")
        os.system(command_string)
    else:
        print("command preview:  " + command_string)
        # print(tag_title)
    index += 1
