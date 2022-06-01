from django.shortcuts import render

from getCommentFromYoutube.utillGetComment import getComments, getThumbnail
from django.views.decorators.csrf import csrf_exempt
from django import template

strbun = template.Library()

def inputSearchingUrl(request):
    # 메인 페이지(검색 페이지)
    return render(request, 'index.html', )

@csrf_exempt
@strbun.filter("geturl")
def getCommentsFromYoutube(request):

    geturl_form = request.POST['urlbox']

    context = {
        'url': geturl_form,
    }

    cm = getComments(geturl_form.split('v=')[1])
    for review in cm:
        print(review)
        print()

    print("댓글 끝")

    gettitle, getimage = getThumbnail(geturl_form.split('v=')[1])
    print(gettitle)
    print(getimage)

    return render(request, 'index2.html', context)