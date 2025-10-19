# **A Comparative Study Between Relational (SQL) and Non-Relational (NoSQL) Databases in Containerized Environments**

## **1. Introduction**

The ongoing debate between relational (SQL) and non-relational (NoSQL) databases has become increasingly relevant in modern software development, particularly with the rise of containerized and microservice-based architectures. In environments where scalability, flexibility, and data integrity are key factors, the choice of database model can significantly influence both system performance and reliability.

During the *Inception* project at 42 Madrid, an end-to-end infrastructure was deployed using Docker containers, including services such as Nginx, WordPress, and a database system. This setup provided a practical opportunity to observe and compare both paradigms—relational databases (MariaDB) and NoSQL databases (MongoDB)—within the same technical context.

This research project aims to analyze, from both a theoretical and experimental perspective, the differences between SQL and NoSQL databases in containerized environments, focusing on aspects such as data consistency, performance, and suitability for different application contexts.

---

## **2. Problem Statement**

The growing adoption of distributed architectures has demonstrated that there is no universally “better” database model. SQL systems prioritize consistency and integrity, while NoSQL systems emphasize flexibility and horizontal scalability. However, in containerized infrastructures where multiple services interact with shared data, these design trade-offs can directly impact overall system stability and maintainability.

The central research question of this study can be formulated as follows:

> How does the choice between SQL and NoSQL databases affect the balance between consistency, scalability, and maintainability in containerized environments?
> 

---

## **3. Objectives**

### **General Objective**

To conduct a comparative analysis of relational (MariaDB) and non-relational (MongoDB) databases within a Docker-based containerized environment, evaluating their behavior, consistency, and scalability to determine their suitability for different project contexts.

### **Specific Objectives**

1. Evaluate **data integrity and consistency** across both models under concurrent transactions.
2. Measure the **ease of deployment, administration, and orchestration** using Docker.
3. Analyze the **complexity of managing relationships** and dependencies between data entities.
4. Identify **optimal usage scenarios** for each paradigm depending on data type and structure.
5. Develop a **decision framework** to guide database migration and selection between SQL and NoSQL systems.

---

## **4. Hypotheses**

- **H1:** In containerized systems with multiple interdependent services, relational databases such as MariaDB provide higher consistency and reliability without requiring additional application-level logic.
- **H2:** NoSQL databases such as MongoDB achieve better horizontal scalability and performance with heterogeneous or unstructured data, but at the cost of transactional integrity.
- **H3:** The optimal choice of database model depends more on **contextual factors** (data structure, workload type, and business criticality) than on raw performance benchmarks.

---

## **5. Theoretical Framework**

### **5.1. Relational Databases (SQL)**

First introduced by Edgar F. Codd in 1970, the relational model organizes data into tables connected by primary and foreign keys. Relational databases are characterized by their adherence to ACID properties—Atomicity, Consistency, Isolation, and Durability—which ensure reliable transactions even in distributed systems. Within containerized environments, databases such as MariaDB and PostgreSQL can be deployed using persistent volumes and network bridges, providing reliable inter-container communication and data persistence.

### **5.2. Non-Relational Databases (NoSQL)**

Emerging in the 2000s with systems such as MongoDB, Cassandra, and Redis, NoSQL databases depart from rigid schema definitions, embracing document, key-value, or graph-based data models. They favor flexibility and horizontal scalability through mechanisms like *sharding* and replication. However, they often follow the BASE model (*Basically Available, Soft state, Eventually consistent*), trading strict consistency for performance and availability.

### **5.3. Containerization and Microservices**

Containerization technologies such as Docker isolate services, allowing them to run independently while sharing resources efficiently. Orchestration tools like Docker Compose or Kubernetes simplify the deployment and scaling of such services. Nevertheless, the distributed nature of containerized architectures poses challenges for maintaining data integrity—especially when using NoSQL systems that lack built-in transactional mechanisms.

---

## **6. Methodology**

The research will be conducted in two main phases:

### **Phase 1: Experimental Implementation**

- **Environment:** A Docker Compose setup including three main containers—web server (Nginx), application service (WordPress or Node.js app), and database (MariaDB or MongoDB).
- **Tests:**
    - *Transactional consistency:* Simulate concurrent read/write operations.
    - *Scalability:* Gradually increase concurrent user loads.
    - *Schema flexibility:* Insert unstructured or dynamic data and analyze behavior.
- **Tools:** Apache JMeter for load testing, Docker Stats for performance metrics, and custom Python scripts for data validation.

### **Phase 2: Comparative Analysis**

- Quantitative comparison of performance and resource usage.
- Qualitative evaluation of maintainability and relationship management complexity.
- Creation of decision matrices linking project characteristics with the most suitable database paradigm.

---

## **7. Expected Results**

It is expected that:

- SQL systems will demonstrate superior **data integrity and transactional consistency** in containerized environments with critical service dependencies.
- NoSQL systems will exhibit **better scalability and flexibility** when dealing with large volumes of unstructured or rapidly changing data.
- The optimal database choice will ultimately depend on the **specific context and business requirements**, not solely on performance metrics.

---

## **8. Preliminary Conclusions**

Based on the initial experimentation within the *Inception* project, relational databases appear to remain the most appropriate option for systems that demand strong consistency and reliability—such as user management, configurations, payment processing, or inventory systems.

Conversely, NoSQL databases such as MongoDB are highly advantageous for analytical workloads, real-time dashboards, and monitoring systems where data is highly dynamic and horizontal scaling is essential.

---

## **9. Suggested References**

- Codd, E. F. (1970). *A Relational Model of Data for Large Shared Data Banks.* Communications of the ACM.
- Brewer, E. (2012). *CAP Twelve Years Later: How the “Rules” Have Changed.* IEEE Computer.
- Fowler, M. (2012). *NoSQL Distilled: A Brief Guide to the Emerging World of Polyglot Persistence.* Addison-Wesley.
- MongoDB Inc. (2024). *MongoDB Manual.*
- MariaDB Foundation. (2024). *MariaDB Server Documentation.*