from django.db import models

# class bnao niche uske baad make migrations fir migrate, uske baad admin me jaake Register your models like this : #admin.site.register(Contact)

class Contact(models.Model):
    full_name = models.CharField(max_length=50, )
    email_address = models.CharField( max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"From: {self.full_name}, E-mail: {self.email_address}"