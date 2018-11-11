from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from dfirtrack_main.logger.default_logger import debug_logger

@login_required(login_url="/login")
def about(request):

    # call logger
    debug_logger(str(request.user), ' ABOUT_ENTERED')

    # show page
    return render(request, 'dfirtrack_main/about.html')

@login_required(login_url="/login")
def faq(request):

    # call logger
    debug_logger(str(request.user), ' FAQ_ENTERED')

    # show page
    return render(request, 'dfirtrack_main/faq.html')
