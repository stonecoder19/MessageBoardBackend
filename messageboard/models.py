from django.db import models
import datetime

# Create your models here.

class Forum(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=1000)
	created = models.DateTimeField(editable=False)
	discussnumber = models.IntegerField(default=0,editable=False)

	def __str__(self):
		return self.name


	def save(self,force_insert=False,force_update=False,using=None):
		if(not self.id):
			self.created = datetime.datetime.now()
		super(Forum,self).save()





class Discussion(models.Model):
	topic = models.CharField(max_length=255)	
	forum = models.ForeignKey(Forum)
	created = models.DateTimeField(editable=False)
	lastposttime = models.DateTimeField('auto_now_add=true',default=datetime.datetime.now(),editable=False)
	lastpostauthor = models.CharField(max_length=255,default = 'John Doe',editable=False)
	firstpostauthor = models.CharField(max_length=255,default = 'Jane Doe',editable=False)
	postnumber = models.IntegerField(default=0,editable=False)

	def __str__(self):
		return self.topic

	def save(self,force_insert=False,force_update=False,using=None):
		forum = Forum.objects.get(id = self.forum_id)
		if(not self.id):
			self.created = datetime.datetime.now()
			forum.discussnumber+=1
		else:
			forum.discussnumber = len(Discussion.objects.filter(forum_id = self.forum_id))
		forum.save()

		super(Discussion,self).save()

class Post(models.Model):
	discussion = models.ForeignKey(Discussion)
	author = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	message = models.TextField()
	created = models.DateTimeField(editable=False)

	def __str__(self):
		return self.title

	def save(self,force_insert=False,force_update=False,using=None):
		discuss = Discussion.objects.get(id = self.discussion_id)
		if(not self.id):
			self.created = datetime.datetime.now()
			discuss.postnumber+=1

		
		discuss.postnumber = len(Post.objects.filter(discussion_id = self.discussion_id))

		if(discuss.postnumber == 0):
			discuss.firstpostauthor = self.author
		discuss.lastpostauthor = self.author
		#discuss.firstpostauthor = Post.objects.filter(discussion_id = self.discussion_id)[0].author
		discuss.lastposttime = datetime.datetime.now()
		discuss.save()
		super(Post,self).save()

