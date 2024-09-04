from rest_framework import serializers

from habit.models import Habit
from habit.validators import RewardValidator, RelatedHabitValidator, DurationTimeValidator, PleasantHabitValidator, \
    RegularityValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = (RewardValidator(field1="reward", field2="related_habit"),
            RelatedHabitValidator(field="related_habit"),
            DurationTimeValidator(field="duration"),
            PleasantHabitValidator(field="is_pleasant"),
            RegularityValidator(field1="frequency_number", field2="frequency_unit"),
        )