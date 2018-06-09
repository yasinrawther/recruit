from django.conf.urls import url
from recruitment.views import Recruiter, RecruiterList


urlpatterns = [
    url(r'^recruiters/$', Recruiter.as_view()),
    url(r'^recruiters_list/$', RecruiterList.as_view()),
]