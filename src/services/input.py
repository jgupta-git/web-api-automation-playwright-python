from dataclasses import dataclass


@dataclass(frozen=True)
class TestUser:
    """Test user credentials"""
    username: str
    password: str


@dataclass
class EmployeeData:
    first_name: str
    last_name: str
    username: str
    password: str
    id: str


class TestData:
    VALID_USER = TestUser(username="Admin", password="admin123")
    INVALID_USER = TestUser(username="Admin", password="admin123*")

    EMPLOYEE_DATA = EmployeeData(
        first_name="John",
        last_name="Doe",
        username="johndoe",
        password="password123",
        id="12345",
    )

    @classmethod
    def initialize_employee_data(cls, random_id: int) -> None:
        id_ = str(random_id)
        cls.EMPLOYEE_DATA = EmployeeData(
            first_name=f"John{id_}",
            last_name=f"Doe{id_}",
            username=f"johndoe{id_}",
            password="password123",
            id=id_,
        )