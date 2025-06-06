from django.db import models

# Create your models here.
# Table to take user email and password
class User(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.email
# Table to take user uploaded file
class UploadedFile(models.Model):
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
# This model stores the analysis result
class AnalysisResult(models.Model):
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    summary = models.TextField()
    risks = models.TextField()
    analyzed_at = models.DateTimeField(auto_now_add=True)