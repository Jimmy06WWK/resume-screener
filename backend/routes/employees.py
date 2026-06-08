# backend/routes/employees.py
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from backend.models.employee import Employee, EmployeeCreate, EmployeeUpdate
from backend.utils.database import get_all_employees, get_employee_by_id, create_employee, update_employee, delete_employee

router = APIRouter()

@router.get("/employees", response_model=List[Employee])
async def list_employees(status: str = "active"):
    return get_all_employees(status)

@router.get("/employees/{emp_id}", response_model=Employee)
async def get_employee(emp_id: int):
    emp = get_employee_by_id(emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.post("/employees", response_model=dict)
async def add_employee(employee: EmployeeCreate):
    emp_id = create_employee(employee.dict())
    return {"success": True, "id": emp_id, "message": "Employee created successfully"}

@router.put("/employees/{emp_id}")
async def edit_employee(emp_id: int, employee: EmployeeUpdate):
    existing = get_employee_by_id(emp_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Employee not found")
    update_data = employee.dict(exclude_none=True)
    update_employee(emp_id, update_data)
    return {"success": True, "message": "Employee updated successfully"}

@router.delete("/employees/{emp_id}")
async def remove_employee(emp_id: int):
    existing = get_employee_by_id(emp_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Employee not found")
    delete_employee(emp_id)
    return {"success": True, "message": "Employee deleted successfully"}