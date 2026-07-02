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

From the repository root, use Docker Compose to build and run the services together:

```bash
# Start all services from workspace root
docker compose up -d --build
```

To stop and remove the containers:

```bash
docker compose down
```

> Note: this uses the root-level `docker-compose.yml` in the repository root. Run the compose commands from a shared parent dir containing both services so the service build contexts resolve correctly.

You can still build and run each service manually if you prefer:

```bash
# Clone repository
git clone https://github.com/misheho/distributed-system-playground.git
cd spring-cloud-api-gateway/api-gateway

# Build
mvn clean package -DskipTests

# Run
java -jar target/api-gateway-0.0.1-SNAPSHOT.jar

cd spring-boot-app/spb-app

# Build
mvn clean package -DskipTests

# Run
java -jar target/spb-app-0.0.1-SNAPSHOT.jar

# Or via IDE (run ApiGatewayApplication.main())