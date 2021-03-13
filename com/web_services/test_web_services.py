import sys
import unittest
import requests


class TestRequests(unittest.TestCase):
    def test_request01(self):

        try:

            response = requests.get("http://127.0.0.1:5000")

            html = response.text
            print(html)

        finally:
            # and shutdown the server
            print("En finally1")

    def test_request02(self):

        try:
            payload = {'user': 'anabel', 'email': 'anabel@gmail.edu'}
            response = requests.post("http://127.0.0.1:5000/users", data=payload)

            html = response.text
            print(html)
        except:
            print("Error inesperado:", sys.exc_info()[0])
            raise

        finally:
            # and shutdown the server
            print("En finally2")
