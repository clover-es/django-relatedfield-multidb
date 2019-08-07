from  django.conf import settings

class DatabaseAppsRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label in settings.DATABASE_APPS_MAPPING:
            return settings.DATABASE_APPS_MAPPING.get(model._meta.app_label)
        else:
            return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in settings.DATABASE_APPS_MAPPING:
            return settings.DATABASE_APPS_MAPPING.get(model._meta.app_label)
        else:
            return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_syncdb(self, db, model):
        if db in settings.DATABASE_APPS_MAPPING.values():
            return settings.DATABASE_APPS_MAPPING.get(model._meta.app_label) == db
        elif model._meta.app_label in settings.DATABASE_APPS_MAPPING:
            return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db in settings.DATABASE_APPS_MAPPING.values():
            return settings.DATABASE_APPS_MAPPING.get(app_label) == db
        elif app_label in settings.DATABASE_APPS_MAPPING:
            return False
        return None