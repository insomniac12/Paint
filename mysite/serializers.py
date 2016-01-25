from rest_framework import serializers
from mysite.models import paints
from django.contrib.auth.models import User
class Serializer(serializers.ModelSerializer):
    owner =serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=paints
        fields=('name','product_type','brand','finish_type','coverage','availability','price','best_for','washability','eco_friendly','image','owner')
        
            

class UserSerializer(serializers.ModelSerializer):
    paint=serializers.PrimaryKeyRelatedField(many=True,queryset=paints.objects.all())
    class Meta:
        model=User
        fields=('id','username','paint')