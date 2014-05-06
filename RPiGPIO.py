#Snap! extension base by PCB
import SimpleHTTPServer
import RPi.GPIO as GPIO

class CORSHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def send_head(self):
	path = self.path
        # path looks like this: /pinwrite?pin=1&state=LOW

	GPIO.setmode(GPIO.BCM)                                                                                                                                                                                                      
	
	ospath = os.path.abspath('')
	if 'pinwrite' in path:
		regex = re.compile(".*pin=([0-9]*).*state=(LOW|HIGH)")
		m = regex.match(path)
		
		pin = int(m.group(1))
		state = True
		if m.group(2) == 'LOW':
			state = False

		GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, state)


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


