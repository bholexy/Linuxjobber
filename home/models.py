from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length = 200)
    response = models.CharField(max_length = 1000)
    
    class Meta:
        verbose_name_plural = 'FAQs'
    
    def __str__(self):
        return self.question
