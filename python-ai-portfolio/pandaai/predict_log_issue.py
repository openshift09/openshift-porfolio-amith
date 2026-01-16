import pandas as pd

# Step 1: Read logs
df = pd.read_csv("logs.csv")
print("LOG DATA:")
print(df)

# Step 2: Count errors so far
errors = df[df["level"] == "ERROR"]
error_count = len(errors)

# Step 3: Check recent errors (last 3 entries)
recent_logs = df.tail(3)
recent_errors = recent_logs[recent_logs["level"] == "ERROR"]

print("\nTotal Errors:", error_count)
print("Recent Errors:", len(recent_errors))

# Step 4: Prediction logic
if len(recent_errors) >= 2:
    print("PREDICTION: System likely to FAIL soon")
else:
    print("PREDICTION: System looks STABLE")
