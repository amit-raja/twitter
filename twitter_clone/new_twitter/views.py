from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime, timezone, timedelta
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.response import Response
from new_twitter.models import user_detail,userFollowing
from rest_framework.permissions import IsAuthenticated
from new_twitter.serializers import  user_detailSerializer, user_detail_tweetSerializer, FollowerSerializer, FollowingSerializer
import datetime

User = settings.AUTH_USER_MODEL


@api_view(['GET'])
def user_detail_tweet(request):
    user_detail = user_detail.objects.all()
    serilaizer=user_detail_tweetSerializer(user_detail,many=True)
    return Response(serilaizer.data)
    
@api_view(['GET'])
def timeline_tweets(request):
	all_tweets=Tweet.objects.none()
	timeline=datetime.datetime.now()-datetime.timedelta(days=1)
	following_tweets=Tweet.objects.filter(author__in=[query.username for query in request.user.follow.all()],created__gt=timeline)
	tweets=Tweet.objects.filter(author =request.user, created__gt=timeline)
	all_tweets=following_tweets.union(tweets)
	serilaizer=user_detailSerializer(all_tweets.order_by('-created'),many=True)
	return Response(serilaizer.data)

@api_view(['GET'])
def following(request):
	try:
		user=request.query_params['user']
		if request.user.follow.filter(username__username=user).exists():
			following=request.user.follow.none()
			user=User.objects.filter(username=user).get()
			serializer=FollowingSerializer(following,context={'user': user})
			return Response(serializer.data)
		else:
			forbidden={'message':'permission denied or user not exist'}
			return Response(data=forbidden,status=status.HTTP_403_FORBIDDEN)
	except:
		following=request.user.follow.none()
		serializer=FollowingSerializer(following,context={'user': request.user})
		return Response(serializer.data)

@api_view(['GET'])
def follower(request):
	try:
		user=request.query_params['user']
		if request.user.follow.filter(username__username=user).exists():
			follower=Follower.objects.filter(username__username=user)
			serializer=FollowerSerializer(follower,many=True)
			return Response(serializer.data)
		else:
			forbidden={'message':'permission denied or user not exits'}
			return Response(data=forbidden,status=status.HTTP_403_FORBIDDEN)
	except:
		follower=Follower.objects.filter(username__username=request.user)
		serializer=FollowerSerializer(follower,many=True)
		return Response(serializer.data)
