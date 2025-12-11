# Project 6 — OpenShift Security with ServiceAccount + SCC

## 📌 Overview
This project demonstrates how OpenShift secures applications using:
- ServiceAccounts (identity)
- SCC (security rules)
- RoleBinding (permission)
- Secure Pod execution

---

## 🧠 Simple Explanation

ServiceAccount = ID card  
SCC = Security rulebook  
RoleBinding = Permission to use rulebook  
Pod = Worker using assigned ID card  

If a pod uses a ServiceAccount linked to an SCC, the pod must follow all rules in that SCC.

---

## 📂 Files
I created a custom SCC that enforces non-root execution and other restrictions.  
I made a ServiceAccount and bound it to the SCC using RoleBinding.  
A pod using this ServiceAccount automatically follows the SCC rules.  
This shows I understand OpenShift’s advanced security model.”**