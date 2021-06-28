from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Listing(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image_url = models.CharField(max_length=300, null=True, blank=True)
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(default=timezone.now)
    starting_bid = models.DecimalField(max_digits=7, decimal_places=2)
    active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE,
        blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings", null=True)

    def __str__(self):
        return f"{self.title}"

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids",null=True)
    bid = models.FloatField(null=True)

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment}"

class Watchlist(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlists")