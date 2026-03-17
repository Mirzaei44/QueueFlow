from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer, JobCreateSerializer
from .tasks import process_job_task
from django_ratelimit.decorators import ratelimit


@ratelimit(key="ip", rate="5/m", method="POST", block=True)
@api_view(["POST"])
def create_job(request):
    serializer = JobCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    job = serializer.save()
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