import requests
import pytest

from interviewFrameworkTest.utilities.Baseclass import BaseClass


class TestRestApi(BaseClass):
    @pytest.mark.TestAPI
    def test_api_status_code(self,setUpEndpoint):
        log = self.logger()
        response = setUpEndpoint
        log.info(f"respone is {type(response)} , {response}")
        assert response.status_code == 200

    @pytest.mark.TestAPI
    def test_api_response_keys(self, setUpEndpoint):
        log = self.logger()
        response = setUpEndpoint
        data = response.json()
        expected_keys = ["id", "name", "username", "email"]
        print(f"data is {data}")
        resp = False
        for record in data:
            print(f"exec for loop, record = {record}")
            for key in expected_keys:
                assert key in record
                resp = True
            #assert all(key in record for key in expected_keys)
        assert resp