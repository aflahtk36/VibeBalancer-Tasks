# Task 5: Assignment – Implement Load Balancer

## Objective
Build a **custom load balancer** that distributes requests across multiple FastAPI servers using:
1. Round Robin Algorithm
2. Least Connections Algorithm

---

## Setup
You will reuse your Week 3 servers:
* `server_1` → `http://localhost:8001`
* `server_2` → `http://localhost:8002`

Ensure both are running.

---

## Part 1: Build a Load Balancer Server
Create a new FastAPI server:
* **Port:** `8000`
* Acts as a **proxy/load balancer**

### Endpoint
`GET /work`
* Accepts the same query parameter: `delay`
* Forwards the request to one of the backend servers
* Returns the backend response to the client

---

## Part 2: Round Robin Algorithm
### Requirements
* Maintain a list of servers:
    ```python
    servers = ["http://localhost:8001", "http://localhost:8002"]
    ```
* Use a pointer/index to alternate requests between servers.

### Expected Behavior
| Request | Server |
| :--- | :--- |
| 1 | `server_1` |
| 2 | `server_2` |
| 3 | `server_1` |

---

## Part 3: Least Connections Algorithm
### Requirements
* Track active connections per server:
    ```python
    connections = {
        "http://localhost:8001": 0,
        "http://localhost:8002": 0
    }
    ```

### Logic
* Select the server with the minimum active connections.
* Increment the count before sending the request.
* Decrement the count after the response is received.

---

## Part 4: Testing

### Test 1: Manual
Open multiple tabs to:
```url
http://localhost:8000/work?delay=3
```

**Observe:**
* Which server handled the request?
* What were the response times?

### Test 2: Script
Write a Python script to:
* Send 5 concurrent requests.
* **Measure:**
    * Total time taken.
    * Distribution of requests across servers.

---

## Part 5: Compare Algorithms
Write down your observations:

**Round Robin**
* Is the distribution equal?
* Does it consider server load?

**Least Connections**
* Does it adapt to varying delays?
* Are faster servers used more frequently?

---

## Deliverables
* Load balancer FastAPI server code (`lb.py` or similar).
* Implementation of both **Round Robin** and **Least Connections**.
* Python testing script (`client.py` or similar).
* Observations (short write-up).

---

## Bonus (Optional)
**Add a new endpoint:**
* `/strategy?type=round_robin`
* `/strategy?type=least_connections`
→ *Switch algorithms dynamically!*

**Add logging:**
* Log which server handled the request.
* Log the current active connections.

---

## Key Insight
You now have:
* Multiple backend servers 
* A load balancer distributing traffic 

This is the foundation of real-world distributed systems. The next natural steps lead to:
* Fault tolerance
* Health checks
* Scaling systems dynamically

## Important!
Update your progress in the excel sheet shared after you are completed with the assignments.
