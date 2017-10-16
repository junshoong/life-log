from django.views.generic.edit import CreateView
from diary.models import Log


class LogCreateView(CreateView):
    model = Log
    fields = ['content']
    
