from messageboard.models import Forum
from messageboard.models import Discussion
from messageboard.models import Post
from rest_framework import serializers



class ForumSerializer(serializers.ModelSerializer):
	class Meta:
		model = Forum
		fields = ('id','name','description','created')



class DiscussionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Discussion
		fields = ('id','forum','topic','created','firstpostauthor','lastposttime','lastpostauthor')

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('id','discussion','author','title','message','created')


			