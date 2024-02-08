from django.urls import path
from tasks.views import ListCreateTaskView, TaskDetailView


urlpatterns = [
    path("", ListCreateTaskView.as_view(), name="task-list-create"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
]