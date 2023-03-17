#!/urs/bin/env python3
'''forms for users and their profiles are defined here'''
from django.contrib.auth.forms import UserCreationForm
from .models import (
    User,
    Viewer,
    Editor,
    ViewerProfile,
    EditorProfile
)
from django import forms


class ViewerCreationForm(UserCreationForm):
    '''Defines form for Viewer Creation
    Args:
        UserCreationForm (form): built in django class for user creation
        - This form inherits from it
    Returns:
        user (viewer) object: Returns the created viewer object on save
    '''

    username = forms.CharField(
        label='Username',
        max_length=20,
        required=True,
        help_text="Enter a unique username"
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        help_text='Enter your email address'
    )

    password1 = forms.CharField(
        label='Password',
        help_text='Enter a password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'},),
        required=True
    )

    password2 = forms.CharField(
        label='Confirm Password',
        help_text='Enter password again',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )

    first_name = forms.CharField(
        label='First Name',
        help_text='What is your first name',
        required=True
    )

    last_name = forms.CharField(
        label='Last Name',
        help_text='What is your last name',
        required=True
    )

    class Meta:
        '''defines meta data for form
        - model: assigns associated proxy model
                (i.e extends User model), Viewer
        - fields: rendered fields on form in web page
        '''
        model = Viewer
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def save(self, commit=True):
        '''assigns role to user (viewer) and saves to database
        Args:
            commit (bool, optional): saves user to db. Defaults to True.
        Returns:
            created user: viewer object
        '''
        user = super().save(commit=False)
        user.role = "VIEWER"
        if commit:
            user.save()
        return user


class ViewerUpdateForm(forms.ModelForm):
    '''Defines form to update viewer
    Args:
        forms (ModelForm): inbuilt django ModelForm
        (optimized to work with existing models in db)
    '''
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    username = forms.CharField(
        help_text='Change username'
    )

    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Change First name'
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Change Last name'
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=True,
        help_text="Select your gender"
    )

    class Meta:
        '''Defines form metadata including:
        - associated proxy model (extends User model): Viewer
        - fields: These appear on the form when page is rendered
        '''
        model = Viewer
        fields = ['username', 'email', 'first_name', 'last_name', 'gender']


class ViewerProfileUpdateForm(forms.ModelForm):
    '''defines form for updating viewer profile

    Args:
        forms (ModelForm): inbuilt ModelForm object
    '''
    class Meta:
        '''Defines Meta Data for form:
        - model: Defines associated model (ViewerProfile)
        - fields: fields to be rendered on the web page
        '''
        model = ViewerProfile

        fields = ['bio', 'picture']


class EditorCreationForm(UserCreationForm):
    '''Defines form for Editor Creation
    Args:
        UserCreationForm (form): built in django class for user creation
        - This form inherits from it
    Returns:
        user (editor) object: Returns the created editor object on save
    '''

    username = forms.CharField(
        label='Username',
        max_length=20,
        required=True,
        help_text="Enter a unique username"
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        help_text='Enter your email address'
    )

    password1 = forms.CharField(
        label='Password',
        help_text='Enter a password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'},),
        required=True
    )

    password2 = forms.CharField(
        label='Confirm Password',
        help_text='Enter password again',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )

    first_name = forms.CharField(
        label='First Name',
        help_text='What is your first name',
        required=True
    )

    last_name = forms.CharField(
        label='Last Name',
        help_text='What is your last name',
        required=True
    )

    class Meta:
        '''defines meta data for form
        - model: assigns associated proxy model
                (i.e extends User model), Editor
        - fields: rendered fields on form in web page
        '''
        model = Editor
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def save(self, commit=True):
        '''assigns role to user (editor) and saves to database
        Args:
            commit (bool, optional): saves user to db. Defaults to True.
        Returns:
            created user: editor object
        '''
        user = super().save(commit=False)
        user.role = "EDITOR"
        if commit:
            user.save()
        return user


class EditorUpdateForm(forms.ModelForm):
    '''Defines form to update editor
    Args:
        forms (ModelForm): inbuilt django ModelForm
        (optimized to work with existing models in db)
    '''
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    username = forms.CharField(
        help_text='Change username'
    )

    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Change First name'
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Change Last name'
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=True,
        help_text="Select your gender"
    )

    class Meta:
        '''Defines form metadata including:
        - associated proxy model (extends User model): Editor
        - fields: These appear on the form when page is rendered
        '''
        model = Editor
        fields = ['username', 'email', 'first_name', 'last_name', 'gender']


class EditorProfileUpdateForm(forms.ModelForm):
    '''defines form for updating editor profile

    Args:
        forms (ModelForm): inbuilt ModelForm object
    '''
    class Meta:
        '''Defines Meta Data for form:
        - model: Defines associated model (EditorProfile)
        - fields: fields to be rendered on the web page
        '''
        model = EditorProfile

        fields = ['bio', 'picture']