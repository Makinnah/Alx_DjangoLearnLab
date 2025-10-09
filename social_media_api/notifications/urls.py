from django.urls import path
from .views import NotificationListView, mark_as_read

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications-list'),
    path('<int:pk>/read/', mark_as_read, name='notifications-mark-read'),
]


from django.urls import path
from .views import NotificationListView, mark_as_read

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<int:notification_id>/read/', mark_as_read, name='mark-as-read'),
]
