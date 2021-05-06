from django.db import models
from django.contrib.auth.models import User

class Telemedicine(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    address = models.TextField()
    oxygen_saturation = models.CharField(max_length=200, blank=True, null=True)
    pulse = models.CharField(max_length = 200, blank=True, null=True)
    contact = models.CharField(max_length=20, null=True)
    person_accompany_name = models.CharField(max_length=200, blank=True, null=True)
    person_accompany_phone = models.CharField(max_length=20, blank=True, null=True)    
    gder = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('others','others'),
    )
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=200, choices=gder, null=True)
    email = models.EmailField(null=True)
    profile = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200, null=True)
    testimonial = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    specilization = models.CharField(max_length=200)
    years_of_practice = models.IntegerField()
    hospital_name = models.CharField(max_length=300)
    consulting_hour = models.CharField(max_length=300)
    gder = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('others','others'),
    )
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=200, choices=gder, null=True)
    address = models.TextField(null=True)
    contact = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    profile = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    pass

class Resource(models.Model):
    CATEGORY = (
        ('blue', 'blue'),
        ('yellow', 'yellow'),
        ('red', 'red'),
        ('green', 'green'),
        ('indigo', 'indigo'),
        ('purple', 'purple'),
        ('pink', 'pink'),
    )
    color = models.CharField(max_length=100, choices=CATEGORY, null=True)
    hashtag = models.CharField(max_length=300, null=True)
    link = models.TextField(null=True)
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title


class Messages(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=12)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name + self.city

class MessageBoard(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200, null=True)
    organization = models.CharField(max_length=200, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name + " " + self.designation


class Volunteer(models.Model):
    gder = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('others','others'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=200, choices=gder, null=True)
    address = models.TextField(null=True)
    contact = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    profile = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Counsellor(models.Model):
    gder = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('others','others'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=200, choices=gder, null=True)
    address = models.TextField(null=True)
    contact = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    profile = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name 

class Donor(models.Model):
    gder = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('others','others'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=200, choices=gder, null=True)
    blood_group = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    contact = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    profile = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name 



