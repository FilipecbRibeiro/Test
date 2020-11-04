from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Signals
# There are two key elements in the signals: the senders and the receivers
# The sender is the one responsible to dispatch a signal
# A sender must be either a Python object, or None to receive signals
# The receiver is the one will receive this signal and then do something
# A receiver must be a function or an instance method which is to receive signals

# The connection between the senders and the receivers is done through "signal dispatchers"
# Which are instances of Signal, via the connect method


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'PROFILE'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return str(self.user)


def create_profile(sender, instance, created, **kwargs):
    # whenever signal calls this method/this receiver we are going to check if this is the first instance
    # (created it's a boolean that it will be True if a new record was created! )
    # if it is we are going ahead and create a new Profile
    # Ver de novo !!!!
    print("entro no create_profile")
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
# this connects the receiver to the sender
# every single time the save method is called it's going to trigger the method on receiver after the save is completed
# and listen to the model on the sender


def update_profile(sender, instance, created, **kwargs):
    print("entro no update_profile")
    if created is False:
        instance.profile.save()
        # this is where it will be logic
        print("Profile updated!")


post_save.connect(update_profile, sender=User)


# @models.permalink
# def get_absolute_url(self):
#     return('item', (), {'pk': self.id, 'slug':self.slug})

# def __unicode(self):
#     return self.title
