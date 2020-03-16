from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from videos.views import  (video_detail_view,
                           video_list_view,
                           video_create_view,
                           video_update_view,
                           video_yolo_view,
                           )

urlpatterns = [
    path('', video_list_view, name='video_list'),
    path('<int:video_id>/', video_detail_view, name = 'video_detail'),
    path('<int:video_id>/update/', video_update_view, name='video_update'),
    path('create/', video_create_view, name='create'),
    path('<int:video_id>/yolo/', video_yolo_view, name='video_yolo'),
                  # path('<int:video_id>', video_detail_view, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
