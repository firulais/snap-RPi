#!/usr/bin/python

"""
Snap! extension to support Raspberry Pi -- server component.
Copyright (C) 2014  Paul C. Brown <p_brown@gmx.com>.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import SimpleHTTPServer
import RPi.GPIO as GPIO

def pinState(pin, state):
    
    GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    if(GPIO.input(pin) == state):
        print "Button pressed"
        return True
                
    return False


class CORSHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def send_head(self):
	path = self.path
        # path looks like this: /pinwrite?pin=1&state=LOW

	GPIO.setmode(GPIO.BCM)                                                                                                                                                                                                      
	
	ospath = os.path.abspath('')
	if 'pinwrite' in path: # write HIGH or LOW to pin
		regex = re.compile(".*pin=([0-9]*).*state=(LOW|HIGH)")
		m = regex.match(path)
		
		pin = int(m.group(1))
		state = True
		if m.group(2) == 'LOW':
			state = False

		GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, state)
                
        elif 'pinread'in path: # read state of pin
                regex = re.compile(".*pin=([0-9]*).*state=(LOW|HIGH)")
                m = regex.match(path)
                
                pin = int(m.group(1))
                state = 0
                if m.group(2) == 'HIGH':
                        state = 1
                
                f = open(ospath + '/return', 'w+')
                f.write(str(pinState(pin, state)))
                f.close()
                f = open(ospath + '/return', 'rb')
                ctype = self.guess_type(ospath + '/rpireturn')
                self.send_response(200)
                self.send_header("Content-type", ctype)
                fs = os.fstat(f.fileno())
                self.send_header("Content-Length", str(fs[6]))
                self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                return f
 

if __name__ == "__main__":
    import os
    import re
    import SocketServer
    import urllib2
    PORT = 8280 #R+P in ASCII Decimal
    Handler = CORSHTTPRequestHandler
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    print "Go ahead and launch Snap!"
    httpd.serve_forever()


