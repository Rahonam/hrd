from django.shortcuts import render, redirect
from .forms import CandidateForm
from .models import Candidate, Application_Submit, Application_Review, Application_Interview, Application_Hire
import time


def home(request):
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save()  # task 1
            time.sleep(15)
            submit = Application_Submit.objects.create(
                candidate=candidate, event_time=time.time())
            time.sleep(15)
            review = Application_Review.objects.create(
                candidate=candidate, event_time=time.time())
            time.sleep(15)
            interview = Application_Interview.objects.create(
                candidate=candidate, event_time=time.time())
            time.sleep(15)
            hire = Application_Hire.objects.create(
                candidate=candidate, event_time=time.time())  # task 9
            return redirect('candidate_list')
    else:
        form = CandidateForm()
    return render(request, 'hiring/apply.html', {'form': form})


def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'hiring/candidate_list.html', {'candidates': candidates})


def track_status(request, pk):
    candidate = Candidate.objects.get(pk=pk)
    try:
        submit_status = Application_Submit.objects.get(candidate=candidate)
    except Application_Submit.DoesNotExist:
        submit_status = None
    try:
        review_status = Application_Review.objects.get(candidate=candidate)
    except Application_Review.DoesNotExist:
        review_status = None
    try:
        interview_status = Application_Interview.objects.get(
            candidate=candidate)
    except Application_Interview.DoesNotExist:
        interview_status = None
    try:
        hire_status = Application_Hire.objects.get(candidate=candidate)
    except Application_Hire.DoesNotExist:
        hire_status = None
    return render(request, 'hiring/track_status.html', {'candidate': candidate, 'submit_status': submit_status, 'review_status': review_status, 'interview_status': interview_status, 'hire_status': hire_status})
