from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# from .models import RegisterUser
from io import TextIOWrapper, StringIO

from django.shortcuts import redirect
import csv, string, random
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.forms import ValidationError


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})









# def validate_csv(value):
#     if not value.name.endswith('.csv'):
#         raise ValidationError('Invalid file type')






# @login_required
# def registerusers(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             file_name = request.FILES['file']
#             if not file_name.name.endswith('.csv'):
#                 messages.info(request, f'You need to upload a CSV file.')
#                 return redirect('registerusers')

#             else:
#                 value, fail, existing, bademail = handle_uploaded_file(request, form.cleaned_data['programs'])

#                 if value == 0 and fail == 0 and existing == 0 and bademail == 0:
#                     form = request.POST
#                     messages.error(request, 'Unarchived users to new program!')
#                     return redirect('registerusers')
#                 elif value == 0 and fail == 0 and existing == 0 and bademail > 0:
#                     form = request.POST
#                     messages.info(request, f'Number of invalid email address: {bademail}')
#                     return redirect('registerusers')
#                 elif value == 0 and fail == 0 and existing > 0 and bademail == 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account already exist: {existing}')
#                     return redirect('registerusers')
#                 elif value == 0 and fail == 0 and existing > 0 and bademail > 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account already exist: {existing}')
#                     messages.info(request, f'Number of invalid email address: {bademail}')
#                     return redirect('registerusers')
#                 elif value == 0 and fail > 0 and existing == 0 and bademail == 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account not added: {fail}')
#                     return redirect('registerusers')
#                 elif value == 0 and fail > 0 and existing == 0 and bademail > 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account not added: {fail}')
#                     messages.info(request, f'Number of invalid email address: {bademail}')
#                     return redirect('registerusers')
#                 elif value == 0 and fail > 0 and existing > 0 and bademail == 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account not added: {fail}')
#                     messages.info(request, f'Number of user-account already exist: {existing}')
#                     return redirect('registerusers')
#                 elif value == 0 and fail > 0 and existing > 0 and bademail > 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account not added: {fail}')
#                     messages.info(request, f'Number of user-account already exist: {existing}')
#                     messages.info(request, f'Number of invalid email address: {bademail}')
#                     return redirect('registerusers')

#                 elif value > 0 and fail == 0 and existing == 0 and bademail > 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account added successfully: {value}')
#                     messages.info(request, f'Number of invalid email address: {bademail}')
#                     return redirect('registerusers')
#                 elif value > 0 and fail == 0 and existing > 0 and bademail == 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account added successfully: {value}')
#                     messages.info(request, f'Number of user-account already exist: {existing}')
#                     return redirect('registerusers')
#                 elif value > 0 and fail == 0 and existing > 0 and bademail > 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account added successfully: {value}')
#                     messages.info(request, f'Number of user-account already exist: {existing}')
#                     messages.info(request, f'Number of invalid email address: {bademail}')
#                     return redirect('registerusers')
#                 elif value > 0 and fail > 0 and existing == 0 and bademail == 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account added successfully: {value}')
#                     messages.info(request, f'Number of user-account already exist: {fail}')
#                     return redirect('registerusers')
#                 elif value > 0 and fail > 0 and existing == 0 and bademail > 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account added successfully: {value}')
#                     messages.info(request, f'Number of user-account not added: {fail}')
#                     messages.info(request, f'Number of invalid email address: {bademail}')
#                     return redirect('registerusers')
#                 elif value > 0 and fail > 0 and existing > 0 and bademail == 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account added successfully: {value}')
#                     messages.info(request, f'Number of user-account not added: {fail}')
#                     messages.info(request, f'Number of user-account already exist: {existing}')
#                     return redirect('registerusers')
#                 elif value > 0 and fail > 0 and existing > 0 and bademail > 0:
#                     form = request.POST
#                     messages.info(request, f'Number of user-account added successfully: {value}')
#                     messages.info(request, f'Number of user-account not added: {fail}')
#                     messages.info(request, f'Number of user-account already exist: {existing}')
#                     messages.info(request, f'Number of invalid email address: {bademail}')
#                     return redirect('registerusers')
#                 else:
#                     form = request.POST
#                     messages.success(request, f'Number of user-account added successfully: {value}')
#                     return redirect('users')
#     else:
#         form = UploadFileForm()
#     return render(request,
#                   'account/registerusers.html',
#                   {'form': form})


# @login_required
# def aboutus(request):
#     return render(request,
#                   'account/aboutus.html',
#                   {'section': 'aboutus'})


# @login_required
# def users(request):
#     registeredUsers = User.objects.filter(is_superuser=False)
#     return render(request, 'account/viewUsers.html', {'registeredUsers': registeredUsers})


# @login_required
# def myprogram(request):
#     return render(request,
#                   'account/myprogram.html',
#                   {'section': 'myprogram'})


# @login_required
# def programs(request):
#     return render(request,
#                   'account/programs.html',
#                   {'section': 'programs'})


# @login_required
# def edit(request):
#     activated = False
#     print(request.user.profile.profile_filled)
#     if (request.user.profile.profile_filled):
#         activated = True
#     else:
#         activated = False

#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user,
#                                  data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile,
#                                        data=request.POST,
#                                        files=request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             theProfile = request.user.profile
#             theProfile.profile_filled = True
#             theProfile.save()
#             messages.success(request, 'Profile updated successfully!')
#             return redirect('edit')
#         else:
#             messages.warning(request, 'Please correct the errors below!')
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#     return render(request,
#                   'account/edit.html',
#                   {'user_form': user_form,
#                    'profile_form': profile_form,
#                    'activated': activated})


# @login_required
# def profile(request, pk):
#     pro = Profile.objects.get(user_id=pk)
#     return render(request,
#                   'account/profile.html',
#                   {'user': pro})


# @login_required
# def cms_frame(request):
#     return render(request,
#                   'account/cms_frame.html',
#                   {'section': 'cms_frame'})


# @login_required
# def django_frame(request):
#     return render(request,
#                   'account/django_frame.html',
#                   {'section': 'django_frame'})


# '''
# @login_required
# def archive(request):
#     form = UploadFileForm()
#     program = 'program_name'
#     # archive = Program.objects.all().filter(program_name=name)[0]

#     archive = User.objects.all()
#     #profilex = Profile.objects.get()
#     print(archive)
#     for archive in archive :
#         if(archive.is_superuser == False):
#             archive.is_active = False
#             archive.save()
#             #messages.success(request, 'Users archived successfully')
#         else:
#             form = UploadFileForm()
#     return render(request,
#                   'account/archive.html',
#                   {'section': 'archive', 'form': form})'''


# @login_required
# def archive(request):
#     if request.method == 'POST':
#         form = programArchiveForm(request.POST)
#         if form.is_valid():
#             theProgram = Program.objects.all().filter(program_name=form.cleaned_data['program'])[0]
#             profiles = Profile.objects.all().filter(program=theProgram)
#             for theProfile in profiles:
#                 if (theProfile.user.is_superuser == False):
#                     theUser = theProfile.user
#                     theUser.is_active = False
#                     theUser.save()
#                     messages.success(request, 'Users archived successfully')
#             return redirect('archive')
#         else:
#             messages.error(request, 'Error creating Program. Retry!')
#             # messages.success(request, 'Users archived successfully')
#     else:
#         form = programArchiveForm()
#     return render(request,
#                   'account/archive.html',
#                   {'section': 'archive', 'form': form})