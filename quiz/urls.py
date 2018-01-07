from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.urls import reverse_lazy, path, re_path
import django.contrib.auth.views as auth_views
from .views import *


urlpatterns = [
    url(r'^$', login_required(QuizListView.as_view()), name='quiz-list'),
    url(r'^login/$',auth_views.login,name='login'),
    url (r'register/$', UserRegistrationView.as_view(), name = 'register'),
    #url(r'topics/', login_required(TopicListView.as_view()), name='topic-list'),
    #url(r'(?P<pk>\d+)/topics/$', login_required(TopicDetailView.as_view()), name='topic-detail'),

    url(r'^logout/$',auth_views.logout, {'next_page': reverse_lazy('login')},name='logout'),
    url(r'(?P<pk>\d+)/$',login_required(QuizDetailView.as_view()),name='quiz-detail'),
    url(r'(?P<pk>\d+)/take-quiz/$',login_required(TakeQuizView.as_view()),name='take-quiz'),
    url(r'(?P<pk>\d+)/student-results/$',login_required(QuizResultsListView.as_view()),name='student-results')
]