from __future__ import unicode_literals

from django.apps import AppConfig


class MongoAdminConfig(AppConfig):
    name = 'mongoadmin'

    def ready(self):
        from mongoengine.base.fields import BaseField
        setattr(BaseField, 'rel', None)
        setattr(BaseField, 'remote_field', None)
        setattr(BaseField, 'is_relation', None)
