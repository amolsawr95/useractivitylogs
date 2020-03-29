from rest_framework import viewsets
from NewApp.models import NewUser,ActivityPeriod
from .serializers import NewUserSerializer,ActivityPeriodSerializer

class NewUserViewset(viewsets.ModelViewSet):
    serializer_class = NewUserSerializer
    queryset = NewUser.objects.all()

class ActivityAddViewset(viewsets.ModelViewSet):
    serializer_class = ActivityPeriodSerializer
    queryset = ActivityPeriod