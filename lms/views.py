from rest_framework import generics, viewsets

from lms.models import Lesson, Well
from lms.paginators import LMSPaginator
from lms.serializers import LessonSerializers, WellSerializers


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    pagination_class = LMSPaginator


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class WellViewSet(viewsets.ModelViewSet):
    serializer_class = WellSerializers
    queryset = Well.objects.all()
    pagination_class = LMSPaginator
