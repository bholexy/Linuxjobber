from django.db import models
from django.contrib.auth.models import User


class GoalStatus(models.Model):
	status_name = models.CharField(max_length = 200)


class ScrumyGoals(models.Model):
	user = models.ForeignKey(User, related_name = '+', on_delete = models.CASCADE)
	goal_name = models.CharField(max_length =  200)
	goal_id = models.IntegerField()
	created_by = models.CharField(max_length = 200)
	moved_by = models.CharField(max_length = 200)
	owner = models.CharField(max_length = 200)
	goal_status = models.ForeignKey(GoalStatus, on_delete = models.PROTECT)
	



class ScrumyHistory(models.Model):
	created_by = models.CharField(max_length = 200)
	moved_by = models.CharField(max_length = 200)
	moved_from = models.CharField(max_length = 200)
	moved_to = models.CharField(max_length = 200)
	time_of_action = models.DateTimeField()
	goal = models.ForeignKey(ScrumyGoals, on_delete = models.CASCADE)