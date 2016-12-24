from django.conf.urls import include, url
from django.contrib import admin
from messageboard import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'uwisocial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^forums/$' , views.ForumList.as_view()),
    url(r'^forums/(?P<pk>[0-9]+)/$' , views.ForumDetail.as_view()),
    url(r'^discussions/$' , views.DiscussionList.as_view()),
    url(r'^discussions/(?P<forumid>[0-9]+)/$' , views.DiscussionForum.as_view()),
    url(r'^posts/$' , views.PostList.as_view()),
    url(r'^posts/(?P<discussionid>[0-9]+)/$' , views.PostDiscussion.as_view())
]
