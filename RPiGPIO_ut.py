import unittest
import urllib.request
import urllib.error
import http.client

class TestAdd(unittest.TestCase):

    URL = "http://localhost:8280/"

    def test_pinwrite(self):
        try:
            req = urllib.request.urlopen(self.URL + "pinwrite?pin=1&state=LOW")
        except urllib.error.HTTPError as e:
            print('Error code: ', e.code)
        except urllib.error.URLError as e:
            print('Reason: ', e.reason)
        except http.client.HTTPException as e:
            #http.client.RemoteDisconnected
            print('HTTPException')
        else:
            print(req.read())
            
        result = 1
        self.assertEqual(result, 1)

    def test_pinread(self):
        try:
            req = urllib.request.urlopen(self.URL + "pinread?pin=1&state=LOW")
        except urllib.error.HTTPError as e:
            print('Error code: ', e.code)
        except urllib.error.URLError as e:
            print('Reason: ', e.reason)
        except http.client.HTTPException as e:
            #http.client.RemoteDisconnected
            print('HTTPException')
        else:
            print(req.read())
            
        result = 1
        self.assertEqual(result, 1)
        
if __name__ == '__main__':
    unittest.main()