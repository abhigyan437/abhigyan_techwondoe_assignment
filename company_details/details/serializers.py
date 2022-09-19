from .models import Company,Team
from rest_framework import serializers
from django.contrib.auth.models import User


class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('uuid','company_name','company_ceo','company_address','company_inception')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('uuid','company_id','team_lead_name')