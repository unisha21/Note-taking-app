# notetaking/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notetaking/note_list.html', {'notes': notes})


@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notetaking/note_detail.html', {'note': note})


@login_required
def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notetaking/note_new.html', {'form': form})


@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notetaking/note_edit.html', {'form': form})


@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note_list')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('note_list')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
