from rest_framework import serializers

from .models import Classes, Subject

class ClassesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Classes
        fields = ['floor', 'semester', 'department', 'room_no', 'class_start_date', 'gender']

    def create(self, validated_data):
        split_department = validated_data["department"].split(' ')
        short_department = split_department[0][0] + split_department[1][0]
        date = str(validated_data['date']).split('-')[0]
        validated_data["name"] = short_department + "-"  + date + "-" + validated_data["gender"]
        return super().create(validated_data)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['title']

