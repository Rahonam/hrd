from django import forms
from .models import Candidate


class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('applicant_name', 'resume_file_name')
