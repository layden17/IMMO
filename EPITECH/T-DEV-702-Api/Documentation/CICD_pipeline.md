[Back](../README.md)

# CI/CD Pipeline Documentation

## Overview

This repository contains the documentation for the CI/CD pipeline implemented for the project. The pipeline is designed to automate building, testing, and deploying processes, ensuring continuous integration and delivery with minimal manual intervention.

---

## Pipeline Stages

### 1. Pre-installation (`start: pre_install`)
This initial step sets up all required dependencies and configurations before proceeding to subsequent stages.

**Tasks performed:**
- Validate configuration files.
- Install necessary dependencies.
- Prepare environment variables.

---

### 2. Build (`build: build_front`)
This stage compiles and prepares the frontend application for deployment.

**Tasks performed:**
- Compile frontend assets (JavaScript, CSS).
- Minify files for production readiness.
- Validate the integrity of the build artifacts.

---

### 3. Testing (`test: test_backend`)
This stage ensures the reliability and quality of the backend through automated tests.

**Tasks performed:**
- Execute backend unit tests.
- Verify test coverage (minimum 20% coverage required).
- Identify and log any regressions or bugs.

---

### 4. Deployment (`deploy: deploy_docker`)
Handles the deployment of containerized environments.

**Tasks performed:**
- Build Docker images for dev and prod environments.
- Push images to a container registry.
- Deploy containers to the designated infrastructure.

Uses :
```bash
docker-compose stop
docker-compose build
docker-compose up
```

to respectively :
- stop the old docker-compose instance,
- build a new one
- start the newly built instance

---
