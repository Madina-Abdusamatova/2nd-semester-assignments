from dataclasses import dataclass, field
@dataclass
class Employee:
    name: str
    emp_id: str
    shifts_worked: int = 0
    ratings: list = field(default_factory = list)

    def log_shift(self, rating: int):
        self.shifts_worked +=1
        self.ratings.append(rating)

    def avg_rating(self)->float:
        if self.ratings == []:
            return 0.0
        else:
            return sum(self.ratings)/len(self.ratings)
        
@dataclass
class Department:
    dept_name: str
    manager: str
    headcount: int
    employees: list = field(default_factory = list)
    staff_count: int = field(init = False, default = 0)

    def __post_init__(self):
        self._refresh()

    def _refresh(self):
        self.staff_count = len(self.employees)

    def hire(self, employee: Employee) -> bool:
        if self.staff_count < self.headcount:
            self.employees.append(employee)
            self._refresh()
            return True
        return False
    
    def star_employee(self) -> str:
        if len(self.employees) == 0:
            return "No data"
        star_employee = self.employees[0]
        for employee in self.employees:
            if employee.avg_rating() > star_employee.avg_rating():
                star_employee = employee
        return star_employee.name


    def dept_stats(self) -> str:
        lines = [f"{self.dept_name} ({self.manager}):"]
        for employee in self.employees:
            lines.append(f"  {employee.name} - {employee.shifts_worked} shifts, avg {employee.avg_rating():.1f} rating")
        lines.append(f"Staff: {self.staff_count}/{self.headcount}")
        return "\n".join(lines)
    
e1 = Employee("Maya", "E201")
e2 = Employee("Ryan", "E202")
e3 = Employee("Zara", "E203")

e1.log_shift(4)
e1.log_shift(5)
e1.log_shift(3)
e2.log_shift(5)
e2.log_shift(5)
e3.log_shift(2)

d = Department("Engineering", "Dr. Patel", 3)
print(d.hire(e1))
print(d.hire(e2))
print(d.hire(e3))
print(d.hire(Employee("Leo", "E204")))
print(d.staff_count)
print(d.star_employee())
print(d.dept_stats())
