from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField, ValidationError
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import USER,TASK
from rest_framework.reverse import reverse
from django.contrib.auth.models import User as auth_user

class UserSerializer(ModelSerializer):

    assigned_to = SerializerMethodField()

    def get_assigned_to(self, obj):
        request = self.context['request']
        base_url = reverse('task-list',request=request)
        final_url = f"{base_url}?assigned_to={obj.user_name}"
        return final_url

    assigned_by = SerializerMethodField()

    def get_assigned_by(self, obj):
        request = self.context['request']
        base_url = reverse('task-list',request=request)
        final_url = f"{base_url}?assigned_by={obj.user_name}"
        return final_url

    class Meta:
        model = USER
        fields = ['user_id','user_name','assigned_by','assigned_to']


class TaskSerializer(ModelSerializer):

    class Meta:
        model = TASK
        fields = '__all__'

class RegisterSerializer(ModelSerializer):

    class Meta:
        model = auth_user
        fields = ['username','password','confirm_password']

    password = CharField(required=True, write_only=True)
    confirm_password = CharField(required=True, write_only=True)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Passwords must match')
        return attrs

    def create(self, validated_data):
        user = auth_user.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user