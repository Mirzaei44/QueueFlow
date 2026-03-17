# QueueFlow

QueueFlow is a minimal backend service built to demonstrate common production backend patterns using Django, Django REST Framework, Celery and Redis.

The project focuses on asynchronous job processing, background workers, task queues, caching, logging, and API protection. It is intentionally lightweight while showcasing real-world backend architecture concepts.

---

## Core Features

- REST API built with Django REST Framework
- Asynchronous job processing using Celery
- Redis used as a message broker and cache layer
- Background workers handling long-running tasks
- Dashboard summary endpoint with Redis caching
- Structured logging for job lifecycle events
- Rate limiting for API protection
- Docker support
- CI pipeline using GitHub Actions

---

## API Endpoints

### Create Job

POST /api/jobs/

Example request:

```json
{
  "name": "summary-job",
  "input_data": {
    "records": 1200
  }
}


⸻

List Jobs

GET /api/jobs/list/


⸻

Job Detail

GET /api/jobs/<id>/


⸻

Dashboard Summary

GET /api/dashboard-summary/

Returns aggregated statistics about jobs. Results are cached in Redis for improved performance.

⸻

System Architecture

Client
  ↓
Django / DRF API
  ↓
Job Creation Endpoint
  ↓
Redis Task Queue
  ↓
Celery Worker
  ↓
Job Processing
  ↓
PostgreSQL / Django ORM
  ↓
Cached Summary (Redis)


⸻

Technology Stack
	•	Python
	•	Django
	•	Django REST Framework
	•	Celery
	•	Redis
	•	Docker
	•	GitHub Actions

⸻

Running the Project Locally

Install dependencies:

pip install -r requirements.txt

Start Redis:

redis-server

Run Django:

python manage.py runserver

Start Celery worker:

celery -A config worker -l info


⸻

Example Workflow
	1.	A client sends a request to create a job.
	2.	The API creates a database record and queues a task.
	3.	Redis stores the task in the queue.
	4.	A Celery worker processes the task asynchronously.
	5.	The worker updates the job status and result.
	6.	Dashboard summary data is cached in Redis.

⸻

Project Purpose

QueueFlow was built as a focused backend engineering exercise to demonstrate:
	•	asynchronous task processing
	•	queue-based architecture
	•	caching strategies
	•	API protection mechanisms
	•	containerisation and CI readiness

The goal is to showcase practical backend development patterns used in modern distributed systems.

