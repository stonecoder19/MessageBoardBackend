from django.shortcuts import render
from messageboard.models import Forum
from messageboard.models import Discussion
from messageboard.models import Post
from django.http import Http404

from messageboard.serializers import ForumSerializer
from messageboard.serializers import DiscussionSerializer
from messageboard.serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PostList(APIView):
	
	def get(self,request,format=None):
		posts = Post.objects.all()
		serializer = PostSerializer(posts,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = PostSerializer(data = request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDiscussion(APIView):
	def get(self,request,discussionid,format=None):
		posts = Post.objects.filter(discussion_id=discussionid)
		serializer = PostSerializer(posts,many=True)
		return Response(serializer.data)




class DiscussionList(APIView):

	def get(self,request,format=None):

		discussions = Discussion.objects.all()
		serializer = DiscussionSerializer(discussions,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = DiscussionSerializer(data = request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Respons(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk,format=None):
		discussion = self.get_object(pk)
		discussion.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

'''class DiscussionDetail(APIView):

	def get_object(self,pk):
		try:
			return Discussion.objects.get(pk)'''



class DiscussionForum(APIView):

	def get(self,request,forumid,format=None):

		discussions = Discussion.objects.filter(forum_id=forumid)
		serializer = DiscussionSerializer(discussions,many=True)
		return Response(serializer.data)





class ForumList(APIView):

	def get(self, request, format=None):

		forums = Forum.objects.all()
		serializer  = ForumSerializer(forums,many=True)
		return Response(serializer.data)


	def post(self, request ,format=None):
		serializer = ForumSerializer(data = request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data , status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request,pk,format=None):
		forum = self.get_object(pk)
		forum.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ForumDetail(APIView):

	def get_object(self,pk):
		try:
			return Forum.objects.get(pk=pk)
		except Forum.DoesNotExist:
			raise Http404


	def get(self,request,pk,format=None):
		forum = self.get_object(pk)
		forum = ForumSerializer(forum)
		return Response(forum.data)

	def put(self, request , pk, format=None):
		forum = self.get_object(pk)
		serializer = ForumSerialize(forum,data=request.Data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk,format=None):
		forum = self.get_object(pk)
		forum.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)




