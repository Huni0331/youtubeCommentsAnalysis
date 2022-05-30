from django.shortcuts import render

from getCommentFromYoutube.utillGetComment import getComments
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

    global reviews

    reviews = getComments(geturl_form.split('v=')[1])

    return render(request, 'index2.html', context)

# predict_views.py 로 reviews 를 보낼 때, 사용하는 함수
def send_reviews() :
    return reviews