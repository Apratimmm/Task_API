from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import USER,TASK
from .serializers import UserSerializer, TaskSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class Simple_Pagination(PageNumberPagination):
    page_size = 5                       #default
    page_query_param = 'page_no'        #url
    page_size_query_param = 'size'      #url
    max_page_size = 8

class Offset_Pagination(LimitOffsetPagination):
    default_limit = 5                   #size
    limit_query_param = 'size'          #url
    offset_query_param = 'index'        #url
    max_limit = 7                       #in_a_page

class show_users(ModelViewSet):
    'Shows the user(s) registered in the database'

    serializer_class = UserSerializer
    queryset = USER.objects.all()
    lookup_field = "user_name"
    pagination_class = Offset_Pagination
    throttle_scope = 'users'


class show_tasks(ModelViewSet):
    'Shows the task(s) registered in the database'

    serializer_class = TaskSerializer
    queryset = TASK.objects.all()
    lookup_field = "task_id"
    pagination_class = Simple_Pagination
    throttle_scope = 'tasks'

    filterset_fields = {
                            'status':['exact','in'],
                            'priority':['exact','in'],
                            'assigned_by':['exact','in'],
                            'assigned_to':['exact','in'],
                            'task_name':['exact','icontains']
                        }

    # def get_queryset(self):
    #
    #     queryset = TASK.objects.all()
    #     status = self.request.query_params.get('status')
    #     priority = self.request.query_params.get('priority')
    #     by = self.request.query_params.get('by')
    #     to = self.request.query_params.get('to')
    #
    #     if status:
    #         queryset = queryset.filter(status__in=status.split(','))
    #
    #     if priority:
    #         queryset = queryset.filter(priority__in=priority.split(','))
    #
    #     if by:
    #         queryset = queryset.filter(assigned_by__in=by.split(','))
    #
    #     if to:
    #         queryset = queryset.filter(assigned_to__in=to.split(','))
    #
    #     return queryset
