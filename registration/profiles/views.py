from django.shortcuts import render,redirect
from .forms import ProfileForm
from .models import Profile


def profile(request):
    #print(request.user)
    try:
        profile=Profile.objects.get(user = request.user)
        context={'profile':profile}
    except:
        context={'errmsg': "You have no profile"}
    return render( request, "profile/profile.html",context)


def createprofile(request):
    if request.method=="POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile_obj = form.save(commit = False)
            profile_obj.user = request.user
            profile_obj.save()
            return redirect('profile')
    else:
        form = ProfileForm
    return render(request,'profile/createprofile.html',{'form':form})
