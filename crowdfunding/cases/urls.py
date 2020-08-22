from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('cases/', views.CaseList.as_view()),
    path('cases/<int:pk>', views.CaseDetail.as_view()),
    path('pledges/', views.PledgeList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)