import pandas as pd; print(pd.__file__); print(pd.__version__)



data = {
    'Name': ['Mahesh', 'Paani', 'Ramesh'],
    'Age': [25, 30, 35],
    'City': ['Mumbai', 'Banaras', 'Delhi'],
    'Pincode': [221101, 221005, 221102],
    'Department': ['IT', 'CSE', 'Accounts'],
    'Skills': ['Python', 'Java', 'Data Analysis']
}

dept = pd.DataFrame(data)
print(pd.__file__)

#print(dept)
print(dept.tail(2))
