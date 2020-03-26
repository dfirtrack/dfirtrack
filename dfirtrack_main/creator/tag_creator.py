from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone
from django_q.tasks import async_task
from dfirtrack_main.forms import TagCreatorForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Tag, System

@login_required(login_url="/login")
def tag_creator(request):
    """ function to create many tags for many systems at once (helper function to call the real function) """

    # form was valid to post
    if request.method == 'POST':
        request_post = request.POST
        request_user = request.user

        # call async function
        async_task(
            "dfirtrack_main.creator.tag_creator.tag_creator_async",
            request_post,
            request_user,
        )

        return redirect('/tag/')

    # show empty form
    else:
        form = TagCreatorForm()

        # call logger
        debug_logger(str(request.user), " TAG_CREATOR_ENTERED")
    return render(request, 'dfirtrack_main/tag/tag_creator.html', {'form': form})

def tag_creator_async(request_post, request_user):
    """ function to create many tags for many systems at once """

    # call logger
    debug_logger(str(request_user), " TAG_CREATOR_BEGIN")
                
    # extract tags (list results from request object via multiple choice field)
    tags = request_post.getlist('tag')

    # extract systems (list results from request object via multiple choice field)
    systems = request_post.getlist('system')

    # iterate over tags
    for tag_id in tags:

        # iterate over systems
        for system_id in systems:

            # create form with request data
            form = TagCreatorForm(request_post)

            # create relation
            if form.is_valid():

                # get objects
                system = System.objects.get(system_id=system_id)
                tag = Tag.objects.get(tag_id=tag_id)

                # add tag to system
                system.tag.add(tag)

                # call logger
                system.logger( str(request_user), " TAG_CREATOR_EXECUTED")

    # call logger
    debug_logger(str(request_user), " TAG_CREATOR_END")
