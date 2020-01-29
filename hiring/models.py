from django.db import models
import datetime
import os
from django.core.validators import FileExtensionValidator


def document_directory_path(instance, filename):
    path = '%Y/{}'.format(filename)
    return datetime.datetime.now().strftime(path)


class Candidate(models.Model):
    SUBMIT = 'Submit'
    REVIEW = 'Review'
    INTERVIEW = 'Interview'
    HIRED = 'Hired'
    STATUS_CHOICES = [
        (SUBMIT, 'Submit'),
        (REVIEW, 'Review'),
        (INTERVIEW, 'Interview'),
        (HIRED, 'Hired')
    ]
    applicant_name = models.CharField(max_length=150)
    resume_file_name = models.FileField(upload_to=document_directory_path, validators=[
                                        FileExtensionValidator(allowed_extensions=['pdf'])])
    status = models.CharField(choices=STATUS_CHOICES,
                              default='Submit', max_length=10)

    def filename(self):
        return os.path.basename(self.resume_file_name.name)


class Application_Submit(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now_add=True)


class Application_Review(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now_add=True)


class Application_Interview(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now_add=True)


class Application_Hire(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now_add=True)
