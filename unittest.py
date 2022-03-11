import unittest
from flask import current_app

def test_registration_form(self):
        response = self.client.get('/ratemybronco/register')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        # make sure all the fields are included
        assert 'name="username"' in html
        assert 'name="email"' in html
        assert 'name="password"' in html
        assert 'name="submit"' in html