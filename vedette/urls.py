from django.urls import path
from .views import *


urlpatterns = [
    # path("search/<str:name>", process_class),
    path("search",Search.as_view()),

    path('history/me', get_user_history),

    path("search/vip/<str:name>", search_vip)
]
