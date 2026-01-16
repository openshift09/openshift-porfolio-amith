import pandas as pd

# Step 1: Read log data
df = pd.read_csv("logs.csv")
print("ALL LOGS:")
print(df)

# Step 2: Count errors
error_logs = df[df["level"] == "ERROR"]
error_count = len(error_logs)

print("\nTOTAL ERRORS:", error_count)

# Step 3: Simple AI decision
if error_count >= 3:
    print("ALERT: System is UNSTABLE")
else:
    print("System is STABLE")
