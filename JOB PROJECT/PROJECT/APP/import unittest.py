import unittest
from fastapi.testclient import TestClient
from main import app

class TestMain(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_get_user_raw_query(self):
        response = self.client.get("/GET_DEV/RAW_QUERY/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_user_orm(self):
        response = self.client.get("/GET_DEV/DRM/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_user(self):
        data = {"USERNAME": "test_user", "PASSWORD": "test_password"}
        response = self.client.post("/GET_DEV/CREATE/", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_create_emp(self):
        data = {"EMPNAME": "test_emp", "EMPPASSWORD": "test_emp_password"}
        response = self.client.post("/GET_DEV/CREATE_EMP/", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_delete_user(self):
        response = self.client.delete("/GET_DEV/DELETE/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "User deleted successfully"})

    def test_delete_emp(self):
        response = self.client.delete("/GET_DEV/DELETE_EMP/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Employee deleted successfully"})

    def test_update_user(self):
        data = {"USERNAME": "updated_user", "PASSWORD": "updated_password"}
        response = self.client.put("/GET_DEV/UPDATE/1", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_update_emp(self):
        data = {"EMPNAME": "updated_emp", "EMPPASSWORD": "updated_emp_password"}
        response = self.client.put("/GET_DEV/UPDATE_EMP/1", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
