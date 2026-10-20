from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

from .models import Class, Puples
from .serializers import PuplesSerializer, ClassSerializer


class PuplesViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassViewSet(ModelViewSet):

    queryset = Puples.objects.all()
    serializer_class = PuplesSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['full_name', 'phone_number', 'address']
    ordering_fields = ['id', 'full_name', 'birth_year', 'course']
    filterset_fields = {
        'course__title': ['exact'],
        'birth_year': ['exact', 'lt', 'lte', 'gt', 'gte'],
    }
