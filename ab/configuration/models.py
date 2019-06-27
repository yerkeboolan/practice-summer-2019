from django.db import models

# Create your models here.


class UserStatusConfigManager(models.Manager):
    pass

class UserStatusConfig(models.Model):
    status = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    # owner

    objects = UserStatusConfigManager()

    def __str__(self):
        return self.status + " " + self.is_active

    class Meta:
        ordering = ['id', 'status']


    def get_history_ent(self):
        return UserStatusConfigHistory(
            status = self.status,
            is_active = self.is_active,
            description = self.description,
            created_date = self.created_date,
            origin_id = self.pk
        )


    def save(self, *args, **kwargs):
        super(UserStatusConfig, self).save(*args, **kwargs)
        user_status_config_history = self.get_history_ent()
        user_status_config_history.is_deleted = False
        user_status_config_history.save()


    def delete(self, *args):
        user_status_config_history = self.get_history_ent()
        user_status_config_history.is_deleted = True
        user_status_config_history.save()
        super(UserStatusConfig, self).delete(*args)


class UserStatusConfigHistory(models.Model):
    status = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # owner
    origin_id = models.IntegerField()
    updated_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.status + " " + self.is_active




