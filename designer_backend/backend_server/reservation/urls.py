from django.urls import include, path

from .adapter._in.reservation_api_controller import ReservationApiController
from .adapter._in.reservation_reservation_holiday_api_controller import ReservationReservationHolidayApiController
from .adapter._in.reservation_rsrv_holiday_schedule_api_controller import ReservationRsrvHolidayScheduleApiController
from .adapter._in.reservation_mod_rsrv_holiday_schedule_api_controller import ReservationModRsrvHolidayScheduleApiController
from .adapter._in.reservation_save_reservation_holiday_api_controller import ReservationSaveReservationHolidayApiController
from .adapter._in.reservation_mod_reservation_holiday_api_controller import ReservationModReservationHolidayApiController
from .adapter._in.reservation_save_rsrv_holiday_schedule_api_controller import ReservationSaveRsrvHolidayScheduleApiController
from .adapter._in.reservation_pop_rsrv_detail_info_api_controller import ReservationPopRsrvDetailInfoApiController

app_name='reservation'

# 진입점 설정
urlpatterns = [
    path('info/', ReservationApiController.as_view()),
    path('getReservationHoliday/', ReservationReservationHolidayApiController.as_view()),
    path('getRsrvHolidaySchedule/', ReservationRsrvHolidayScheduleApiController.as_view()),
    path('modRsrvHolidaySchedule/', ReservationModRsrvHolidayScheduleApiController.as_view()),
    path('saveReservationHoliday/', ReservationSaveReservationHolidayApiController.as_view()),
    path('modReservationHoliday/', ReservationModReservationHolidayApiController.as_view()),
    path('saveRsrvHolidaySchedule/', ReservationSaveRsrvHolidayScheduleApiController.as_view()),
    path('getPopRsrvDetailInfo/', ReservationPopRsrvDetailInfoApiController.as_view()),
]
