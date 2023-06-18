#create seriallizers

from rest_framework import serializers
from api.models import *

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        company_id=serializers.ReadOnlyField()
        model=Company
        fields="__all__"

    
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

        
