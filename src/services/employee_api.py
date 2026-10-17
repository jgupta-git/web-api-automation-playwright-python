from playwright.sync_api import APIRequestContext

BASE_URL = (
    "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees"
)


class EmployeeApi:
    def __init__(self, request: APIRequestContext):
        self.request = request

    def create_employee(
        self, first_name: str, last_name: str, employee_id: str, middle_name: str = ""
    ) -> dict:
        response = self.request.post(
            BASE_URL,
            data={
                "firstName": first_name,
                "middleName": middle_name,
                "lastName": last_name,
                "empPicture": None,
                "employeeId": employee_id,
            },
        )
        assert response.ok, f"POST employee failed: {response.status} {response.text()}"
        return response.json()["data"]
