from django.urls import include, path

from .adapter._in.reservation_api_controller import ReservationApiController

app_name='reservation'

# 진입점 설정
urlpatterns = [
    path('info/', ReservationApiController.as_view()),
]
