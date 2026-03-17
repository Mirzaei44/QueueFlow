⸻
# QueueFlow

QueueFlow is a minimal backend service designed to demonstrate real-world backend architecture patterns using Django, Celery, Redis and Docker.

The project focuses on asynchronous job processing, task queues, caching, logging, API protection and CI/CD automation. It is intentionally lightweight while showcasing patterns commonly used in production backend systems.

---

## Features

- REST API built with Django REST Framework
- Asynchronous job processing using Celery
- Redis used as message broker and cache layer
- Background workers handling long-running tasks
- Dashboard summary endpoint with Redis caching
- Structured logging for job lifecycle events
- API rate limiting
- Docker support
- GitHub Actions CI pipeline
- Cloud-ready architecture (AWS compatible)

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Celery
- Redis
- Docker
- GitHub Actions

---

## Architecture

Client
↓
Django REST API
↓
Create Job Endpoint
↓
Redis Queue
↓
Celery Worker
↓
Job Processing
↓
Database (Django ORM)
↓
Cached Dashboard Summary (Redis)

---

## API Endpoints

### Create Job

POST `/api/jobs/`

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

Docker

Build the container:

docker build -t queueflow .

Run the container:

docker run -p 8000:8000 queueflow


⸻

CI Pipeline

The repository includes a GitHub Actions workflow that automatically runs Django checks on every push.

This ensures the project remains deployable and prevents broken commits from reaching the main branch.

⸻

Cloud Deployment (AWS Ready)

The architecture is compatible with common AWS backend deployments such as:
	•	EC2 for the Django application
	•	Redis (Elasticache) for task queue and caching
	•	Celery workers running on separate compute instances
	•	RDS or managed database for persistent storage
	•	Docker containers for consistent deployment

⸻

## Scaling Notes

QueueFlow is designed with a queue-based architecture, meaning job processing can be scaled horizontally by running multiple Celery workers against the same Redis broker.

This allows background jobs to be processed concurrently without blocking the main API service.

⸻


Purpose of the Project

QueueFlow was built as a backend engineering exercise to demonstrate:
	•	asynchronous background processing
	•	queue-based architecture
	•	caching strategies
	•	API protection
	•	CI/CD automation
	•	containerised deployment

The goal is to showcase practical backend development patterns used in modern distributed systems.

---
