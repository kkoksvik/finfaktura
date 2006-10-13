# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faktura.ui'
#
# Created: Thu Oct 12 00:07:42 2006
#      by: The PyQt User Interface Compiler (pyuic) 3.15.1
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *

image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x22\x00\x00\x00\x30" \
    "\x08\x06\x00\x00\x00\x74\x59\xa8\x52\x00\x00\x05" \
    "\x0d\x49\x44\x41\x54\x58\x85\xed\x98\xc1\x72\xdb" \
    "\x36\x10\x86\x3f\x00\x02\x45\x91\xa6\x65\xab\x52" \
    "\x63\xc7\x9d\x4c\x73\xee\xa9\x87\x5e\x3a\x7d\x80" \
    "\x5e\xdb\xe7\xe9\xb5\x4f\xd2\x4b\xdb\x63\x67\xfa" \
    "\x1a\x9d\xcc\x64\xa6\xb9\x25\x51\x62\x39\x4e\xe5" \
    "\x2a\x51\x64\x32\x24\x41\x72\x7b\x90\xc8\x50\xb2" \
    "\xdc\xc6\x8d\xeb\xe6\x90\xbd\x60\xb9\xc0\x02\xff" \
    "\x2e\xb0\xbb\x00\x95\x88\x70\x13\xb4\x58\x2c\x9a" \
    "\x85\xa2\x28\x52\x9b\xfd\xfa\x26\x40\x24\x49\x22" \
    "\xc7\xc7\xc7\x1c\x1f\x1f\x5f\x3a\xe6\x46\x80\x18" \
    "\x63\x28\x8a\x8c\x9d\x9d\x1d\xa2\x28\x22\xcb\x32" \
    "\x49\x92\x64\x6d\x2b\x3a\x35\x33\x9b\xcd\x64\x3a" \
    "\x9d\xe2\xfb\x3e\x07\x07\x07\x74\xbb\xdd\x0b\xee" \
    "\x7b\x47\x38\x14\x45\xc9\xfd\xfb\xf7\x28\x4b\xe8" \
    "\xf7\xf7\xf8\xe4\x93\x23\xb1\xd6\xaa\x06\x48\x96" \
    "\x65\x32\x9f\xbf\x62\x32\x99\x10\x04\x01\xa3\xd1" \
    "\x08\xe7\x9c\x54\x55\xf5\xaf\x96\xd4\x5a\x53\xeb" \
    "\xd6\x06\xed\xed\xed\x61\xad\x25\xcf\x7b\x78\x5e" \
    "\x97\xe1\xf0\x23\xaa\xaa\x22\xcb\x32\xe9\x76\xbb" \
    "\x4a\xe5\x79\x2e\x69\x9a\x62\x8c\x21\x8e\x63\xce" \
    "\xcf\x63\xd2\xf4\x35\x7b\x7b\x7b\xf4\xfb\x7d\xca" \
    "\xb2\x5c\xda\x63\x0c\x65\x59\x5e\x68\x95\x5a\x3a" \
    "\xae\x7d\xe8\xeb\x3e\x80\xb3\xb3\x3f\xc9\xf3\x0c" \
    "\xcf\xeb\x72\xeb\xd6\xc7\x18\x63\xd0\x5a\xe3\x9c" \
    "\xa3\xaa\x2a\xb4\x2e\xb1\x36\xa0\x63\xad\x55\xd6" \
    "\x5a\x00\xc6\xe3\xb1\x3c\x7b\xf6\x8c\xc1\x60\xc0" \
    "\xe1\xe1\xe1\xb5\x6c\xcd\xc9\xc9\x89\xbc\x7a\xf5" \
    "\x8a\x28\x8a\x78\xfa\xf4\x69\x03\x48\x6b\x43\x10" \
    "\x04\xcd\x1a\x9d\xb6\x92\xef\xf7\x38\x3a\x3a\x62" \
    "\x30\x18\x5c\x07\x86\x86\xb2\x2c\x23\x49\x12\x06" \
    "\x83\x3e\x93\xc9\x84\xe7\xcf\x4f\xb9\x75\xeb\x80" \
    "\xbb\x77\x3f\xc5\x39\x27\xd6\x5a\xa5\xda\x2e\x7d" \
    "\xf0\xe0\x81\xf8\x7e\x0f\xad\x15\x9e\xe7\x5d\x8b" \
    "\x57\x1e\x3d\x7a\x2c\x69\xfa\x1a\xad\x35\xb7\x6f" \
    "\xdf\x46\x29\x85\xd6\x7a\xcd\x1b\x00\xea\xa6\x12" \
    "\xda\x3f\xd1\x5a\x1e\x79\xf4\xe8\xb1\xdc\xbf\x7f" \
    "\xef\x42\x8c\x5f\x27\x39\xe7\xb6\xce\xbd\xe6\x91" \
    "\x3a\x64\xb5\xd6\xd4\xf1\x7d\x53\xb4\xe6\x91\x34" \
    "\x4d\xc9\xf3\xfc\x5a\x41\xa4\x69\x26\xed\x3a\x33" \
    "\x9d\x4e\x65\x9b\x57\x9a\xa8\xc9\xb2\x4c\xce\xcf" \
    "\xcf\x6b\x20\xe2\xfb\xbe\x6a\x27\xb5\x76\x92\xaa" \
    "\xa9\x9d\x63\xea\xef\x76\x0e\x31\xc6\xe0\x5c\xce" \
    "\x6c\x36\xc3\x18\x23\x00\x49\x92\xe0\xfb\x3e\x55" \
    "\x55\x09\xbc\x49\x78\x0d\x90\x6e\xb7\xab\xac\xb5" \
    "\xd2\xed\x76\x79\xf1\xe2\x05\x69\x9a\x89\xd6\x8a" \
    "\x20\x08\x48\x92\x04\x00\xcf\xf3\xe8\x74\x3a\xec" \
    "\xee\xee\xbe\x55\x09\xa8\x8d\x0b\x82\x00\x63\x0c" \
    "\xb3\xd9\x0c\xcf\xf3\xb0\xd6\xbb\xa0\xbf\x76\x46" \
    "\x92\x24\x91\x4d\xcb\xdb\x99\xb4\xb6\x7a\x33\xf4" \
    "\xfe\x8e\xd2\x34\x95\xaa\xaa\x08\x82\x40\x65\x59" \
    "\x26\x97\xe9\xbf\x9f\xe1\xfb\x7f\xd2\x07\x20\x9b" \
    "\xf4\x01\xc8\x26\x7d\x00\xb2\x49\x1f\x80\x6c\x52" \
    "\xa7\xae\x84\xd6\x5a\x55\x5f\xdb\x36\x65\x35\x5f" \
    "\x2b\xb5\xc7\xd5\xad\x73\x0e\xad\x97\x76\x19\x63" \
    "\xa8\xaf\x13\xed\xf2\x50\x53\xbb\x28\xd6\xf3\x5e" \
    "\x5b\x8a\x5f\x81\x02\xe0\xf4\x34\x69\x16\xf4\xfd" \
    "\x1e\x4f\x9e\x8c\x89\xa2\xb0\x19\x7b\x78\x78\x40" \
    "\x18\xb2\x59\xf4\xbe\x16\x80\xf1\x58\x38\x3d\x05" \
    "\xa5\xe0\xe5\x4b\x30\x06\x3e\xff\x1c\x06\x83\x0a" \
    "\x68\x5b\x54\x02\x25\x22\xe5\x1a\x10\xa5\x0c\x60" \
    "\x10\xc9\x49\xd3\xb4\x91\x6b\xad\x89\xe3\x18\x6b" \
    "\x77\x58\xbe\x3c\x72\x7a\x3d\x0f\xad\x6d\x4b\xcf" \
    "\x43\x89\x20\x00\xb3\x19\x9c\x9f\x83\xb5\xe0\xdc" \
    "\xb2\x1d\x0e\x97\xed\x45\x1a\x5e\x90\x88\xbc\x46" \
    "\xa9\x78\x6b\x1f\x74\x81\xc9\x8a\x3f\x5a\xb5\xd9" \
    "\x4a\x6f\x8e\x52\xae\x7d\x1f\x81\x3f\xfe\x60\x85" \
    "\x1a\xca\x72\x3b\x08\x91\x08\xa5\x1e\xb3\x58\x54" \
    "\xcd\x23\xa9\xd7\x1b\x12\x86\xbf\x22\xf2\x03\x4a" \
    "\xfd\x88\x73\x0e\xbb\xa1\x2c\xe2\x51\x55\x5f\x30" \
    "\x9d\xfe\x42\x59\xc6\xec\xef\xf7\x09\x82\x3e\xf0" \
    "\x3d\xf0\x1d\x4a\xe4\xdb\xb5\x43\x92\xe7\x6f\x78" \
    "\xcf\x6b\x4f\x64\x51\xca\x01\x1e\x65\xf9\x0d\x45" \
    "\xb1\xbc\xb3\x28\x55\xe0\x79\x21\x70\x82\xc8\x63" \
    "\x94\xfa\x72\x65\x88\xc3\x98\x36\x98\x9f\x81\x21" \
    "\x69\xfa\x15\x65\x99\xe3\xfb\x5d\x8c\xb1\x88\xfc" \
    "\x8e\x52\xbf\xbd\xdb\x61\xad\xa3\x66\x9b\x1c\x2e" \
    "\x46\x9d\x73\x4e\xe2\x38\x46\xa9\x0a\x6b\x2d\xd6" \
    "\xfa\x4d\xd4\x74\xea\xc9\x26\x93\x27\x32\x9b\xcd" \
    "\x88\xa2\x5d\x76\x76\x76\x39\x3b\x3b\xe3\xce\x9d" \
    "\x43\x82\xa0\xaf\xb6\x2d\xd0\x6e\x37\x81\xb5\xe5" \
    "\x6d\xfe\xcd\xfd\xd7\xa2\xb5\x6d\xfa\x9c\x73\xd2" \
    "\x78\x64\x3c\x1e\x4b\x92\x24\x28\xa5\xb0\xd6\xd2" \
    "\xef\xf7\x99\xcf\xe7\xec\xee\xee\x52\x14\x05\xfb" \
    "\xfb\xfb\xf8\xbe\xff\x9f\x3d\x31\xb6\x6e\x4d\x3b" \
    "\x51\xdd\xd4\x3b\xa7\x01\x92\x24\x73\x99\x4e\x5f" \
    "\x02\x10\x45\x11\x83\xc1\xe0\x4a\x0b\x2f\x16\x0b" \
    "\x39\x39\x39\x61\x34\x1a\x11\x86\xcb\xe4\x75\x95" \
    "\x9f\x3d\x4d\xad\x49\x12\xb7\x14\x68\x8d\xef\x9b" \
    "\x4b\x15\x2e\xa3\xe5\x9b\xe8\x35\x8b\xc5\x82\x87" \
    "\x0f\x1f\xb2\x58\x2c\xae\xa4\xdf\x00\x71\xce\xe1" \
    "\x79\x1e\x61\x18\x32\x9f\x27\x64\x59\x76\xa5\x70" \
    "\xea\xf5\x7a\x0c\x06\x03\xaa\x4a\x18\x8d\x46\x0c" \
    "\x87\xc3\xab\x6d\x65\x9e\xe7\x22\x22\x88\x08\xab" \
    "\xbf\x47\x92\xa6\x69\x23\xab\xe5\x9b\xfc\x66\xbb" \
    "\x6d\xec\x36\xf9\x65\x7a\xef\xcd\xbb\xa6\x23\xf2" \
    "\xd9\x7b\x81\xa4\xa3\xd4\x9d\x15\x5b\xb2\x5e\x65" \
    "\x69\xc9\xf9\x9b\x3e\xb3\x85\x6f\x7f\xff\x93\x7c" \
    "\x39\xbf\x12\x11\xe2\x18\x09\x43\xde\x8a\xe2\x18" \
    "\x3c\xcf\x5d\x7b\x5e\xe9\x00\x38\xf7\x12\xd8\x7b" \
    "\x2b\x05\xa5\x12\xaa\xca\x90\x24\x89\xc4\x71\x4c" \
    "\x18\x7a\x18\xe3\x93\xe7\xf9\xda\x3f\xf6\xe9\x74" \
    "\x2a\x4a\x29\x8a\xa2\x20\x0c\xc3\xa6\x6f\x32\x79" \
    "\x22\x45\xb1\x8c\xac\xf6\x63\x5c\x15\xc5\x4f\x52" \
    "\x96\x39\xc6\x78\x5b\x96\x2d\xda\x78\x81\x82\xa2" \
    "\xd0\x74\x3a\xd5\x4a\x56\xac\xf5\xbd\x91\x6d\xb3" \
    "\xf7\x32\xf9\x0a\x88\xc8\xb9\x38\xe7\x61\x6d\x8e" \
    "\x73\x4b\x30\xd6\x2e\xef\x02\x97\x7d\xd7\xb2\xab" \
    "\x8c\xdf\xa6\xd3\xe6\xdf\x9b\xf0\xfd\x0b\xba\x7b" \
    "\x3b\x68\x2e\x95\x4c\x0f\x00\x00\x00\x00\x49\x45" \
    "\x4e\x44\xae\x42\x60\x82"
image1_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x08\x00\x00\x00\x08" \
    "\x08\x06\x00\x00\x00\xc4\x0f\xbe\x8b\x00\x00\x00" \
    "\x47\x49\x44\x41\x54\x18\x95\x85\x8e\xc1\x0d\xc0" \
    "\x30\x08\xc4\x1c\x36\xb8\xfd\x87\xf4\x08\xe9\xa7" \
    "\x54\x28\x79\xd4\x12\x1f\x73\x88\x5b\x2a\x49\xb6" \
    "\xba\x18\xb4\x5b\xc0\x6e\xd9\xa1\x24\x9f\x43\xe5" \
    "\x0d\x5d\xa3\x52\xf3\x72\xd2\xae\xce\xc5\x49\x5d" \
    "\x3f\x47\x49\x80\xdf\x92\xd5\x72\xf6\x98\xee\x01" \
    "\xbc\x80\x33\xa3\xcb\xe0\x0d\xd1\x00\x00\x00\x00" \
    "\x49\x45\x4e\x44\xae\x42\x60\x82"
image2_data = [
"100 100 2165 2",
"cQ c #000000",
"d8 c #000002",
"da c #000004",
"es c #000005",
"dF c #000007",
"d7 c #000008",
"b7 c #000009",
"d6 c #00000a",
"dJ c #00000b",
"dI c #00000c",
"ew c #00000d",
"cN c #00000e",
"ev c #00000f",
"df c #000010",
"eu c #000011",
"dK c #000012",
"ec c #000013",
"d2 c #000015",
"cR c #000100",
"ob c #000102",
"bj c #000103",
"wA c #000104",
"bi c #000105",
"ex c #000106",
"eE c #000108",
"m8 c #000110",
"ed c #000112",
"gG c #000115",
"aM c #000200",
"bk c #000201",
"hf c #000202",
"eZ c #000203",
"xh c #000205",
"eF c #000207",
"s0 c #000209",
"C1 c #00020b",
"kI c #00020e",
"dL c #000213",
"aL c #000300",
"eX c #000302",
"eY c #000304",
"s. c #000308",
"fW c #00030a",
"ee c #00030c",
"gF c #000312",
"aK c #000400",
"mB c #000402",
"rw c #000403",
"D4 c #000405",
"bl c #000500",
"aJ c #000600",
"vd c #000604",
"aI c #000700",
"aH c #000800",
"aN c #000900",
"p4 c #000a00",
"lP c #000b00",
"Et c #000c00",
"uV c #000d00",
"fH c #010000",
"gj c #010002",
"Cx c #010004",
"b3 c #010005",
"b2 c #010006",
"b5 c #010008",
"vP c #010009",
"b6 c #01000a",
"BQ c #01000b",
"cL c #01000c",
"sk c #01000d",
"eb c #01000e",
"cM c #01000f",
"Af c #010010",
"fh c #010011",
"cK c #010100",
"dc c #010101",
"b4 c #010103",
"e# c #010109",
"ea c #01010b",
"dH c #01010d",
"cJ c #010200",
"hi c #010204",
"d9 c #010206",
"eU c #010207",
"bg c #010300",
"bh c #010302",
"C0 c #010310",
"bf c #010400",
"be c #010500",
"lQ c #010504",
"fT c #010600",
"gE c #01060c",
"nT c #010700",
"lY c #010800",
"oi c #010900",
"uz c #010a00",
"DT c #010d00",
"BR c #010e00",
"ws c #011000",
"xD c #020001",
"gh c #020008",
"b8 c #02000b",
"bY c #02000d",
"gm c #02000e",
"de c #020010",
"yM c #020014",
"vo c #020100",
"b1 c #020106",
"b0 c #020107",
"bZ c #020109",
"cI c #020200",
"db c #020202",
"cH c #020204",
"pA c #02020a",
"tL c #02020c",
"dG c #02020e",
"c# c #020300",
"o2 c #020305",
"hj c #020307",
"eV c #020308",
"er c #020400",
"yp c #020403",
"CZ c #020410",
"xU c #020413",
"oA c #020500",
"rK c #020600",
"fk c #020607",
"CL c #020609",
"uR c #020612",
"fj c #020700",
"wQ c #02070a",
"c8 c #020800",
"vN c #020900",
"uG c #020a00",
"qP c #020b00",
"wl c #020d00",
"kG c #020e00",
"ie c #030000",
"iV c #030002",
"Dy c #030004",
"yf c #030005",
"xH c #030007",
"if c #030009",
"xI c #03000b",
"Ce c #03000e",
"Cd c #030010",
"mV c #030011",
"yo c #030013",
"iW c #030102",
"xE c #030106",
"q8 c #03010c",
"dg c #03010e",
"v8 c #03010f",
"fe c #030200",
"eT c #030207",
"fi c #030208",
"cG c #03020a",
"hh c #030212",
"jC c #030300",
"et c #030301",
"vG c #030303",
"bW c #030305",
"uc c #03030b",
"hk c #03030d",
"f2 c #03030f",
"c9 c #030400",
"f0 c #030406",
"eB c #030408",
"yc c #030409",
"bV c #030500",
"wt c #030502",
"jA c #030600",
"fV c #03060b",
"wk c #030708",
"nI c #03070a",
"vC c #030710",
"fo c #030800",
"Cz c #030802",
"w4 c #030804",
"dM c #03080e",
"pH c #030900",
"ig c #030a00",
"he c #030e00",
"w9 c #040000",
"x. c #040005",
"vO c #04000e",
"ye c #040108",
"Cy c #04010a",
"fJ c #040116",
"DR c #040205",
"hW c #04020d",
"cO c #04020f",
"yL c #040210",
"wE c #040301",
"d3 c #040308",
"hZ c #040309",
"gk c #04030b",
"o3 c #040311",
"xF c #040400",
"lu c #040402",
"fI c #040404",
"jm c #040406",
"gH c #04040c",
"ud c #040410",
"kV c #040500",
"eW c #040507",
"eD c #040509",
"f1 c #04050a",
"Bn c #040600",
"o5 c #040603",
"fZ c #040605",
"px c #040700",
"pe c #040800",
"Dw c #040809",
"fl c #04080b",
"m9 c #040811",
"EF c #040900",
"fL c #040a00",
"zS c #040b00",
"CM c #040b04",
"Cr c #040d00",
"EL c #041000",
"D3 c #041100",
"kl c #041200",
"iU c #050004",
"w8 c #050100",
"hx c #050102",
"vQ c #050209",
"gi c #05020b",
"gV c #05020d",
"rg c #050217",
"Di c #050304",
"wd c #050308",
"bX c #05030e",
"hv c #050310",
"iT c #050400",
"fG c #050402",
"cF c #050409",
"cP c #05040a",
"fF c #05040c",
"DQ c #050500",
"j6 c #050503",
"kh c #050505",
"h0 c #050507",
"vw c #05050d",
"AF c #050511",
"mU c #050600",
"d5 c #050601",
"xs c #050608",
"eA c #05060a",
"e. c #05060b",
"xC c #050700",
"uT c #050702",
"j4 c #050704",
"xJ c #050800",
"t# c #050801",
"h2 c #050900",
"oa c #050908",
"fn c #05090a",
"uw c #05090c",
"f3 c #050a00",
"z. c #050a06",
"oQ c #050b00",
"pd c #050d00",
"hA c #050e00",
"qg c #050f00",
"t3 c #051000",
"DS c #06000a",
"Dx c #060200",
"Dj c #060201",
"wG c #060203",
"CI c #060211",
"xG c #060300",
"jD c #06030a",
"CK c #06030c",
"fg c #060314",
"Dh c #060405",
"hy c #060409",
"dh c #06040f",
"gl c #060411",
"dC c #060412",
"C2 c #060501",
"iD c #06050a",
"dE c #06050b",
"n0 c #06050d",
"tU c #060513",
"d4 c #060604",
"jo c #060606",
"ki c #060608",
"py c #06060e",
"By c #060701",
"wz c #060702",
"tx c #060709",
"eC c #06070b",
"o4 c #06070c",
"pz c #060803",
"fX c #060805",
"v3 c #060807",
"Eq c #060900",
"uK c #06090e",
"fm c #060910",
"ca c #060a00",
"fU c #060a09",
"fM c #060c00",
"gn c #060d00",
"C3 c #060d06",
"j3 c #060f00",
"fO c #061000",
"zx c #061400",
"n. c #061500",
"id c #070300",
"CJ c #070311",
"sN c #070415",
"fK c #070417",
"wF c #070508",
"kU c #070510",
"n1 c #070512",
"dd c #070513",
"iS c #070601",
"fd c #070602",
"ns c #07060b",
"b9 c #07060c",
"fE c #07060e",
"d. c #070705",
"wH c #070707",
"d# c #070709",
"ty c #07070f",
"h1 c #070800",
"jB c #070802",
"o7 c #07080c",
"nJ c #07081a",
"fY c #070906",
"o6 c #070908",
"Cq c #070a00",
"qu c #070c00",
"vX c #070c08",
"B# c #070d01",
"fN c #070e00",
"Es c #070f02",
"B1 c #071000",
"Ae c #071100",
"u8 c #071400",
"nt c #080516",
"dD c #080611",
"zf c #080613",
"kj c #08070c",
"di c #08070d",
"yg c #08070f",
"yd c #080717",
"ni c #080806",
"c. c #080808",
"qe c #08080a",
"hz c #080904",
"z1 c #08090b",
"dj c #08090d",
"wP c #08090e",
"vD c #080a05",
"ve c #080a09",
"nK c #080a17",
"uy c #080b00",
"kH c #080b12",
"y9 c #080d09",
"gW c #080f00",
"rm c #081000",
"rf c #081200",
"lg c #081300",
"cS c #081500",
"hX c #090712",
"qp c #090715",
"qE c #09080d",
"lt c #09080e",
"hY c #090810",
"ux c #090907",
"ff c #090909",
"ey c #090a0e",
"uS c #090a1c",
"Dv c #090b06",
"Ap c #090c11",
"qX c #090e00",
"nL c #090e0a",
"kW c #091000",
"pV c #091100",
"ic c #091300",
"z2 c #091400",
"vp c #091500",
"xr c #091600",
"aO c #091700",
"qQ c #0a0718",
"q7 c #0a090f",
"j5 c #0a0a0a",
"jn c #0a0a0c",
"ez c #0a0b0f",
"u9 c #0a0b10",
"sO c #0a0c00",
"iE c #0a0c01",
"ta c #0a0c0b",
"v9 c #0a0f08",
"v2 c #0a0f0b",
"wu c #0a1000",
"ls c #0a1100",
"Ed c #0a110a",
"d1 c #0a1300",
"Ee c #0a1400",
"m7 c #0a1700",
"uQ c #0a1900",
"hw c #0b0704",
"uU c #0b0917",
"tz c #0b0a0f",
"qf c #0b0b0b",
"CY c #0b0c07",
"pW c #0b0d0c",
"vF c #0b0e00",
"xV c #0b0e17",
"dk c #0b0f12",
"BP c #0b1000",
"q6 c #0b1009",
"bU c #0b1100",
"Ep c #0b1200",
"Cs c #0b1400",
"EX c #0b1700",
"aG c #0b1800",
"vH c #0b1900",
"sl c #0c091c",
"yn c #0c0c0a",
"cE c #0c1300",
"tA c #0c1400",
"mC c #0c1900",
"m. c #0c1a00",
"vg c #0c1b00",
"iF c #0d1200",
"y8 c #0d120c",
"v4 c #0d1400",
"rV c #0d1500",
"hV c #0d1900",
"v. c #0d1b00",
"qD c #0d1c00",
"rW c #0e0d13",
"vf c #0e0e10",
"hg c #0e101c",
"Du c #0e1300",
"rF c #0e1800",
"tw c #0e1900",
"rv c #0e1b00",
"qd c #0e1c00",
"o# c #0f1a00",
"mA c #0f1b00",
"gD c #0f1d00",
"A2 c #101010",
"vE c #101300",
"sm c #101302",
"Eb c #101600",
"nr c #101700",
"oz c #101900",
"nH c #101b00",
"fS c #101c00",
"dN c #101f00",
"iX c #110e15",
"kk c #110e17",
"lR c #111700",
"Ct c #111a00",
"wO c #111b00",
"bm c #111c00",
"uv c #111d00",
"r9 c #111e00",
"ef c #111f00",
"pX c #112100",
"jl c #121700",
"bd c #121900",
"cb c #121a00",
"jp c #121b00",
"fp c #121c00",
"vn c #121d00",
"rL c #121f00",
"fP c #122000",
"C4 c #122500",
"xB c #131900",
"ue c #131a00",
"AN c #131b00",
"pl c #131c00",
"Cw c #131f00",
"yy c #132300",
"v7 c #141a00",
"w3 c #141c00",
"go c #141d00",
"iC c #142100",
"yz c #142400",
"Bo c #151b00",
"pw c #151d00",
"tV c #151e00",
"o1 c #151f00",
"dB c #152000",
"Cu c #152100",
"sd c #152300",
"fQ c #152400",
"sj c #161e00",
"iR c #162000",
"tl c #162200",
"sZ c #162300",
"ah c #162400",
"E7 c #162900",
"nU c #171e00",
"s6 c #172300",
"fR c #172400",
"ai c #172500",
"ag c #172600",
"o8 c #172700",
"x# c #182100",
"sM c #182200",
"sD c #182600",
"q9 c #192000",
"qF c #192100",
"s1 c #192200",
"B2 c #192500",
"nM c #192700",
"sz c #1a2300",
"Cv c #1a2600",
"wW c #1b2200",
"AE c #1b2203",
"Ff c #1b2500",
"eS c #1b2600",
"mL c #1b2900",
"af c #1b2b00",
"xt c #1c2400",
"s# c #1c2600",
"gg c #1c2700",
"AO c #1c2900",
"aj c #1c2a00",
"s5 c #1d2b00",
"cc c #1d2d00",
"fD c #1e2800",
"fc c #1e2900",
"w5 c #1f250b",
"EG c #1f2800",
"A3 c #202705",
"ih c #202b00",
"u2 c #202d00",
"EM c #202f00",
"DU c #203000",
"CX c #212b00",
"rG c #212c00",
"gI c #212e00",
"ms c #222d00",
"vR c #223000",
"vv c #223100",
"BO c #232c00",
"uL c #233300",
"vc c #233800",
"wc c #242e00",
"pf c #243000",
"aF c #243200",
"oP c #243300",
"aP c #243400",
"tM c #252f00",
"ak c #253300",
"gC c #253500",
"to c #263401",
"lF c #263b00",
"CH c #272f00",
"gX c #273100",
"f4 c #273200",
"cT c #273700",
"lX c #283200",
"bT c #283300",
"p3 c #283500",
"EY c #283600",
"Dz c #283a00",
"gp c #293400",
"e0 c #293700",
"ae c #293a00",
"eg c #293b00",
"pB c #294100",
"ze c #2a3400",
"eq c #2a3600",
"B. c #2a3700",
"w7 c #2b3206",
"Bm c #2b3209",
"Fe c #2c3800",
"rh c #2c3900",
"nS c #2c3b00",
"yW c #2c4300",
"B0 c #2d3700",
"Eo c #2d3800",
"Ba c #2d3b00",
"zy c #2d3d00",
"hd c #2e3d06",
"Bz c #2f3a00",
"Dg c #2f3b00",
"hl c #2f3d00",
"eG c #314000",
"kT c #323b02",
"al c #324108",
"tQ c #32410a",
"t4 c #333e04",
"cD c #343d04",
"Bx c #343f00",
"lh c #353d0a",
"yq c #354100",
"oH c #354200",
"hU c #35430e",
"D2 c #354800",
"jz c #364200",
"yG c #364502",
"j7 c #364900",
"Ea c #373f0c",
"nu c #374300",
"c7 c #374400",
"wR c #374514",
"mj c #374708",
"lZ c #384205",
"aE c #384800",
"oo c #384900",
"hB c #394500",
"jk c #394507",
"Aq c #39490b",
"Ef c #394c00",
"mT c #3a440f",
"Dt c #3a4503",
"Ag c #3a4c00",
"h3 c #3b4506",
"iY c #3b4508",
"bc c #3b4510",
"dl c #3b4d03",
"bn c #3e4a08",
"xg c #3e4a0c",
"qR c #3e4c00",
"am c #3e4e0d",
"t9 c #3e4e10",
"ad c #3e4f08",
"Dk c #3e5600",
"EE c #3f490c",
"z0 c #3f4a08",
"qo c #404f00",
"Fl c #405800",
"nj c #414b0e",
"un c #414d0d",
"aQ c #425500",
"xK c #434d10",
"hu c #435104",
"B3 c #435200",
"we c #435400",
"lO c #445416",
"EH c #454f12",
"p9 c #455107",
"gq c #455200",
"z3 c #455517",
"us c #45560f",
"vW c #455701",
"d0 c #46530d",
"an c #46580c",
"jE c #475315",
"EZ c #475800",
"lv c #495517",
"yN c #495610",
"uH c #4a580d",
"j2 c #4b5813",
"pc c #4c5a0f",
"gY c #4d5a0a",
"oR c #4d5a0b",
"xi c #4d6011",
"BN c #4f5c0d",
"iB c #4f6210",
"Cc c #506210",
"DP c #525f1a",
"vM c #52600b",
"BA c #526011",
"ac c #526514",
"o9 c #526b05",
"iG c #535f1d",
"kg c #536011",
"qq c #53620d",
"kJ c #536211",
"w6 c #545c2d",
"zE c #54651e",
"uF c #556713",
"dO c #556817",
"cC c #566314",
"E# c #566415",
"lf c #566720",
"yV c #566e0c",
"ib c #576613",
"lG c #576d08",
"yX c #576f0d",
"AM c #586513",
"dA c #586617",
"ii c #58670a",
"vB c #586e09",
"A1 c #596132",
"m6 c #596c1d",
"z# c #596e0f",
"cd c #597015",
"mW c #5a690c",
"tT c #5a6d1e",
"lr c #5b6911",
"zg c #5b6c1c",
"Cf c #5b6d23",
"qC c #5b6f18",
"bS c #5c6b10",
"x3 c #5c6e1c",
"EK c #5c6e22",
"yx c #5c6f1d",
"uP c #5c720d",
"pY c #5c750f",
"lS c #5d6b13",
"AP c #5d6e1e",
"nh c #5d6f1b",
"oc c #5d6f1d",
"gB c #5d6f23",
"oB c #5d711c",
"cU c #5d7217",
"lE c #5d730e",
"En c #5e6c14",
"hc c #5e7024",
"vI c #5e7115",
"kX c #5e7117",
"Ec c #5e711f",
"C5 c #5e7702",
"yK c #5f6e13",
"EI c #5f6e1d",
"qO c #5f7014",
"kF c #5f711f",
"vx c #5f7125",
"km c #5f7218",
"mD c #5f7220",
"m# c #5f7221",
"Cb c #5f7314",
"vh c #5f7419",
"yb c #606d25",
"qG c #606e1f",
"uf c #606e21",
"o0 c #606f1c",
"wr c #607321",
"Fk c #607904",
"rx c #616d23",
"zD c #616f1a",
"x4 c #616f20",
"si c #61701d",
"tv c #617128",
"B4 c #617216",
"wV c #61751c",
"uW c #617619",
"sP c #626a3b",
"oy c #62711e",
"yh c #627120",
"nG c #627229",
"mz c #62732c",
"w. c #62741e",
"n# c #62761d",
"wX c #636f27",
"tW c #637021",
"pv c #63702a",
"sL c #63721f",
"tB c #64711f",
"fq c #64731e",
"ub c #64752e",
"Ad c #64771e",
"y7 c #647725",
"um c #647819",
"v6 c #656d3e",
"sn c #656e37",
"v5 c #656e39",
"xA c #657125",
"tb c #657127",
"w2 c #657222",
"rU c #65722d",
"gr c #65731b",
"hT c #65772d",
"l9 c #657827",
"qv c #667321",
"fb c #66771b",
"wm c #667730",
"nN c #667822",
"ab c #667a21",
"CN c #667b1c",
"qc c #667b1e",
"q5 c #667b20",
"bo c #677925",
"E6 c #677c1d",
"wy c #68742a",
"AD c #687432",
"hC c #68771a",
"E0 c #687b12",
"uu c #687b2a",
"aR c #687e12",
"xT c #697728",
"xq c #697b25",
"gA c #697d26",
"zT c #697e1f",
"qh c #697e21",
"wv c #6a7727",
"n2 c #6a791c",
"t. c #6a7b2b",
"wI c #6a7d14",
"ru c #6a7d24",
"yA c #6a7f24",
"wB c #6b7737",
"EW c #6b7a29",
"p5 c #6b7c1c",
"pU c #6b7e22",
"wj c #6b801b",
"Bl c #6c7732",
"r. c #6c782c",
"o. c #6c7d2d",
"ao c #6c8027",
"xu c #6d792d",
"wD c #6d792f",
"rX c #6d7b24",
"f5 c #6d7f1c",
"uJ c #6d812c",
"ED c #6e7b29",
"CW c #6e7d22",
"eH c #6e8221",
"fC c #6e8223",
"eR c #6f8320",
"bb c #707e2f",
"mr c #707e31",
"dm c #708624",
"oj c #71802f",
"oh c #71832f",
"yF c #71852c",
"uA c #718725",
"BZ c #728220",
"Bb c #728430",
"mM c #73802e",
"aD c #73862d",
"Ao c #748328",
"u3 c #74832e",
"e1 c #75882e",
"Bp c #778933",
"Ca c #778c25",
"DA c #78911c",
"gJ c #798c23",
"Cp c #7a8831",
"iQ c #7a8b2d",
"Df c #7b8c26",
"c6 c #7b8c2c",
"D1 c #7b921e",
"t2 c #7c912a",
"gz c #7c9132",
"u7 c #7c922e",
"jq c #7c931f",
"ep c #7d8e30",
"mK c #7d9331",
"Ar c #7e9334",
"aa c #7e9430",
"Ds c #7f9026",
"vb c #7fa00b",
"B5 c #809133",
"pG c #809135",
"hm c #80932a",
"E8 c #809634",
"ap c #80972f",
"mt c #81912f",
"re c #819330",
"hb c #819637",
"gU c #81972a",
"k8 c #81a20d",
"pm c #829132",
"gZ c #829230",
"gs c #839235",
"iZ c #839330",
"BB c #839532",
"qY c #84923b",
"dZ c #849932",
"v# c #849a38",
"EV c #859638",
"BM c #859733",
"pI c #85982d",
"vm c #85982f",
"zo c #859f22",
"vq c #869834",
"pC c #86a120",
"Fg c #879935",
"nV c #88993d",
"eh c #89a034",
"Eg c #89a036",
"aC c #8a9f38",
"zz c #8aa32b",
"E1 c #8ba02b",
"Bw c #8c9e2e",
"nq c #8ca138",
"EN c #8da33e",
"wN c #8da432",
"D5 c #8da43c",
"AQ c #8ea33a",
"C# c #8ea435",
"gy c #8ea43f",
"xa c #8fa42f",
"AG c #8fa43f",
"nR c #8fa539",
"ij c #90a32f",
"hS c #90a642",
"vY c #90a644",
"aS c #90a82e",
"nv c #91a430",
"Em c #92a339",
"wS c #92a74a",
"yH c #92a839",
"zh c #92aa3c",
"kY c #92ac2d",
"mI c #92b501",
"l0 c #93a446",
"mi c #93a849",
"tK c #93a93a",
"iA c #93a947",
"vu c #93ab39",
"ha c #93ab3b",
"Ah c #93ae2b",
"zj c #93b600",
"au c #93b602",
"cr c #93b809",
"li c #94a53b",
"gt c #94a640",
"z4 c #94a94c",
"j8 c #94ad2d",
"p. c #94b125",
"jI c #94b204",
"bN c #94b504",
"mG c #94b50e",
"xR c #94b607",
"fx c #94b701",
"sW c #94b909",
"Ax c #94bb00",
"B6 c #95a741",
"le c #95ad3d",
"cV c #95ae39",
"zn c #95b129",
"i. c #95b607",
"xZ c #95bb06",
"rn c #96a747",
"EC c #96a83c",
"uM c #96ae3e",
"jj c #96ae40",
"aq c #96af37",
"pZ c #96b130",
"oE c #96b907",
"dP c #97ae42",
"a# c #97af41",
"zp c #97b134",
"y6 c #97b33a",
"nm c #97b40c",
"uB c #97b531",
"yj c #97b70e",
"hp c #97b805",
"x0 c #97b811",
"dW c #97b903",
"sI c #97ba06",
"k5 c #97bc0c",
"lb c #97bd08",
"ss c #97bd10",
"y1 c #97bd12",
"bR c #98aa3a",
"rE c #98ab40",
"xW c #98b040",
"yY c #98b43b",
"Fs c #98b50b",
"Dl c #98b620",
"FB c #98b71c",
"xn c #98b817",
"a8 c #98ba03",
"fy c #98ba0c",
"wp c #98bb17",
"z7 c #98bc00",
"rB c #98bd0b",
"bC c #98bd0e",
"t0 c #98be06",
"zN c #98be07",
"tF c #98bf00",
"zt c #98bf04",
"sv c #98bf0c",
"y3 c #98c007",
"z9 c #98c105",
"tE c #98c200",
"jF c #99aa4c",
"A9 c #99ab3b",
"ht c #99ad3c",
"j1 c #99ae47",
"B7 c #99b03b",
"yE c #99b23a",
"ug c #99b431",
"ce c #99b441",
"nx c #99b707",
"FC c #99b721",
"Dp c #99b800",
"DD c #99b805",
"uY c #99b812",
"ft c #99b900",
"Fi c #99b910",
"h7 c #99b916",
"EJ c #99b918",
"Bq c #99b91a",
"ql c #99ba07",
"f. c #99ba09",
"f8 c #99bb02",
"a5 c #99bb04",
"zH c #99bb0c",
"bJ c #99bb0d",
".X c #99bc06",
"#o c #99bc08",
"l# c #99bc18",
"sg c #99bd01",
"rk c #99bd03",
"kA c #99be0c",
"zO c #99be0e",
"ti c #99be0f",
"bt c #99bf08",
"jY c #99bf0a",
"tf c #99c202",
"zZ c #9aac40",
"dz c #9aad42",
"jy c #9aae3f",
"yr c #9aaf46",
"rM c #9ab043",
"gu c #9ab13f",
"gx c #9ab145",
"E. c #9ab334",
"vK c #9ab41d",
"sR c #9ab510",
"xx c #9ab60c",
"Ft c #9ab70f",
"C6 c #9ab91e",
"#b c #9aba17",
"iJ c #9aba19",
"#v c #9aba1b",
"cZ c #9abb14",
"qL c #9abc05",
"tr c #9abc0d",
"r6 c #9abc0e",
".W c #9abd07",
"#p c #9abd09",
"z6 c #9abd0b",
"lo c #9abe02",
"qV c #9abe04",
"ps c #9abe06",
"Aj c #9abf00",
"sV c #9abf0d",
"ch c #9abf0f",
"k6 c #9abf10",
"Ay c #9ac008",
"sF c #9ac00b",
"r1 c #9ac013",
"k3 c #9ac102",
"sf c #9ac104",
"A. c #9ac106",
"y2 c #9ac10c",
"sw c #9ac10e",
"sT c #9ac20a",
"Aw c #9ac305",
"mk c #9bad41",
"sC c #9bb43c",
"C. c #9bb43e",
"#T c #9bb538",
"nX c #9bb810",
"qi c #9bb83a",
"EP c #9bb909",
"Aa c #9bba14",
"jt c #9bba1e",
"mc c #9bbb1a",
"qk c #9bbb1c",
"ts c #9bbc17",
"u0 c #9bbd04",
"uj c #9bbd06",
"#z c #9bbd0e",
"lJ c #9bbd0f",
"jw c #9bbe02",
"#n c #9bbe08",
"hM c #9bbe0a",
"m2 c #9bbf07",
"nc c #9bbf13",
"wi c #9bc001",
"kB c #9bc00e",
"sX c #9bc011",
"AX c #9bc109",
"k4 c #9bc10c",
"y0 c #9bc207",
"cB c #9cb03f",
"se c #9cb442",
"s4 c #9cb53d",
"dn c #9cb53f",
"gv c #9cb540",
"#S c #9cb637",
"B8 c #9cb639",
"sc c #9cb63b",
"xc c #9cba0c",
"DE c #9cba0d",
"ay c #9cbc13",
"ur c #9cbc1b",
"Ex c #9cbc1d",
"dw c #9cbd0a",
"cx c #9cbd0e",
".6 c #9cbd14",
"uq c #9cbd16",
"l6 c #9cbd18",
"AV c #9cbe05",
"lB c #9cbe0f",
"xm c #9cbe10",
"cY c #9cbe12",
"#A c #9cbf09",
"#. c #9cbf0b",
"k1 c #9cbf0d",
"jf c #9cbf1a",
"m3 c #9cc006",
"#i c #9cc008",
"nP c #9cc016",
"bs c #9cc018",
"kQ c #9cc101",
"ci c #9cc10f",
"wo c #9cc111",
"u# c #9cc112",
"bw c #9cc20a",
"jX c #9cc20d",
"ky c #9cc308",
"s2 c #9db044",
"qx c #9db715",
"#U c #9db73c",
"hI c #9db813",
"oF c #9db829",
"#R c #9db837",
"y. c #9dba10",
"te c #9dba12",
"EQ c #9dbb0b",
"Ey c #9dbb1f",
"DL c #9dbd02",
"vk c #9dbd10",
"eK c #9dbd12",
"Ew c #9dbd1c",
"#u c #9dbd1e",
"gP c #9dbe0f",
"#y c #9dbe15",
"pR c #9dbe17",
".3 c #9dbe19",
"hN c #9dbf10",
".7 c #9dbf13",
".V c #9dc00a",
".S c #9dc00c",
"#h c #9dc00e",
"ne c #9dc105",
"nz c #9dc107",
"m0 c #9dc109",
"lL c #9dc117",
"cn c #9dc119",
"jW c #9dc210",
"bD c #9dc212",
"lK c #9dc30b",
"zr c #9dc314",
"st c #9dc316",
"yu c #9dc405",
"Fv c #9eb145",
"ba c #9eb146",
"pg c #9eb23f",
"Fw c #9eb243",
"A4 c #9eb34e",
"AC c #9eb448",
"gw c #9eb646",
"AR c #9eb738",
"rl c #9eb839",
"rJ c #9eb83b",
"#Q c #9eb936",
"C8 c #9ebb11",
"wK c #9ebb15",
"zX c #9ebc0c",
"cy c #9ebd19",
"c3 c #9ebd1a",
"ji c #9ebd33",
"A5 c #9ebe05",
"Bf c #9ebe11",
"lp c #9ebe13",
"uk c #9ebe15",
"t7 c #9ebe1f",
"k9 c #9ebe2c",
"jK c #9ebf00",
"bM c #9ebf0e",
"hq c #9ebf10",
".5 c #9ebf16",
"m4 c #9ebf18",
"h8 c #9ebf1a",
"eL c #9ec009",
"ax c #9ec00a",
"#g c #9ec011",
"mQ c #9ec012",
".s c #9ec014",
"dv c #9ec105",
"e8 c #9ec10b",
".C c #9ec10d",
".P c #9ec10f",
"#8 c #9ec206",
"xP c #9ec208",
"fv c #9ec20a",
"yQ c #9ec218",
"by c #9ec21a",
"pQ c #9ec303",
"kw c #9ec311",
"lc c #9ec314",
"oX c #9ec400",
"i9 c #9ec40d",
"yT c #9ec506",
"me c #9ec508",
"nd c #9ec50a",
"zs c #9ec60d",
"tg c #9ec70b",
"zd c #9fb141",
"DO c #9fb14e",
"vS c #9fb340",
"s9 c #9fb546",
"zF c #9fb551",
"r8 c #9fb73f",
"og c #9fb839",
"rI c #9fb920",
"AY c #9fb922",
"B9 c #9fb93e",
"jH c #9fba1f",
"Bt c #9fbb0e",
"qT c #9fbb19",
"Fu c #9fbc14",
"a9 c #9fbd10",
"k. c #9fbd21",
"DH c #9fbe08",
"gS c #9fbe18",
"k# c #9fbe1a",
"iy c #9fbe23",
"xj c #9fbe32",
"x9 c #9fbf04",
"jv c #9fbf1e",
"dp c #9fbf20",
"vA c #9fbf2d",
"gR c #9fc00f",
"hO c #9fc017",
".4 c #9fc019",
".2 c #9fc01b",
"yP c #9fc029",
"AU c #9fc10b",
".F c #9fc112",
".Y c #9fc113",
".r c #9fc115",
"jg c #9fc124",
"eN c #9fc203",
"rb c #9fc206",
".T c #9fc20c",
"nA c #9fc20e",
".A c #9fc210",
"uD c #9fc21d",
"zP c #9fc21e",
"e6 c #9fc300",
"mw c #9fc307",
"oN c #9fc30b",
"yC c #9fc317",
"bB c #9fc319",
"tj c #9fc31b",
"pp c #9fc402",
"zk c #9fc404",
"#5 c #9fc405",
"cj c #9fc412",
"jV c #9fc414",
"je c #9fc415",
"oW c #9fc500",
"jS c #9fc50d",
"jc c #9fc50e",
"r4 c #9fc510",
"ks c #9fc60b",
"bH c #9fc611",
"bI c #9fc615",
"aZ c #9fc70e",
"c0 c #9fc70f",
"bG c #9fc808",
"aY c #9fc80a",
"ct c #9fc80c",
"sA c #a0b445",
"nF c #a0b647",
"lN c #a0b652",
"sK c #a0b742",
"lw c #a0b745",
"bp c #a0b74b",
"q# c #a0b91d",
"rz c #a0b927",
"tk c #a0b943",
"lH c #a0b944",
"hH c #a0ba1b",
"FO c #a0ba21",
"yB c #a0ba3f",
"CT c #a0bd0d",
"qs c #a0bd13",
"Fa c #a0bd17",
"kM c #a0be0e",
"n8 c #a0be20",
"AH c #a0be2a",
"Fo c #a0bf0a",
"lV c #a0bf0c",
"AA c #a0bf19",
"p0 c #a0bf24",
"vz c #a0bf26",
"h6 c #a0c01d",
"DW c #a0c01f",
"ju c #a0c021",
"or c #a0c100",
"jL c #a0c102",
"a4 c #a0c10e",
"rq c #a0c112",
"#q c #a0c118",
"#a c #a0c11a",
"#x c #a0c11c",
"ld c #a0c128",
"yv c #a0c12c",
"e9 c #a0c209",
"kR c #a0c20c",
".z c #a0c213",
".G c #a0c214",
".K c #a0c216",
".U c #a0c30d",
".E c #a0c30f",
".n c #a0c311",
"bz c #a0c31e",
"e5 c #a0c402",
"iu c #a0c408",
"xd c #a0c40a",
"#m c #a0c40c",
"a2 c #a0c418",
"cm c #a0c41c",
"#7 c #a0c505",
"ke c #a0c506",
"cu c #a0c513",
"a1 c #a0c515",
"el c #a0c516",
"zV c #a0c601",
"cs c #a0c60e",
"av c #a0c60f",
"a0 c #a0c611",
"su c #a0c617",
"r2 c #a0c619",
"yt c #a0c708",
"bF c #a0c70a",
"aX c #a0c70c",
"zK c #a0c712",
"h4 c #a1b252",
"hD c #a1b345",
"Bk c #a1b34d",
"wb c #a1b449",
"AL c #a1b53c",
"Fh c #a1b542",
"tN c #a1b546",
"w# c #a1b64d",
"Bu c #a1bb19",
"rZ c #a1bb1a",
"up c #a1bb22",
"#V c #a1bb40",
"A7 c #a1bc17",
"FP c #a1bc1f",
"yU c #a1bc47",
"D# c #a1bd11",
"Am c #a1bd13",
"zB c #a1bd1b",
"Db c #a1be0a",
"vU c #a1be18",
"DY c #a1be26",
"qz c #a1bf11",
"kf c #a1bf12",
"oO c #a1bf29",
"sS c #a1c00a",
"FH c #a1c00d",
"hr c #a1c01c",
"on c #a1c025",
"#K c #a1c027",
"rC c #a1c114",
"#c c #a1c11e",
"#w c #a1c120",
"#t c #a1c122",
"oL c #a1c20f",
"qU c #a1c211",
"rj c #a1c213",
".t c #a1c219",
"p7 c #a1c21b",
"q2 c #a1c21d",
"oe c #a1c22d",
"pi c #a1c30a",
"oK c #a1c30c",
"pj c #a1c30d",
"## c #a1c314",
"no c #a1c315",
".M c #a1c317",
"nC c #a1c405",
"rQ c #a1c406",
".9 c #a1c40e",
".R c #a1c410",
".m c #a1c412",
"#B c #a1c509",
"#j c #a1c50b",
"dr c #a1c50d",
"oM c #a1c519",
"tq c #a1c606",
"iv c #a1c607",
"jT c #a1c614",
"jU c #a1c616",
"cq c #a1c617",
"E3 c #a1c702",
"rA c #a1c710",
"j. c #a1c712",
"kt c #a1c80b",
"tG c #a1c80d",
"wY c #a2b63d",
"sa c #a2b647",
"kn c #a2b849",
"n9 c #a2b944",
"e2 c #a2ba40",
"vi c #a2bb43",
"na c #a2bb45",
"sb c #a2bc23",
"sy c #a2bc3f",
"lD c #a2bc41",
"q0 c #a2bd16",
"mY c #a2bd22",
"BW c #a2be11",
"hJ c #a2be14",
"xM c #a2be1b",
"vs c #a2be1c",
"AS c #a2be2d",
"AJ c #a2bf0d",
"ol c #a2bf17",
"pk c #a2bf2f",
"i8 c #a2c010",
"jP c #a2c013",
"AT c #a2c022",
"#L c #a2c02e",
"mo c #a2c10e",
"Bd c #a2c11e",
"D7 c #a2c125",
"aV c #a2c126",
"lk c #a2c207",
"gb c #a2c215",
"aW c #a2c21f",
"r7 c #a2c221",
"tn c #a2c223",
"DI c #a2c300",
"oV c #a2c304",
"bK c #a2c312",
"jR c #a2c314",
".h c #a2c31a",
"iL c #a2c31c",
"iK c #a2c31e",
"it c #a2c40b",
".# c #a2c415",
".a c #a2c416",
".b c #a2c418",
"eM c #a2c507",
"rP c #a2c509",
".c c #a2c50f",
"Qt c #a2c511",
".f c #a2c513",
".g c #a2c60a",
".e c #a2c60c",
".d c #a2c60e",
"co c #a2c61a",
"sY c #a2c61c",
"ov c #a2c705",
"dV c #a2c707",
"du c #a2c708",
"jd c #a2c715",
"Bh c #a2c717",
"bx c #a2c718",
"FW c #a2c800",
"FX c #a2c801",
"FY c #a2c803",
"r5 c #a2c811",
"jb c #a2c813",
"Av c #a2c90c",
"tc c #a3b547",
"nk c #a3b64b",
"oG c #a3b851",
"il c #a3bb25",
"pb c #a3bb43",
"my c #a3bb4b",
"zR c #a3bc44",
"E5 c #a3bc47",
"CC c #a3bd1c",
"FJ c #a3bd24",
"x6 c #a3bd28",
"qH c #a3bd42",
"FA c #a3be21",
"#P c #a3be39",
"qW c #a3be3d",
"oC c #a3bf46",
"xw c #a3c00e",
"CS c #a3c010",
"jQ c #a3c016",
"FQ c #a3c01a",
"yl c #a3c026",
"g5 c #a3c028",
"rN c #a3c02a",
"jO c #a3c111",
"gL c #a3c121",
"mv c #a3c125",
"kD c #a3c12d",
"kN c #a3c20f",
"eP c #a3c21e",
"Ei c #a3c226",
"F. c #a3c227",
"jM c #a3c30a",
"bO c #a3c316",
"kr c #a3c318",
"zb c #a3c31a",
"rr c #a3c320",
"l2 c #a3c322",
"mg c #a3c324",
"jh c #a3c331",
"kq c #a3c411",
"mp c #a3c413",
"iO c #a3c415",
".Z c #a3c41b",
".1 c #a3c41d",
"ds c #a3c41f",
"DJ c #a3c500",
"aw c #a3c50c",
"en c #a3c50e",
"eO c #a3c50f",
".o c #a3c516",
".w c #a3c517",
".v c #a3c519",
"em c #a3c607",
"os c #a3c60a",
"cv c #a3c610",
".i c #a3c612",
".l c #a3c614",
"dq c #a3c70b",
"dS c #a3c70d",
"ek c #a3c70f",
"iw c #a3c808",
"ja c #a3c816",
"Ak c #a3c900",
"zW c #a3c902",
"kz c #a3c912",
"j# c #a3c914",
"r3 c #a3c91a",
"k2 c #a3ca0d",
"sU c #a3ca17",
"zL c #a3cb13",
"Cg c #a4bb51",
"op c #a4bc26",
"ro c #a4bc30",
"aB c #a4bc44",
"tS c #a4bc4c",
"g4 c #a4bd2e",
"eI c #a4bd3e",
"im c #a4be1d",
"sB c #a4be25",
"DZ c #a4be36",
"pF c #a4be37",
"q4 c #a4be41",
"kL c #a4bf22",
"pT c #a4bf3e",
"CD c #a4c013",
"i2 c #a4c014",
"CR c #a4c016",
"ph c #a4c01d",
"lT c #a4c01e",
"p1 c #a4c02d",
"ei c #a4c038",
"iq c #a4c10d",
"sq c #a4c10f",
"ip c #a4c111",
"az c #a4c127",
"rs c #a4c131",
"q1 c #a4c20c",
"ho c #a4c226",
"oY c #a4c22c",
"ys c #a4c230",
"jN c #a4c30e",
"xN c #a4c310",
"ge c #a4c31d",
"eo c #a4c320",
"g6 c #a4c328",
"Do c #a4c401",
"n5 c #a4c407",
"jJ c #a4c409",
"pK c #a4c40b",
"rc c #a4c419",
"ka c #a4c41b",
"D8 c #a4c421",
"#s c #a4c423",
"wT c #a4c432",
"n7 c #a4c512",
"rR c #a4c514",
"e4 c #a4c516",
".u c #a4c51c",
".0 c #a4c51e",
"#d c #a4c520",
"cw c #a4c610",
".y c #a4c617",
".x c #a4c618",
".J c #a4c61a",
"fw c #a4c711",
".j c #a4c713",
"gO c #a4c715",
"bA c #a4c722",
"cg c #a4c725",
"ix c #a4c80c",
"l4 c #a4c80e",
"#H c #a4c810",
"ck c #a4c81c",
"cl c #a4c820",
"#4 c #a4c909",
"#6 c #a4c90a",
"sx c #a4c917",
"s7 c #a4c91a",
"xe c #a4ca03",
"Az c #a4ca12",
"mf c #a4ca13",
"Bg c #a4ca15",
"bu c #a4cb0c",
"AW c #a4cb0e",
"kx c #a4cb10",
"w1 c #a5b747",
"ym c #a5b84c",
"EU c #a5b84d",
"rY c #a5ba3b",
"rt c #a5bc47",
"xp c #a5be48",
"v1 c #a5be49",
"oT c #a5bf1e",
"FK c #a5bf26",
"t6 c #a5bf28",
"pu c #a5bf44",
"in c #a5c019",
"u5 c #a5c023",
"AB c #a5c033",
"Fj c #a5c03d",
"io c #a5c114",
"n4 c #a5c115",
"DM c #a5c11f",
"ar c #a5c139",
"Cl c #a5c20e",
"Cm c #a5c212",
"BU c #a5c21a",
"mm c #a5c21c",
"vl c #a5c228",
"Bi c #a5c22a",
"lI c #a5c236",
"ir c #a5c30d",
"r0 c #a5c313",
"wh c #a5c316",
"dx c #a5c323",
"f# c #a5c325",
"Dn c #a5c404",
"pO c #a5c40e",
"FG c #a5c40f",
"DX c #a5c41e",
"k0 c #a5c428",
"qJ c #a5c429",
"zJ c #a5c42b",
"oJ c #a5c50a",
"om c #a5c50c",
"mZ c #a5c518",
"kp c #a5c51c",
"#r c #a5c522",
"nD c #a5c613",
"c2 c #a5c615",
"#I c #a5c61d",
"BH c #a5c621",
"gc c #a5c710",
"f9 c #a5c711",
"#2 c #a5c718",
"e7 c #a5c719",
"#f c #a5c71b",
"dT c #a5c812",
".k c #a5c814",
".B c #a5c816",
"#E c #a5c90d",
"#k c #a5c90f",
"#l c #a5c911",
"jZ c #a5c91f",
"#C c #a5ca0a",
"m1 c #a5ca0b",
"xk c #a5ca1b",
"yR c #a5cb13",
"y4 c #a5cb1c",
"mH c #a5cc0d",
"tZ c #a5cd15",
"CG c #a6b946",
"rH c #a6ba47",
"ox c #a6bb42",
"td c #a6bd2e",
"f6 c #a6be36",
"D0 c #a6be42",
"mS c #a6be44",
"qb c #a6bf49",
"qB c #a6bf4a",
"Ck c #a6c01e",
"Fb c #a6c027",
"FN c #a6c029",
"pn c #a6c11a",
"h5 c #a6c136",
"vV c #a6c13e",
"pN c #a6c215",
"CP c #a6c21f",
"ER c #a6c220",
"BG c #a6c231",
"nZ c #a6c239",
"A6 c #a6c30f",
"#M c #a6c335",
"pL c #a6c337",
"x7 c #a6c414",
"qm c #a6c426",
"xX c #a6c42e",
"j0 c #a6c432",
"FT c #a6c50f",
"FI c #a6c512",
"Be c #a6c51f",
"Ej c #a6c52a",
"x8 c #a6c609",
"is c #a6c60d",
"ga c #a6c61b",
"dU c #a6c71e",
"#e c #a6c720",
"tI c #a6c722",
"h9 c #a6c80f",
"ny c #a6c811",
"gd c #a6c812",
".p c #a6c819",
".q c #a6c81a",
".H c #a6c81c",
"l3 c #a6c913",
".8 c #a6c915",
".Q c #a6c917",
"zu c #a6c925",
"#G c #a6ca0e",
"kd c #a6ca10",
"#3 c #a6ca12",
"ui c #a6ca20",
"ut c #a6ca22",
"pr c #a6cb09",
"ot c #a6cb0b",
"#F c #a6cb0c",
"sE c #a6cb19",
"kv c #a6cb1b",
"pq c #a6cc05",
"xQ c #a6cc07",
"bv c #a6cd10",
"u. c #a6cd12",
"yS c #a6ce0b",
"zM c #a6ce15",
"th c #a6ce16",
"ww c #a7b755",
"so c #a7b850",
"p2 c #a7ba4e",
"Co c #a7bb40",
"t5 c #a7bb4a",
"hE c #a7bc3d",
"BY c #a7bd34",
"xy c #a7bf2b",
"tu c #a7bf4d",
"l8 c #a7bf51",
"Fz c #a7c02e",
"s3 c #a7c128",
"l1 c #a7c13a",
"h# c #a7c144",
"Dm c #a7c21b",
"wg c #a7c225",
"Cj c #a7c321",
"rD c #a7c330",
"Da c #a7c412",
"qy c #a7c414",
"pa c #a7c42a",
"tJ c #a7c42e",
"zQ c #a7c436",
"qj c #a7c438",
"FR c #a7c515",
"DG c #a7c517",
"lW c #a7c529",
"nb c #a7c533",
"FS c #a7c611",
"mP c #a7c613",
"qM c #a7c620",
"vt c #a7c62a",
"g7 c #a7c62d",
"gM c #a7c71e",
"dR c #a7c726",
"BI c #a7c728",
"zv c #a7c738",
"kO c #a7c817",
"a3 c #a7c819",
"#1 c #a7c823",
"yD c #a7c831",
"uC c #a7c833",
"gN c #a7c91a",
".N c #a7c91b",
"kb c #a7c91d",
"tY c #a7c92a",
"k7 c #a7c92d",
"a6 c #a7ca0e",
"ra c #a7ca14",
"g. c #a7ca16",
".D c #a7ca18",
"kP c #a7cb11",
"ln c #a7cb13",
"#D c #a7cc0d",
"ku c #a7cc1a",
"tH c #a7cd16",
"la c #a7cd18",
"A# c #a7ce13",
"oS c #a8bc3f",
"BC c #a8bc4b",
"sh c #a8bd44",
"BS c #a8bf53",
"hG c #a8c02a",
"xf c #a8c044",
"m5 c #a8c050",
"iH c #a8c142",
"tP c #a8c149",
"FL c #a8c229",
"tO c #a8c22b",
"As c #a8c245",
"#W c #a8c247",
"pJ c #a8c326",
"c4 c #a8c338",
"qt c #a8c340",
"i7 c #a8c417",
"Dc c #a8c418",
"t1 c #a8c433",
"#O c #a8c43c",
"i3 c #a8c511",
"ow c #a8c52d",
"xo c #a8c535",
"qa c #a8c537",
"za c #a8c539",
"i4 c #a8c610",
"Br c #a8c616",
"rp c #a8c619",
"q3 c #a8c630",
"x1 c #a8c632",
"u6 c #a8c634",
"u1 c #a8c723",
"pt c #a8c72b",
"DB c #a8c72c",
"sr c #a8c80b",
"Al c #a8c80d",
"xO c #a8c80f",
"CO c #a8c825",
"wM c #a8c829",
"FF c #a8c916",
"Ev c #a8c920",
"y5 c #a8c932",
"qI c #a8c934",
"uZ c #a8ca14",
"C7 c #a8ca1b",
"nB c #a8ca1c",
".I c #a8ca1e",
"uO c #a8ca2e",
"n6 c #a8cb0f",
"lm c #a8cb15",
"lA c #a8cb17",
"FE c #a8cb19",
"uh c #a8cb29",
"zl c #a8cc10",
"sG c #a8cc14",
"pP c #a8cd0e",
"ou c #a8ce09",
"ri c #a9be47",
"u4 c #a9bf40",
"rT c #a9c04e",
"ma c #a9c151",
"ua c #a9c153",
"uE c #a9c240",
"vy c #a9c24a",
"yO c #a9c24d",
"CQ c #a9c321",
"tm c #a9c32c",
"gf c #a9c33b",
"ko c #a9c33e",
"ng c #a9c344",
"Ez c #a9c427",
"hs c #a9c435",
"ul c #a9c439",
"BT c #a9c43f",
"Eh c #a9c441",
"mh c #a9c443",
"CE c #a9c51b",
"#N c #a9c53c",
"p8 c #a9c53d",
"po c #a9c612",
"i5 c #a9c614",
"i6 c #a9c616",
"eJ c #a9c62e",
"lC c #a9c636",
"zq c #a9c63a",
"oU c #a9c711",
"hK c #a9c719",
"np c #a9c731",
"nY c #a9c812",
"r# c #a9c82d",
"AI c #a9c90c",
"F# c #a9c910",
"iM c #a9ca21",
"p# c #a9ca23",
"#J c #a9ca25",
"br c #a9ca33",
"Fn c #a9cb1c",
".L c #a9cb1f",
"g# c #a9cc18",
"qK c #a9cc1a",
"fu c #a9cd07",
"fz c #a9cd13",
"lz c #a9cd15",
"cp c #a9cd21",
"xl c #a9cf1a",
"g0 c #aabc4c",
"pM c #aabc50",
"De c #aabf3c",
"c5 c #aac14c",
"vJ c #aac24a",
"zY c #aac329",
"fa c #aac341",
"BX c #aac422",
"mO c #aac42b",
"FM c #aac42d",
"aT c #aac43f",
"hR c #aac449",
"Bc c #aac538",
"zG c #aac544",
"D. c #aac61c",
"vj c #aac633",
"oq c #aac713",
"e3 c #aac72f",
"mF c #aac737",
"h. c #aac739",
"wL c #aac818",
"g8 c #aac832",
"bq c #aac844",
"Fp c #aac914",
"FD c #aac92e",
"jr c #aac930",
"mR c #aaca29",
"nf c #aaca2b",
"rO c #aacb1a",
"hL c #aacb1c",
"Au c #aacb22",
"FV c #aacc1d",
"EO c #aacd17",
"Fm c #aacd19",
"c1 c #aace16",
"bE c #aacf1d",
"tC c #abbd4d",
"EB c #abc03f",
"BL c #abc04b",
"g3 c #abc138",
"BF c #abc23c",
"Er c #abc256",
"Fy c #abc33b",
"ia c #abc34b",
"fB c #abc442",
"kE c #abc44e",
"x2 c #abc44f",
"dY c #abc540",
"Ek c #abc637",
"BV c #abc71d",
"CB c #abc725",
"fs c #abc727",
"Bs c #abc818",
"rS c #abc832",
"zU c #abc838",
"tp c #abc935",
"g9 c #abc937",
"nn c #abca15",
"pE c #abca26",
"dX c #abca27",
"js c #abca2f",
"cX c #abca31",
"uN c #abcb2c",
"bL c #abcc19",
"dt c #abcc27",
"md c #abcd1e",
"a7 c #abce10",
"kc c #abce18",
"z8 c #abce1a",
".O c #abce1c",
"sH c #abcf17",
"xv c #acbf4c",
"oZ c #acc04d",
"tX c #acc04f",
"qZ c #acc13e",
"xL c #acc244",
"hF c #acc337",
"lj c #acc430",
"Ac c #acc44c",
"wq c #acc452",
"nO c #acc550",
"p6 c #acc631",
"aA c #acc63e",
"eQ c #acc63f",
"b. c #acc72c",
"sJ c #acc837",
"dQ c #acc83f",
"Ab c #acc933",
"mn c #acca1c",
"fA c #acca2a",
"#Z c #acca38",
"ll c #accb16",
"iI c #accb2f",
"#0 c #accb30",
"gQ c #accc1f",
"ly c #accc2d",
"at c #accd28",
"iN c #accf10",
"kC c #acd026",
"xz c #adbf4f",
"ry c #adc04d",
"qS c #adc344",
"CF c #adc435",
"wZ c #adc438",
"vL c #adc440",
"Bj c #adc442",
"sp c #adc533",
"rd c #adc53b",
"vr c #adc53d",
"ml c #adc636",
"Fc c #adc637",
"yw c #adc650",
"kS c #adc72e",
"BJ c #adc83d",
"vZ c #adc843",
"nE c #adc938",
"DF c #adca20",
"tt c #adca3a",
"a. c #adcb37",
"lx c #adcb39",
"yk c #adcc19",
"zI c #adcc31",
"as c #adcc33",
"FU c #add01a",
"l5 c #add119",
"x5 c #aec24f",
"i0 c #aec342",
"CU c #aec536",
"EA c #aec632",
"qr c #aec63c",
"vT c #aec735",
"tD c #aec738",
"BK c #aec745",
"xb c #aec92e",
"mq c #aec93e",
"yI c #aecb35",
"mx c #aecb3b",
"va c #aecb3d",
"E4 c #aecb3f",
"pD c #aecd31",
"cf c #aecd41",
"#9 c #aece2d",
"hP c #aece2f",
"of c #aecf26",
"yZ c #aecf3a",
"DK c #aed008",
"Ci c #aed11b",
"uo c #afc350",
"ya c #afc354",
"oI c #afc44b",
"ik c #afc53e",
"Bv c #afc638",
"zc c #afc836",
"nl c #afc839",
"mE c #afc853",
"#X c #afc94c",
"C9 c #afca23",
"gT c #afca3b",
"D6 c #afca45",
"E9 c #afca47",
"cz c #afcc36",
"kZ c #afcc3c",
"Fr c #afcd1f",
"pS c #afcd37",
"CA c #afcd39",
"qA c #afcd3b",
"D9 c #afce33",
"Ai c #afd029",
"mu c #b0c647",
"mN c #b0c64a",
"iP c #b0c741",
"yJ c #b0c745",
"Dd c #b0c92f",
"dy c #b0ca42",
"t8 c #b0ca4f",
"i# c #b0cd37",
"s8 c #b0cd3d",
"Ch c #b0cd41",
"At c #b0ce38",
"DC c #b0cf1a",
"zA c #b0d02f",
"l. c #b0d138",
"xY c #b0d42a",
"mX c #b1c645",
"n3 c #b1c740",
"ok c #b1c749",
"Dr c #b1c83c",
"nW c #b1c842",
"b# c #b1c844",
"cA c #b1c941",
"wn c #b1c959",
"i1 c #b1ca30",
"y# c #b1ca3b",
"od c #b1ca55",
"hQ c #b1ce3e",
"oD c #b1d035",
"El c #b2c84c",
"BE c #b2c945",
"wf c #b2c947",
"AK c #b2cb32",
"ES c #b2cb3b",
"iz c #b2cb56",
"j9 c #b2cd3e",
"DV c #b2cd4a",
"Dq c #b2ce22",
"cW c #b2ce45",
"f7 c #b2cf25",
"aU c #b2cf3f",
"mb c #b2cf43",
"lU c #b2d11e",
"nQ c #b2d138",
"ej c #b2d231",
"v0 c #b2d33a",
"uI c #b3c84f",
"fr c #b3c94b",
"Fd c #b3ca44",
"qN c #b3ca46",
"lq c #b3ca48",
"gK c #b3cb41",
"wU c #b3d044",
"Fq c #b3d21f",
"CV c #b4c751",
"zC c #b4c946",
"Fx c #b4c950",
"zw c #b4cc5a",
"nw c #b4cd33",
"#Y c #b4cf4e",
"jx c #b4d02e",
"l7 c #b4d143",
"sQ c #b5c469",
"g2 c #b5ca47",
"qw c #b5ca4b",
"wa c #b5ca51",
"jG c #b5cb4c",
"BD c #b5cb4d",
"Cn c #b5ce32",
"bP c #b5d131",
"zi c #b5d149",
"tR c #b5d244",
"w0 c #b6cb48",
"qn c #b6cb52",
"ET c #b6cc50",
"wJ c #b6cf3f",
"xS c #b6d048",
"lM c #b6d24a",
"An c #b7cc49",
"kK c #b7cd4f",
"do c #b7d448",
"zm c #b7d63d",
"wC c #b8c575",
"wx c #b8c76c",
"uX c #b8d159",
"mJ c #b8d350",
"q. c #b9cc56",
"g1 c #b9cd52",
"z5 c #b9d453",
"AZ c #bacf58",
"DN c #bad14d",
"Eu c #bad455",
"hn c #bcd351",
"yi c #bcd44c",
"A0 c #bdca7a",
"A8 c #bdd445",
"bQ c #c1d750",
"E2 c #c1d951",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#.#.#.a.a.a.a.a.a.b.a.a.#.a.a.b.b.b.b.a.#.#Qt.c.d.e.d.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.f.#.#.#.#.#.#.a.a.#.f.#.#.a.a.a.a.#.#.fQt.c.d.e.d.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.e.g.e.e.e.e.d.d.c.cQtQt.f.f.#.fQtQtQtQtQtQtQtQtQtQtQt.c.d.d.d.d.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.e.g.e.e.e.e.d.d.d.d.c.c.c.cQtQtQt.cQt.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.f.f.fQtQtQtQt.c.c.d.d.d.d.d.cQtQt.fQt.f.f.f.f.#.#.a.a.b.b.h.b.fQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.#.a.a.a.#.#.f.fQt.c.c.d.d.e.e.dQtQtQtQtQtQtQtQt.f.f.#.#.a.b.b.a.fQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.#.a.#.#.#.#.f.fQt.c.c.c.c.d.d.d.c.c.d.d.e.g.g.g.g.g.e.d.d.c.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#.f.f.f.f.f.f.f.fQtQtQtQt.c.c.d.e.e.g.g.g.e.e.e.d.d.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.i.j.k.l.m.n.o.p.q.a.r.s.t.u.u.v.b.w.x.x.y.#.z.A.B.A.CQt.i.A.n.DQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.i.E.C.C.n.f.m.F.F.G.a.H.I.I.H.v.J.a.K.r.K.v.H.L.M.s.M.N.N.a.G.#.fQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.O.B.A.P.l.Q.B.R.S.T.c.c.U.V.W.X.iQt.n.F.Y.M.Z.0.1.2.3.4.5.6.7.G.fQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.R.EQt.k.8.k.i.c.c.c.9.U.T.9.c#..P##.x.Z#a.3#b#c#c#d#e#f.##g#hQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c#i#j#k#l#m#n#o#p.m.f.a.w.w.v.b.b#q.h.0#r#s#t#u#v#w#x#y#z#A#B#C#D.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c#E#F#G#H.R###I#J#t#K#L#M#N#O#P#Q#R#S#T#U#V#W#X#Y#N#Z#0#1#2#3#4#5.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.d#6#7#8.R.L#9a.#N#Wa#aaabacadaeafagahaiajakalamanaoapaqarasat.GauQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cav.cavQt.f.f.f.#.f.fQt.c.c.d.dawaxayazaAaBaCaDaEaFaGaHaIaHaJaKaLaMaMaLaLaKaJaNaNaOaPaQaRaSaTaUaVaW.h.#Qt.d.c.c.f.#.#.#.#.f.fQt.f.f.f.f.fQt.fQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.caXaYaXaZa0a1a2a2.Z.va3a4a5a6a7a8a9b.b#babbbcbdaKbebfbfbfbfbgbgbhbibibjbkbkaMaMaMaLaKblaJaHbmbnbobpbqbrbsbtbubvbwbxbybzbAbBbCbDbE.#.#.#.#.#.f.#.f.f.fQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtavbFbGaYaZbHbIa2a2.JbJbKbLbMbNbObPbQbRbSbTbUbVbWbXbYbYbZb0b1b1b1b1b2b3b3b4b4b3b5b6b7b8b9c.c#aMcacbcccdcecfcgchcicjckclcmcncocpcqcr.a.#.a.#.#.#.#.f.f.fQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtavcsctctaZa0cua1cu.RcvcwcxcyczcAcBcCcDcEblaMc#cFcGb8bZb0cHcIc#c#c#cJcJcJcJcKb4b5cLcMcNcNcOcPcQcRaLaHcScTcUcVcWcX#bcY.y.8.U.m.N.0cZ.a.f.#.f.f.f.fQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQta0avc0c0c0a0a0avcs#kc1c2c3c4c5c6c7c8aMaMc9d.d#b1dab1b1cHdbc#c#c#c#cJcJcJcJcJdcb3b5dddedfcNdgdhdidjdkaLaJaOdldmdndodp.Y.ddqdr.Pdsdt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQta0a0bHcucua0cs.gdudvdwdxdydzdAdBaJbWdCdDdEcHcQcQcQcIcIdbcIc#c#c#c#bjbibjaMaMaMaMbjdadFdGdHdIdJdJdIdKdLdMblaIdNdOdPdQdR.i.gdSdT#IdU.f.c.c.c.c.c.c.c.c.cQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtcubIa1cuavaXdVdudWdXdYdZd0d1aJaLcNd2dfb7d3d4d5c9cIdbcHcHdbdbc#dbd6dId7bibjbkbkbkd8d9e.e#b7b7eaebececedeeaMaIefegeheiej.p.Vek.B#h.c.d.d.d.d.d.c.c.c.cQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.fa1elelcu.dduemeneodYepeqaJaLerd.dhdIb7escQetcIcQb1b0bZb8b8bZbZb8euecevewd6d7exbieyezeAdadaeBeCeDeEdFb7eeeFaMaKaHeGeHeIeJeKeLeMeN.g.e.e.e.d.d.d.d.c.cQtQtQtQt.f.fQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.felela1a0.e.eeOePeQeReSblcRd4cRcQd3cPcPcPeTdaesdFb8b8b8b8bZb0b0b0d7d7d7d7exexexexeUeVdadad9djeWcRaKeXeYesdFeseZaKaIe0e1e2e3e4e5e6du.e.d.d.d.d.d.d.c.cQtQtQtQt.f.fQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.fe7.xe8dSe9f.f#fafbfcaKcKb3b3fdfeffd8esb8fgdfdKfhcNcLfibWcJcRcRaMfjaJblaKaLaKfkflfmdFdFdFdFdFexfnbgaMcRcRdaeUd6escRfofpfqfrfsftfudqfvcvfwcv#Afxcv.c.cQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.Jfy.dfzdwfAfBfCfDblcQfEfFb1fGfHfIeTdFdIdKfJfKdCficJaLbefLfMfNfOfPfQaifRfSfOaJblaKaLfTfUfVdFdJfWeWfXfYfZf0f1f2ewdJfZf3f4f5f6f7f8f9.R.i.EQtg..ig#QtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.fgagbgcgdgegfepggaLd8ghgigjfHfHfHdagkglgmcNdJdacRaKgngogpgqgrgsgtgugvgwgxgygzgAgBgCgDaHblaLgEgFgGcNf2gHdad8eBgHdHdIgHaMaJgIgJgKgLgM.qgN.z.zgNgO.f.fQtQtQt.c.c.c.cQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.fgPgQgRgSgTgUeqblb4ddgVb3fHfHfHgjfFb6b5d3cQaMaKgWgXgYgZg0g1g2g3g4g5g6g7g8g9h.#Oh#hahbhchdheaKhfhgcNhhdGdFdahihjdFdJhkf0aLaNhlhmhnho.h.Z.b.b.b.Y#g.#.fQtQt.c.c.c.cQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQthphqhrhshthuaJcRb5hvb3fHhwhwhxhyb7cPhzaLaJhAhBhChDhEhFhGhHhIhJhKhL.Q.m.ShM#.hNhOhPhQhRhShThUhVaKd8hWhXhYd3d8d8b3eshZh0h1h2aIh3h4h5h6h7h8#e.0.Z.I.#.fQtQt.c.d.d.cQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.ch9i.i#iaibicaLd.b2b0gjfHhwidiehyifbWaLigihiiijikiliminioipiqirisit#jiuiuivdViwix.9.7iydQiziAiBiCaKcRcQd#iDdad8d#d8h0d8cQiEaLiFiGiHiI#uiJ#riKiLiM.a.#.f.c.c.d.d.d.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.diNiOiPiQiRblercRiSiTfHfHiUiVieiWiXcRf3iYiZi0i1i2i3i4i3i5i6i7ioi8e8i9j.j#jajba0jca0jdjejfjgjhjijjjkjlaLcRjmesdajndbcIcQcQjod4cRjpjqjrjsjtjujvh8.1.b.#.f.c.c.d.e.d.cQtQtQt",
"QtQt.c.cQtQt.f.fQtQtQtQtQt.c.d.ejwjxjyjzbljAjBcRjCcKfHgjjDjDiUiSaMgnjEjFjGjHjIjJjKjLjMjNjOjPjQjR.UjSjTjUcqjVjWjXjYa0jbcichcqjZj0j1j2j3aKj4d7dFiDj5cRj6fIdahZb5aKj7j8j9k.k##qkakb.#.fQtQtQt.c.d.d.cQtQtQt",
"Qt.c.d.d.c.f.#.#.mg.kc.T.Tkdkeh9kfbQkgaJkhb6kic#aMcRcQkjb5bXkkaMklkmknkoazkpiOcweOeneOeOkqiOkr.#ksktkukvkwjbkxkykzkAbxa2bDkwkBkCkDkEkFkGaLkHkIb7hibgbgbgcHb0b8c#aIkJkKkLkMenkNkOeOeO.cQt.a.aa0avQtQtQtQt",
"Qt.c.d.d.c.f.a.a.f.jfwe8#HkPkQkRkSbRkTaLkUcNdaetcRkVb4esesd8cQkWkXkYkZk0.7#hk1#..fQt.c.c.cQt.a.fk2k3k4jdcjk5k6clk7k8k9l.l#cqlalblcldlelflgaLfVdFd9bhbgbgcHb0b8b1aMlhliljkMlklljNenen.c.f.b.bcuavQtQtQtQt",
".fQt.d.d.c.f.#.a.lQte8.VlmlnlolplqlrlsaMltb7d8lucIfIcPdacRaLfolvlwlxlyhO.C.d.c.cQtQt.d.d.d.c.f.f#3.elzlAlBh6lClDlElFlGlHlI#vlJ.9lKlLlMlNlOlPaLlQd9d9hihib1b0bZb1cRlRlSi0lTi8lUlVeOkqQt.f.b.acua0QtQtQtQt",
".fQt.d.d.c.f.#.a##.fe8.Tlmfw.ClWbalXblc9d#dacQlud3esbXjoaLlYlZl0l1l2.s.CdS#G#3l3QtQt.d.e.e.eQtQt#3l4l5.Bl6l7l8l9m.aNdNm#mambmcmdmemfmgmhmimjaIfMbheUeUeUb1b1b0b1cQaKbTmkmlmmmnmokqmp.f.#.a.acua0QtQtQtQt",
".fQt.c.d.cQt.#.a.FgO.c.ccv.m#fmqmrbUaLhzcIlucRetbZdJcLd5aJmsmtmumvlB.V.e.gmw.T.n.fQt.d.e.g.g.c.d#Glo#odsmxmymzmAaLmBaJmCmDmEmFmGkymHmIiJmJmKmLaJbge#eaeab0b1b1b1esergnmMmNmOa9mPmpiO.a.a.#.#a1cuQtQtQtQt",
".fQt.c.d.cQt.#.amQ.Bl3ek.C.amRmSmTbVc9c.cRmUc9dbdImVb7aMj3mWmXmYmZm0#Bm1#8m2.n.o.#.f.d.gdu.g.d.edVm3m4aUm5m6m7aKm8dKm9bln.n#nanbncndnehMnfngnhaNbed9eaeab0cHcHb1dFniaKnjnknlnmnnmpiO.b.a.f.fa1a1.fQtQtQt",
".fQt.c.c.d.c.f.ano#2fwdrk1#enpnqnrbWnsjmcRc9c#b4cNntdaaKnunvnwnxnyne#BixnznAnBkb.b.#.d.gdudu.d.enCnDnEnFnGnHaKnInJdKnKnLaInMnNnOjhnPkd#Bk1nQnRnSnTbge#eab0cHcHcHdFkiaMnUnVnWnXnYkqiO.b.aQtQta1el.fQtQtQt",
".f.fQt.c.d.c.f.#.J.o.9#mhNmRnZe1aKbXn0dacQcRcQesfhn1cRlsn2n3n4n5n6mwdq#E.V.m.HhO.a.f.edVdVdu.dQtn7n8n9o.o#aKoadFkIdIdJobblaImCocodoe.Yneiuofogohoibfhie#b1cHdbcHesdacQblojokolomeOmp.b.aQt.celel.fQtQtQt",
".#.f.fQt.d.dQt.#.H.Ym0.d##on#WoobebYb8b0dbdbb1b8cNb2aLgXhDopoqoros.e.e.eQt.f.b.a.l#motouovdul3.ZowoxoyozaLhje#eUd8fZd8cRcRoAaKlPoBoCoDoEmw.BoFoGf4bljAdad3b4cQdcb4d8d#caoHoIoloJoKoLno##.c.ccqoM.fQtQtQt",
".#.#.fQt.d.dQt.#.b.GoN.d.aoOa#oPbebYbZb1dbcHb8gmdIcQoQoRoSoToUoVos.e.e.e.c.f.#.f.UmwoWoXkQm0nooYoZo0o1aKo2o3f2o4o5bfero6o7dacRblo8o9p.p##j.cpapbpcpdpecRb4b3b4dbcQcQcPaLpfpgphoJpipj####.c.ccqoM.fQtQtQt",
".#.#.#Qt.e.eQt.#hO.b.d.d.bpkaaaGbebZb1cHcHb0gmdebYaMplpmhFpnpojJos.g.g.g.e.d.c.d#Gpppqprps.sptpupvpwaKpxpydIdJf1cRoApzfZesdFpAc8lPpBpCpD.RdrpEpFpGdBpHaMd8b1d8etcRcQhZaMo#pIpJpKpioK.m.m.c.ccqcq.fQtQtQt",
".#.#.#Qt.e.g.c.#m4.H.ddr.vpLabaNbfb1cHdbcHb0dedecGbfbTpMhGpNi5pOaw.g.g.g.e.e.d.epPpQot#lpRpSpTpUpVaMcRpWdFdJb7escRfYo5cRdaeAhiblpXpYpZp0.mekgbp1p2p3lYaLd8b0d8cKcRcQdhcRp4p5p6mooKoK.R.m.cQtjUjU.fQtQtQt",
".#.#.a.f.e.g.c.#p7.I#m#m.Zp8acaIbfcHcIcIdbb0dedeb2pep9q.q#ipi6kNeO.d.e.e.e.e.e.e.gm3.WpRqaqbqcqdaLdad8d8eshZcGesdaqedadaqfc#aLqgqhqiqjqk#2.dqlqmqnqoaIaKd8b0d8cQcQdaqpcQaIqqqrqspjoK.R.mQtQtjTjTQtQtQtQt",
".#.#.a.f.e.g.c.#.0.InzoN.ZqtadaHbfdbcIc#dbb0dededaquqvqwqxiqqyqzmpQt.c.d.d.d.d.d.c#hm4qAqBqCqDaJjAeTd8d8qEd3dab1bWdadFiDc#aKqFqGqHqIqJ#dqKoNqLqMqNqOqPaLb3b5cQcQd8b5qQdaaJqRqSqTqUoK.R.mQtQtj.j.QtQtQtQt",
".#.#.a.f.g.g.c.#.0.HqV#jiLqWaeaIbgcHc#c#c#b1deded8qXqYqZq0q1ipkfbO.a.f.f.f.f.f.#.qq2q3q4q5qDaJq6aLaMcRc.q7esd8dbcQd8q8b1aMq9r.oZr#je.s.yra#jrbrcrdrerfaLeTdFdbcQb3dJrgbZblrhrijHrjpj.R.m.fQtj.j.QtQtQtQt",
".f.f.#.f.c.d.c.f.Z.wrk.diLrlafblbgcHc#c#cIb1debYcRrmrnrorpomkMrq.#.#.f.fQtQtQt.arrrsrtrurvaJq6rwoAcRdcdaesesb3d8b1dah0aMgnrxryrzcYrAcirB.c#k#jrCrDrErFaLeBdFlucRbWdFcMb5aKrGrHrIrjpj##noQt.crArAQtQtQtQt",
".d.c.f.a.a.#.c.c.z.l#H.CiLrJahaLbkb3cKcKbid6evd7rKrLrMrNrOrP.C.Eksk2l3l3#GdurQrRrSrTrUrVaLpxpxoAb4b5b6b6b5b5b5b6dIrWaMnrrXrYrZr0bxr1r2r3r4r5mfr6r7r8r9aLs.esjAaMcRcJb3cQaKs#sasbiOkqiLiL.c.ecsavQtQtQtQt",
".e.d.f.aiL.b.c.dQtQt.c.AdsscahaMbjb3dcdcexd6ewbiaJsdseg6l3ivi9r4bFsfdreksgm3nDn8shsisjaMdad3ercRb2skskcLb5b2b5cLsldFsmsnsospsqsrcjssstsusvswsxckiKsyiCaLeFexaKaLaMcJcKcQaMszsAsBmpkqiKiK.cducsavQtQtQtQt",
".d.cQt.#.h.b.c.e.k.m.E.zrrsCsDaMbkb4dcdcbjexdIbiaKfRgwg7.9kej.jUsEsFsGsHsI#ysJsKsLsMaKaMcHd8cJetb2b6b5b2b4dcb3b5sNdFsOsPsQg2sRsScssTbHsUsVsWsXsYl2pusZaLeFs0cRbfcJcRcQcKaMs1s2s3mpeOiLiL.c.gava0QtQtQtQt",
".c.cQt.#.h.a.d.e.8.n.Pnol2s4s5aLbkb4dcdcbkbid6biaLs6gxg8.V#7jabxs7jTg..liKs8s9t.ozfTt#tad8d8d#bWb2b2b2b4cJcJcJb4dJfEcRlRtbtctdtejStftgthsxchtitjk0tktlaLexfWd8bVc#cJd8dbaMs#s2tmiOeO.h.h.d.gava0QtQtQtQt",
"QtQt.f.#.b.a.d.e.8.m.P.MtntktoaLaMb4b4dcaMbkd7biaLnHgytp#ntqjaoMbDkwtrtstttutvtwaLtxtydFb2tzltesb2b2b4cKbgbgbgcJb2gkcHaLtAtBtCtDcjtEtFtGtHsx.wtItJtKfSaLextLdafZdcdbb0b4aLtMtNtOiOeO.b.a.d.ea0cuQtQtQtQt",
"QtQt.f.#.b.a.d.e.i.o.z#qjutPtQaKaMb3b3b4aMaMexbiaKfOgzh.#AdVjdjejbk5h6tRtStTbmaKeBtUdIdJdEiDesesb5b2b3cKbgbfbfbgd8dFn0d5bltVtWtXtYtZlKt0jca0.n.1t1t2t3aLd7dGeso2d8eTcGcQaKt4t5t6iOeO.#.#.d.da0cuQtQtQtQt",
".f.f.f.#.b.a.d.enA.p.wpRt7t8t9blaMb2b5b2aMaMbibifkaJgA#O#hiwa0jWu.u#mFuaubmCaKfUucuddHeagkdad8b1b6cLb5b4cJbgbfbgcQb2b7dEh1aKueufuguhuikAm2nzujukulumaIfXb6dgdab4dacPfFcQaJunuoupbOeOQtQt.d.ccua1.fQtQtQt",
".f.f.f.#.b.a.d.e#hnB#fuqur#YusaJaMb5cLb6bkaMbiexflblgBh#.r#6jcjXksutpuuuuvaKuwfWf1e.pyeUeseTjod8cLskb6b3cKcJbgbguxb3bYbYdac9uyuzuAuBuCuD.m.erPkpuEuFbleycLdgd8cQdadEfEcRuGuHuIrIbOen.c.c.cQta1a1.fQtQtQt",
".f.fQt.f.b.a.d.e.f.G.JiL#x#OuJaHaLdJcMdddad8eyeUuKaKuLuMuNfwjcsFmfuOuPuQaLuRuSdJd8uTaMcReTkidccHb7uUhvdFhZd8cQd5dbb1b8bYb8b0cIfTuVuWuXj0uYuZu0u1riu2bfn0dIq8fHfed3b0fiaMaHu3u4u5bOen.d.dQt.fa1a1.fQtQtQt",
".fQt.cQt.b.a.c.d.m.a.v.Z.5u6u7u8aKb8cNdedFd9u9eVdFaLv.v#vahOcuj.jWvbvcaNvddKdKdIvepxoAj4d#dad8d8vfd8dakjdEesesdab1b0bZb8b8bZb1bfuzvgvhvivjePvkvlvmvnaMcOdIcGfHvocFesd#aLvpvqvrvsiOeO.e.d.f.#ela1.fQtQtQt",
"QtQt.cQt.b.bQt.c.n#2noe7lBvtvuvvblfEdIcNtLvwe.esdFfjaHvxvyvzlcjbcqvAvBdNblvCnKdJd8bVvDfXb3dFhWkiaMvEvFcRvGfFdJcLb8bZb0b1b1cHdbbgaKaJvHvIvJc4vKvLvMvNfHvOvPvQvofHiDdauxblvRvSvTvUiOeO.e.d.#.bela1.fQtQtQt",
"Qt.c.dQt.b.bQt.c.AgN.z.D.W#evVvWaJqehWdIdHeadFesdFvXaJhdvYvZjfjXu#v0v1m#cSblv2obcRo6v3cRb1kjb1aMv4v5v6v7aLc9fFv8b8bZcHdbdbcIc#bgexv9aIgDw.w#wawbwcaKfHgib3wdfefHd3b4jBaJwewfwgwhiOkq.d.c.a.helcuQtQtQtQt",
".c.d.d.c.b.b.fQt.zgN.zl3wigOlxwjaIc#cFq8dIdJdFeUeswkaLwlwmwnjgsVwowppLwqwrwsaIvNwteyesdaqfc#aMwuwvwwwxwytAaKwzdFbZb0dbc#c#c#c#bhgHwAaJaHhAwBwCwDwuaMwEwFiVwGiUgjeswHeraHwIwJwKwLiOkq.d.c.hiLelcuQtQtQtQt",
".d.e.e.c.b.h.#.f###2.n#Hpp#BwMwNwOaMcKdEdJdJucwPeseswQaKwRwSwTa1jWelqkwUmEwVsDaIpxd9dFeCc#aKwWwXwYwZw0w1w2w3aLetb1b1cIc#c#c#cIhipAdFw4pHaLw5w6w7bfcRiTfdw8w9x.b3b3uxaLx#xaxbxcllmpmp.dQtiLiKelcuQtQtQtQt",
".e.e.e.c.b.h.#.f.o.o.mxdxepp#yxfxgcaaMqeb7dHpyeBxhdFuRhfo#xixjxksFxlxmxnxoxpxqxraKcRgHxsaLxtxuxvhHxwxxxyxzxAxBxCc#dbcIc#dbcHb1d9dauweVdFhhesaMpxxDxEfHxFxGiexHxIvQkVxJxKxLxMxNxOmpmp.dQtiLiKela0QtQtQtQt",
".d.d.e.c.a.b.#.f.y.#.fxPxQpQxRxSxTueaLffdJebf1cRveeFxUxVaKrLxWxXxYxZe8.Ox0x1x2x3kGblc8blhAx4x5x6x7x8x9y.y#yaybaHfTbfbgbhb1d9b1hio2d8ycdIecyddbcRxHyefHcKjCfHyfgVygaMpVyhyiyjykpjkqeO.e.d.biLelcuQtQtQtQt",
".c.c.cQt.f.f.fQt.f.fQt.c.e.d.fylymrGblyncNyob3cRcRfXdHdIypblyqyrysjejSytyuchyvywyxyyp4yzyAyBwM.obxjVavr4yCyDyEyFp4aJaMdFe#escRcRbkdcb4b3b5b2dccKd8d8cQcRcQcQgjess0aKyGyHyI.veK.wQt.eovov.c.#.b.b.fQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtePyJyKlscRyLyMescRcRhzb8v8fEcRlRyNyOyPyQyRySyTu#yvyUyVyWyXyYyZsxy0r1y1y2y3y3y4y5y6y7gDbly8oboby9aMcKdcdcdcdcdcdcdckhfIvGdbdcdcdccRz.lPz#zaiLk1kb.v.f.ddVov.eQt.a.b.fQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtzbzczdzeaKygfJcLescQd#q8gmzfd8aMhAzgzhzi#szjzkzl.zzmznzozpzqk0xmjYsuzrbHzsztjWzuzvzwqCzxaIblaKcRcRdcdcdcdcdcdcdcdccQcQdcvGfIvGvGpxblzyzzzAm3kQg..a.a.#.c.d.cQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtbOzBzCzDv4cJv8v8dJesd3b8dJdggkcQaKp4zEzFzGur.Sdu#8zH#1zIzJ#u.3.FjXsxzKzLzMtGzNzOzPzQzRkmdNaNzSbjdFb4dcdcdcdcdcdcdccQcQcQdbcQcQcQaKp4zTzU.fzVzWm0##.b.aQt.c.c.c.c.cQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtkqzXzYzZz0aKd8bYdIb8cGb0dFb7q8fEz1aLz2z3z4z5nfz6nez7l4l3.A.nz8kcjSksz9A.kxA#ks#i.RAaAbAcAdAeaKvwAfb2dcdcdcdcdcdcdcfIdcdbkhcQcQcQblAgAhAiAjAkpq#Ano.a.#.c.e.d.cQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQteOAlAmAnAow3aLcQb8bXgkb0daesdFb7dFApaLwlAqArAsAtAu.j#mxPxddSl4#H#kAvAwAxAyAzaXne.gf9AAABACADAEd8AFb3dcdcdcdcdcdcdcdccQdcc.jodcwHbdAGAH.xivzVdV.k.a.a.f.e.g.e.dQt.fQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtenAIAJAKALAMANaLvGb5hWeTcHdbdcd8das0wkaLaJAOAPAQARASATkpc2AUa8AVl4AWkxAXbtcv#mjwrPe9gbAYAZA0A1aLwHdcdcdcdcdcdcdcdccQcQcQwHc.khA2A3A4#L#x.fdrdr.Dno.#Qt.e.g.g.dQt.fQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQteOA5A6A7A8A9B.aIjAd8cGcPb4luwzwzwHeswArwB#blaHBaBbw#xfBcazBdBekaBf#pBgBhje.H.vlpkpu1BiBjBkBlBmBncQdcdcdcdcdcdcdcdcjocQcQkhdccQfIBoBppursBq.H.B.A.A.#.f.c.d.e.e.cQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtkqBrBsBtBuBvBwBxaJcResb7b5cQcRcRBybgbhhihibhbffToiBzBABBBCBDBEBFBGaW.ZBHBIe3sJBJBKBLBMBNBOBPkVifBQdakhcQcQfIdccQjodbdbdbdbdbdbdbbeBRmDBSBT#v.Fcve8.#.b.b.aQt.edu.g.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtmpBUBVqyBWBXBYBZB0aKc#hZfFnsd.kVcRbfbghie#dHeahibfblB1B2BaB3B4B5B6B7B8B9C.C#CaCbCcgIfpnTaLcResCdCedafIcQcQdccQcQcQdbdbdbdbdbdbdbbfaJefCfCgChl6.SCi.#.hiL.h.f.edudu.dQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtiOCjCki6ClCmCnCoCpw3CqcJdEdEdad8cKbfbghie#dHebead9pxpezSuGuzCrCsCtCus6CvB2CwlgaJblaLcRfHCxxHCyb3Cxd8vGdccQdbdccQcQdbdbdbdbdbdbdbbgCzblrvvxv1CA.b.U.f.a.h.b.f.d.g.g.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtbOCBCCCDA6q1CECFCGtWCHaKaMnidadacFbgbghieUeadHdHe#dacRaMaMaKaLaLaMaKaMaMaMaMaMfZdjhWhvCICJCKwdiWfecQdbvGdbkhc.wHkhdbdbdbdbdbdbdbbhCLCMaJqDCNvVCO.CQt.f.#.#Qt.c.d.dQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtiOCPCQCRCSA6CTBuCUCVCWCXlYpxCYnsb5b0b1b1b1b1b1b1b1cFbWb4b4b1eTeTeUCZC0kIC1dFdFdFdFb7b7vPb3iView8C2cQdcfIcQcQjoc.dcdbdbdbdbdbdbdbbhcRC3uGaHC4C5C6C7.c.d.c.c.c.c.f.f.fQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtmpC8C9D.D#DaA6DbDcDdDeDfDgaIaLfIcGb8bZb0cHdbcIdbcHeTeThZfFgkbZesdFdJdIdIdJdJb7dFesb1jmDhDiDjieiefHfHdcvGcQcQdckhcQdbdbdbdbdbdbdbbhaLaLpdaIuVDkDl.GQt.cQtQt.c.c.#.#.fQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtkqjOi7DmpnDci3DnDoDpDqDrDsDtDuc9dEbYbYbZcHcIc#cIdbbWb1esesd8dcwzDvveDweBd9bio2j6BycKcKcKcIDxhxDyb3gjdcvGcQcQwHA2fIdbdbdbdbdbdbdbbgaMaKaKkGDzDADBlB.f.#.b.a.f.cQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtkqDCDDDEDFDGDHDIDJDKDLDMDNDODPjpblcIb0b1cHdbcIdbdbd8d8eTbWdccQcJc9aMaMcRaMbhbgcRcRDQcIcKcKfHDRDSifdabkpxaKblbdA3BobebfbgbhbhbhbgbfaKrFDTDUv#DVDW.A.f.#.b.aQt.c.d.d.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQteOeOeOeOeOenososawrRDXDYDZD0D1D2aIaMcRcQdaesesesb4cQcQcQcQcQb3vGcRaMc#c9cIcQd8d8h0bWb4d8b3b1yefis0z.blp4AgAGA4BpD3aJblD4cRaKaMaKt3p4egD5D6D7.Mg#QtQtQt.c.d.e.e.e.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.d.d.e.e.e.d.cgO.qiMD8tnD9pSE.E#EaEbaKaMd.qeeTd8cQcQcQdab5dJdFc#cJcJcJdbd3dEb9dFesb1jmvGetc#oAaKlPzyzTAhAHpkpuEcgDblC3EdaLaKEep4EfEgEhEicY.PcvQtQt.c.d.d.e.e.d.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.d.d.d.c.ck1#g#fdsxn#vEjEkElEmEnEoEpaKaMcQd#cPhZdhqpqQrgcMb3cQcQd8b2cGfFn0cPd#uxBybVoAEqpVyGz#zzzUAi.x#xrsErCfaGaJuGEsaKEtegEgEuu6.4.B.R.C.f.f.fQtQt.c.c.cQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.cQt.f.z.vEv#dEwExEyEzEAEBECEDEEq9EFcaaLaMcRcQdabZb5cQcQcQcQd8cQcQcRBnaLblaJoiEGEHEIyHzazA.fAjiv.fEJvZCgEKuQaHaIELEMENEhu6iJ.aEOfwQt.#.#.#.f.fQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.f.fQtQtQtQtQtqK#2.G.K.uBHrrgeEPEQERESETEUEVEWoHpftwp4aIaJblaKaLaMaMaMaLaKblaHaHEXEYEZE0E1xLE2yIiLm3zVAkE3#j.q#vE4E5E6E7uVDzE8E9F..2.aQtoN.9.8.#.a.#.f.fQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.#.#.#.f.fQtQtQtk1gO.#lJcY.7.6.GF#jJkMFaFbFcFdjGoIpgvmp5qqqRFerGFfszx#s#tMt4unuHu3FgFhlqwJxbxMFirck1kQzWpqdV#j.k.ztsa.FjFkFlDAE9aV.6.yFm.Tm0Qt.P.#.#.#.fQt.c.c.cQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.#.#.#.#.#.f.f.foE.QqK#2FngNno#2FoFpFqFrjPFsFtFuolphpJp6qrBjrirHsasAFvFwtNBCuoFxqSFyFzFAvUqzxNnDeKkbg.m0#A.k.D.Alm.C.sD8FBFCFD#w.M#g.m.j.RQt.flB.#.#Qt.c.c.d.d.d.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.#.a.#.#.#.#.f.f.m.D.n#h.DFE.m.BFFFGlVFHFIFpnYisoJoJpKmoqsqTjHrIFJFKFLFMtmFNFJFOFPvsFQwhFRFSFTeO.w.v.a##no.ano.Ae8FU.T.CFV.wlBlBqK.l.P.f.Q.PlBgN.#.fQt.c.c.d.d.d.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.#.#.#.#.#.#.#.#.f.fQtQtQt.c.c.ceneneOkqmpmpkqeOoKpipioKpjqUrjrjiOmpmpiOiOiObObObOiOiOiOiOmpmpkqQt.f.a.b.a.a.#.#.#.#.fQt.cQt.f.#.#.#.a.a.a.a.#.#.fQtQtQtQt.c.c.cQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.f.#.#.#.#.#.#.f.fQtQt.c.d.d.denenkqmpiOiOiOmpoLpjoKoKoKoKpjpjkqkqeOeOeOeOeOeneOeOeOkqmpmpmpeO.e.d.#.a.#.fQt.f.b.h.a.f.d.c.#.a.#.#.a.b.b.a.#.fQtQt.f.f.f.fQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.f.#.#.#.#.#.fQtQt.c.d.d.d.d.cQt.f.a.b.b.bno##.m.R.R.R.R##iLiKiL.h.b.#Qt.c.d.e.e.e.d.d.d.govdV.cQt.c.e.e.c.biL.h.#.cQt.b.h.#.#.a.b.b.a.#.fQt.f.#.#.a.a.#.fQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.cQt.f.#.#.#.#.#.fQt.c.d.e.dQt.f.#.#.a.a.a.ano##.m.m.m.m.mnoiLiKiL.h.a.#Qt.c.d.d.d.c.cQtQt.ddVov.d.c.e.g.g.d.a.h.b.#.cQt.a.b.#.f.a.b.b.a.#.fQt.f.a.a.a.a.fQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.d.e.d.cQt.f.#.#.#.#.fQt.c.d.e.c.#.b.b.a.#.fQt.c.c.c.c.cQtQt.fQt.c.d.c.d.d.d.d.cQt.f.#.a.hiLiL.b.c.e.c.c.d.e.e.dQt.f.fQt.c.c.f.fQtQt.#.a.a.#.fQt.f.f.a.a.a.f.c.d.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.e.g.e.d.cQt.#.#.#.#.fQtQt.c.d.c.a.b.a.a.#.fQt.c.c.c.cQtQtQtQt.c.edu.g.g.e.d.cQt.f.#.b.hiLiKiKiL.#QtQt.c.c.c.d.d.d.e.d.c.c.cQt.c.cQt.#.a.a.#.fQt.f.#.a.a.f.cdudu.dQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.gdu.g.e.cQt.#.#.a.#.fQtQt.c.d.da0cucucua1a1a1elcqcqcqjUjTj.j.rAcscsavava0a0cua1a1elelelelelelel.b.aQt.cQtQt.f.c.gdV.g.d.f.fQt.c.cQt.#.a.a.#.fQt.f.#.a.#.cduFWFX.eQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.e.g.e.d.cQt.f.#.#.#.fQtQt.c.c.cavava0a0cua1eleloMoMcqjUjTj.j.rAavava0a0cucua1a1a1a1a1cucucua0cu.b.bQt.cQt.f.fQt.gdu.g.d.#.#Qt.c.cQt.#.#.#.#.fQt.f.f.#.f.dduFXFY.eQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.c.c.cQtQtQt.f.f.fQtQtQtQtQtQtQtQtQtQtQt.f.f.f.f.f.f.fQtQtQtQtQtQtQtQtQtQt.f.f.f.f.fQtQtQtQtQt.f.fQtQtQtQtQtQt.c.d.c.c.f.fQtQtQtQt.f.f.f.fQtQtQtQt.fQt.c.d.e.e.cQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt"
]
image3_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x74\x49\x44\x41\x54\x38\x8d\xed\xd5\xc1\x09\xc0" \
    "\x20\x0c\x05\xd0\x6f\xe9\x36\x81\x2c\x10\xb2\xff" \
    "\xdd\x85\xd2\x53\x85\xb6\xa9\x91\x48\x0f\x05\x3f" \
    "\x08\x1a\xf0\x29\x12\x10\xf8\x28\xc5\xa9\xd9\xc4" \
    "\xde\x96\xcd\x2b\x9a\xd9\xeb\x00\x00\x66\x0e\x2f" \
    "\xe0\xc2\x51\x98\x39\xc4\xf7\x0c\x4c\x44\x6d\x5e" \
    "\x6b\x35\x38\xcf\x92\x82\x45\xe4\xb2\xf6\xf0\x14" \
    "\xac\xaa\x8f\xda\x1d\x4f\xc1\xa5\x74\x1b\x22\x07" \
    "\x9f\x9d\x11\x1d\x96\xea\x8a\x91\x2c\x78\xc1\x0b" \
    "\xee\x64\xe6\x07\x19\xf5\x7e\x92\x03\xad\x45\x2a" \
    "\x04\xcc\x4e\x50\x20\x00\x00\x00\x00\x49\x45\x4e" \
    "\x44\xae\x42\x60\x82"
image4_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x99\x49\x44\x41\x54\x38\x8d\xed\x94\x41\x0e\x85" \
    "\x20\x0c\x44\x5f\x89\xc7\x36\x7f\x61\xbc\x77\x5d" \
    "\x28\x48\xa4\x28\x60\xff\xce\xd9\x54\x8b\xbe\x8e" \
    "\x13\x04\x3e\x1d\x92\x81\x77\xf4\x81\xa1\x23\xdc" \
    "\x2b\x34\xf6\xf4\x7a\x3d\xe2\xb8\x65\xa8\x84\x3f" \
    "\x40\x01\x98\x2a\x0b\x3d\x5f\x62\xc5\x83\x00\xaa" \
    "\x1a\xd7\x05\x50\x44\x9a\xb9\xd5\x07\xa7\x73\xa8" \
    "\xa4\xba\x4f\x92\xa2\xdf\x33\x3c\x64\xc6\x3b\xeb" \
    "\xbd\x82\xe5\xb8\xad\xde\xcb\xcc\x78\x20\xeb\x42" \
    "\x66\xc6\x39\x74\x5d\xfa\x80\xf3\x6f\xaf\x66\xc6" \
    "\x6f\xa1\x9c\x3f\x88\x2f\xb4\x70\xec\x05\xcd\xc0" \
    "\xbe\xd0\x78\x93\xf6\x8e\x17\x14\x92\x63\x5f\x68" \
    "\x6c\x3e\xef\xf6\xba\x3c\x8f\xdd\x36\x6d\xc4\xc0" \
    "\x45\x2c\x87\x81\xf8\x08\x00\x00\x00\x00\x49\x45" \
    "\x4e\x44\xae\x42\x60\x82"
image5_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\xa0\x49\x44\x41\x54\x38\x8d\xd5\x95\x4d\x0a\x80" \
    "\x20\x10\x85\x9f\xd1\x46\x68\xe1\x8d\xe6\x62\xd2" \
    "\x22\xbc\x98\x37\x6a\x21\xb4\xac\x45\x19\x92\xc6" \
    "\x64\x69\xe0\xb7\xf1\x87\xf1\xf1\x1c\x47\x05\x2a" \
    "\x21\x8e\x76\x2d\xad\xdb\xfb\x9e\x99\xf6\x56\x8f" \
    "\x80\xb5\x36\x4b\x85\x88\xce\x35\x44\x04\x00\xe8" \
    "\x0a\x39\x8c\xe8\xf9\x90\x34\xd2\x29\x2c\xc3\x7c" \
    "\x8e\xbd\x53\x0f\xeb\x58\x3a\x05\xe9\x54\x34\x1f" \
    "\x8a\x02\x7b\x2a\x7d\x3a\x1f\x09\xbf\x85\x4d\xc5" \
    "\xd5\xd9\x53\xaa\x39\x6e\x4f\x38\xca\xb1\x99\xe2" \
    "\xd2\xe1\x08\xab\xe1\x56\xf8\x2e\x30\x97\x7f\xcb" \
    "\x4d\x8f\xf9\x42\xd7\x5d\xbe\xbe\xd2\xe1\x43\x95" \
    "\x3a\x93\xf6\xca\xad\x3d\x61\x11\xf4\x4b\x7d\x4f" \
    "\x82\x0f\xf9\xc0\x06\x9b\xb5\x1e\xcd\xed\x31\x8c" \
    "\x5c\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60" \
    "\x82"
image6_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x02" \
    "\x9c\x49\x44\x41\x54\x38\x8d\x8d\x95\xad\x76\xdb" \
    "\x40\x10\x85\x3f\xf7\x18\xcc\x32\x89\xd9\x50\xd0" \
    "\x61\x36\x34\x4c\x98\xc3\x62\x96\x40\x87\x25\x6f" \
    "\x50\x3f\x42\x61\x61\x02\x1b\xe6\xb2\x84\x25\x50" \
    "\x61\x2e\x8b\xe1\x42\x99\x49\x6c\x86\x6d\xc1\x4a" \
    "\xb2\xfc\x77\xda\x21\x92\x66\x57\x77\xee\xdc\x3b" \
    "\x5a\xf5\x38\x13\xaf\xaf\xaf\x41\x44\x48\xd3\x74" \
    "\x2f\x6f\x66\x00\xa8\x2a\x00\x55\x55\x91\x24\x09" \
    "\x57\x57\x57\xbd\xee\xbe\xfe\x39\x60\x11\x61\x32" \
    "\x99\xb4\x40\x87\x6b\x4d\x94\x65\x89\xf7\xfe\x68" \
    "\xcf\x59\x60\x80\xcd\x66\x73\x04\x76\x58\x48\x55" \
    "\x71\xce\xfd\x3f\xf0\x29\x00\x33\x3b\x2a\x70\xaa" \
    "\x23\x80\x6f\xa7\x92\x79\x9e\x07\x33\x6b\x99\x38" \
    "\xe7\x70\xce\xed\xe9\xdd\xe8\x2f\x22\x47\xfa\x9e" \
    "\x65\xac\xaa\x24\x49\x42\x59\x96\x88\x48\x6b\x54" \
    "\x37\x4e\xb5\xff\x4f\xc6\x10\x5b\x3c\x9c\x88\x2e" \
    "\x68\x53\xec\x9c\x14\x27\x19\x37\x6c\x4e\x31\xed" \
    "\xe6\x55\x75\x6f\x42\xba\x71\xa4\x0d\xc0\x6a\xb5" \
    "\x0a\x59\x96\x31\x1c\x0e\xcf\x82\x37\x46\x7e\x7e" \
    "\x7e\x02\x20\x92\x30\x9f\x5f\xb7\x78\x7b\x8c\xdf" \
    "\xdf\xdf\x83\xf7\x9e\xfc\x23\x47\x66\x82\x88\xb4" \
    "\x00\x87\xd7\x86\x69\x59\x94\xe4\x79\xce\xb6\xda" \
    "\xf2\xf0\xf0\x10\x66\xb3\x19\xd7\xd7\xd7\xbd\x5e" \
    "\x17\x74\xb3\xf1\x54\xc5\x16\x35\x80\xd3\x4c\x01" \
    "\x9c\xa4\x08\x02\x0e\x7c\xe1\x59\xaf\xff\xb0\xdd" \
    "\x16\xa8\x1a\x17\x17\x19\x8b\xc5\x22\x4a\xd1\x30" \
    "\xbd\x9c\x5e\xe2\xd2\x14\x55\x03\x53\x8e\x6c\x31" \
    "\x03\x84\x9c\x4f\x3e\x78\x65\x6a\x53\xd2\xaf\x94" \
    "\xe7\x97\x67\xfc\x57\xfc\xfa\xd4\x94\x6c\x74\x11" \
    "\x41\x9f\x9e\x7e\x85\xb2\x28\xc3\xff\xc4\x57\xf8" \
    "\x0a\xa3\x30\x0a\x12\x24\x8c\xc2\x28\xac\xd7\xeb" \
    "\xf0\xe3\xfb\xcf\x30\x1e\x8f\xc3\x60\x90\x85\x24" \
    "\x49\x42\x36\xc8\x42\xbf\xda\x56\xdc\xdd\xdd\x9c" \
    "\x75\xf7\x30\x52\x52\x2e\x99\x92\x23\xcc\x98\x31" \
    "\x1e\x8f\x49\x64\x48\x69\x05\xcf\xbf\x5e\xa8\xaa" \
    "\x8a\x74\x90\xd2\x37\xc0\xfb\x22\xce\xa3\x19\x88" \
    "\x10\x6b\x48\xed\x36\x38\x5c\x54\xdc\x14\xc4\xf1" \
    "\x60\xdf\xb9\xc1\x33\xb4\x21\x7f\xd8\x80\x19\xe9" \
    "\x70\x18\xd7\x6b\x77\xfa\x65\x51\xe0\x45\xa2\x9e" \
    "\x66\xb4\xbe\x39\x88\x2e\xd6\x9d\x38\x03\x15\x20" \
    "\xe6\x04\xf0\xb6\xc5\x88\x67\x88\xdf\x6c\x5a\x4f" \
    "\x1c\xf5\xb8\x35\x09\x6b\x00\xb1\x76\x28\x14\x8b" \
    "\x35\x74\x6f\x67\x3b\x39\xd2\x78\xda\x09\x45\xe9" \
    "\x23\x60\x65\xe7\x05\xad\xc9\x76\x37\x1a\x20\x0a" \
    "\x76\xb8\xe2\x30\x2b\xa9\xfb\x6c\x7a\x63\x32\x99" \
    "\xf2\x0d\xeb\xb0\x6c\xc9\x6a\x7c\xb4\xfa\xba\x07" \
    "\xea\x9a\x6d\x35\x68\x0d\x58\xcb\x39\x18\x0c\x58" \
    "\x2c\xee\x22\x63\xef\x7d\x63\x15\x88\x41\x25\x40" \
    "\x15\x9d\x33\x8b\x30\xd2\xb0\xb2\x1d\x18\x3b\xcd" \
    "\x31\x43\x04\x96\xcb\x25\xf3\xf9\xbc\xd7\xcf\xb2" \
    "\x8c\x8f\xb7\x0f\x7e\xbf\xbd\xa1\x6a\xc4\xf3\x47" \
    "\xd8\x1b\x3e\xe9\x3c\xcb\x0e\xb2\xed\xb3\x9e\xa6" \
    "\xe5\x72\xc9\xe3\xe3\x63\x0f\x3a\x87\xd0\x6a\xb5" \
    "\x0a\xab\xd5\x1b\xdb\xfa\xff\xa5\x68\x6d\xca\xce" \
    "\x99\xdd\x5f\x03\x54\xcb\x78\x5f\x19\x93\xe9\x84" \
    "\xdb\xdb\x5b\xee\xef\xef\x5b\xbc\xbf\xd1\xf6\x9e" \
    "\x0c\x3f\xec\x24\x86\x00\x00\x00\x00\x49\x45\x4e" \
    "\x44\xae\x42\x60\x82"
image7_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x73\x49\x44\x41\x54\x38\x8d\xed\x92\xc1\x0e\x80" \
    "\x20\x08\x40\xb1\xef\x66\x1d\x1c\xff\x4d\x87\x6a" \
    "\xa8\x88\xa1\x76\x69\xf9\x36\x0f\x28\x3e\xd8\x00" \
    "\x60\xf1\x59\x42\x5f\x3a\x71\xf5\x36\x02\xe0\x8e" \
    "\x99\x2b\x09\x88\x01\xd0\x28\x54\x17\x6a\xe4\x7f" \
    "\x21\xce\x1f\xb5\xb0\x5d\x38\xed\xdc\x90\x60\xd0" \
    "\xf1\x13\x79\x63\x5b\x3b\xc9\x2b\xd5\x18\xe2\x39" \
    "\xa9\x43\xec\x1d\x5a\xb7\x78\x5c\xee\x10\x7b\xe4" \
    "\xb2\x15\xaf\x40\x91\xf8\x94\xde\x47\x18\x1e\xce" \
    "\xa5\x9e\xde\x9e\xc5\x9f\x38\x00\x62\xac\x28\xb1" \
    "\xe3\xd7\x01\xd9\x00\x00\x00\x00\x49\x45\x4e\x44" \
    "\xae\x42\x60\x82"
image8_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x74\x49\x44\x41\x54\x38\x8d\xed\x92\xc1\x0a\xc0" \
    "\x20\x08\x40\x6d\xdf\x2d\x3b\x84\xff\xed\x0e\xa3" \
    "\x58\x6a\x26\xd1\x65\xe0\x83\x0e\xa5\x3e\x85\x04" \
    "\x48\x7e\x4b\x91\x0f\x54\x89\xf1\x9e\xa5\xa3\xca" \
    "\x0f\x8a\x89\x63\x65\xb3\x06\xc4\x2d\xd6\x13\xc6" \
    "\x49\xbd\xc2\x59\x83\x16\x13\x62\x19\xf0\xf9\x36" \
    "\xc0\xa2\xef\x00\xd7\x5a\x62\x61\x4d\x3a\xb2\x29" \
    "\x96\xf2\xa3\x62\xff\xa3\x37\xc5\xeb\xed\xe9\x62" \
    "\xaa\xd1\xa2\xe8\x4a\xaa\xa2\xf7\x50\xdd\x12\x74" \
    "\x8c\x0f\xd0\xab\x93\x24\x67\x78\x00\x59\x6e\x28" \
    "\xb1\x74\x3f\x46\x86\x00\x00\x00\x00\x49\x45\x4e" \
    "\x44\xae\x42\x60\x82"
image9_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x82\x49\x44\x41\x54\x38\x8d\xcd\xd3\x41\x12\x80" \
    "\x20\x08\x05\x50\xe8\xe0\x2e\xbc\x38\xad\x32\x73" \
    "\x50\x3e\x48\x53\x7f\xe3\xe4\x8c\x4f\x24\x25\xfa" \
    "\x28\xe2\x9c\x6f\x39\x92\x0b\xf9\x27\x6c\xb6\x01" \
    "\x85\x35\x88\x77\x61\x13\x88\xc2\x57\x64\x18\xcd" \
    "\xa0\x15\xf5\x20\xb4\xe6\xb5\x5b\xe1\x09\xdc\x06" \
    "\x22\xb8\xe2\x2a\xcf\x31\x05\x6e\x18\xdf\xdf\xf8" \
    "\x06\x06\xaa\x55\x1c\xc6\x35\x64\xc4\xdc\xf8\x0c" \
    "\xd0\x20\x1d\x57\x7a\x5c\x85\xa8\x84\x5f\xdc\x02" \
    "\x5e\xa5\x30\x7a\xfc\xcd\x07\xe2\x3a\x1d\xf2\x83" \
    "\xec\x2b\x37\xd9\xad\x5f\xb4\xdf\xef\xd4\x9c\xfb" \
    "\xf7\x2f\xac\x98\xc8\xcc\x89\x00\x00\x00\x00\x49" \
    "\x45\x4e\x44\xae\x42\x60\x82"
image10_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\xbf\x49\x44\x41\x54\x38\x8d\xd5\x93\x41\x0a\x83" \
    "\x30\x10\x45\xdf\x48\x8e\xe5\x1d\xbc\x8c\x3b\xa9" \
    "\x8b\xf4\x6a\x9e\xab\xd3\x85\x35\x0d\x26\x63\x62" \
    "\x44\x4a\x3f\x0c\x42\x66\xfc\xf3\xf8\x24\xf0\x6f" \
    "\x12\x40\x2b\x66\xda\x8c\x55\xf3\xde\x22\x12\xcf" \
    "\x9d\x92\xcb\x98\xc0\xba\x2d\x7c\x45\x44\xcf\x9a" \
    "\x07\x63\x8b\xba\xd5\x3c\x44\x91\x23\x5e\xcf\x7c" \
    "\xc1\x62\x36\x97\xa9\x25\x40\xc1\x1f\xf4\xfd\xa7" \
    "\x52\x75\x01\x5d\x24\xa9\x38\x9e\x7d\x6f\x53\xdf" \
    "\x4f\xe4\xcc\xab\x32\x3e\xea\x0f\x03\xc0\xc4\xb2" \
    "\xa0\x71\x2c\xe6\xad\xd8\x9b\x59\xb7\x66\x1c\x3b" \
    "\xe0\x95\x98\x5f\x26\x16\x79\xee\x4e\xbc\xc2\x2c" \
    "\x97\x88\x55\x1f\xe6\xa2\xcb\xc4\x96\x9a\x89\x4b" \
    "\xcb\x6f\x23\xee\x36\x1a\xab\x62\xe2\x52\xc5\x72" \
    "\x94\xdf\xbf\xb6\x10\xbb\xf2\xc8\x97\xb8\xa4\x6c" \
    "\xc6\x67\x7e\xaa\x51\x95\x71\xfa\x08\x7e\xa8\x37" \
    "\x62\xda\x9a\xba\xcb\x20\x23\x5f\x00\x00\x00\x00" \
    "\x49\x45\x4e\x44\xae\x42\x60\x82"
image11_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\xd5\x49\x44\x41\x54\x38\x8d\xc5\x95\x5d\x0a\x84" \
    "\x30\x0c\x84\x27\xe2\xa9\x0a\x9e\x6c\x8b\x0f\x4b" \
    "\x3d\xd9\x82\xd7\xca\x3e\x58\xd7\xfe\x4c\xd0\xba" \
    "\x5d\x76\x40\x02\x4d\xf2\x65\xda\x0a\x05\x7e\x24" \
    "\x39\xc9\xeb\x8d\x9e\xaa\x88\x41\xa0\xc9\xaa\xd8" \
    "\xc8\x2a\xb3\x2f\x9c\x42\x5b\xe1\xe3\x0e\x0d\xcf" \
    "\x00\xc0\x03\x08\xf0\xb3\xa7\xa0\x74\x10\xa9\xd7" \
    "\x14\x2e\x00\xb4\x2c\x5a\x5f\xab\x69\x6b\x97\x9b" \
    "\x1c\x83\x7f\xc0\xc3\x16\xb6\xe4\x16\x5b\x64\xf7" \
    "\x8d\x71\x63\x59\x91\x9b\xdc\x45\x70\xde\x47\xc0" \
    "\x47\x32\xdd\x5e\x5b\xcc\x35\xf0\xc9\x77\x62\xae" \
    "\x78\x79\x36\xdc\xcf\x75\x13\x57\x7e\x79\xf4\x8c" \
    "\x4b\x27\xaa\x0f\x13\x27\xb2\x40\xf5\x11\x7f\xcb" \
    "\xe3\x48\xaa\x33\xb6\xe0\x22\x4b\x05\x4d\x07\x46" \
    "\xb8\x02\x5e\x2e\x3b\x3e\x73\xcd\xe0\xdd\x1c\x97" \
    "\xf0\x2e\x8e\xd9\xd0\xaf\x1d\xb3\x81\x22\x4b\xdf" \
    "\x33\xee\xe6\x98\xa9\x34\xa0\xf6\x17\xb4\x55\x40" \
    "\xd0\x0b\xcf\x4c\xa0\x8f\xc0\xdf\xf4\x06\xe3\x25" \
    "\xc1\x98\x1b\xc4\x18\x76\x00\x00\x00\x00\x49\x45" \
    "\x4e\x44\xae\x42\x60\x82"
image12_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x02" \
    "\x5d\x49\x44\x41\x54\x38\x8d\xd5\x93\xa1\x72\xdb" \
    "\x40\x10\x86\x3f\x67\x0a\x56\xec\xc4\x22\x78\xd0" \
    "\x65\x36\x93\xa0\xc2\x1c\x68\xd6\xc2\xe6\x0d\xf2" \
    "\x1a\x81\x81\x11\x34\x94\x99\xc2\x54\xa8\x32\x9b" \
    "\x55\xf0\xe0\x89\xdd\xb1\x5b\xa6\x02\xb7\x9d\x66" \
    "\x92\xd6\x99\xb6\xd3\x99\xfe\xe8\x6e\x67\xe7\xdb" \
    "\x7f\x77\xef\xe0\x7f\xd3\xe2\xc7\x4b\xd7\x75\xb3" \
    "\x73\x0e\xef\x3d\x51\x15\x00\x23\x82\xb5\x16\x6b" \
    "\x2d\x57\x57\x57\x8b\x17\x29\xbf\x02\xb7\x6d\x3b" \
    "\x0f\x87\x03\xb9\x2d\x58\xae\xd7\x60\x04\x00\xef" \
    "\x1c\xe3\xc7\x03\x06\xa8\xaa\x8a\xeb\xeb\xeb\x57" \
    "\xc1\x17\xdf\xa0\x6d\xdb\x52\x5d\xd7\x54\xef\xb6" \
    "\x00\xa8\x2a\x49\x13\x8a\x12\x35\x32\xec\x3a\xc4" \
    "\x2b\x9b\xcd\xe6\x55\xce\x2f\xfa\xbe\x9f\x87\xc3" \
    "\x40\xfd\xe1\x3d\xcb\x4d\x8d\xaa\xa2\x4e\x48\xee" \
    "\x12\xc6\x82\x38\x08\xc1\x07\x96\x9b\x1a\x8a\x9c" \
    "\xe3\xf1\xf8\xaa\x51\x5c\x38\xe7\xc8\xad\xa5\xaa" \
    "\x6b\x00\xc4\x5f\x12\x9c\x67\xd2\x23\x93\x8c\x88" \
    "\xe6\xc8\x60\xd1\x18\xb1\xd5\x92\xd1\x39\xba\xae" \
    "\x9b\xcf\x83\xa7\x89\x65\xb5\x46\x51\x34\x80\x1b" \
    "\x1d\x2e\x1f\x49\x45\xc0\xe3\x50\x09\x64\x08\xea" \
    "\x15\x44\x90\xc2\xe0\xbd\x3f\xef\x58\x53\xc2\xe4" \
    "\x86\xa0\x01\x9f\x4d\x84\xf5\x84\x18\x41\x83\x62" \
    "\xb0\x40\x8e\x8b\x23\xc9\x24\x50\x10\x93\x31\x4d" \
    "\xd3\x59\xf0\x1b\x80\x98\x14\x11\x20\x25\x14\x40" \
    "\x15\xf1\x96\x4c\x0b\xbc\x1b\x48\x4b\x07\xe4\x68" \
    "\x88\x80\xc0\x29\xeb\xd7\x8e\x41\x41\xf5\xb4\x34" \
    "\xfd\x76\x86\x4c\x05\x3f\x1e\x08\x4b\x0f\x85\x80" \
    "\x26\x54\x40\x63\x40\x44\xce\x83\x8b\xbc\xc0\x39" \
    "\x87\xa6\x13\x50\xa3\xa2\x28\x5e\x1d\x5a\x44\x14" \
    "\xd0\x70\x8a\xa5\x98\x08\x21\x62\xad\x3d\x0f\xb6" \
    "\xd6\xe2\x87\xcf\xa4\x98\x50\x8d\x27\x40\x50\x44" \
    "\x73\x70\x42\x8c\x91\xaf\x8d\x10\xfd\x44\x81\x60" \
    "\x8c\x39\x0b\x5e\x00\xdc\xdd\xdd\xcd\x8e\x80\xa9" \
    "\xde\x42\x02\x48\xe8\x04\x84\x08\x56\xf0\x3e\x02" \
    "\x90\x7d\x72\x94\x65\xc9\xba\x5a\xe3\x46\x87\x31" \
    "\xe6\xa7\x9f\xe5\x02\x60\xb5\x5a\x61\x02\xc4\xee" \
    "\x40\xa6\x89\x4c\x33\xf2\xcb\x0c\xb1\x06\x51\x28" \
    "\x14\xf8\xf8\x99\xb2\x2c\xb9\xb9\xb9\x59\xb8\xd1" \
    "\xf1\xf8\xf8\x48\xd3\x34\xb4\x6d\xfb\xe2\x9b\xfe" \
    "\x5e\xad\xef\xfb\xf9\x78\x3c\x32\x3a\x87\x18\x81" \
    "\xec\xb4\x20\x0d\x11\x51\xa8\xeb\x9a\xed\x76\xbb" \
    "\x00\x18\x86\x61\xee\xba\x8e\xfd\x7e\x8f\x31\x86" \
    "\xed\x76\xcb\x6a\xb5\x7a\xe2\xfe\x59\x1b\x5d\xd7" \
    "\xcd\xde\x7b\x62\x8c\x88\x08\x79\x9e\x63\xad\xa5" \
    "\xaa\xaa\x67\xb9\xbb\xdd\x6e\x6e\x9a\x06\xef\x3d" \
    "\x75\x5d\x3f\x29\xfe\xc7\xea\xfb\x7e\xbe\xbd\xbd" \
    "\x9d\xad\xb5\x73\x59\x96\xf3\xfd\xfd\xfd\xfc\xa2" \
    "\xe3\xdf\xd5\xc3\xc3\xc3\xdc\x34\x0d\xd3\x34\xb1" \
    "\xd9\x6c\xfe\x1e\x18\x4e\x63\xdc\xef\xf7\xa4\x94" \
    "\xfe\x26\xf6\x1f\xe9\x0b\xbc\x4c\x5e\x59\xd6\x14" \
    "\xca\xf4\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42" \
    "\x60\x82"

class faktura(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        self.image1 = QPixmap()
        self.image1.loadFromData(image1_data,"PNG")
        self.image3 = QPixmap()
        self.image3.loadFromData(image3_data,"PNG")
        self.image4 = QPixmap()
        self.image4.loadFromData(image4_data,"PNG")
        self.image5 = QPixmap()
        self.image5.loadFromData(image5_data,"PNG")
        self.image6 = QPixmap()
        self.image6.loadFromData(image6_data,"PNG")
        self.image7 = QPixmap()
        self.image7.loadFromData(image7_data,"PNG")
        self.image8 = QPixmap()
        self.image8.loadFromData(image8_data,"PNG")
        self.image9 = QPixmap()
        self.image9.loadFromData(image9_data,"PNG")
        self.image10 = QPixmap()
        self.image10.loadFromData(image10_data,"PNG")
        self.image11 = QPixmap()
        self.image11.loadFromData(image11_data,"PNG")
        self.image12 = QPixmap()
        self.image12.loadFromData(image12_data,"PNG")
        self.image2 = QPixmap(image2_data)

        if not name:
            self.setName("faktura")

        f = QFont(self.font())
        f.setPointSize(8)
        self.setFont(f)
        self.setIcon(self.image0)

        self.setCentralWidget(QWidget(self,"qt_central_widget"))

        self.buttonGroup1_2_2 = QButtonGroup(self.centralWidget(),"buttonGroup1_2_2")
        self.buttonGroup1_2_2.setGeometry(QRect(20,470,921,220))

        self.myndigheteneRegistrertTekst_2_3 = QLabel(self.buttonGroup1_2_2,"myndigheteneRegistrertTekst_2_3")
        self.myndigheteneRegistrertTekst_2_3.setGeometry(QRect(12,18,761,40))
        self.myndigheteneRegistrertTekst_2_3.setTextFormat(QLabel.RichText)

        self.myndigheteneRegistrertTekst_2_4_2 = QLabel(self.centralWidget(),"myndigheteneRegistrertTekst_2_4_2")
        self.myndigheteneRegistrertTekst_2_4_2.setGeometry(QRect(45,106,100,18))
        self.myndigheteneRegistrertTekst_2_4_2.setTextFormat(QLabel.RichText)

        self.okonomiRegnskapTotalMva = QLabel(self.centralWidget(),"okonomiRegnskapTotalMva")
        self.okonomiRegnskapTotalMva.setGeometry(QRect(153,106,790,20))

        self.fakturaTab = QTabWidget(self.centralWidget(),"fakturaTab")
        self.fakturaTab.setEnabled(1)
        self.fakturaTab.setGeometry(QRect(10,10,960,760))
        self.fakturaTab.setTabShape(QTabWidget.Rounded)

        self.tab = QWidget(self.fakturaTab,"tab")

        self.groupBox6 = QGroupBox(self.tab,"groupBox6")
        self.groupBox6.setGeometry(QRect(750,60,200,360))

        self.fakturaDetaljerTekst = QLabel(self.groupBox6,"fakturaDetaljerTekst")
        self.fakturaDetaljerTekst.setGeometry(QRect(11,21,178,330))
        self.fakturaDetaljerTekst.setTextFormat(QLabel.RichText)
        self.fakturaDetaljerTekst.setAlignment(QLabel.WordBreak | QLabel.AlignTop | QLabel.AlignLeft)

        self.fakturaFakturaliste = QListView(self.tab,"fakturaFakturaliste")
        self.fakturaFakturaliste.addColumn(self.__tr("#"))
        self.fakturaFakturaliste.addColumn(self.__tr("Tekst"))
        self.fakturaFakturaliste.addColumn(self.__tr("Mottaker"))
        self.fakturaFakturaliste.addColumn(self.__trUtf8("\x42\x65\x6c\xc3\xb8\x70"))
        self.fakturaFakturaliste.addColumn(self.__tr("Forfall"))
        self.fakturaFakturaliste.addColumn(self.__tr("Betalt"))
        self.fakturaFakturaliste.setGeometry(QRect(10,42,730,680))
        self.fakturaFakturaliste.setAllColumnsShowFocus(1)
        self.fakturaFakturaliste.setShowSortIndicator(1)
        self.fakturaFakturaliste.setRootIsDecorated(0)
        self.fakturaFakturaliste.setResizeMode(QListView.AllColumns)

        self.groupBox8_2 = QGroupBox(self.tab,"groupBox8_2")
        self.groupBox8_2.setGeometry(QRect(750,420,200,300))

        self.fakturaBetaltDato = QDateEdit(self.groupBox8_2,"fakturaBetaltDato")
        self.fakturaBetaltDato.setGeometry(QRect(9,200,100,21))
        self.fakturaBetaltDato.setOrder(QDateEdit.YMD)
        self.fakturaBetaltDato.setDate(QDate(2006,1,1))
        self.fakturaBetaltDato.setAutoAdvance(1)

        self.textLabel3_2 = QLabel(self.groupBox8_2,"textLabel3_2")
        self.textLabel3_2.setGeometry(QRect(8,179,114,14))

        self.line1 = QFrame(self.groupBox8_2,"line1")
        self.line1.setGeometry(QRect(10,150,170,20))
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.line1.setFrameShape(QFrame.HLine)

        self.textLabel4_2 = QLabel(self.groupBox8_2,"textLabel4_2")
        self.textLabel4_2.setGeometry(QRect(10,100,141,14))

        self.fakturaBetalt = QPushButton(self.groupBox8_2,"fakturaBetalt")
        self.fakturaBetalt.setGeometry(QRect(115,200,64,23))

        self.fakturaLagKvittering = QPushButton(self.groupBox8_2,"fakturaLagKvittering")
        self.fakturaLagKvittering.setGeometry(QRect(105,120,74,23))

        self.textLabel2_2 = QLabel(self.groupBox8_2,"textLabel2_2")
        self.textLabel2_2.setGeometry(QRect(10,30,145,14))

        self.line1_2 = QFrame(self.groupBox8_2,"line1_2")
        self.line1_2.setGeometry(QRect(10,80,170,20))
        self.line1_2.setFrameShape(QFrame.HLine)
        self.line1_2.setFrameShadow(QFrame.Sunken)
        self.line1_2.setFrameShape(QFrame.HLine)

        self.fakturaLagEpost = QPushButton(self.groupBox8_2,"fakturaLagEpost")
        self.fakturaLagEpost.setGeometry(QRect(48,50,60,23))
        self.fakturaLagEpost.setAutoMask(0)

        self.fakturaLagPapir = QPushButton(self.groupBox8_2,"fakturaLagPapir")
        self.fakturaLagPapir.setGeometry(QRect(120,50,60,23))

        self.fakturaVisKansellerte = QCheckBox(self.tab,"fakturaVisKansellerte")
        self.fakturaVisKansellerte.setGeometry(QRect(750,40,180,20))

        self.fakturaNy = QPushButton(self.tab,"fakturaNy")
        self.fakturaNy.setGeometry(QRect(10,10,89,23))

        self.fakturaFakta = QGroupBox(self.tab,"fakturaFakta")
        self.fakturaFakta.setGeometry(QRect(200,310,580,420))

        self.textLabel8 = QLabel(self.fakturaFakta,"textLabel8")
        self.textLabel8.setGeometry(QRect(20,53,40,21))
        textLabel8_font = QFont(self.textLabel8.font())
        self.textLabel8.setFont(textLabel8_font)

        self.textLabel5_2 = QLabel(self.fakturaFakta,"textLabel5_2")
        self.textLabel5_2.setGeometry(QRect(20,130,40,31))
        textLabel5_2_font = QFont(self.textLabel5_2.font())
        self.textLabel5_2.setFont(textLabel5_2_font)
        self.textLabel5_2.setFocusPolicy(QLabel.NoFocus)

        self.textLabel1_8 = QLabel(self.fakturaFakta,"textLabel1_8")
        self.textLabel1_8.setGeometry(QRect(200,390,30,21))
        textLabel1_8_font = QFont(self.textLabel1_8.font())
        self.textLabel1_8.setFont(textLabel1_8_font)

        self.textLabel5 = QLabel(self.fakturaFakta,"textLabel5")
        self.textLabel5.setGeometry(QRect(20,20,51,14))
        textLabel5_font = QFont(self.textLabel5.font())
        self.textLabel5.setFont(textLabel5_font)

        self.fakturaFaktaLegginn = QPushButton(self.fakturaFakta,"fakturaFaktaLegginn")
        self.fakturaFaktaLegginn.setGeometry(QRect(478,391,95,23))

        self.fakturaFaktaVareFjern = QPushButton(self.fakturaFakta,"fakturaFaktaVareFjern")
        self.fakturaFaktaVareFjern.setGeometry(QRect(250,350,41,20))

        self.fakturaFaktaSum = QLabel(self.fakturaFakta,"fakturaFaktaSum")
        self.fakturaFaktaSum.setGeometry(QRect(250,390,200,21))
        self.fakturaFaktaSum.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.fakturaFaktaAntall = QSpinBox(self.fakturaFakta,"fakturaFaktaAntall")
        self.fakturaFaktaAntall.setGeometry(QRect(130,250,90,21))
        self.fakturaFaktaAntall.setMaxValue(100000)
        self.fakturaFaktaAntall.setValue(1)

        self.textLabel7_6 = QLabel(self.fakturaFakta,"textLabel7_6")
        self.textLabel7_6.setGeometry(QRect(80,250,40,21))
        textLabel7_6_font = QFont(self.textLabel7_6.font())
        self.textLabel7_6.setFont(textLabel7_6_font)

        self.textLabel1_4 = QLabel(self.fakturaFakta,"textLabel1_4")
        self.textLabel1_4.setGeometry(QRect(78,163,72,14))

        self.textLabel1_4_2 = QLabel(self.fakturaFakta,"textLabel1_4_2")
        self.textLabel1_4_2.setGeometry(QRect(78,203,72,14))

        self.fakturaFaktaVareDetaljer = QLabel(self.fakturaFakta,"fakturaFaktaVareDetaljer")
        self.fakturaFaktaVareDetaljer.setGeometry(QRect(80,180,211,20))
        self.fakturaFaktaVareDetaljer.setTextFormat(QLabel.RichText)
        self.fakturaFaktaVareDetaljer.setAlignment(QLabel.WordBreak | QLabel.AlignTop | QLabel.AlignLeft)

        self.fakturaFaktaVarePris = QLabel(self.fakturaFakta,"fakturaFaktaVarePris")
        self.fakturaFaktaVarePris.setGeometry(QRect(80,220,211,20))
        self.fakturaFaktaVarePris.setTextFormat(QLabel.RichText)
        self.fakturaFaktaVarePris.setAlignment(QLabel.WordBreak | QLabel.AlignTop | QLabel.AlignLeft)

        self.fakturaFaktaVareLeggtil = QPushButton(self.fakturaFakta,"fakturaFaktaVareLeggtil")
        self.fakturaFaktaVareLeggtil.setGeometry(QRect(230,250,60,21))

        self.fakturaFaktaTekst = QTextEdit(self.fakturaFakta,"fakturaFaktaTekst")
        self.fakturaFaktaTekst.setGeometry(QRect(80,53,470,60))
        self.fakturaFaktaTekst.setTabChangesFocus(1)

        self.fakturaFaktaMottaker = QComboBox(0,self.fakturaFakta,"fakturaFaktaMottaker")
        self.fakturaFaktaMottaker.setGeometry(QRect(80,19,470,21))
        self.fakturaFaktaMottaker.setEditable(0)

        self.fakturaFaktaVare = QComboBox(0,self.fakturaFakta,"fakturaFaktaVare")
        self.fakturaFaktaVare.setGeometry(QRect(80,140,210,21))
        self.fakturaFaktaVare.setDuplicatesEnabled(0)

        self.fakturaFaktaOrdrelinje = QListBox(self.fakturaFakta,"fakturaFaktaOrdrelinje")
        self.fakturaFaktaOrdrelinje.setGeometry(QRect(310,140,240,230))

        self.line6 = QFrame(self.fakturaFakta,"line6")
        self.line6.setGeometry(QRect(149,281,140,20))
        self.line6.setFrameShape(QFrame.HLine)
        self.line6.setFrameShadow(QFrame.Sunken)
        self.line6.setFrameShape(QFrame.HLine)

        self.fakturaFaktaKryss = QLabel(self.fakturaFakta,"fakturaFaktaKryss")
        self.fakturaFaktaKryss.setEnabled(1)
        self.fakturaFaktaKryss.setGeometry(QRect(570,10,8,8))
        self.fakturaFaktaKryss.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.fakturaFaktaKryss.sizePolicy().hasHeightForWidth()))
        self.fakturaFaktaKryss.setMaximumSize(QSize(8,8))
        self.fakturaFaktaKryss.setPixmap(self.image1)
        self.fakturaFaktaKryss.setScaledContents(1)

        self.fakturaSendepostBoks = QGroupBox(self.tab,"fakturaSendepostBoks")
        self.fakturaSendepostBoks.setGeometry(QRect(200,120,441,391))

        self.fakturaSendepostTekst = QTextEdit(self.fakturaSendepostBoks,"fakturaSendepostTekst")
        self.fakturaSendepostTekst.setGeometry(QRect(8,41,421,311))
        self.fakturaSendepostTekst.setTextFormat(QTextEdit.PlainText)

        self.fakturaSendepostAvbryt = QPushButton(self.fakturaSendepostBoks,"fakturaSendepostAvbryt")
        self.fakturaSendepostAvbryt.setGeometry(QRect(300,361,51,21))

        self.fakturaSendepostSend = QPushButton(self.fakturaSendepostBoks,"fakturaSendepostSend")
        self.fakturaSendepostSend.setGeometry(QRect(358,361,71,21))
        self.fakturaSendepostSend.setDefault(1)

        self.fakturaSendepostTittel = QLabel(self.fakturaSendepostBoks,"fakturaSendepostTittel")
        self.fakturaSendepostTittel.setGeometry(QRect(8,17,420,21))
        self.fakturaSendepostTittel.setTextFormat(QLabel.RichText)
        self.fakturaTab.insertTab(self.tab,QString.fromLatin1(""))

        self.tab_2 = QWidget(self.fakturaTab,"tab_2")

        self.kundeNy = QPushButton(self.tab_2,"kundeNy")
        self.kundeNy.setGeometry(QRect(10,10,83,23))

        self.kundeKundeliste = QListView(self.tab_2,"kundeKundeliste")
        self.kundeKundeliste.addColumn(self.__tr("#"))
        self.kundeKundeliste.addColumn(self.__tr("Navn"))
        self.kundeKundeliste.addColumn(self.__tr("Epost"))
        self.kundeKundeliste.addColumn(self.__tr("Status"))
        self.kundeKundeliste.addColumn(self.__tr("Adresse"))
        self.kundeKundeliste.addColumn(self.__tr("Telefon"))
        self.kundeKundeliste.addColumn(self.__tr("Telefaks"))
        self.kundeKundeliste.setGeometry(QRect(10,42,720,680))
        self.kundeKundeliste.setAllColumnsShowFocus(1)
        self.kundeKundeliste.setShowSortIndicator(1)
        self.kundeKundeliste.setResizeMode(QListView.AllColumns)

        self.groupBox7 = QGroupBox(self.tab_2,"groupBox7")
        self.groupBox7.setGeometry(QRect(737,62,213,660))

        self.kundeNyfaktura = QPushButton(self.groupBox7,"kundeNyfaktura")
        self.kundeNyfaktura.setGeometry(QRect(40,610,140,21))
        self.kundeNyfaktura.setAcceptDrops(1)

        self.kundeDetaljerTekst = QLabel(self.groupBox7,"kundeDetaljerTekst")
        self.kundeDetaljerTekst.setGeometry(QRect(10,20,200,570))
        self.kundeDetaljerTekst.setTextFormat(QLabel.RichText)
        self.kundeDetaljerTekst.setAlignment(QLabel.WordBreak | QLabel.AlignTop | QLabel.AlignLeft)

        self.kundeVisFjernede = QCheckBox(self.tab_2,"kundeVisFjernede")
        self.kundeVisFjernede.setGeometry(QRect(740,40,210,21))

        self.kundeInfo = QGroupBox(self.tab_2,"kundeInfo")
        self.kundeInfo.setGeometry(QRect(190,520,650,210))

        self.textLabel1_3_3_5 = QLabel(self.kundeInfo,"textLabel1_3_3_5")
        self.textLabel1_3_3_5.setGeometry(QRect(25,150,50,21))

        self.textLabel2 = QLabel(self.kundeInfo,"textLabel2")
        self.textLabel2.setGeometry(QRect(25,25,60,21))

        self.kundeInfoNavn = QLineEdit(self.kundeInfo,"kundeInfoNavn")
        self.kundeInfoNavn.setGeometry(QRect(87,25,310,21))

        self.kundeInfoPostnummer = QLineEdit(self.kundeInfo,"kundeInfoPostnummer")
        self.kundeInfoPostnummer.setGeometry(QRect(87,150,50,21))

        self.kundeInfoStatus = QComboBox(0,self.kundeInfo,"kundeInfoStatus")
        self.kundeInfoStatus.setGeometry(QRect(470,20,160,21))
        self.kundeInfoStatus.setEditable(1)
        self.kundeInfoStatus.setSizeLimit(20)
        self.kundeInfoStatus.setDuplicatesEnabled(0)

        self.textLabel1_3_3_2_4 = QLabel(self.kundeInfo,"textLabel1_3_3_2_4")
        self.textLabel1_3_3_2_4.setGeometry(QRect(24,180,50,21))

        self.textLabel1_3_3_3_4 = QLabel(self.kundeInfo,"textLabel1_3_3_3_4")
        self.textLabel1_3_3_3_4.setGeometry(QRect(180,180,50,14))

        self.kundeInfoPoststed = QLineEdit(self.kundeInfo,"kundeInfoPoststed")
        self.kundeInfoPoststed.setGeometry(QRect(238,150,160,21))

        self.kundeInfoTelefaks = QLineEdit(self.kundeInfo,"kundeInfoTelefaks")
        self.kundeInfoTelefaks.setGeometry(QRect(240,180,70,21))

        self.kundeInfoTelefon = QLineEdit(self.kundeInfo,"kundeInfoTelefon")
        self.kundeInfoTelefon.setGeometry(QRect(87,180,70,21))

        self.kundeInfoEpost = QLineEdit(self.kundeInfo,"kundeInfoEpost")
        self.kundeInfoEpost.setGeometry(QRect(87,80,310,21))

        self.kundeInfoAdresse = QTextEdit(self.kundeInfo,"kundeInfoAdresse")
        self.kundeInfoAdresse.setGeometry(QRect(87,108,311,35))
        self.kundeInfoAdresse.setTabChangesFocus(1)

        self.textLabel2_3_2 = QLabel(self.kundeInfo,"textLabel2_3_2")
        self.textLabel2_3_2.setGeometry(QRect(25,50,50,21))
        self.textLabel2_3_2.setTextFormat(QLabel.PlainText)

        self.textLabel2_3 = QLabel(self.kundeInfo,"textLabel2_3")
        self.textLabel2_3.setGeometry(QRect(25,78,50,21))

        self.textLabel4 = QLabel(self.kundeInfo,"textLabel4")
        self.textLabel4.setGeometry(QRect(420,20,40,21))

        self.textLabel3 = QLabel(self.kundeInfo,"textLabel3")
        self.textLabel3.setGeometry(QRect(25,102,50,31))

        self.textLabel1_3_4_2 = QLabel(self.kundeInfo,"textLabel1_3_4_2")
        self.textLabel1_3_4_2.setGeometry(QRect(180,150,50,21))

        self.kundeInfoKontaktperson = QLineEdit(self.kundeInfo,"kundeInfoKontaktperson")
        self.kundeInfoKontaktperson.setGeometry(QRect(88,52,310,21))

        self.kundeInfoKryss = QLabel(self.kundeInfo,"kundeInfoKryss")
        self.kundeInfoKryss.setEnabled(1)
        self.kundeInfoKryss.setGeometry(QRect(640,10,8,8))
        self.kundeInfoKryss.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.kundeInfoKryss.sizePolicy().hasHeightForWidth()))
        self.kundeInfoKryss.setMaximumSize(QSize(8,8))
        self.kundeInfoKryss.setPixmap(self.image1)
        self.kundeInfoKryss.setScaledContents(1)

        self.kundeInfoEndre = QPushButton(self.kundeInfo,"kundeInfoEndre")
        self.kundeInfoEndre.setGeometry(QRect(537,181,106,23))
        self.fakturaTab.insertTab(self.tab_2,QString.fromLatin1(""))

        self.TabPage = QWidget(self.fakturaTab,"TabPage")

        self.varerNy = QPushButton(self.TabPage,"varerNy")
        self.varerNy.setGeometry(QRect(10,10,74,23))

        self.varerVareliste = QListView(self.TabPage,"varerVareliste")
        self.varerVareliste.addColumn(self.__tr("#"))
        self.varerVareliste.addColumn(self.__tr("Navn"))
        self.varerVareliste.addColumn(self.__tr("Detaljer"))
        self.varerVareliste.addColumn(self.__tr("Pris"))
        self.varerVareliste.addColumn(self.__tr("Enhet"))
        self.varerVareliste.setGeometry(QRect(10,42,720,680))
        self.varerVareliste.setAllColumnsShowFocus(1)
        self.varerVareliste.setShowSortIndicator(1)
        self.varerVareliste.setResizeMode(QListView.AllColumns)

        self.groupBox8 = QGroupBox(self.TabPage,"groupBox8")
        self.groupBox8.setGeometry(QRect(737,62,213,660))

        self.varerDetaljerTekst = QLabel(self.groupBox8,"varerDetaljerTekst")
        self.varerDetaljerTekst.setGeometry(QRect(10,20,200,630))
        self.varerDetaljerTekst.setTextFormat(QLabel.RichText)
        self.varerDetaljerTekst.setAlignment(QLabel.WordBreak | QLabel.AlignTop | QLabel.AlignLeft)

        self.varerVisFjernede = QCheckBox(self.TabPage,"varerVisFjernede")
        self.varerVisFjernede.setGeometry(QRect(740,40,180,20))

        self.varerInfo = QGroupBox(self.TabPage,"varerInfo")
        self.varerInfo.setGeometry(QRect(300,510,490,220))

        self.textLabel10 = QLabel(self.varerInfo,"textLabel10")
        self.textLabel10.setGeometry(QRect(30,30,60,21))

        self.varerInfoEnhet = QComboBox(0,self.varerInfo,"varerInfoEnhet")
        self.varerInfoEnhet.setGeometry(QRect(100,60,180,21))
        self.varerInfoEnhet.setEditable(1)

        self.textLabel10_4 = QLabel(self.varerInfo,"textLabel10_4")
        self.textLabel10_4.setGeometry(QRect(290,60,24,21))

        self.textLabel10_3 = QLabel(self.varerInfo,"textLabel10_3")
        self.textLabel10_3.setGeometry(QRect(30,90,70,21))

        self.varerInfoPris = QSpinBox(self.varerInfo,"varerInfoPris")
        self.varerInfoPris.setGeometry(QRect(321,60,150,21))
        self.varerInfoPris.setMaxValue(100000)

        self.textLabel10_2 = QLabel(self.varerInfo,"textLabel10_2")
        self.textLabel10_2.setGeometry(QRect(30,60,60,21))

        self.textLabel7_3 = QLabel(self.varerInfo,"textLabel7_3")
        self.textLabel7_3.setGeometry(QRect(30,180,60,21))

        self.varerInfoDetaljer = QTextEdit(self.varerInfo,"varerInfoDetaljer")
        self.varerInfoDetaljer.setGeometry(QRect(100,90,371,81))
        self.varerInfoDetaljer.setTabChangesFocus(1)

        self.varerInfoNavn = QLineEdit(self.varerInfo,"varerInfoNavn")
        self.varerInfoNavn.setGeometry(QRect(100,30,371,21))

        self.varerInfoKryss = QLabel(self.varerInfo,"varerInfoKryss")
        self.varerInfoKryss.setEnabled(1)
        self.varerInfoKryss.setGeometry(QRect(480,10,8,8))
        self.varerInfoKryss.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.varerInfoKryss.sizePolicy().hasHeightForWidth()))
        self.varerInfoKryss.setMaximumSize(QSize(8,8))
        self.varerInfoKryss.setPixmap(self.image1)
        self.varerInfoKryss.setScaledContents(1)

        self.varerInfoLegginn = QPushButton(self.varerInfo,"varerInfoLegginn")
        self.varerInfoLegginn.setGeometry(QRect(402,192,81,21))

        self.varerInfoMva = QSpinBox(self.varerInfo,"varerInfoMva")
        self.varerInfoMva.setGeometry(QRect(100,180,61,21))
        self.varerInfoMva.setValue(25)
        self.fakturaTab.insertTab(self.TabPage,QString.fromLatin1(""))

        self.TabPage_2 = QWidget(self.fakturaTab,"TabPage_2")

        self.textLabel1 = QLabel(self.TabPage_2,"textLabel1")
        self.textLabel1.setGeometry(QRect(10,10,70,21))

        self.textLabel1_3 = QLabel(self.TabPage_2,"textLabel1_3")
        self.textLabel1_3.setGeometry(QRect(10,200,70,21))

        self.textLabel1_3_5 = QLabel(self.TabPage_2,"textLabel1_3_5")
        self.textLabel1_3_5.setGeometry(QRect(10,371,84,40))

        self.textLabel1_3_3 = QLabel(self.TabPage_2,"textLabel1_3_3")
        self.textLabel1_3_3.setGeometry(QRect(8,274,80,21))

        self.textLabel1_3_4 = QLabel(self.TabPage_2,"textLabel1_3_4")
        self.textLabel1_3_4.setGeometry(QRect(198,274,50,21))

        self.textLabel1_3_3_4 = QLabel(self.TabPage_2,"textLabel1_3_3_4")
        self.textLabel1_3_3_4.setGeometry(QRect(358,304,50,21))

        self.dittfirmaTelefaks = QLineEdit(self.TabPage_2,"dittfirmaTelefaks")
        self.dittfirmaTelefaks.setGeometry(QRect(414,303,70,21))

        self.dittfirmaPoststed = QLineEdit(self.TabPage_2,"dittfirmaPoststed")
        self.dittfirmaPoststed.setGeometry(QRect(274,274,210,21))

        self.dittfirmaPostnummer = QLineEdit(self.TabPage_2,"dittfirmaPostnummer")
        self.dittfirmaPostnummer.setGeometry(QRect(120,273,50,21))

        self.textLabel1_3_3_2 = QLabel(self.TabPage_2,"textLabel1_3_3_2")
        self.textLabel1_3_3_2.setGeometry(QRect(8,304,50,21))

        self.dittfirmaTelefon = QLineEdit(self.TabPage_2,"dittfirmaTelefon")
        self.dittfirmaTelefon.setGeometry(QRect(120,303,70,21))

        self.textLabel1_3_3_3 = QLabel(self.TabPage_2,"textLabel1_3_3_3")
        self.textLabel1_3_3_3.setGeometry(QRect(198,304,70,21))

        self.dittfirmaMobil = QLineEdit(self.TabPage_2,"dittfirmaMobil")
        self.dittfirmaMobil.setGeometry(QRect(274,303,70,21))

        self.textLabel1_2_3 = QLabel(self.TabPage_2,"textLabel1_2_3")
        self.textLabel1_2_3.setGeometry(QRect(10,340,90,21))

        self.dittfirmaKontonummer = QLineEdit(self.TabPage_2,"dittfirmaKontonummer")
        self.dittfirmaKontonummer.setGeometry(QRect(120,340,270,21))

        self.textLabel1_2_4 = QLabel(self.TabPage_2,"textLabel1_2_4")
        self.textLabel1_2_4.setGeometry(QRect(10,140,100,21))

        self.textLabel1_2 = QLabel(self.TabPage_2,"textLabel1_2")
        self.textLabel1_2.setGeometry(QRect(10,170,100,21))

        self.dittfirmaKontaktperson = QLineEdit(self.TabPage_2,"dittfirmaKontaktperson")
        self.dittfirmaKontaktperson.setGeometry(QRect(120,140,290,21))

        self.textLabel7_2 = QLabel(self.TabPage_2,"textLabel7_2")
        self.textLabel7_2.setGeometry(QRect(9,527,60,21))

        self.textLabel7 = QLabel(self.TabPage_2,"textLabel7")
        self.textLabel7.setGeometry(QRect(9,500,60,21))

        self.textLabel1_7 = QLabel(self.TabPage_2,"textLabel1_7")
        self.textLabel1_7.setGeometry(QRect(8,691,118,20))

        self.dittfirmaMva = QSpinBox(self.TabPage_2,"dittfirmaMva")
        self.dittfirmaMva.setGeometry(QRect(120,500,61,21))
        self.dittfirmaMva.setValue(25)

        self.textLabel9 = QLabel(self.TabPage_2,"textLabel9")
        self.textLabel9.setGeometry(QRect(189,527,40,21))

        self.dittfirmaForfall = QSpinBox(self.TabPage_2,"dittfirmaForfall")
        self.dittfirmaForfall.setGeometry(QRect(120,527,61,21))
        self.dittfirmaForfall.setValue(21)

        self.dittfirmaFakturakatalogSok = QPushButton(self.TabPage_2,"dittfirmaFakturakatalogSok")
        self.dittfirmaFakturakatalogSok.setGeometry(QRect(618,691,91,21))

        self.textLabel1_5 = QLabel(self.TabPage_2,"textLabel1_5")
        self.textLabel1_5.setGeometry(QRect(10,40,141,21))

        self.dittfirmaOrganisasjonsnummer = QLineEdit(self.TabPage_2,"dittfirmaOrganisasjonsnummer")
        self.dittfirmaOrganisasjonsnummer.setGeometry(QRect(160,40,190,21))

        self.dittfirmaFirmanavn = QLineEdit(self.TabPage_2,"dittfirmaFirmanavn")
        self.dittfirmaFirmanavn.setGeometry(QRect(160,10,550,21))

        self.line2 = QFrame(self.TabPage_2,"line2")
        self.line2.setGeometry(QRect(8,87,700,20))
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.line2.setFrameShape(QFrame.HLine)

        self.dittfirmaLogoPixmap = QLabel(self.TabPage_2,"dittfirmaLogoPixmap")
        self.dittfirmaLogoPixmap.setGeometry(QRect(770,10,141,140))
        self.dittfirmaLogoPixmap.setFrameShape(QLabel.Box)
        self.dittfirmaLogoPixmap.setFrameShadow(QLabel.Sunken)
        self.dittfirmaLogoPixmap.setLineWidth(1)
        self.dittfirmaLogoPixmap.setMargin(1)
        self.dittfirmaLogoPixmap.setPixmap(self.image2)
        self.dittfirmaLogoPixmap.setScaledContents(1)

        self.dittfirmaFinnFjernLogo = QPushButton(self.TabPage_2,"dittfirmaFinnFjernLogo")
        self.dittfirmaFinnFjernLogo.setGeometry(QRect(796,160,87,23))

        self.dittfirmaAdresse = QTextEdit(self.TabPage_2,"dittfirmaAdresse")
        self.dittfirmaAdresse.setGeometry(QRect(120,200,291,61))
        self.dittfirmaAdresse.setTextFormat(QTextEdit.PlainText)
        self.dittfirmaAdresse.setTabChangesFocus(1)
        self.dittfirmaAdresse.setAutoFormatting(QTextEdit.AutoNone)

        self.dittfirmaVilkar = QTextEdit(self.TabPage_2,"dittfirmaVilkar")
        self.dittfirmaVilkar.setGeometry(QRect(120,380,270,100))
        self.dittfirmaVilkar.setTextFormat(QTextEdit.PlainText)
        self.dittfirmaVilkar.setTabChangesFocus(1)
        self.dittfirmaVilkar.setAutoFormatting(QTextEdit.AutoNone)

        self.dittfirmaEpost = QLineEdit(self.TabPage_2,"dittfirmaEpost")
        self.dittfirmaEpost.setGeometry(QRect(120,170,290,21))

        self.frame3 = QFrame(self.TabPage_2,"frame3")
        self.frame3.setGeometry(QRect(718,232,227,480))
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setFrameShadow(QFrame.Raised)

        self.dittfirmaLagre = QPushButton(self.frame3,"dittfirmaLagre")
        self.dittfirmaLagre.setGeometry(QRect(62,428,110,40))

        self.dittfirmaHjelpetekst = QLabel(self.frame3,"dittfirmaHjelpetekst")
        self.dittfirmaHjelpetekst.setGeometry(QRect(10,10,211,220))
        self.dittfirmaHjelpetekst.setTextFormat(QLabel.RichText)
        self.dittfirmaHjelpetekst.setAlignment(QLabel.WordBreak | QLabel.AlignTop)

        self.dittfirmaLagreInfo = QLabel(self.frame3,"dittfirmaLagreInfo")
        self.dittfirmaLagreInfo.setGeometry(QRect(10,220,211,200))
        self.dittfirmaLagreInfo.setTextFormat(QLabel.RichText)
        self.dittfirmaLagreInfo.setAlignment(QLabel.WordBreak | QLabel.AlignJustify | QLabel.AlignBottom)

        self.dittfirmaFakturakatalog = QLineEdit(self.TabPage_2,"dittfirmaFakturakatalog")
        self.dittfirmaFakturakatalog.setGeometry(QRect(140,690,470,21))
        self.fakturaTab.insertTab(self.TabPage_2,QString.fromLatin1(""))

        self.TabPage_3 = QWidget(self.fakturaTab,"TabPage_3")

        self.frame3_3 = QFrame(self.TabPage_3,"frame3_3")
        self.frame3_3.setGeometry(QRect(720,240,227,480))
        self.frame3_3.setFrameShape(QFrame.StyledPanel)
        self.frame3_3.setFrameShadow(QFrame.Raised)

        self.epostHjelpefelt = QLabel(self.frame3_3,"epostHjelpefelt")
        self.epostHjelpefelt.setGeometry(QRect(10,10,211,390))
        self.epostHjelpefelt.setTextFormat(QLabel.RichText)
        self.epostHjelpefelt.setAlignment(QLabel.WordBreak | QLabel.AlignTop)

        self.epostLagre = QPushButton(self.frame3_3,"epostLagre")
        self.epostLagre.setGeometry(QRect(62,428,110,40))

        self.epostSeksjonSmtp = QGroupBox(self.TabPage_3,"epostSeksjonSmtp")
        self.epostSeksjonSmtp.setEnabled(1)
        self.epostSeksjonSmtp.setGeometry(QRect(20,440,670,140))

        self.textLabel1_12 = QLabel(self.epostSeksjonSmtp,"textLabel1_12")
        self.textLabel1_12.setGeometry(QRect(20,30,213,14))

        self.textLabel3_4_2 = QLabel(self.epostSeksjonSmtp,"textLabel3_4_2")
        self.textLabel3_4_2.setGeometry(QRect(119,114,131,21))

        self.textLabel4_4 = QLabel(self.epostSeksjonSmtp,"textLabel4_4")
        self.textLabel4_4.setGeometry(QRect(566,28,29,14))

        self.epostSmtpServer = QLineEdit(self.epostSeksjonSmtp,"epostSmtpServer")
        self.epostSmtpServer.setGeometry(QRect(248,24,300,21))

        self.epostSmtpPort = QSpinBox(self.epostSeksjonSmtp,"epostSmtpPort")
        self.epostSmtpPort.setGeometry(QRect(608,24,50,21))
        self.epostSmtpPort.setButtonSymbols(QSpinBox.UpDownArrows)
        self.epostSmtpPort.setValue(25)

        self.epostSmtpAuth = QCheckBox(self.epostSeksjonSmtp,"epostSmtpAuth")
        self.epostSmtpAuth.setEnabled(0)
        self.epostSmtpAuth.setGeometry(QRect(118,71,214,19))

        self.epostSmtpTLS = QCheckBox(self.epostSeksjonSmtp,"epostSmtpTLS")
        self.epostSmtpTLS.setEnabled(0)
        self.epostSmtpTLS.setGeometry(QRect(118,54,281,19))

        self.textLabel3_4 = QLabel(self.epostSeksjonSmtp,"textLabel3_4")
        self.textLabel3_4.setGeometry(QRect(118,91,131,21))

        self.epostSmtpBrukernavn = QLineEdit(self.epostSeksjonSmtp,"epostSmtpBrukernavn")
        self.epostSmtpBrukernavn.setEnabled(0)
        self.epostSmtpBrukernavn.setGeometry(QRect(198,91,261,21))

        self.epostSmtpPassord = QLineEdit(self.epostSeksjonSmtp,"epostSmtpPassord")
        self.epostSmtpPassord.setEnabled(0)
        self.epostSmtpPassord.setGeometry(QRect(198,114,261,21))

        self.epostSeksjonSendmail = QGroupBox(self.TabPage_3,"epostSeksjonSendmail")
        self.epostSeksjonSendmail.setEnabled(1)
        self.epostSeksjonSendmail.setGeometry(QRect(20,590,670,110))

        self.textLabel5_4 = QLabel(self.epostSeksjonSendmail,"textLabel5_4")
        self.textLabel5_4.setGeometry(QRect(28,41,91,14))

        self.epostSendmailSti = QLineEdit(self.epostSeksjonSendmail,"epostSendmailSti")
        self.epostSendmailSti.setGeometry(QRect(128,35,330,21))

        self.epostSeksjonGmail = QGroupBox(self.TabPage_3,"epostSeksjonGmail")
        self.epostSeksjonGmail.setEnabled(1)
        self.epostSeksjonGmail.setGeometry(QRect(20,280,670,141))

        self.textLabel1_10_3 = QLabel(self.epostSeksjonGmail,"textLabel1_10_3")
        self.textLabel1_10_3.setGeometry(QRect(30,40,150,14))

        self.textLabel2_4_3 = QLabel(self.epostSeksjonGmail,"textLabel2_4_3")
        self.textLabel2_4_3.setGeometry(QRect(30,70,135,14))

        self.epostGmailPassord = QLineEdit(self.epostSeksjonGmail,"epostGmailPassord")
        self.epostGmailPassord.setGeometry(QRect(191,68,280,21))
        self.epostGmailPassord.setEchoMode(QLineEdit.Password)

        self.epostGmailHuskEpost = QCheckBox(self.epostSeksjonGmail,"epostGmailHuskEpost")
        self.epostGmailHuskEpost.setGeometry(QRect(480,33,53,19))

        self.epostGmailEpost = QLineEdit(self.epostSeksjonGmail,"epostGmailEpost")
        self.epostGmailEpost.setGeometry(QRect(191,34,280,21))

        self.epostGmailUbrukelig = QLabel(self.epostSeksjonGmail,"epostGmailUbrukelig")
        self.epostGmailUbrukelig.setGeometry(QRect(90,40,521,60))
        epostGmailUbrukelig_font = QFont(self.epostGmailUbrukelig.font())
        epostGmailUbrukelig_font.setPointSize(10)
        epostGmailUbrukelig_font.setBold(1)
        self.epostGmailUbrukelig.setFont(epostGmailUbrukelig_font)
        self.epostGmailUbrukelig.setFrameShape(QLabel.Box)
        self.epostGmailUbrukelig.setLineWidth(1)
        self.epostGmailUbrukelig.setAlignment(QLabel.WordBreak | QLabel.AlignCenter)

        self.epostLosning = QButtonGroup(self.TabPage_3,"epostLosning")
        self.epostLosning.setGeometry(QRect(20,20,340,140))

        self.epostLosningGmail = QRadioButton(self.epostLosning,"epostLosningGmail")
        self.epostLosningGmail.setGeometry(QRect(20,53,301,21))
        self.epostLosning.insert( self.epostLosningGmail,1)

        self.epostLosningAuto = QRadioButton(self.epostLosning,"epostLosningAuto")
        self.epostLosningAuto.setGeometry(QRect(20,30,301,21))
        self.epostLosningAuto.setChecked(1)
        self.epostLosning.insert( self.epostLosningAuto,0)

        self.epostLosningSmtp = QRadioButton(self.epostLosning,"epostLosningSmtp")
        self.epostLosningSmtp.setGeometry(QRect(20,77,301,21))
        self.epostLosning.insert( self.epostLosningSmtp,2)

        self.epostLosningSendmail = QRadioButton(self.epostLosning,"epostLosningSendmail")
        self.epostLosningSendmail.setGeometry(QRect(20,103,301,21))
        self.epostLosning.insert( self.epostLosningSendmail,3)

        self.epostAvsenderadresse = QLineEdit(self.TabPage_3,"epostAvsenderadresse")
        self.epostAvsenderadresse.setGeometry(QRect(150,170,351,21))

        self.textLabel2_6 = QLabel(self.TabPage_3,"textLabel2_6")
        self.textLabel2_6.setGeometry(QRect(22,169,110,21))

        self.epostLosningTest = QPushButton(self.TabPage_3,"epostLosningTest")
        self.epostLosningTest.setGeometry(QRect(20,200,124,23))

        self.line6_2 = QFrame(self.TabPage_3,"line6_2")
        self.line6_2.setGeometry(QRect(10,240,700,20))
        self.line6_2.setFrameShape(QFrame.HLine)
        self.line6_2.setFrameShadow(QFrame.Sunken)
        self.line6_2.setFrameShape(QFrame.HLine)
        self.fakturaTab.insertTab(self.TabPage_3,QString.fromLatin1(""))

        self.TabPage_4 = QWidget(self.fakturaTab,"TabPage_4")

        self.okonomiDetaljregnskap = QTextBrowser(self.TabPage_4,"okonomiDetaljregnskap")
        self.okonomiDetaljregnskap.setGeometry(QRect(20,200,920,490))
        self.okonomiDetaljregnskap.setCursor(QCursor(4))
        self.okonomiDetaljregnskap.setFrameShadow(QTextBrowser.Raised)
        self.okonomiDetaljregnskap.setHScrollBarMode(QTextBrowser.AlwaysOff)
        self.okonomiDetaljregnskap.setTextFormat(QTextBrowser.RichText)

        self.groupBox9_2 = QGroupBox(self.TabPage_4,"groupBox9_2")
        self.groupBox9_2.setGeometry(QRect(18,21,921,160))

        self.okonomiAvgrensningerKundeliste = QComboBox(0,self.groupBox9_2,"okonomiAvgrensningerKundeliste")
        self.okonomiAvgrensningerKundeliste.setGeometry(QRect(440,62,440,21))

        self.okonomiAvgrensningerVareliste = QComboBox(0,self.groupBox9_2,"okonomiAvgrensningerVareliste")
        self.okonomiAvgrensningerVareliste.setGeometry(QRect(440,93,440,21))

        self.okonomiAvgrensningerDatoManed = QComboBox(0,self.groupBox9_2,"okonomiAvgrensningerDatoManed")
        self.okonomiAvgrensningerDatoManed.setEnabled(0)
        self.okonomiAvgrensningerDatoManed.setGeometry(QRect(530,30,110,21))
        self.okonomiAvgrensningerDatoManed.setDuplicatesEnabled(0)

        self.okonomiAvgrensningerDatoPeriode = QComboBox(0,self.groupBox9_2,"okonomiAvgrensningerDatoPeriode")
        self.okonomiAvgrensningerDatoPeriode.setEnabled(0)
        self.okonomiAvgrensningerDatoPeriode.setGeometry(QRect(650,30,231,21))
        self.okonomiAvgrensningerDatoPeriode.setDuplicatesEnabled(0)

        self.okonomiAvgrensningerDatoAr = QSpinBox(self.groupBox9_2,"okonomiAvgrensningerDatoAr")
        self.okonomiAvgrensningerDatoAr.setGeometry(QRect(440,30,80,21))
        self.okonomiAvgrensningerDatoAr.setMaxValue(3000)
        self.okonomiAvgrensningerDatoAr.setMinValue(1900)
        self.okonomiAvgrensningerDatoAr.setValue(2006)

        self.okonomiAvgrensningerDato = QCheckBox(self.groupBox9_2,"okonomiAvgrensningerDato")
        self.okonomiAvgrensningerDato.setGeometry(QRect(340,30,55,19))

        self.okonomiAvgrensningerKunde = QCheckBox(self.groupBox9_2,"okonomiAvgrensningerKunde")
        self.okonomiAvgrensningerKunde.setGeometry(QRect(340,63,74,19))

        self.okonomiAvgrensningerVare = QCheckBox(self.groupBox9_2,"okonomiAvgrensningerVare")
        self.okonomiAvgrensningerVare.setGeometry(QRect(340,93,55,19))

        self.myndigheteneRegistrertTekst_2_4_3 = QLabel(self.groupBox9_2,"myndigheteneRegistrertTekst_2_4_3")
        self.myndigheteneRegistrertTekst_2_4_3.setGeometry(QRect(14,46,100,18))

        self.myndigheteneRegistrertTekst_2_4 = QLabel(self.groupBox9_2,"myndigheteneRegistrertTekst_2_4")
        self.myndigheteneRegistrertTekst_2_4.setGeometry(QRect(13,25,100,18))

        self.textLabel1_9_2 = QLabel(self.groupBox9_2,"textLabel1_9_2")
        self.textLabel1_9_2.setGeometry(QRect(14,89,100,16))

        self.okonomiRegnskapTotalUMva = QLabel(self.groupBox9_2,"okonomiRegnskapTotalUMva")
        self.okonomiRegnskapTotalUMva.setGeometry(QRect(121,25,210,20))
        self.okonomiRegnskapTotalUMva.setTextFormat(QLabel.RichText)

        self.okonomiRegnskapTotalMMva = QLabel(self.groupBox9_2,"okonomiRegnskapTotalMMva")
        self.okonomiRegnskapTotalMMva.setGeometry(QRect(122,46,210,20))
        self.okonomiRegnskapTotalMMva.setTextFormat(QLabel.RichText)

        self.textLabel1_9 = QLabel(self.groupBox9_2,"textLabel1_9")
        self.textLabel1_9.setGeometry(QRect(14,69,100,16))

        self.okonomiRegnskapAntallFakturaer = QLabel(self.groupBox9_2,"okonomiRegnskapAntallFakturaer")
        self.okonomiRegnskapAntallFakturaer.setGeometry(QRect(122,89,210,20))

        self.okonomiRegnskapMoms = QLabel(self.groupBox9_2,"okonomiRegnskapMoms")
        self.okonomiRegnskapMoms.setGeometry(QRect(122,69,210,20))
        self.okonomiRegnskapMoms.setTextFormat(QLabel.RichText)

        self.okonomiRegnskapRegnut = QPushButton(self.groupBox9_2,"okonomiRegnskapRegnut")
        self.okonomiRegnskapRegnut.setGeometry(QRect(90,120,160,21))

        self.line4 = QFrame(self.groupBox9_2,"line4")
        self.line4.setGeometry(QRect(290,30,20,111))
        self.line4.setFrameShape(QFrame.VLine)
        self.line4.setFrameShadow(QFrame.Sunken)
        self.line4.setFrameShape(QFrame.VLine)

        self.okonomiFakturaerSkrivut = QPushButton(self.TabPage_4,"okonomiFakturaerSkrivut")
        self.okonomiFakturaerSkrivut.setGeometry(QRect(864,699,74,23))
        self.fakturaTab.insertTab(self.TabPage_4,QString.fromLatin1(""))

        self.TabPage_5 = QWidget(self.fakturaTab,"TabPage_5")

        self.groupBox9 = QGroupBox(self.TabPage_5,"groupBox9")
        self.groupBox9.setGeometry(QRect(10,200,921,220))

        self.myndigheteneSkjemaHent = QPushButton(self.groupBox9,"myndigheteneSkjemaHent")
        self.myndigheteneSkjemaHent.setGeometry(QRect(820,20,80,25))

        self.myndigheteneSkjemaListe = QListView(self.groupBox9,"myndigheteneSkjemaListe")
        self.myndigheteneSkjemaListe.addColumn(self.__tr("Skjema"))
        self.myndigheteneSkjemaListe.header().setClickEnabled(0,self.myndigheteneSkjemaListe.header().count() - 1)
        self.myndigheteneSkjemaListe.addColumn(self.__tr("Navn"))
        self.myndigheteneSkjemaListe.addColumn(self.__tr("Instans"))
        self.myndigheteneSkjemaListe.addColumn(self.__tr("URL"))
        self.myndigheteneSkjemaListe.setGeometry(QRect(10,70,900,140))
        self.myndigheteneSkjemaListe.setAllColumnsShowFocus(1)

        self.myndigheteneSkjemaTekst = QLabel(self.groupBox9,"myndigheteneSkjemaTekst")
        self.myndigheteneSkjemaTekst.setGeometry(QRect(10,20,800,41))

        self.buttonGroup1 = QButtonGroup(self.TabPage_5,"buttonGroup1")
        self.buttonGroup1.setGeometry(QRect(8,22,921,161))

        self.myndigheteneRegistrertHent = QPushButton(self.buttonGroup1,"myndigheteneRegistrertHent")
        self.myndigheteneRegistrertHent.setGeometry(QRect(820,20,80,25))

        self.myndigheteneRegistrertTekst = QLabel(self.buttonGroup1,"myndigheteneRegistrertTekst")
        self.myndigheteneRegistrertTekst.setGeometry(QRect(10,20,761,121))
        self.myndigheteneRegistrertTekst.setTextFormat(QLabel.RichText)

        self.buttonGroup1_2 = QButtonGroup(self.buttonGroup1,"buttonGroup1_2")
        self.buttonGroup1_2.setGeometry(QRect(0,0,921,161))

        self.myndigheteneRegistrertHent_2 = QPushButton(self.buttonGroup1_2,"myndigheteneRegistrertHent_2")
        self.myndigheteneRegistrertHent_2.setGeometry(QRect(820,20,80,25))

        self.myndigheteneRegistrertTekst_2 = QLabel(self.buttonGroup1_2,"myndigheteneRegistrertTekst_2")
        self.myndigheteneRegistrertTekst_2.setGeometry(QRect(12,18,761,121))
        self.myndigheteneRegistrertTekst_2.setTextFormat(QLabel.RichText)
        self.fakturaTab.insertTab(self.TabPage_5,QString.fromLatin1(""))

        self.TabPage_6 = QWidget(self.fakturaTab,"TabPage_6")

        self.groupBox11 = QGroupBox(self.TabPage_6,"groupBox11")
        self.groupBox11.setGeometry(QRect(18,181,581,161))

        self.groupBox11_2 = QGroupBox(self.TabPage_6,"groupBox11_2")
        self.groupBox11_2.setGeometry(QRect(20,510,581,200))

        self.comboBox9 = QComboBox(0,self.groupBox11_2,"comboBox9")
        self.comboBox9.setGeometry(QRect(108,31,460,21))

        self.pushButton19 = QPushButton(self.groupBox11_2,"pushButton19")
        self.pushButton19.setGeometry(QRect(448,71,120,21))

        self.groupBox10 = QGroupBox(self.TabPage_6,"groupBox10")
        self.groupBox10.setGeometry(QRect(20,30,580,130))

        self.sikkerhetskopiGmailHuskPassord = QCheckBox(self.groupBox10,"sikkerhetskopiGmailHuskPassord")
        self.sikkerhetskopiGmailHuskPassord.setGeometry(QRect(460,50,53,19))

        self.sikkerhetskopiGmailPassord = QLineEdit(self.groupBox10,"sikkerhetskopiGmailPassord")
        self.sikkerhetskopiGmailPassord.setGeometry(QRect(170,50,280,21))
        self.sikkerhetskopiGmailPassord.setAcceptDrops(0)
        self.sikkerhetskopiGmailPassord.setEchoMode(QLineEdit.Password)
        self.sikkerhetskopiGmailPassord.setDragEnabled(0)

        self.textLabel1_10 = QLabel(self.groupBox10,"textLabel1_10")
        self.textLabel1_10.setGeometry(QRect(10,30,150,14))

        self.textLabel2_4 = QLabel(self.groupBox10,"textLabel2_4")
        self.textLabel2_4.setGeometry(QRect(10,50,135,14))

        self.sikkerhetskopiGmailLastopp = QPushButton(self.groupBox10,"sikkerhetskopiGmailLastopp")
        self.sikkerhetskopiGmailLastopp.setEnabled(0)
        self.sikkerhetskopiGmailLastopp.setGeometry(QRect(10,80,166,23))

        self.sikkerhetskopiGmailEpost = QLineEdit(self.groupBox10,"sikkerhetskopiGmailEpost")
        self.sikkerhetskopiGmailEpost.setGeometry(QRect(170,22,280,21))

        self.sikkerhetskopiGmailHuskEpost = QCheckBox(self.groupBox10,"sikkerhetskopiGmailHuskEpost")
        self.sikkerhetskopiGmailHuskEpost.setGeometry(QRect(460,23,53,19))

        self.sikkerhetskopiGmailFramgang = QProgressBar(self.groupBox10,"sikkerhetskopiGmailFramgang")
        self.sikkerhetskopiGmailFramgang.setGeometry(QRect(231,80,320,22))

        self.sikkerhetskopiGmailUbrukelig = QLabel(self.groupBox10,"sikkerhetskopiGmailUbrukelig")
        self.sikkerhetskopiGmailUbrukelig.setGeometry(QRect(30,30,521,60))
        sikkerhetskopiGmailUbrukelig_font = QFont(self.sikkerhetskopiGmailUbrukelig.font())
        sikkerhetskopiGmailUbrukelig_font.setPointSize(10)
        sikkerhetskopiGmailUbrukelig_font.setBold(1)
        self.sikkerhetskopiGmailUbrukelig.setFont(sikkerhetskopiGmailUbrukelig_font)
        self.sikkerhetskopiGmailUbrukelig.setFrameShape(QLabel.Box)
        self.sikkerhetskopiGmailUbrukelig.setLineWidth(1)
        self.sikkerhetskopiGmailUbrukelig.setAlignment(QLabel.WordBreak | QLabel.AlignCenter)
        self.fakturaTab.insertTab(self.TabPage_6,QString.fromLatin1(""))

        self.fileNewAction = QAction(self,"fileNewAction")
        self.fileNewAction.setIconSet(QIconSet(self.image3))
        self.fileOpenAction = QAction(self,"fileOpenAction")
        self.fileOpenAction.setIconSet(QIconSet(self.image4))
        self.fileSaveAction = QAction(self,"fileSaveAction")
        self.fileSaveAction.setIconSet(QIconSet(self.image5))
        self.fileSaveAsAction = QAction(self,"fileSaveAsAction")
        self.filePrintAction = QAction(self,"filePrintAction")
        self.filePrintAction.setIconSet(QIconSet(self.image6))
        self.fileExitAction = QAction(self,"fileExitAction")
        self.editUndoAction = QAction(self,"editUndoAction")
        self.editUndoAction.setIconSet(QIconSet(self.image7))
        self.editRedoAction = QAction(self,"editRedoAction")
        self.editRedoAction.setIconSet(QIconSet(self.image8))
        self.editCutAction = QAction(self,"editCutAction")
        self.editCutAction.setIconSet(QIconSet(self.image9))
        self.editCopyAction = QAction(self,"editCopyAction")
        self.editCopyAction.setIconSet(QIconSet(self.image10))
        self.editPasteAction = QAction(self,"editPasteAction")
        self.editPasteAction.setIconSet(QIconSet(self.image11))
        self.editFindAction = QAction(self,"editFindAction")
        self.editFindAction.setIconSet(QIconSet(self.image12))
        self.helpContentsAction = QAction(self,"helpContentsAction")
        self.helpIndexAction = QAction(self,"helpIndexAction")
        self.helpAboutAction = QAction(self,"helpAboutAction")




        self.qt_dead_widget_MenuBar = QMenuBar(self,"qt_dead_widget_MenuBar")



        self.languageChange()

        self.resize(QSize(998,814).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.fileNewAction,SIGNAL("activated()"),self.fileNew)
        self.connect(self.fileOpenAction,SIGNAL("activated()"),self.fileOpen)
        self.connect(self.fileSaveAction,SIGNAL("activated()"),self.fileSave)
        self.connect(self.fileSaveAsAction,SIGNAL("activated()"),self.fileSaveAs)
        self.connect(self.filePrintAction,SIGNAL("activated()"),self.filePrint)
        self.connect(self.fileExitAction,SIGNAL("activated()"),self.fileExit)
        self.connect(self.editUndoAction,SIGNAL("activated()"),self.editUndo)
        self.connect(self.editRedoAction,SIGNAL("activated()"),self.editRedo)
        self.connect(self.editCutAction,SIGNAL("activated()"),self.editCut)
        self.connect(self.editCopyAction,SIGNAL("activated()"),self.editCopy)
        self.connect(self.editPasteAction,SIGNAL("activated()"),self.editPaste)
        self.connect(self.editFindAction,SIGNAL("activated()"),self.editFind)
        self.connect(self.helpIndexAction,SIGNAL("activated()"),self.helpIndex)
        self.connect(self.helpContentsAction,SIGNAL("activated()"),self.helpContents)
        self.connect(self.helpAboutAction,SIGNAL("activated()"),self.helpAbout)
        self.connect(self.epostSmtpServer,SIGNAL("lostFocus()"),self.epostSmtpServer_lostFocus)

        self.setTabOrder(self.fakturaTab,self.fakturaNy)
        self.setTabOrder(self.fakturaNy,self.fakturaFakturaliste)
        self.setTabOrder(self.fakturaFakturaliste,self.fakturaFaktaMottaker)
        self.setTabOrder(self.fakturaFaktaMottaker,self.fakturaFaktaVare)
        self.setTabOrder(self.fakturaFaktaVare,self.fakturaFaktaAntall)
        self.setTabOrder(self.fakturaFaktaAntall,self.fakturaFaktaVareLeggtil)
        self.setTabOrder(self.fakturaFaktaVareLeggtil,self.fakturaFaktaOrdrelinje)
        self.setTabOrder(self.fakturaFaktaOrdrelinje,self.fakturaFaktaVareFjern)
        self.setTabOrder(self.fakturaFaktaVareFjern,self.fakturaFaktaTekst)
        self.setTabOrder(self.fakturaFaktaTekst,self.fakturaFaktaLegginn)
        self.setTabOrder(self.fakturaFaktaLegginn,self.kundeNy)
        self.setTabOrder(self.kundeNy,self.kundeKundeliste)
        self.setTabOrder(self.kundeKundeliste,self.kundeNyfaktura)
        self.setTabOrder(self.kundeNyfaktura,self.kundeInfoNavn)
        self.setTabOrder(self.kundeInfoNavn,self.kundeInfoKontaktperson)
        self.setTabOrder(self.kundeInfoKontaktperson,self.kundeInfoEpost)
        self.setTabOrder(self.kundeInfoEpost,self.kundeInfoAdresse)
        self.setTabOrder(self.kundeInfoAdresse,self.kundeInfoPostnummer)
        self.setTabOrder(self.kundeInfoPostnummer,self.kundeInfoPoststed)
        self.setTabOrder(self.kundeInfoPoststed,self.kundeInfoStatus)
        self.setTabOrder(self.kundeInfoStatus,self.kundeInfoTelefon)
        self.setTabOrder(self.kundeInfoTelefon,self.kundeInfoTelefaks)
        self.setTabOrder(self.kundeInfoTelefaks,self.kundeInfoEndre)
        self.setTabOrder(self.kundeInfoEndre,self.varerNy)
        self.setTabOrder(self.varerNy,self.varerVareliste)
        self.setTabOrder(self.varerVareliste,self.varerInfoNavn)
        self.setTabOrder(self.varerInfoNavn,self.varerInfoEnhet)
        self.setTabOrder(self.varerInfoEnhet,self.varerInfoPris)
        self.setTabOrder(self.varerInfoPris,self.varerInfoDetaljer)
        self.setTabOrder(self.varerInfoDetaljer,self.varerInfoMva)
        self.setTabOrder(self.varerInfoMva,self.varerInfoLegginn)
        self.setTabOrder(self.varerInfoLegginn,self.dittfirmaFirmanavn)
        self.setTabOrder(self.dittfirmaFirmanavn,self.dittfirmaOrganisasjonsnummer)
        self.setTabOrder(self.dittfirmaOrganisasjonsnummer,self.dittfirmaKontaktperson)
        self.setTabOrder(self.dittfirmaKontaktperson,self.dittfirmaEpost)
        self.setTabOrder(self.dittfirmaEpost,self.dittfirmaAdresse)
        self.setTabOrder(self.dittfirmaAdresse,self.dittfirmaPostnummer)
        self.setTabOrder(self.dittfirmaPostnummer,self.dittfirmaPoststed)
        self.setTabOrder(self.dittfirmaPoststed,self.dittfirmaTelefon)
        self.setTabOrder(self.dittfirmaTelefon,self.dittfirmaMobil)
        self.setTabOrder(self.dittfirmaMobil,self.dittfirmaTelefaks)
        self.setTabOrder(self.dittfirmaTelefaks,self.dittfirmaKontonummer)
        self.setTabOrder(self.dittfirmaKontonummer,self.dittfirmaVilkar)
        self.setTabOrder(self.dittfirmaVilkar,self.dittfirmaMva)
        self.setTabOrder(self.dittfirmaMva,self.dittfirmaForfall)

        self.textLabel3_2.setBuddy(self.fakturaBetaltDato)
        self.textLabel8.setBuddy(self.fakturaFaktaTekst)
        self.textLabel5_2.setBuddy(self.fakturaFaktaOrdrelinje)
        self.textLabel5.setBuddy(self.fakturaFaktaMottaker)
        self.textLabel7_6.setBuddy(self.fakturaFaktaAntall)
        self.textLabel1_3_3_5.setBuddy(self.kundeInfoPostnummer)
        self.textLabel2.setBuddy(self.kundeInfoNavn)
        self.textLabel1_3_3_2_4.setBuddy(self.kundeInfoTelefon)
        self.textLabel1_3_3_3_4.setBuddy(self.kundeInfoTelefaks)
        self.textLabel2_3_2.setBuddy(self.kundeInfoKontaktperson)
        self.textLabel2_3.setBuddy(self.kundeInfoEpost)
        self.textLabel4.setBuddy(self.kundeInfoStatus)
        self.textLabel3.setBuddy(self.kundeInfoAdresse)
        self.textLabel1_3_4_2.setBuddy(self.kundeInfoPoststed)
        self.textLabel10.setBuddy(self.varerInfoNavn)
        self.textLabel10_4.setBuddy(self.varerInfoPris)
        self.textLabel10_3.setBuddy(self.varerInfoDetaljer)
        self.textLabel10_2.setBuddy(self.varerInfoEnhet)
        self.textLabel7_3.setBuddy(self.varerInfoMva)


    def languageChange(self):
        self.setCaption(self.__tr("Fryktelig fin faktura"))
        self.buttonGroup1_2_2.setTitle(self.__tr("Oppgaver"))
        self.myndigheteneRegistrertTekst_2_3.setText(self.__tr("textLabel2"))
        self.myndigheteneRegistrertTekst_2_4_2.setText(self.__tr("Totalt m/mva:"))
        self.okonomiRegnskapTotalMva.setText(self.__tr("textLabel1"))
        self.groupBox6.setTitle(self.__tr("Detaljer"))
        self.fakturaDetaljerTekst.setText(QString.null)
        self.fakturaFakturaliste.header().setLabel(0,self.__tr("#"))
        self.fakturaFakturaliste.header().setLabel(1,self.__tr("Tekst"))
        self.fakturaFakturaliste.header().setLabel(2,self.__tr("Mottaker"))
        self.fakturaFakturaliste.header().setLabel(3,self.__trUtf8("\x42\x65\x6c\xc3\xb8\x70"))
        self.fakturaFakturaliste.header().setLabel(4,self.__tr("Forfall"))
        self.fakturaFakturaliste.header().setLabel(5,self.__tr("Betalt"))
        self.groupBox8_2.setTitle(self.__tr("Handlinger"))
        self.textLabel3_2.setText(self.__tr("Fakturaen er betalt:"))
        self.textLabel4_2.setText(self.__tr("Du trenger en kvittering:"))
        self.fakturaBetalt.setText(self.__tr("Betalt"))
        self.fakturaBetalt.setAccel(QString.null)
        QToolTip.add(self.fakturaBetalt,self.__trUtf8("\x4d\x61\x72\x6b\x65\x72\x65\x72\x20\x66\x61\x6b\x74\x75\x72\x61\x65\x6e\x20\x73\x6f\x6d\x20\x62\x65\x74\x61\x6c\x74\x20\x28\x70\xc3\xa5\x20\x61\x6e\x67\x69\x74\x74\x20\x64\x61\x74\x6f\x29"))
        self.fakturaLagKvittering.setText(self.__tr("Skriv &ut"))
        self.fakturaLagKvittering.setAccel(self.__tr("Alt+U"))
        QToolTip.add(self.fakturaLagKvittering,self.__trUtf8("\x53\x6b\x72\x69\x76\x65\x72\x20\x75\x74\x20\x65\x6e\x20\x6b\x76\x69\x74\x74\x65\x72\x69\x6e\x67\x20\x70\xc3\xa5\x20\x73\x6b\x72\x69\x76\x65\x72\x65\x6e"))
        self.textLabel2_2.setText(self.__tr("Du skal sende fakturaen:"))
        self.fakturaLagEpost.setText(self.__tr("Epost"))
        self.fakturaLagEpost.setAccel(QString.null)
        QToolTip.add(self.fakturaLagEpost,self.__tr("Lager en faktura av angitt type"))
        self.fakturaLagPapir.setText(self.__tr("Papir"))
        self.fakturaLagPapir.setAccel(QString.null)
        QToolTip.add(self.fakturaLagPapir,self.__tr("Lager en faktura av angitt type"))
        self.fakturaVisKansellerte.setText(self.__tr("vis kan&sellerte"))
        self.fakturaVisKansellerte.setAccel(self.__tr("Alt+S"))
        QToolTip.add(self.fakturaVisKansellerte,self.__tr("Angir om kansellerte fakturaer skal vises"))
        self.fakturaNy.setText(self.__tr("&Ny faktura"))
        self.fakturaNy.setAccel(self.__tr("Alt+N"))
        QToolTip.add(self.fakturaNy,self.__tr("Lager en ny faktura"))
        self.fakturaFakta.setTitle(self.__tr("Fakturafakta"))
        self.textLabel8.setText(self.__tr("&Tekst"))
        self.textLabel5_2.setText(self.__tr("&Varer"))
        self.textLabel1_8.setText(self.__tr("Sum:"))
        self.textLabel5.setText(self.__tr("&Mottaker"))
        self.fakturaFaktaLegginn.setText(self.__tr("&Lag faktura"))
        self.fakturaFaktaLegginn.setAccel(self.__tr("Alt+L"))
        QToolTip.add(self.fakturaFaktaLegginn,self.__tr("Lager den nye fakturaen"))
        self.fakturaFaktaVareFjern.setText(self.__tr("F&jern"))
        self.fakturaFaktaVareFjern.setAccel(self.__tr("Alt+J"))
        QToolTip.add(self.fakturaFaktaVareFjern,self.__tr("Fjerner den markerte varen fra fakturaen"))
        self.fakturaFaktaSum.setText(self.__tr("0 kr"))
        QToolTip.add(self.fakturaFaktaSum,self.__tr("Fakturaens verdi hittil"))
        QToolTip.add(self.fakturaFaktaAntall,self.__tr("Antall enheter av varen du har solgt"))
        self.textLabel7_6.setText(self.__tr("&Antall"))
        self.textLabel1_4.setText(self.__tr("Beskrivelse:"))
        self.textLabel1_4_2.setText(self.__tr("Pris:"))
        self.fakturaFaktaVareDetaljer.setText(QString.null)
        self.fakturaFaktaVarePris.setText(QString.null)
        self.fakturaFaktaVareLeggtil.setText(self.__tr("Le&gg til"))
        self.fakturaFaktaVareLeggtil.setAccel(self.__tr("Alt+G"))
        QToolTip.add(self.fakturaFaktaVareLeggtil,self.__tr("Legger til den valgte varen fra listen over"))
        QToolTip.add(self.fakturaFaktaTekst,self.__tr("Fakturatekst"))
        QWhatsThis.add(self.fakturaFaktaTekst,self.__trUtf8("\x42\x65\x73\x6b\x72\x69\x76\x65\x6c\x73\x65\x20\x61\x76\x20\x68\x76\x61\x20\x66\x61\x6b\x74\x75\x72\x61\x65\x6e\x20\x68\x61\x6e\x64\x6c\x65\x72\x20\x6f\x6d\x2e\x20\x44\x65\x74\x20\x6b\x61\x6e\x20\x76\xc3\xa6\x72\x65\x20\x74\x79\x70\x65\x6e\x20\x6f\x70\x70\x64\x72\x61\x67\x20\x75\x74\x66\xc3\xb8\x72\x74\x20\x65\x6c\x6c\x65\x72\x20\x6f\x70\x70\x64\x72\x61\x67\x65\x74\x73\x20\x74\x65\x6d\x61\x2e"))
        QToolTip.add(self.fakturaFaktaMottaker,self.__tr("Fakturaens mottaker (kunden)"))
        QToolTip.add(self.fakturaFaktaVare,self.__tr("Registrerte varer"))
        QToolTip.add(self.fakturaFaktaOrdrelinje,self.__tr("Varene som er lagt inn i fakturaen"))
        self.fakturaSendepostBoks.setTitle(self.__tr("Send epost"))
        self.fakturaSendepostAvbryt.setText(self.__tr("Avbryt"))
        self.fakturaSendepostSend.setText(self.__tr("Send"))
        self.fakturaSendepostTittel.setText(self.__tr("Sender epost til"))
        self.fakturaTab.changeTab(self.tab,self.__tr("&Faktura"))
        self.kundeNy.setText(self.__tr("&Ny kunde"))
        self.kundeNy.setAccel(self.__tr("Alt+N"))
        self.kundeKundeliste.header().setLabel(0,self.__tr("#"))
        self.kundeKundeliste.header().setLabel(1,self.__tr("Navn"))
        self.kundeKundeliste.header().setLabel(2,self.__tr("Epost"))
        self.kundeKundeliste.header().setLabel(3,self.__tr("Status"))
        self.kundeKundeliste.header().setLabel(4,self.__tr("Adresse"))
        self.kundeKundeliste.header().setLabel(5,self.__tr("Telefon"))
        self.kundeKundeliste.header().setLabel(6,self.__tr("Telefaks"))
        self.groupBox7.setTitle(self.__tr("Detaljer"))
        self.kundeNyfaktura.setText(self.__tr("N&y faktura til kunden"))
        self.kundeNyfaktura.setAccel(self.__tr("Alt+Y"))
        self.kundeVisFjernede.setText(self.__tr("vis f&jernede"))
        self.kundeVisFjernede.setAccel(self.__tr("Alt+J"))
        self.kundeInfo.setTitle(self.__tr("Kundeinfo"))
        self.textLabel1_3_3_5.setText(self.__tr("Postnr"))
        self.textLabel2.setText(self.__tr("N&avn"))
        self.kundeInfoPostnummer.setInputMask(self.__tr("0000; ","Kommentar: Sett inn norsk postnummer"))
        QToolTip.add(self.kundeInfoPostnummer,self.__tr("Sett inn norsk postnummer"))
        self.textLabel1_3_3_2_4.setText(self.__tr("Telefon"))
        self.textLabel1_3_3_3_4.setText(self.__tr("Telefaks"))
        self.kundeInfoTelefaks.setInputMask(self.__tr("00000000; "))
        self.kundeInfoTelefon.setInputMask(self.__tr("00000000; "))
        self.textLabel2_3_2.setText(self.__tr("K&ontakt"))
        self.textLabel2_3.setText(self.__tr("&Epost"))
        self.textLabel4.setText(self.__tr("&Status"))
        self.textLabel3.setText(self.__tr("A&dresse"))
        self.textLabel1_3_4_2.setText(self.__tr("Pos&tsted"))
        self.kundeInfoEndre.setText(self.__tr("&Lag ny kunde"))
        self.kundeInfoEndre.setAccel(self.__tr("Alt+L"))
        self.fakturaTab.changeTab(self.tab_2,self.__tr("&Kunder"))
        self.varerNy.setText(self.__tr("&Ny vare"))
        self.varerNy.setAccel(self.__tr("Alt+N"))
        self.varerVareliste.header().setLabel(0,self.__tr("#"))
        self.varerVareliste.header().setLabel(1,self.__tr("Navn"))
        self.varerVareliste.header().setLabel(2,self.__tr("Detaljer"))
        self.varerVareliste.header().setLabel(3,self.__tr("Pris"))
        self.varerVareliste.header().setLabel(4,self.__tr("Enhet"))
        self.groupBox8.setTitle(self.__tr("Detaljer"))
        self.varerVisFjernede.setText(self.__tr("vis f&jernede"))
        self.varerVisFjernede.setAccel(self.__tr("Alt+J"))
        self.varerInfo.setTitle(self.__tr("Vareinfo"))
        self.textLabel10.setText(self.__tr("N&avn"))
        self.textLabel10_4.setText(self.__tr("&Pris"))
        self.textLabel10_3.setText(self.__tr("&Detaljer"))
        self.textLabel10_2.setText(self.__tr("&Enhet"))
        self.textLabel7_3.setText(self.__tr("&MVA-sats"))
        self.varerInfoLegginn.setText(self.__tr("&Lag ny vare"))
        self.varerInfoLegginn.setAccel(self.__tr("Alt+L"))
        self.fakturaTab.changeTab(self.TabPage,self.__tr("&Varer"))
        self.textLabel1.setText(self.__tr("Firmanavn"))
        self.textLabel1_3.setText(self.__tr("Adresse"))
        self.textLabel1_3_5.setText(self.__trUtf8("\x53\x74\x61\x6e\x64\x61\x72\x64\x0a\x62\x65\x74\x61\x6c\x69\x6e\x67\x73\x76\x69\x6c\x6b\xc3\xa5\x72"))
        self.textLabel1_3_3.setText(self.__tr("Postnummer"))
        self.textLabel1_3_4.setText(self.__tr("Poststed"))
        self.textLabel1_3_3_4.setText(self.__tr("Telefaks"))
        self.dittfirmaTelefaks.setInputMask(self.__tr("00000000; "))
        self.dittfirmaPostnummer.setInputMask(self.__tr("0000; "))
        self.textLabel1_3_3_2.setText(self.__tr("Telefon"))
        self.dittfirmaTelefon.setInputMask(self.__tr("00000000; "))
        self.textLabel1_3_3_3.setText(self.__tr("Mobiltelefon"))
        self.dittfirmaMobil.setInputMask(self.__tr("00000000; "))
        self.textLabel1_2_3.setText(self.__tr("Kontonummer"))
        self.dittfirmaKontonummer.setInputMask(self.__tr("00000000000; "))
        self.textLabel1_2_4.setText(self.__tr("Kontaktperson"))
        self.textLabel1_2.setText(self.__tr("Epost"))
        self.textLabel7_2.setText(self.__tr("Forfall"))
        self.textLabel7.setText(self.__tr("MVA-sats"))
        self.textLabel1_7.setText(self.__tr("Katalog for fakturaer"))
        self.textLabel9.setText(self.__tr("dager"))
        self.dittfirmaFakturakatalogSok.setText(self.__trUtf8("\x53\xc3\xb8\x6b\x2e\x2e\x2e"))
        self.textLabel1_5.setText(self.__tr("Organisasjonsnummer"))
        QToolTip.add(self.dittfirmaLogoPixmap,self.__tr("Logo"))
        self.dittfirmaFinnFjernLogo.setText(self.__tr("Finn logo"))
        self.dittfirmaLagre.setText(self.__tr("&Lagre"))
        self.dittfirmaLagre.setAccel(self.__tr("Alt+L"))
        self.dittfirmaHjelpetekst.setText(QString.null)
        self.dittfirmaLagreInfo.setText(QString.null)
        self.dittfirmaFakturakatalog.setText(self.__tr("~"))
        self.fakturaTab.changeTab(self.TabPage_2,self.__tr("&Ditt firma"))
        self.epostHjelpefelt.setText(QString.null)
        self.epostLagre.setText(self.__tr("&Lagre"))
        self.epostLagre.setAccel(self.__tr("Alt+L"))
        self.epostSeksjonSmtp.setTitle(self.__tr("SMTP"))
        self.textLabel1_12.setText(self.__tr("Send gjennom server (SMTP server):"))
        self.textLabel3_4_2.setText(self.__tr("Passord:"))
        self.textLabel4_4.setText(self.__tr("Port:"))
        self.epostSmtpServer.setText(self.__tr("localhost"))
        self.epostSmtpAuth.setText(self.__tr("Serveren krever at jeg logger inn"))
        self.epostSmtpTLS.setText(self.__trUtf8("\x53\x65\x72\x76\x65\x72\x65\x6e\x20\x73\x74\xc3\xb8\x74\x74\x65\x72\x20\x6b\x72\x79\x70\x74\x65\x72\x74\x65\x20\x6f\x76\x65\x72\x66\xc3\xb8\x72\x69\x6e\x67\x65\x72\x20\x28\x54\x4c\x53\x29"))
        self.textLabel3_4.setText(self.__tr("Brukernavn:"))
        self.epostSeksjonSendmail.setTitle(self.__tr("Sendmail"))
        self.textLabel5_4.setText(self.__tr("Sti til sendmail:"))
        self.epostSendmailSti.setText(self.__tr("/usr/sbin/sendmail"))
        self.epostSeksjonGmail.setTitle(self.__tr("Gmail"))
        self.textLabel1_10_3.setText(self.__tr("Full epostadresse i gmail:"))
        self.textLabel2_4_3.setText(self.__tr("Passord for innlogging:"))
        self.epostGmailHuskEpost.setText(self.__tr("Husk"))
        self.epostGmailUbrukelig.setText(self.__trUtf8("\x44\x75\x20\x6d\xc3\xa5\x20\x69\x6e\x73\x74\x61\x6c\x6c\x65\x72\x65\x20\x6d\x6f\x64\x75\x6c\x65\x6e\x20\x27\x6c\x69\x62\x67\x6d\x61\x69\x6c\x27\x20\x66\x6f\x72\x20\xc3\xa5\x20\x73\x65\x6e\x64\x65\x20\x67\x6a\x65\x6e\x6e\x6f\x6d\x20\x47\x6d\x61\x69\x6c\x2e"))
        self.epostLosning.setTitle(self.__trUtf8("\x45\x70\x6f\x73\x74\x6c\xc3\xb8\x73\x6e\x69\x6e\x67\x20\x66\x6f\x72\x20\x73\x65\x6e\x64\x69\x6e\x67\x20\x61\x76\x20\x65\x2d\x66\x61\x6b\x74\x75\x72\x61"))
        self.epostLosningGmail.setText(self.__tr("Gmail"))
        self.epostLosningAuto.setText(self.__tr("Velg automatisk"))
        self.epostLosningSmtp.setText(self.__tr("SMTP"))
        self.epostLosningSendmail.setText(self.__tr("Sendmail"))
        self.textLabel2_6.setText(self.__tr("Avsenderadresse:"))
        self.epostLosningTest.setText(self.__tr("Test forbindelse"))
        self.fakturaTab.changeTab(self.TabPage_3,self.__tr("&Epost"))
        QToolTip.add(self.okonomiDetaljregnskap,self.__tr("Detaljert regnskap"))
        self.groupBox9_2.setTitle(self.__tr("Regnskap"))
        self.okonomiAvgrensningerDato.setText(self.__tr("Dato:"))
        self.okonomiAvgrensningerKunde.setText(self.__tr("Mottaker:"))
        self.okonomiAvgrensningerVare.setText(self.__tr("Vare:"))
        self.myndigheteneRegistrertTekst_2_4_3.setText(self.__tr("Totalt m/mva:"))
        self.myndigheteneRegistrertTekst_2_4.setText(self.__tr("Totalt u/mva:"))
        self.textLabel1_9_2.setText(self.__tr("Antall fakturaer:"))
        self.okonomiRegnskapTotalUMva.setText(self.__tr("textLabel1"))
        self.okonomiRegnskapTotalMMva.setText(self.__tr("textLabel1"))
        self.textLabel1_9.setText(self.__tr("MVA:"))
        self.okonomiRegnskapAntallFakturaer.setText(self.__tr("textLabel1"))
        self.okonomiRegnskapMoms.setText(self.__tr("textLabel1"))
        self.okonomiRegnskapRegnut.setText(self.__tr("Regn ut"))
        self.okonomiFakturaerSkrivut.setText(self.__tr("Skriv &ut"))
        self.okonomiFakturaerSkrivut.setAccel(self.__tr("Alt+U"))
        self.fakturaTab.changeTab(self.TabPage_4,self.__trUtf8("\x26\xc3\x98\x6b\x6f\x6e\x6f\x6d\x69"))
        self.groupBox9.setTitle(self.__tr("Skjemaplikter"))
        self.myndigheteneSkjemaHent.setText(self.__trUtf8("\x48\x65\x6e\x74\x20\x70\xc3\xa5\x20\x6e\x79\x74\x74"))
        self.myndigheteneSkjemaListe.header().setLabel(0,self.__tr("Skjema"))
        self.myndigheteneSkjemaListe.header().setLabel(1,self.__tr("Navn"))
        self.myndigheteneSkjemaListe.header().setLabel(2,self.__tr("Instans"))
        self.myndigheteneSkjemaListe.header().setLabel(3,self.__tr("URL"))
        self.myndigheteneSkjemaTekst.setText(self.__tr("textLabel1"))
        self.buttonGroup1.setTitle(self.__trUtf8("\x52\x65\x67\x69\x73\x74\x72\x65\x72\x74\x20\x69\x20\x42\x72\xc3\xb8\x6e\x6e\xc3\xb8\x79\x73\x75\x6e\x64"))
        self.myndigheteneRegistrertHent.setText(self.__trUtf8("\x48\x65\x6e\x74\x20\x70\xc3\xa5\x20\x6e\x79\x74\x74"))
        self.myndigheteneRegistrertTekst.setText(self.__tr("textLabel2"))
        self.buttonGroup1_2.setTitle(self.__trUtf8("\x52\x65\x67\x69\x73\x74\x72\x65\x72\x74\x20\x69\x20\x42\x72\xc3\xb8\x6e\x6e\xc3\xb8\x79\x73\x75\x6e\x64"))
        self.myndigheteneRegistrertHent_2.setText(self.__trUtf8("\x48\x65\x6e\x74\x20\x70\xc3\xa5\x20\x6e\x79\x74\x74"))
        self.myndigheteneRegistrertTekst_2.setText(self.__tr("textLabel2"))
        self.fakturaTab.changeTab(self.TabPage_5,self.__tr("&Myndighetene"))
        self.groupBox11.setTitle(self.__tr("Filsystem"))
        self.groupBox11_2.setTitle(self.__tr("Kvitteringer"))
        self.pushButton19.setText(self.__tr("Vis"))
        self.groupBox10.setTitle(self.__tr("Gmail"))
        self.sikkerhetskopiGmailHuskPassord.setText(self.__tr("Husk"))
        QToolTip.add(self.sikkerhetskopiGmailPassord,self.__tr("Ditt passord ved Gmail"))
        self.textLabel1_10.setText(self.__tr("Full epostadresse i gmail:"))
        self.textLabel2_4.setText(self.__tr("Passord for innlogging:"))
        self.sikkerhetskopiGmailLastopp.setText(self.__tr("Last opp sikkerhetskopi"))
        self.sikkerhetskopiGmailHuskEpost.setText(self.__tr("Husk"))
        self.sikkerhetskopiGmailUbrukelig.setText(self.__trUtf8("\x44\x75\x20\x6d\xc3\xa5\x20\x69\x6e\x73\x74\x61\x6c\x6c\x65\x72\x65\x20\x6d\x6f\x64\x75\x6c\x65\x6e\x20\x27\x6c\x69\x62\x67\x6d\x61\x69\x6c\x27\x20\x66\x6f\x72\x20\xc3\xa5\x20\x6c\x61\x73\x74\x65\x20\x6f\x70\x70\x20\x73\x69\x6b\x6b\x65\x72\x68\x65\x74\x73\x6b\x6f\x70\x69\x65\x72\x20\x74\x69\x6c\x20\x47\x6d\x61\x69\x6c\x2e"))
        self.fakturaTab.changeTab(self.TabPage_6,self.__tr("&Sikkerhetskopi"))
        self.fileNewAction.setText(self.__tr("New"))
        self.fileNewAction.setMenuText(self.__tr("&New"))
        self.fileNewAction.setAccel(self.__tr("Ctrl+N"))
        self.fileOpenAction.setText(self.__tr("Open"))
        self.fileOpenAction.setMenuText(self.__tr("&Open..."))
        self.fileOpenAction.setAccel(self.__tr("Ctrl+O"))
        self.fileSaveAction.setText(self.__tr("Save"))
        self.fileSaveAction.setMenuText(self.__tr("&Save"))
        self.fileSaveAction.setAccel(self.__tr("Ctrl+S"))
        self.fileSaveAsAction.setText(self.__tr("Save As"))
        self.fileSaveAsAction.setMenuText(self.__tr("Save &As..."))
        self.fileSaveAsAction.setAccel(QString.null)
        self.filePrintAction.setText(self.__tr("Print"))
        self.filePrintAction.setMenuText(self.__tr("&Print..."))
        self.filePrintAction.setAccel(self.__tr("Ctrl+P"))
        self.fileExitAction.setText(self.__tr("Exit"))
        self.fileExitAction.setMenuText(self.__tr("E&xit"))
        self.fileExitAction.setAccel(QString.null)
        self.editUndoAction.setText(self.__tr("Undo"))
        self.editUndoAction.setMenuText(self.__tr("&Undo"))
        self.editUndoAction.setAccel(self.__tr("Ctrl+Z"))
        self.editRedoAction.setText(self.__tr("Redo"))
        self.editRedoAction.setMenuText(self.__tr("&Redo"))
        self.editRedoAction.setAccel(self.__tr("Ctrl+Y"))
        self.editCutAction.setText(self.__tr("Cut"))
        self.editCutAction.setMenuText(self.__tr("Cu&t"))
        self.editCutAction.setAccel(self.__tr("Ctrl+X"))
        self.editCopyAction.setText(self.__tr("Copy"))
        self.editCopyAction.setMenuText(self.__tr("&Copy"))
        self.editCopyAction.setAccel(self.__tr("Ctrl+C"))
        self.editPasteAction.setText(self.__tr("Paste"))
        self.editPasteAction.setMenuText(self.__tr("&Paste"))
        self.editPasteAction.setAccel(self.__tr("Ctrl+V"))
        self.editFindAction.setText(self.__tr("Find"))
        self.editFindAction.setMenuText(self.__tr("&Find..."))
        self.editFindAction.setAccel(self.__tr("Ctrl+F"))
        self.helpContentsAction.setText(self.__tr("Contents"))
        self.helpContentsAction.setMenuText(self.__tr("&Contents..."))
        self.helpContentsAction.setAccel(QString.null)
        self.helpIndexAction.setText(self.__tr("Index"))
        self.helpIndexAction.setMenuText(self.__tr("&Index..."))
        self.helpIndexAction.setAccel(QString.null)
        self.helpAboutAction.setText(self.__tr("About"))
        self.helpAboutAction.setMenuText(self.__tr("&About"))
        self.helpAboutAction.setAccel(QString.null)


    def fileNew(self):
        print "faktura.fileNew(): Not implemented yet"

    def fileOpen(self):
        print "faktura.fileOpen(): Not implemented yet"

    def fileSave(self):
        print "faktura.fileSave(): Not implemented yet"

    def fileSaveAs(self):
        print "faktura.fileSaveAs(): Not implemented yet"

    def filePrint(self):
        print "faktura.filePrint(): Not implemented yet"

    def fileExit(self):
        print "faktura.fileExit(): Not implemented yet"

    def editUndo(self):
        print "faktura.editUndo(): Not implemented yet"

    def editRedo(self):
        print "faktura.editRedo(): Not implemented yet"

    def editCut(self):
        print "faktura.editCut(): Not implemented yet"

    def editCopy(self):
        print "faktura.editCopy(): Not implemented yet"

    def editPaste(self):
        print "faktura.editPaste(): Not implemented yet"

    def editFind(self):
        print "faktura.editFind(): Not implemented yet"

    def helpIndex(self):
        print "faktura.helpIndex(): Not implemented yet"

    def helpContents(self):
        print "faktura.helpContents(): Not implemented yet"

    def helpAbout(self):
        print "faktura.helpAbout(): Not implemented yet"

    def epostSmtpServer_lostFocus(self):
        print "faktura.epostSmtpServer_lostFocus(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("faktura",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("faktura",s,c,QApplication.UnicodeUTF8)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = faktura()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
