# coding: UTF-8
# Date: 2022/1/20
# Author: Leon

from tortoise import Model
from tortoise.fields import IntField, DateField, CharField, BooleanField, DatetimeField


class Schedule(Model):
    id = IntField(pk=True)
    create_at = DatetimeField()
    date = DatetimeField()
    work = CharField(255)
    to_who = CharField(255)
    how_to = CharField(255)
    status = CharField(255)
    comments = CharField(255)

    class Meta:
        table = 'schedule'

    def __str__(self):
        return f"User {self.id}: {self.work}"
