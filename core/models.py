from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='players/')
    rating = models.FloatField(default=1.0)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nickname} ({self.role})"

class Match(models.Model):
    opponent = models.CharField(max_length=100)
    tournament = models.CharField(max_length=100)
    date = models.DateTimeField()
    is_home = models.BooleanField(default=False)
    stream_link = models.URLField(blank=True)

    def __str__(self):
        return f"FURY vs {self.opponent}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name