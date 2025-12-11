# Project 7 — OpenShift Health Checks (Beginner Friendly)

## 📌 Overview
This project demonstrates how OpenShift uses:
- Liveness Probes
- Readiness Probes

to keep applications healthy and automatically restart them when needed.

---

## 🧠 Concept (Simple Explanation)

Liveness Probe = “Is the app alive?”  
→ If not, OpenShift restarts the container.

Readiness Probe = “Is the app ready to serve traffic?”  
→ If not, OpenShift avoids sending customers to it.

---

## 📂 Files

Liveness Probe = “Is the app alive?”  
→ If not, OpenShift restarts the container.

Readiness Probe = “Is the app ready to serve traffic?”  
→ If not, OpenShift avoids sending customers to it.

**“I implemented both liveness and readiness probes.  
Liveness ensures the container is restarted if it becomes unhealthy.  
Readiness ensures the pod does not receive traffic until it's ready.  
This demonstrates how OpenShift maintains reliability automatically.”**