from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .models import Response

# Pagination Stuff
from django.core.paginator import Paginator


@login_required
def tweetsHome(request):
    responses = Response.objects.filter(
        user_id=request.user).select_related('tweet_id').order_by("-id")
    total_records = responses.count()

    # Setup pagination
    RECORDS_PER_PAGE = 25
    paginator = Paginator(responses, RECORDS_PER_PAGE)
    curr_page = request.GET.get('page')
    if curr_page is None:
        curr_page = 1
    else:
        try:
            # default is string
            curr_page = int(curr_page)
        except ValueError:
            # django automatically shows page 1 if not integer
            # thus we will also use page = 1
            curr_page = 1

    current_page_responses = paginator.get_page(curr_page)

    # showing pagination as per current page
    start = 1
    end = current_page_responses.paginator.num_pages

    if curr_page > end:
        # django automatically shows last page if page value is exceeded
        # thus we will also use page = end
        curr_page = end

    PAGINATION_GAP = 4
    MAX_PAGINATION_NUMBERS = 9

    if (end - start) > MAX_PAGINATION_NUMBERS:
        new_start = curr_page - PAGINATION_GAP
        new_end = curr_page + PAGINATION_GAP

        if new_end > end:
            start = new_start - (new_end - end)
        elif new_start < 1:
            end = new_end + (abs(start - new_start))
        else:
            start = new_start
            end = new_end
    # // showing pagination as per current page

    return render(request,
                  'tweets/index.html',
                  {
                      'responses': responses,
                      'active_page': 'tweets',
                      'current_page_responses': current_page_responses,
                      'start': start,
                      'end': end,
                      'total_records': total_records,
                  })
