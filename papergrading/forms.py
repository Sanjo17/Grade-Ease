from django import forms
from django.contrib.auth.models import User
from . import models


class KeyUploadForm(forms.ModelForm):

    class Meta:
        model = models.AnswerKey
        fields = ['course','key_file']
        


class StudentAnswerFileUploadForm(forms.ModelForm):

    class Meta:
        model = models.StudentPaper
        fields = ['course','answer_file','student']
        

