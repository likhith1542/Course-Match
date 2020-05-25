from django.db import models

# Create your models here.
class Poll(models.Model):
    question=models.CharField(max_length=9,unique=True)
    option_one=models.CharField(max_length=7)
    option_two = models.CharField(max_length=7)
    option_three = models.CharField(max_length=7)
    option_four = models.CharField(max_length=7)
    option_five = models.CharField(max_length=7)
    option_six=models.CharField(max_length=7)
    option_seven=models.CharField(max_length=7)
    option_eight = models.CharField(max_length=7)
    option_nine=models.CharField(max_length=7)
    option_ten = models.CharField(max_length=7)
    
    def __str__(self):
        return self.question

