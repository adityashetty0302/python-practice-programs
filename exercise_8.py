# Task 8
#
# Please write a program to compress and decompress the string "Music industry hails passage of the Music Modernization Act".


import zlib

ip_str = "Music industry hails passage of the Music Modernization Act"
print('Before compression \n' + ip_str)
compressed = zlib.compress(ip_str.encode('utf-8'))
decompressed = zlib.decompress(compressed)
print('\nAfter compression & decompression \n' + decompressed.decode('utf-8'))
