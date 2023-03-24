# create a view to display a list of approved or unapproved Picture or Document objects based on the user's role.

# Import the necessary modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Picture, Document, UserRole

# Define the view function
@login_required
def file_list(request, approved):
    user_roles = UserRole.objects.filter(user=request.user)
    file_list = []
    for user_role in user_roles:
        if user_role.role.name == 'admin':
            if approved == 'approved':
                file_list += Picture.objects.filter(approved=True)
                file_list += Document.objects.filter(approved=True)
            elif approved == 'unapproved':
                file_list += Picture.objects.filter(approved=False)
                file_list += Document.objects.filter(approved=False)
        elif user_role.role.name == 'field_manager':
            if approved == 'approved':
                file_list += Picture.objects.filter(approved=True, field_manager=request.user)
                file_list += Document.objects.filter(approved=True, field_manager=request.user)
            elif approved == 'unapproved':
                file_list += Picture.objects.filter(approved=False, field_manager=request.user)
                file_list
