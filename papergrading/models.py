from django.db import models
from exam.models import Course
from student.models import Student

class AnswerKey(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    key_file = models.FileField(upload_to='answer_keys/',null=True,blank=True)

class StudentPaper(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    answer_file = models.FileField()




