from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from todoapp.models import todolist,Reg,Log
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# def home(request):
#     tasks=todolist.objects.all()
#     context={'tasks':tasks}
#     return render(request,"index.html",context)

def home(request):
    
    tasks = todolist.objects.all()

    if request.method == 'POST':
        new_task = request.POST.get('new_task')
        priority = request.POST.get('priority')
        task = todolist(task_name=new_task, priority=priority)
        task.save()

    context = {'tasks': tasks}

    return render(request, 'index.html', context)

#app/views.py

def delete(request, pk):
    task = get_object_or_404(todolist, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')  # Redirect to the desired page after deletion

    context = {'task': task}
    return render(request, 'delete.html', context)


def mark_done(request, task_id):
    task = get_object_or_404(todolist, pk=task_id)
    task.is_done = not task.is_done # task.is_done= True   # Assuming your task model has a boolean field 'is_done'
    task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


    # # Toggle the 'is_done' field
    # task.is_done = not task.is_done

def register(request):
    context={}
    if request.method=="POST":
        uname=request.POST["uname"]
        upass=request.POST["upass"]
        ucpass=request.POST["ucpass"]
        if uname=="" or upass=="" or ucpass=="":
            context["errmsg"]="Fields cannot be empty"
            return render(request,"registration.html",context)
        elif upass!=ucpass:
            context["errmsg"]="password and confirm password didn't match"
            return render(request,"registration.html",context)
        else:
            try:
                u=User.objects.create(username=uname,email=uname)
                u.set_password(upass)
                u.save()
                context["success"]="User created successfully"
                return render(request,"registration.html",context)

            except Exception:
                context["success"]="user with same username already exists"
                return render(request,"registration.html",context)
    else:
        return render(request,"registration.html",context)        
    
    

def user_login(request):
    context = {}

    if request.method == "POST":
        uname = request.POST.get("uname")
        upass = request.POST.get("upass")

        if not uname or not upass:
            context["errmsg"] = "Fields cannot be empty"
            return render(request, "loginpage.html", context)

        user = authenticate(request, username=uname, password=upass)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            context["errmsg"] = "Invalid username or password"
            return render(request, "loginpage.html", context)
    else:
        return render(request, "loginpage.html", context)
    



