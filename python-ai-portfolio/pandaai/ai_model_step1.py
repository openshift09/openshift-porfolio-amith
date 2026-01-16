import pandas as pd

# Create dataset
data = {
    "experience": [1, 2, 3, 4, 5],
    "salary": [30000, 35000, 40000, 50000, 60000],
    "selected": [0, 0, 1, 1, 1]   # 1 = selected, 0 = rejected
}

df = pd.DataFrame(data)
print(df)

X = df[["experience", "salary"]]   # features
y = df["selected"]                 # label

print(X)
print(y)
