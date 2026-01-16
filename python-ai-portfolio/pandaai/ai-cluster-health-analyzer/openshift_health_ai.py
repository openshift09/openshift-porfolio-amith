from collections import defaultdict

# --- Read node status ---
with open("oc_nodes.txt") as f:
    node_lines = f.readlines()

node_status = {}
for line in node_lines:
    node, status = line.strip().split()
    node_status[node] = status

# --- Read pod status ---
with open("oc_pods.txt") as f:
    pod_lines = f.readlines()

pod_failures = defaultdict(int)
pod_total = defaultdict(int)

for line in pod_lines:
    node, pod, status = line.strip().split()
    pod_total[node] += 1
    if status != "Running":
        pod_failures[node] += 1

print("\nOPENSHIFT CLUSTER HEALTH REPORT\n")

unhealthy_nodes = 0

for node in node_status:
    total = pod_total[node]
    fails = pod_failures[node]

    failure_rate = fails / total if total > 0 else 0

    print(f"{node}: status={node_status[node]}, pod failure rate={round(failure_rate,2)}")

    if node_status[node] != "Ready" or failure_rate >= 0.5:
        print(f"ALERT: {node} is UNHEALTHY\n")
        unhealthy_nodes += 1
    else:
        print(f"STATUS: {node} is HEALTHY\n")

# --- Final cluster decision ---
if unhealthy_nodes >= 2:
    print("CLUSTER STATUS: 🚨 DEGRADED")
else:
    print("CLUSTER STATUS: ✅ HEALTHY")
