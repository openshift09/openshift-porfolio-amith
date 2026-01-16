import pandas as pd

data = {
    "name": ["Amit", "Ravi", "Neha"],
    "age": [30, 28, 26],
    "salary": [50000, 45000, 40000]
}

df = pd.DataFrame(data)
print(df)
