from django.urls import path
from .views import create_job, list_jobs, job_detail, dashboard_summary, queue_status
from .views import health_check
urlpatterns = [
    path("jobs/", create_job, name="create-job"),
    path("jobs/list/", list_jobs, name="list-jobs"),
    path("jobs/<int:job_id>/", job_detail, name="job-detail"),
    path("dashboard-summary/", dashboard_summary, name="dashboard-summary"),
    path("health/", health_check),
    path("queue-status/", queue_status, name="queue-status"),
]