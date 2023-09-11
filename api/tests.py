#!
import requests

# Create your tests here.


class TestPersonCRUD:
    base_url = "http://localhost:8000/api"

    def _call(self, method, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = method(url, json=data)
        return response

    def test_create_person(self, data):
        response = self._call(requests.post, "", data)
        if response.status_code == 201:
            print("Create Person Test Passed✅", "\n")
            return response.json().get("id")
        else:
            print(response.json())
            print("Create Person Test Failed❌")

    def test_get_person(self, person_id):
        response = self._call(requests.get, person_id)
        if response.status_code == 200:
            print("Get Person Test Passed✅")
            print("Response Data:", response.json(), "\n")
        else:
            print("Get Person Test Failed❌")

    def test_update_person(self, person_id, data):
        response = self._call(requests.put, person_id, data)
        if response.status_code == 200:
            print("Update Person Test Passed✅")
            print("Response Data:", response.json(), "\n")
        else:
            print("Update Person Test Failed❌")

    def test_delete_person(self, person_id):
        response = self._call(requests.delete, person_id)
        if response.status_code == 204:
            print("Delete Person Test Passed✅")
        else:
            print("Delete Person Test Failed❌")


if __name__ == "__main__":
    test = TestPersonCRUD()
    person_id = test.test_create_person({"name": "John Doe"})
    test.test_get_person(person_id)
    test.test_update_person(person_id, {"name": "John Doe Jr"})
    test.test_delete_person(person_id)
