from django.db import models


class MedicalCondition(models.Model):
    medicalConditionName = models.CharField(max_length=200)

    def __str__(self):
        return self.medicalConditionName


class User(models.Model):
    name = models.CharField(max_length=200)
    abbrev = models.CharField(max_length=10)
    tktNum = models.CharField(max_length=200)
    mobileNum = models.CharField(max_length=200)
    age = models.IntegerField()
    height = models.FloatField()
    isOwner = models.BooleanField(default=False)
    medicalConditions = models.ManyToManyField(MedicalCondition, related_name="MedicalCondition")

    def __str__(self):
        """A string representation of the model."""
        return self.mobileNum + "_" + self.abbrev

class Group(models.Model):
    mobileNum = models.CharField(max_length=200)

    def __str__(self):
        return self.mobileNum


class GroupMembers(models.Model):
    mobileNum = models.CharField(max_length=200)
    members = models.ManyToManyField(User, related_name="Group_members")

    def __str__(self):
        return self.mobileNum

