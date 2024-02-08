from django.urls import path
from tasks.views import ListCreateTaskView


urlpatterns = [
    path("", ListCreateTaskView.as_view(), name="task-list-create"),
]