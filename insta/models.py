import datetime

from django.contrib.auth.models import User
from django.db import models


class Profile(User):
    bio = models.CharField(blank=True, max_length=200)
    is_business_profile = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "Profile"


class Post(models.Model):
    posted_by = models.ForeignKey(Profile, related_name="posts", on_delete=models.CASCADE)
    post_details = models.TextField(max_length=200)
    likes = models.ManyToManyField(Profile, related_name="liked_posts", blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=False)

    def __str__(self):
        return f"Post: {self.post_details} by {self.posted_by.username}"

    def like_post(self, user):
        self.likes.add(user)


class Message(models.Model):
    sender = models.ForeignKey(Profile, related_name="message_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name="message_receiver", on_delete=models.CASCADE)
    content = models.TextField(max_length=200, null=False)

    def __str__(self):
        return f"Message: {self.content} from {self.sender.username} to {self.receiver.username}"
