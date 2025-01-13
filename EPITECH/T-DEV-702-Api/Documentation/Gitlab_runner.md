[Back](../README.md)

# Connecting the GitLab Runner to the GitLab Server

This document outlines the steps to connect a GitLab Runner to a GitLab server, including configuration details and the registration process.

---

## 1. GitLab Server Information

### Server URL and Port
- **GitLab Server URL**: `https://t-dev.epitest.eu`
- **Default Port**: 443 (used for HTTPS)
- If your GitLab server uses a custom port, ensure that the runner is configured to communicate over the correct port.

---

## 2. Supported Protocols
- **HTTPS (recommended)**:
  - Ensures secure communication between the runner and the server.
  - Verify that the SSL certificate for your GitLab server is valid.
- **HTTP (not recommended)**:
  - May be used for local or non-production servers but is insecure for public deployments.

---

## 3. Prerequisites
Before proceeding, ensure:
1. **GitLab Runner is installed**: Follow the installation guide for your operating system.
2. **Registration Token is available**:
   - Go to your GitLab project.
   - Navigate to **Settings > CI/CD > Runners**.
   - Copy the **registration token**.

---

## 4. Registering the GitLab Runner
Use the following command to register your runner with the GitLab server:
```bash
gitlab-runner register --url https://t-dev.epitest.eu --token <YOUR_TOKEN>
```

## 5. Running the Gitlab Runner
If no gitlab runner is connected to your repository, the pipeline won't be able to run.

```bash
gitlab-runner run
```