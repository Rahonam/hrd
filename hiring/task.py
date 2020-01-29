from hiring.models import Candidate, Application_Submit, Application_Review, Application_Interview, Application_Hire
from celery import shared_task


@shared_task
