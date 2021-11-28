#!/usr/bin/env python3

from mpd import MPDClient
client = MPDClient()               # create client object
client.timeout = 10                # network timeout in seconds (floats allowed), default: None
client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
client.connect("localhost", 6600)  # connect to localhost:6600
print(client.mpd_version)          # print the MPD version
print(client.find("any", "house")) # print result of the command "find any house"
print(client.status())
client.idle()
print(client.status())

print(client.currentsong())
client.close()                     # send the close command
client.disconnect()                # disconnect from the server