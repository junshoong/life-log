from django.conf.urls import url
from diary.views import LogCreateView

urlpatterns = [
    url(r'^$', LogCreateView.as_view(), name='home'),
]
