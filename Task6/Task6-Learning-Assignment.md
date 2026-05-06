
# Task 6: Learning – Scrape Metrics & Observability

## Background

Welcome to Phase V of VibeBalancer! Now that your load balancer intelligently distributes traffic, the next step is understanding its performance. As a system scales, you need to know if a server is overloaded, if requests are failing, or how fast responses are returning. This is solved through **metrics and observability**.

Observability enables you to understand what's happening inside your systems by analyzing the data they produce. We can't talk about observability without discussing three key types of data: **metrics, logs, and traces**. For this task, we will focus purely on **metrics**—numbers that show how your system is performing, like response times or CPU usage.

---

## Topics to Learn

### 1. System vs. Application Metrics

- **System Metrics:**  
  Hardware performance like CPU usage and memory usage.  
  The `psutil` library in Python allows you to monitor these cross-platform (including Windows) without needing OS-specific terminal commands.

- **Application Metrics:**  
  Software performance like total HTTP requests, request duration, and active connections.

---

## Resources

- **Intuition:**  
  [Master the psutil Library in Python](https://www.youtube.com/watch?v=Zv_-H4m24Rw)

- **Learning:**  
  [PROMETHEUS Metrics for your Python FastAPI App](https://www.youtube.com/watch?v=WWzl53ObYvo)

- **Optional Deep Dive:**  
  [Monitor Python FastAPI in Real-Time with Prometheus & Grafana](https://www.youtube.com/watch?v=tskCWURmPDo)

---

## After Learning

Once you have gone through the resources, proceed to the assignment provided below. If you hit any roadblocks, reach out to your mentors.

---

# Task 6: Assignment – Scrape Metrics

## Objective

Enhance VibeBalancer by exposing internal application metrics and system-level hardware metrics via a dedicated HTTP endpoint.

---

## Setup

You will build upon your existing FastAPI load balancer and backend servers from Week 5.

Install the required cross-platform library:

```bash
pip install psutil
````

---

## Part 1: Track Application Metrics

Update your load balancer logic to keep track of the following globally:

* **Total Requests:** Counter for every request received.
* **Active Connections:** Current number of in-flight requests.
* **Total Errors:** Counter for failed requests (e.g., timeouts).

---

## Part 2: Track System Metrics

Use `psutil` to track machine health:

* **CPU Usage:** Current CPU utilization (%)
* **Memory Usage:** Current RAM utilization (%)

---

## Part 3: Expose the Metrics Endpoint

Create a new endpoint:

* **Endpoint:** `GET /metrics`
* **Behavior:** Returns combined application + system metrics.

### Expected JSON

```json
{
  "application": {
    "total_requests": 150,
    "active_connections": 3,
    "total_errors": 0
  },
  "system": {
    "cpu_usage_percent": 14.5,
    "memory_usage_percent": 62.1
  }
}
```

---

## Part 4: Testing

1. Start backend servers + load balancer
2. Run your Week 5 testing script (concurrent requests)
3. Open:

```
http://localhost:8000/metrics
```

4. Observe:

   * Active connections fluctuating
   * CPU usage changing under load

---

## Deliverables

* Updated `lb.py` with `/metrics` endpoint
* Screenshot or JSON response under load

---

## Key Insight

These metrics enable **real-time monitoring** and unlock **auto-scaling**.

When:

* `cpu_usage_percent` is high
* `active_connections` spikes

→ You can automatically spin up new backend servers to maintain low latency.

---

## Reference

[Instrumenting Prometheus Metrics in FastAPI](https://www.youtube.com/watch?v=WWzl53ObYvo)

