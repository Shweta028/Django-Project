from django.db import models
from django.urls import reverse

# Create your models here.

class DeviceGroup(models.Model):
    groupname = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'devicegroups'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        try:
            return (self.groupname + " is  " + self.description)
        except TypeError:
            return "NO GROUP"


class Device(models.Model):
    IP_Address = models.GenericIPAddressField(unique=True)
    hostname = models.CharField(max_length=30, unique=True)
    devicegroups = models.ManyToManyField(DeviceGroup, blank=True)

    def __str__(self):
        return self.hostname + " / " + self.IP_Address
    def get_absolute_url(self):
        return reverse('device_detail', kwargs={'pk': self.pk})

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=False)
    password = models.CharField(blank=False, max_length=20)
    def __str__(self):
        return self.username