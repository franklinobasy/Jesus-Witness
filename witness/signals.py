#!/usr/bin/env python3
'''handles user signals'''
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import (
    User,
    Editor,
    Viewer,
    EditorProfile,
    ViewerProfile
)

# viewer signals


@receiver(post_save, sender=Viewer)
def create_viewer_profile(sender, instance, created, **kwargs):
    '''creates viewer profile when viewer user is saved'''
    if created and instance.role == 'VIEWER':
        with transaction.atomic():
            ViewerProfile.objects.create(user=instance)


@receiver(post_save, sender=Viewer)
def save_viewer_profile(sender, instance, **kwargs):
    '''saves (updates) viewer profile'''
    instance.viewerprofile.save()

# editor signals


@receiver(post_save, sender=Editor)
def create_editor_profile(sender, instance, created, **kwargs):
    '''creates editor profile when viewer user is saved'''
    if created and instance.role == 'EDITOR':
        with transaction.atomic():
            EditorProfile.objects.create(user=instance)


@receiver(post_save, sender=Editor)
def save_editor_profile(sender, instance, **kwargs):
    '''saves (updates) editor profile'''
    instance.editorprofile.save()