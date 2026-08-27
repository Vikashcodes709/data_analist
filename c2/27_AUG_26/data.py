import pandas as pd

data = {
    'Name': ['Mahesh', 'Paani', 'Ramesh'],
    'Age': [25, 30, 35],
    'City': ['Mumbai', 'Banaras', 'Delhi'],
    'pincode': [221101, 221005, 221102],
    'Department': ['IT', 'CSE', 'Accounts'],
    'Skills': ['Python', 'Java', 'Data Analysis']
}

dept = pd.DataFrame(data)

print(dept)
