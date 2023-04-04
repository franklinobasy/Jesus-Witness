from django.shortcuts import redirect, render
from django.contrib import messages

from witness.forms import EditorCreationForm, ViewerCreationForm


def register(request):
    return render(request, 'witness/register.html')


def register_viewer(request):
    if request.method == 'POST':
        form = ViewerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {first_name}')
            return redirect('login')
    else:
        form = ViewerCreationForm()
    return render(request, 'witness/register-viewer.html', {'form': form})


def register_editor(request):
    if request.method == 'POST':
        form = EditorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {first_name}')
            return redirect('login')
    else:
        form = EditorCreationForm()
    return render(request, 'witness/register-editor.html', {'form': form})
