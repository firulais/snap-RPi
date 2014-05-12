#Snap! extension base by PCB
import SimpleHTTPServer
import RPi.GPIO as GPIO

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
                f = open(ospath + '/rpireturn', 'w+')
                f.write(str(t.get_sample()))
                f.close()
                f = open(ospath + '/rpireturn', 'rb')
                ctype = self.guess_type(ospath + '/pireturn')
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


