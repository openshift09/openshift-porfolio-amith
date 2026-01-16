import pandas as pd
from sklearn.linear_model import LogisticRegression

# Step 1: Create data (like an Excel table)
data = {
    "experience": [1, 2, 3, 4, 5],
    "salary": [30000, 35000, 40000, 50000, 60000],
    "selected": [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print("DATA TABLE:")
print(df)

# Step 2: Separate input and output
X = df[["experience", "salary"]]
y = df["selected"]

# Step 3: Train AI model
model = LogisticRegression()
model.fit(X, y)

print("\nAI MODEL TRAINED")

# Step 4: Ask AI a question
prediction = model.predict([[3, 45000]])
print("\nPrediction for experience=3, salary=45000:")
print("Selected (1 = Yes, 0 = No):", prediction[0])



from sklearn.model_selection import train_test_split

# Split data: 80% learning, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Train AI again using training data
model.fit(X_train, y_train)

# Test AI using test data
accuracy = model.score(X_test, y_test)

print("\nAI Accuracy:", accuracy)

