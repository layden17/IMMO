[Back](../README.md)

# Application Architecture

**Frontend**

*Technology:* React

*Role:* Provide the user interface.

*Dockerfile:*
* Use a Node.js image for the build process.
* Copy static files (CSS, JS, etc.).

**Backend**

*Technology:* Node.js (Express)

*Role:* REST API for business functionalities (product, order, and user management).

*Dockerfile:*
* Use an appropriate image for the backend.
* Include dependencies.
* Expose a port for API calls.

**Database**

*Technology:* MongoDB

*Role:* Store data such as products, users, orders, etc.

*Configuration:*
* A volume for data persistence.
* Environment variables for configuration (username, password, etc.).

**CI/CD**

* Integration with GitLab CI to automate container builds and deployments.
