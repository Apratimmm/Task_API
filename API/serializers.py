from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import USER,TASK
from rest_framework.reverse import reverse

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


