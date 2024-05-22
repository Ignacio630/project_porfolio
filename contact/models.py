from django.db import models

# Create your models here.


class Contact(models.Model):
    options = [
        {'project','Project'},
        {'job_offer','Job offer'},
    ]
    email = models.EmailField()
    reason = models.CharField(max_length=100, blank=False, choices=options)
    comments = models.TextField(max_length=1000)


    def __str__(self) -> str:
        return f"Email: {self.email}\nReason{self.reason}\nComments{self.comments}"