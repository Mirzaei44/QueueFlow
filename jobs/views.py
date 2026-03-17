from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer, JobCreateSerializer
from .tasks import process_job_task
from django_ratelimit.decorators import ratelimit
from django.core.cache import cache
from django.db.models import Count
from django.http import JsonResponse
from django.core.cache import cache
import redis
@ratelimit(key="ip", rate="5/m", method="POST", block=True)
@api_view(["POST"])
def create_job(request):
    serializer = JobCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    job = serializer.save()
    cache.delete("dashboard_summary")
    task = process_job_task.delay(job.id)
    data = JobSerializer(job).data
    data["task_id"] = task.id
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def list_jobs(request):
    jobs = Job.objects.all().order_by("-created_at")
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    serializer = JobSerializer(job)
    return Response(serializer.data)



@api_view(["GET"])
def dashboard_summary(request):
    cached_data = cache.get("dashboard_summary")

    if cached_data:
        return Response({
            "source": "cache",
            "data": cached_data
        })

    total_jobs = Job.objects.count()
    completed_jobs = Job.objects.filter(status="completed").count()
    pending_jobs = Job.objects.filter(status="pending").count()
    processing_jobs = Job.objects.filter(status="processing").count()
    failed_jobs = Job.objects.filter(status="failed").count()

    summary = {
        "total_jobs": total_jobs,
        "completed_jobs": completed_jobs,
        "pending_jobs": pending_jobs,
        "processing_jobs": processing_jobs,
        "failed_jobs": failed_jobs,
    }

    cache.set("dashboard_summary", summary, timeout=60)

    return Response({
        "source": "database",
        "data": summary
    })
    
    
def health_check(request):
    status = {
        "api": "ok",
        "redis": "unknown",
        "cache": "unknown"
    }

    # check redis
    try:
        r = redis.Redis(host="127.0.0.1", port=6379)
        r.ping()
        status["redis"] = "ok"
    except Exception:
        status["redis"] = "error"

    # check cache
    try:
        cache.set("health_test", "ok", timeout=5)
        if cache.get("health_test") == "ok":
            status["cache"] = "ok"
    except Exception:
        status["cache"] = "error"

    return JsonResponse(status)