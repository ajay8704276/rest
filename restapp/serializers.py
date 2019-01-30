from rest_framework import serializers

from restapp.models import Task
from django.contrib.auth import get_user_model


class TaskSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Task
        fields = ('id', 'task_name', 'task_desc', 'task_completed', 'task_date_created','image')


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validate_data):
        user = get_user_model().objects.create(
            username = validate_data['username']
        )

        user.set_password(validate_data['password'])
        user.save()
        return user
    class Meta:
        model = get_user_model()
        fields = ('username','password')

