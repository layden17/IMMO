[Back](../README.md)

# Development and production environments

Development and production environments are configured differently. The development environment is designed for testing and building, while the production environment ensures a reliable and secure user experience.

*Development Environment:*

* Configured to facilitate debugging and rapid development.
* Includes detailed logs, error tracking tools, and debugging extensions.
* Uses fictitious or anonymized data to prevent any risk to sensitive information.

*Production Environment:*

* Optimized for stability, performance, and security.
* Disables debugging tools and limits logs to protect sensitive data.
* Implements strict configurations, such as using environment variables for API keys and sensitive credentials.

### Differences between dev and prod

#### Dev ports
- Front : 3000
- Back : 5001
- DB : 27017

#### Prod ports
- Front : 3003
- Back : 5000
- DB : 27017
