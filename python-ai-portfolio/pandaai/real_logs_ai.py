import pandas as pd

# Step 1: Read raw log file
with open("real_logs.txt", "r") as file:
    lines = file.readlines()

# Step 2: Convert logs into structured data
levels = []
messages = []

for line in lines:
    parts = line.strip().split(" ", 1)
    levels.append(parts[0])
    messages.append(parts[1])

# Step 3: Create a table (DataFrame)
df = pd.DataFrame({
    "level": levels,
    "message": messages
})

print("STRUCTURED LOG DATA:")
print(df)

# Step 4: Simple AI-style decision
error_count = len(df[df["level"] == "ERROR"])

print("\nTotal Errors:", error_count)

if error_count >= 3:
    print("AI DECISION: SYSTEM AT RISK")
else:
    print("AI DECISION: SYSTEM LOOKS OK")
