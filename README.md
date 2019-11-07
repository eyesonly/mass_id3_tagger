# mass_id3_tagger
## Sets title tag and track number of files in directory _en mass_ to match what is in a file

## Arguments:
1.  Argument 1: Directory with files to be tagged. If necessary add a numeric prefix to file names to make them sort to match file
2.  Argument 2: Filename, each line is the text of the track title to use
3.  Argument 3: If set to anything will execute the change, otherwise it will preview

## Requirements
id3v2 package (on Debian/Ubuntu). So, not for Windows then, I guess

## Example of command call
```
./python_mass_tagger.py Album_folder_containing_files_to_tag/ Path_to/taglist.txt make_it_so
```
