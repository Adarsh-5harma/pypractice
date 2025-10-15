from dataclasses import dataclass

@dataclass
class HourlyEmployees:
    # Employee that are paid based on number of hours worked
    name: str
    id: int
    hourly_rate: float = 0.0
    hours_worked: float = 0.0
    commission_rate: float = 100.0
    commission_landed: float = 0.0
    employer_fixed_cost: float = 1000.0

    def calculate_pay(self) -> float:
        # Calculate the total pay for the employee
        return (
            self.hourly_rate * self.hours_worked +
            self.commission_rate * self.commission_landed +
            self.employer_fixed_cost
        )


@dataclass
class SalariedEmployees:
    # Employee that are paid a fixed salary
    name: str
    id: int
    monthly_salary: float = 0.0
    commission_rate: float = 100.0
    commission_landed: float = 0.0
    percentage: float = 1.0

    def calculate_pay(self) -> float:
        # Calculate the total pay for the employee
        return (
            self.monthly_salary * self.percentage +
            self.commission_rate * self.commission_landed
        )


@dataclass
class Freelancer:
    # Employee that are paid based on deliverables
    name: str
    id: int
    hours_worked: int = 0
    hourly_rate: float = 0.0
    commission_rate: float = 100.0
    commission_landed: float = 0.0
    vat_number: str = ""

    def calculate_pay(self) -> float:
        # Calculate the total pay for the employee
        return (
            self.hourly_rate * self.hours_worked +
            self.commission_rate * self.commission_landed
        )


hourly_obj = HourlyEmployees(name="Adarsh", id=1, hourly_rate=50.0, hours_worked=160, commission_landed=3)
print(f"Adarsh's Pay: {hourly_obj.calculate_pay()}")

salary_obj = SalariedEmployees(name="Sid", id=2, monthly_salary=5000.0, commission_landed=5, percentage=1.0)
print(f"Sid's Pay: {salary_obj.calculate_pay()}")

freelance_obj = Freelancer(name="Suyog", id=3, hourly_rate=70.0, hours_worked=120, commission_landed=2, vat_number="VAT12345")
print(f"Suyog's Pay: {freelance_obj.calculate_pay()}")
