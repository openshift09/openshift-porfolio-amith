from collections import defaultdict

# Read cluster logs
with open("cluster_logs.txt", "r") as file:
    logs = file.readlines()

node_failures = defaultdict(int)
node_pods = defaultdict(int)

# Parse logs
for line in logs:
    node, pod, status = line.strip().split()

    node_pods[node] += 1
    if status == "FAIL":
        node_failures[node] += 1

print("CLUSTER HEALTH REPORT\n")

unhealthy_nodes = 0

# Analyze node health
for node in node_pods:
    total = node_pods[node]
    fails = node_failures[node]
    failure_rate = fails / total

    print(node, "- failure rate:", round(failure_rate, 2))

    if failure_rate >= 0.6:
        print("ALERT:", node, "is UNHEALTHY\n")
        unhealthy_nodes += 1
    else:
        print("STATUS:", node, "is HEALTHY\n")

# Cluster decision
if unhealthy_nodes >= 2:
    print("CLUSTER STATUS: 🚨 DEGRADED")
else:
    print("CLUSTER STATUS: ✅ HEALTHY")
