import django_setup
from scheduleapp.models import Grade, Group , Teacher , Schedule

all_grades = Grade.objects.all()

for grade in all_grades:
    print(f"{grade.student.name} got {grade.get_value_display()} in {grade.subject.name}")

#create schedule
group_id = int(input("enter group id"))
group = Group.objects.get(id=group_id)

teacher_name = input("enter teache name")
teacher = Teacher.objects.get(name=teacher_name)

import datetime
now = datetime.datetime.time(datetime.datetime.now())
Schedule.objects.create(time = now, group=group,teacher=teacher)
