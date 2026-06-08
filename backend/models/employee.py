from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    id: Optional[int] = None
    employee_code: str
    first_name: str
    last_name: str
    thai_name: Optional[str] = ""
    department: str
    position: str
    level: str
    hire_date: str
    birth_date: Optional[str] = ""
    email: str
    phone: str
    address: Optional[str] = ""
    bank_account: Optional[str] = ""
    bank_name: Optional[str] = ""
    salary: Optional[float] = 0
    status: str = "active"
    resign_date: Optional[str] = ""
    created_at: Optional[str] = ""

class EmployeeCreate(BaseModel):
    employee_code: str
    first_name: str
    last_name: str
    thai_name: Optional[str] = ""
    department: str
    position: str
    level: str
    hire_date: str
    birth_date: Optional[str] = ""
    email: str
    phone: str
    address: Optional[str] = ""
    bank_account: Optional[str] = ""
    bank_name: Optional[str] = ""
    salary: Optional[float] = 0

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    thai_name: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    level: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    salary: Optional[float] = None
    status: Optional[str] = None