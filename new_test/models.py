from django.db import models
from user_profile.models import User

# Create your models here.

#Create your models here.

# class Group_Test(models.Model):
#     name = models.CharField(max_length=100)
#     theme = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name, self.theme
#
#
# class Test(models.Model):
#     group_test = models.ForeignKey(Group_Test)
#     name = models.CharField(max_length=500)
#     theme = models.CharField(max_length=500)
#     result = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.name
#
#
#
# class Question(models.Model):
#     test = models.ForeignKey(Test)
#     name = models.CharField(max_length=500)
#     answer_1 = models.CharField(max_length=100)
#     answer_2 = models.CharField(max_length=100)
#     answer_true = models.CharField(max_length=100)
#     result = models.IntegerField(default=0)
#
#     def true_answer(self,answer):
#         if self.answer_true == answer:
#             self.result += 1
#             return self.result
#
#
#
#
#     def __str__(self):
#         return self.name
#
#
