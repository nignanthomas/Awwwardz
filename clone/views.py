from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile,Project,Rating
from .forms import *
# from django.http import JsonResponse
# import json
from django.db.models import Q

# Create your views here.

def index(request):
    user = request.user
    return render(request,'index.html',{"user":user})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        results = Project.filter_by_search_term(search_term)
        message=f"Search results for: {search_term}"
        return render(request,'search.html',{"message":message,"results":results})

    else:
        message="You haven't searched for any term."
        return render(request,'search.html',{"message":message})




@login_required(login_url='/accounts/login/')
def profile(request,id):
    user_object = request.user
    current_user = Profile.objects.get(username__id=request.user.id)
    user = Profile.objects.get(username__id=id)
    projects = Project.objects.filter(upload_by = user)
    return render(request, "profile.html", {"current_user":current_user,"projects":projects,"user":user,"user_object":user_object,})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = Profile.objects.get(username__id=request.user.id)
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.upload_by = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})



@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    user_edit = Profile.objects.get(username__id=current_user.id)
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            print('success')
    else:
        form=ProfileForm(instance=request.user.profile)
        print('error')


    return render(request,'edit_profile.html',locals())
