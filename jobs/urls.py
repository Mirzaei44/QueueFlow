from django.urls import path
from .views import create_job, list_jobs, job_detail, dashboard_summary

urlpatterns = [
    path("jobs/", create_job, name="create-job"),
    path("jobs/list/", list_jobs, name="list-jobs"),
    path("jobs/<int:job_id>/", job_detail, name="job-detail"),
    path("dashboard-summary/", dashboard_summary, name="dashboard-summary"),
]