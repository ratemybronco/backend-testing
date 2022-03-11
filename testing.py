from unicodedata import name
from flask.testing import FlaskClient
import main

def test_landing():
    print("Testing the landing page loader: ")
    # send a request to backend and see if the returning code is 200
    with app.test_client() as route:
        response = route.get('/')
        if self.assertEquals(response.status_code, 200) : print("Passed.")
        print(response)

    



if __name__ == "__main__":
    test_landing()