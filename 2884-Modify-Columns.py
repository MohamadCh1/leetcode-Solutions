import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employee = employees
    employee['salary'] = (employees['salary'].apply(lambda x:x*2))
    return employee