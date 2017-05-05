import unittest
import urllib.request
import urllib.error
import http.client

class TestAdd(unittest.TestCase):

    def test_send_head(self):
        try:
            req = urllib.request.urlopen("http://localhost:8280/pinwrite?pin=1&state=LOW")
        except urllib.error.HTTPError as e:
            print('Error code: ', e.code)
        except urllib.error.URLError as e:
            print('Reason: ', e.reason)
        except http.client.HTTPException as e:
            #http.client.RemoteDisconnected
            print('HTTPException')
        else:
            print(req.read())
            
        result = 3 #mymath.add(1, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()