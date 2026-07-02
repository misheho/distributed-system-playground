# distributed-system-playground

Centralized API gateway providing routing, authentication, rate limiting, and request/response transformation for our microservices ecosystem.

Parent repository for a self-study of distributed architecture used to learn implementation of an API-gateway, principles of Spring Boot application development, python application development, dockerization and other features. 

---

## 🚀 Features

- **Spring Boot App** — simple java app used to learn different principles of API development and integration with PostGRE DB
- **Spring Cloud API Gateway** — routes requests to the Spring Boot App and the python app; to be used for concurrency implementation learning

---

## 📋 Prerequisites

Ensure the following are installed before building:

| Requirement | Minimum Version | Install Guide |
|-------------|-----------------|---------------|
| Java JDK | 21+ | [OpenJDK Downloads](https://openjdk.org/) |
| Maven | 3.8+ | [Apache Maven](https://maven.apache.org/) |
| Docker | 20+ (for containerized deploy) | [Docker Hub](https://www.docker.com/) |
| PostgreSQL | 14+ (backend database) | Optional, for auth module |

---

## 🔧 Quick Start

### Local Development

```bash
# Clone repository
git clone https://github.com/org/api-gateway.git
cd api-gateway

# Build
mvn clean package -DskipTests

# Run
java -jar target/api-gateway-1.0.0.jar

# Or via IDE (run ApiGatewayApplication.main())