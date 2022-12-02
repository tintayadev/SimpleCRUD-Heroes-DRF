from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('alias')
    serializer_class = HeroSerializer
