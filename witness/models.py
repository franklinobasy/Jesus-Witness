from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    Group,
    Permission
)
from django.contrib import admin


def profile_image_path(instance, filename):
    # uploads profile images to profiles/<username>/<filename>
    return 'profiles/{0}/{1}'.format(instance.username, filename)

class User(AbstractUser):
    '''defines our custom AUTH_USER_MODEL
    (see settings.py; line 137)
    Args:
        AbstractUser (AbstractUser): custom User parent
    '''
    class Role(models.TextChoices):
        '''defines roles for users
        Args:
            models (TextChoices): Defines the role choices for users
        '''
        EDITOR = 'EDITOR', 'Editor'
        VIEWER = 'VIEWER', 'Viewer'

    class Gender(models.TextChoices):
        NONE = 'NONE', 'None',
        MALE = "MALE", "Male",
        FEMALE = "FEMALE", "Female"
        

    # Role.choices here constrains user to only select one of these
    # listed choices.
    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.VIEWER
    )

    first_name = models.CharField(
        max_length=20,
        null=False
    )

    last_name = models.CharField(
        max_length=20,
        null=False
    )

    gender = models.CharField(
        max_length=50,
        choices=Gender.choices,
        default=Gender.NONE
    )

# For editors


class EditorManager(BaseUserManager):
    '''manager for editor proxy table
    Args:
        BaseUserManager (BaseUserManager): Editor manager
    '''

    def get_queryset(self, *args, **kwargs):
        '''helps query data belonging to users with role editor
        Returns:
            Editor: editor objects from user table
        '''
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.EDITOR)


class Editor(User):
    '''Defines the editor proxy model
    Args:
        User (User): Custom AUTH_USER_MODEL
    Returns:
        editor: created user(editor) object
    '''
    base_role = User.Role.EDITOR

    editor = EditorManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "only for editors"

    def save(self, *args, **kwargs):
        '''saves editor object and adds it to group; editors
        '''
        super().save(*args, **kwargs)

        editors_group, created = Group.objects.get_or_create(name="Editors")

        # add group permissions here

        self.groups.add(editors_group)

    def delete(self, *args, **kwargs):
        '''removes editor object from group before calling parent delete method
        This is done to prevent a foreign key constraint with the groups table
        '''
        self.groups.remove(Group.objects.get(name='editors'))
        super().delete(*args, **kwargs)


class EditorProfile(models.Model):
    '''defines methods and attributes for editor
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="Jesus loves me!")
    picture = models.ImageField(
            upload_to=profile_image_path,
            default='profiles/default.png'
        )
    # add more editor profile data

    def __str__(self):
        return f"{self.user.username} profile"


# For Property Owners
class ViewerManager(BaseUserManager):
    '''Manages Owners in User table
    Args:
        BaseUserManager (BaseUserManager): in built django method
        for managing users
    '''

    def get_queryset(self, *args, **kwargs):
        '''returns viewer objects from user table
        Returns:
            User: viewer objects
        '''
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.VIEWER)


class Viewer(User):
    '''Defines the viewer proxy model
    Args:
        User (User): Custom AUTH_USER_MODEL
    Returns:
        viewer: created user(viewer) object
    '''
    base_role = User.Role.VIEWER
    viewer = ViewerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "only for viewers"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        viewers_group, created = Group.objects.get_or_create(name="Viewers")

        # add group permissions here

        self.groups.add(viewers_group)


class ViewerProfile(models.Model):
    '''defines viewer profile and establishes a
    one to one relationship with corresponding viewer
    Args:
        models (Model): inbuilt django Model class
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="Jesus loves me!")
    picture = models.ImageField(
            upload_to=profile_image_path,
            default='profiles/default.png'
        )
    # add more viewer profile data

    def __str__(self):
        return f"{self.user.username} profile"


# customize viewer admin panel


class EditorAdmin(admin.ModelAdmin):
    '''adds viewer details to admin panel
    Args:
        admin (ModelAdmin): built-in django Admin model
    '''
    list_display = ('username', 'email', 'first_name',
                    'last_name')
    
class ViewerAdmin(admin.ModelAdmin):
    '''adds viewer details to admin panel
    Args:
        admin (ModelAdmin): built-in django Admin model
    '''
    list_display = ('username', 'email', 'first_name',
                    'last_name')