from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class userFollowing(models.Model):
    username=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    #following= models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    #followers = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    followers=models.ManyToManyField(User,related_name='follow',blank=True)
    #follow_time = models.DateTimeField(auto_now_add=True)

    '''class Meta:
        constraints = [
            models.UniqueConstraint(fields=[""],  name="unique_followers")
        ]'''

        #ordering = ["-created"]

    '''def __str__(self):
        f"{self.user_id} follows {self.following_user_id}"'''


class user_detail(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    #user_name = models.CharField(max_length=40)
    tweets = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='tweet_like', blank=True)
    #retweeted = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    retweets=models.ManyToManyField(User,related_name='retweeted',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #= models.DateTimeField(auto_now_add=True)
    #retweet = models.BooleanField(default=False)
