from rest_framework import serializers
from NewApp.models import NewUser,ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = ['start_time','end_time']

class NewUserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)
    class Meta:
        model = NewUser
        fields = ['id', 'real_name', 'tz','activity_periods']
    
    
    def create(self,validated_data):
        activity_periods = validated_data.pop('activity_periods')
        newuser = NewUser.objects.create(**validated_data)
        for activity_period in activity_periods:
            ActivityPeriod.objects.create(**activity_period,newuser=newuser)
        return newuser
