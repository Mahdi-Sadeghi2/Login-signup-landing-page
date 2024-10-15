# from django.db import models
# from django.contrib.auth.hashers import make_password
# # Create your models here.


# class UserModel(models.Model):
#     user_name = models.CharField(
#         max_length=225, help_text="Enter your username")
#     email = models.EmailField()
#     date_created = models.DateTimeField(auto_now_add=True)
#     phone_number = models.IntegerField(
#         max_length=11, help_text="Enter your cellphone number(with zero)")
#     password = models.CharField(
#         max_length=15, help_text="Enter your password(max length 15 characters)")

#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)

#     def __str__(self):
#         return self.user_name
