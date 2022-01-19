# coding: UTF-8
# Date: 2022/1/20
# Author: Leon

from tortoise import Model
from tortoise.fields import IntField, DateField, CharField, BooleanField


class User(Model):
    id = IntField(pk=True)
    username = CharField(64)
    password = CharField(64)
    email = CharField(255)
    is_admin = BooleanField()
    avatar = CharField(255)

    class Meta:
        table = 'user'

    def __str__(self):
        return f"User {self.id}: {self.username}: {'admin group' if self.is_admin else 'user group'}"

    def to_dict(self):
        return dict(
            {
                "id": self.id,
                "username": self.username,
                "password": self.password,
                "email": self.email,
                "is_admin": self.is_admin,
                "avatar": self.avatar
            }
        )
