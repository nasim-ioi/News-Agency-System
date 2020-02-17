from django.urls import path
from .views import *

urlpatterns = [
    path('post_report/<int:user_id>' , Post_report , name = "post_report") , 
    path('get_for_update/<int:user_id>' , Get_for_update , name = "get_for_update") , 
    path('visit_reporters/' , Visit_reporter , name = "visit_reporter") , 
    path('update_report/<int:report_id>', Update_report , name = "update_reporter") ,
    path('get_reports/<str:stdate>' , Get_report , name = "get_report") ,
    path('delete_reports/<int:report_id>' , Delete_report , name = "delete_report")
]