import django_filters
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

# Create your views here.
from restapp.models import Task
from restapp.serializers import TaskSerializers, UserSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('task_completed',)
    ordering = ('-task_date_created',)
    search_fields = ('task_name',)


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializers


# class DueTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.order_by('-task_date_created').filter(task_completed=False)
#     serializer_class = TaskSerializers
#
#
# class CompletedViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.order_by('-task_date_created').filter(task_completed=True)
#     serializer_class = TaskSerializers
