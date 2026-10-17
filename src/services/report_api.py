from playwright.sync_api import APIRequestContext

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/reports"


class ReportApi:
    def __init__(self, request: APIRequestContext):
        self.request = request

    def get_defined_report(self, report_id: int) -> dict:
        response = self.request.get(f"{BASE_URL}/defined/{report_id}")
        assert response.ok, f"GET defined report {report_id} failed: {response.status}"
        return response.json()["data"]

    def get_report_data(self, report_id: int, limit: int = 50, offset: int = 0) -> list:
        response = self.request.get(
            f"{BASE_URL}/data",
            params={
                "limit": limit,
                "offset": offset,
                "reportId": report_id,
                "name": "pim_defined",
                "_dateFormattingEnabled": "true",
            },
        )
        assert response.ok, f"GET report data {report_id} failed: {response.status}"
        return response.json()["data"]
