# Week 5: Task 5 - Learning
## Introduction to Load Balancing Algorithms

In the previous tasks, you learned how to create backend servers using FastAPI and experienced first-hand how a single server can become a bottleneck when multiple users make requests simultaneously. 

To solve this, modern applications use **Load Balancers**. A load balancer sits in front of your servers and distributes incoming client requests across all available servers capable of fulfilling them. This maximizes speed and capacity utilization and ensures that no single server is overworked, which could degrade performance.

Please go through the following resources in order to understand the intuition behind load balancing and learn about specific algorithms.

### 1. Intuition: 6 Load Balancing Algorithms Every Developer Should Know
Start here for a high-level overview of why load balancers are necessary and the difference between static and dynamic routing algorithms.
* **Video:** [Top 6 Load Balancing Algorithms Every Developer Should Know](https://www.youtube.com/watch?v=dBmxNsS3BGE) 

### 2. Deep Dive: Round Robin Algorithm
Round Robin is the most basic, foundational load-balancing algorithm. It is a static algorithm that distributes requests to servers in a sequential, cyclic order.
* **Video:** [Round Robin Load Balancing Algorithm](https://www.youtube.com/watch?v=VaqHjAcHXZQ)

### 3. Deep Dive: Least Connections Algorithm
Unlike Round Robin, Least Connections is a dynamic algorithm. It tracks how many active requests each server is currently handling and routes new requests to the server with the lowest current workload.
* **Video:** [LTM Load Balancing Algorithms: Least Connections Types](https://www.youtube.com/watch?v=tAAmZ3bz8AA)

### 4. Comparisons and Use Cases
Read up on the specific differences and when to choose one algorithm over the other.
* **Article:** [Round Robin Load Balancing Important Differences](https://www.vmware.com/topics/round-robin-load-balancing)

### 5. Further Reading (Optional)
If you want to read an academic perspective on how these mechanisms are researched and implemented at a system level:
* **Paper:** [Web Server Load Balancing Mechanism with Least Connection Algorithm and Multi-Agent System](https://www.researchgate.net/publication/375044722_Web_Server_Load_Balancing_Mechanism_with_Least_Connection_Algorithm_and_Multi-Agent_System)

### 6. Check out the articles attached in this folder for a deeper understanding!
