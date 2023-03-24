# Import the necessary modules
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Picture, Document

# Define the view function
def approve_file(request, file_type, file_id):
    if request.method == 'POST':
        if file_type == 'picture':
            file = get_object_or_404(Picture, id=file_id)
        elif file_type == 'document':
            file = get_object_or_404(Document, id=file_id)
        else:
            return HttpResponseRedirect('/')

        file.approved = True
        file.save()

        return HttpResponseRedirect('/')

    else:
        if file_type == 'picture':
            file = get_object_or_404(Picture, id=file_id)
        elif file_type == 'document':
            file = get_object_or_404(Document, id=file_id)
        else:
            return HttpResponseRedirect('/')

        return render(request, 'approve_file.html', {'file': file})
