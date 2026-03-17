import logging

from celery import shared_task
from django.utils import timezone

from .models import Job

logger = logging.getLogger("jobs")


@shared_task
def process_job_task(job_id):
    logger.info(f"Starting job processing for job_id={job_id}")

    job = Job.objects.get(id=job_id)
    job.status = "processing"
    job.save(update_fields=["status"])

    records = job.input_data.get("records", 0)

    job.output_data = {
        "summary": f"Processed dataset with {records} records",
        "score": min(records // 10, 100),
    }
    job.status = "completed"
    job.completed_at = timezone.now()
    job.save(update_fields=["output_data", "status", "completed_at"])

    logger.info(f"Completed job_id={job.id} with status={job.status}")

    return {"job_id": job.id, "status": job.status}