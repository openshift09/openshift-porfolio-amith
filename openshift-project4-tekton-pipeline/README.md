# Project 4 — Tekton Pipeline (Beginner Friendly Demo)

## 📌 Overview
This project demonstrates a simple Tekton Pipeline on OpenShift using two tasks:
1. Build task  
2. Deploy task  

The purpose is to understand the structure of Tekton in the simplest possible way.

---

## 📂 Files Included
task-build.yaml → Worker 1 (builds)
task-deploy.yaml → Worker 2 (deploys)
pipeline.yaml → Connects workers into a sequence
pipelinerun.yaml → Starts the pipeline

## 💡 Concept (Explained for Beginners)
Tekton works like a factory assembly line:
- Tasks = workers  
- Pipeline = full process  
- PipelineRun = start button  

**“I built a simple Tekton pipeline with two tasks — build and deploy.  
This helped me understand Tekton’s structure: Tasks → Pipeline → PipelineRun.  
This project shows I can work with OpenShift Pipelines in a very clean and2 structured way.”**
