import csv,io
from csv import reader
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db import transaction
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from .models import UserType
@transaction.atomic



# Create your views here.
def BulkStudentRegistrationView(request):
    prompt = {'Order' : 'Order of the CSV should be name, contact_number'}
    if request.method == 'GET':
        return render(request,'bulkregistration.html',prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a CSV File')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    for column in csv.reader(io_string,delimiter=",",quotechar = "|"):
        user = UserType.objects.create_user(
                username = column[1],
                password = column[1],

        )
    
    user.save()
    print('success')
    # messages.info(request,'File has been uploaded')
    return render(request,'register.html')