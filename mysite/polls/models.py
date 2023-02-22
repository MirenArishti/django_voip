import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Document(models.Model):
    name = models.CharField(max_length=255, default='Document_name')
    date = models.DateField()
    # client = models.ForeignKey(ClientDetail, on_delete=models.CASCADE)
    myfile = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['pcap'])])
    # photo = models.ImageField(upload_to='cars')
    def __str__(self):
        return self.name