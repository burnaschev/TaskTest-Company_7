from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, WellViewSet

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'well', WellViewSet, basename='well')
router.register(r'subscription', WellViewSet, basename='subscription')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/view/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson_view'),
    path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete'),

]
urlpatterns += router.urls
