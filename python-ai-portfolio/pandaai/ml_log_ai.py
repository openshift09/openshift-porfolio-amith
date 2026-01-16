import pandas as pd
from sklearn.linear_model import LogisticRegression

# Step 1: Read past log data
df = pd.read_csv("log_training.csv")
print("PAST SYSTEM DATA:")
print(df)

# Step 2: Separate inputs and output
X = df[["errors", "warnings","recent_errors"]]   # what AI looks at
y = df["system_state"]           # final result

# Step 3: Train AI
model = LogisticRegression()
model.fit(X, y)

print("\nAI has learned from past data")

# Step 4: Ask AI a new question
prediction = model.predict([[2, 0]])

print("\nNew Situation:")
print("Errors = 2, Warnings = 0")

if prediction[0] == 1:
    print("AI Prediction: SYSTEM AT RISK")
else:
    print("AI Prediction: SYSTEM SAFE")


from sklearn.model_selection import train_test_split

# Step 5: Split past data into learning and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Step 6: Train AI using learning data
model.fit(X_train, y_train)

# Step 7: Test AI using unseen data
accuracy = model.score(X_test, y_test)

print("\nAI Accuracy:", accuracy)

from sklearn.model_selection import cross_val_score

# Step 8: Test AI multiple times
scores = cross_val_score(model, X, y, cv=3)

print("\nMultiple Test Scores:", scores)
print("Average Accuracy:", scores.mean())

