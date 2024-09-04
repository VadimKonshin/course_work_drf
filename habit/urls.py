from django.urls import path

from habit.apps import HabitConfig
from rest_framework.routers import SimpleRouter

from habit.views import HabitViewSet, PublicHabitListAPIView

app_name = HabitConfig.name

router = SimpleRouter()
router.register("", HabitViewSet, basename="habit")

urlpatterns = [
    path("public/", PublicHabitListAPIView.as_view(), name="public"),
] + router.urls