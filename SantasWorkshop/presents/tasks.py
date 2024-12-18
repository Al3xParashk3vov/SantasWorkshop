from celery import shared_task


@shared_task
def create_user_profile_task(sender, instance, created, **kwargs):
    if created:
        create_user_profile.delay(instance.Profile)
