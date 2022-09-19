from rest_framework import viewsets,filters
from .serializers import CompanySerializer,TeamSerializer
from .models import Company,Team
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import userSerializers
from django.contrib.auth.models import User


class userviewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializers

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

#@login_required
class CompanyViewSet(viewsets.ModelViewSet):
    search_fields = ['uuid','company_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Company.objects.all().order_by('company_name')
    serializer_class = CompanySerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('uuid')
    serializer_class = TeamSerializer
