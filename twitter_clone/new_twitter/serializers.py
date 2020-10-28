from rest_framework import serializers
from new_twitter.models import user_detail,userFollowing
from django.conf import settings

class user_detailSerializer(serializers.ModelSerializer):
	likes=serializers.SerializerMethodField(read_only=True)
	retweets=serializers.SerializerMethodField(read_only=True)
	user_id= serializers.StringRelatedField(many=False)
	class Meta:
		model=user_detail
		fields=['id','tweets','user_id','likes','retweets']

	def get_likes(self,obj):
		return obj.likes.count()

	def get_retweets(self,obj):
		return obj.retweets.count()

class user_detail_tweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_detail
        fields = "__all__"

class FollowerSerializer(serializers.ModelSerializer):
	username=serializers.StringRelatedField(many=False)
	followers=serializers.StringRelatedField(many=True)

	class Meta:
		model=userFollowing
		fields=['username','followers']

class FollowingSerializer(serializers.Serializer):
	username=serializers.SerializerMethodField(read_only=True)
	followers=serializers.SerializerMethodField(read_only=True)

    
	
	def get_username(self,obj):
		user = self.context.get("user")
		print(user)
		
		return user.username

	def get_following(self,obj):
		user = self.context.get("user")
		print(user.follow.all())
		following=[i.username.username for i in user.follow.all()]
		return following


'''class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = userFollowing
        fields = ("id", "user_id")'''

