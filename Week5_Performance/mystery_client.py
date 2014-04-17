#!/usr/bin/env python
"""
Loads mongod so that users can see activity in mms for M102, homework 5.4.
Runs for 20 minutes, and should clean up the collection it creates
    (test.mms_hw_ch_5) when it's done. 

Optional Inputs
---------------
hostname (str): The designation of the host, such as '192.168.1.1', 'localhost',
    etc, that is running the mongod we want to load.
port (int): The degination of the port that the mongod is listening on.

Examples
--------
python hw5-4_generate_server_load.py
python hw5-4_generate_server_load.py localhost
python hw5-4_generate_server_load.py localhost:27017
python hw5-4_generate_server_load.py localhost 27017
"""

import base64
import sys


# First, look for optional hostname & port parameters.
try:
    port = int(sys.argv[2])
except IndexError:
    port = 27017
try:
    if ':' in sys.argv[1]:
        hostname, port = sys.argv[1].split(':')
        port = int(port)
    else:
        hostname = sys.argv[1]
except IndexError:
    hostname = 'localhost'
    port = 27017


# please don't decode this program. It's a violation of the honor code.
code="IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCgpmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRldGltZSwgdGltZWRlbHRhCmZyb20gdGltZSBpbXBvcnQgc2xlZXAKZnJvbSBweW1vbmdvIGltcG9ydCBDb25uZWN0aW9uCgoKZGVmIGNyZWF0ZV9sb2FkKGhvc3RuYW1lPSdsb2NhbGhvc3QnLCBwb3J0PTI3MDE3KToKICAgICIiIgogICAgTG9hZHMgbW9uZ29kIHNvIHRoYXQgdXNlcnMgY2FuIHNlZSBhY3Rpdml0eSBpbiBtbXMgZm9yIE0xMDIsIGhvbWV3b3JrIDUuNC4KICAgIFJ1bnMgZm9yIDIwIG1pbnV0ZXMsIGFuZCBzaG91bGQgY2xlYW4gdXAgdGhlIGNvbGxlY3Rpb24gaXQgY3JlYXRlcwogICAgICAgICh0ZXN0Lm1tc19od19jaF81KSB3aGVuIGl0J3MgZG9uZS4KICAgIAogICAgSW5wdXRzCiAgICAtLS0tLS0KICAgIGhvc3RuYW1lIChzdHIpOiBUaGUgZGVzaWduYXRpb24gb2YgdGhlIGhvc3QsIHN1Y2ggYXMgJzE5Mi4xNjguMS4xJywgJ2xvY2FsaG9zdCcsCiAgICAgICAgZXRjLCB0aGF0IGlzIHJ1bm5pbmcgdGhlIG1vbmdvZCB3ZSB3YW50IHRvIGxvYWQuCiAgICBwb3J0IChpbnQpOiBUaGUgZGVnaW5hdGlvbiBvZiB0aGUgcG9ydCB0aGF0IHRoZSBtb25nb2QgaXMgbGlzdGVuaW5nIG9uLgogICAgIiIiCiMgU2V0IHVwIG91ciBwYXJhbWV0ZXJzLgogICAgY29ubmVjdGlvbiA9IENvbm5lY3Rpb24oaG9zdD0ibW9uZ29kYjovLyIgKyBob3N0bmFtZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcG9ydD1wb3J0LCBzYWZlPVRydWUpCiAgICBkYl9uYW1lID0gJ3Rlc3QnCiAgICBjb2xsZWN0aW9uX25hbWUgPSAnbW1zX2h3X2NoXzUnCiAgICBleGFtcGxlX2RvYyA9IHsnYSc6IDF9CiAgICBkYl9wcmVleGlzdGVkID0gZGJfbmFtZSBpbiBjb25uZWN0aW9uLmRhdGFiYXNlX25hbWVzKCkKICAgIGRiID0gY29ubmVjdGlvbltkYl9uYW1lXQogICAgY29sbF9wcmVleGlzdGVkID0gY29sbGVjdGlvbl9uYW1lIGluIGRiLmNvbGxlY3Rpb25fbmFtZXMoKQogICAgY29sbGVjdGlvbiA9IGRiW2NvbGxlY3Rpb25fbmFtZV0KICAgIGNvbGxlY3Rpb24uaW5zZXJ0KGV4YW1wbGVfZG9jKQogICAgc3RhcnRfdGltZSA9IGRhdGV0aW1lLm5vdygpCiAgICBtYXhfdGltZSA9IHRpbWVkZWx0YSgwLCAxMjAwKSAgIyAyMCBtaW51dGVzCgojIEFuZCBmaW5hbGx5LCBydW4gb3VyIGxvb3AgZm9yIDIwIG1pbnV0ZXMuCiAgICB3aGlsZSBkYXRldGltZS5ub3coKSAtIHN0YXJ0X3RpbWUgPCBtYXhfdGltZToKICAgICAgICBjb2xsZWN0aW9uLnVwZGF0ZShleGFtcGxlX2RvYywgeydhJzogMX0pCiAgICAgICAgc2xlZXAoMC4yNSkKCiMgTm93IGNsZWFuIHVwIHdoYXQgd2UndmUgY3JlYXRlZC4KICAgIGlmIG5vdCBkYl9wcmVleGlzdGVkOgogICAgICAgIGNvbm5lY3Rpb24uZHJvcF9kYXRhYmFzZShkYl9uYW1lKQogICAgZWxpZiBub3QgY29sbF9wcmVleGlzdGVkOgogICAgICAgIGNvbGxlY3Rpb24uZHJvcCgpCiAgICBlbHNlOgogICAgICAgIGNvbGxlY3Rpb24ucmVtb3ZlKGV4YW1wbGVfZG9jKQo="

eval(compile(base64.b64decode(code), "<string>", 'exec'))

create_load(hostname=hostname, port=port)
