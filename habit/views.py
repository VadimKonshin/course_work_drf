from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginations import HabitPaginator
from habit.permissions import IsOwner
from habit.serializer import HabitSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(operation_description="Список привычек")
)

class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = (IsOwner, IsAuthenticated)
    pagination_class = HabitPaginator
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ("action",)
    ordering_fields = ("time",)

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user.pk).order_by('id')

class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitPaginator