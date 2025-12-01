from employee import employee_info

def test_employee_info():
    result = employee_info("Alice", "A123", "HR", 45000)
    
    expected = (
        "Employee Name: Alice\n"
        "Employee ID: A123\n"
        "Department: HR\n"
        "Salary: 45000"
    )

    assert result == expected
