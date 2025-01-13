[Back](../README.md)

## Pipeline Diagram

Below is a detailed representation of the CI/CD pipeline flow:

```plaintext
       +--------------------+
       |    Pre-install     |
       |   (pre_install)    |
       +--------------------+
                 |
                 v
       +--------------------+
       |       Build        |
       |    (build_front)   |
       +--------------------+
                 |
                 v
       +--------------------+
       |      Testing       |
       |   (test_backend)   |
       +--------------------+
                 |
                 v
       +--------------------------+
       |        Deployment        |
       |                          |
       |  +--------------------+  |
       |  | Docker Deployment  |  |
       |  +--------------------+  |
       |                          |
       +--------------------------+