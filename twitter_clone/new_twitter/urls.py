from django.urls import path
from new_twitter.views import (
   timeline_tweets,
   following,
   user_detail,
   user_detail_tweet,
   follower,
) 

urlpatterns = [
   path('user_timeline', timeline_tweets),
   path('user_following', following),
   path('user_detail',user_detail_tweet),
   path('user_follwer',follower),
   ]