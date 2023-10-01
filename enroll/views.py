from django.shortcuts import render
from . forms import UserForm
# Create your views here.


def custom(request):
    if request.method == 'POST':
        show = UserForm(request.POST)
        if show.is_valid():
            print('Name: ', show.cleaned_data['name'])
            print('Email: ', show.cleaned_data['email'])
            print('Password: ', show.cleaned_data['password'])
    else:
        show = UserForm()
    return render(request, 'enroll/user.html', {'form': show})
