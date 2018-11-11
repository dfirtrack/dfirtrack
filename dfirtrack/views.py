from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

def login_redirect(request):
    return redirect('/login')

@login_required(login_url="/login")
def page_400(request):
    data = {}
    return render(request, 'dfirtrack_main/400.html', data)

@login_required(login_url="/login")
def page_403(request):
    data = {}
    return render(request, 'dfirtrack_main/403.html', data)

@login_required(login_url="/login")
def page_404(request):
    data = {}
    return render(request, 'dfirtrack_main/404.html', data)

@login_required(login_url="/login")
def page_500(request):
    data = {}
    return render(request, 'dfirtrack_main/500.html', data)
