from django.shortcuts import render

from getCommentFromYoutube.utillGetComment import getComments
from django.views.decorators.csrf import csrf_exempt
from django import template

import numpy as np
import pandas as pd
from openpyxl import Workbook



# 엑셀에 테이블 시트 생성
wb = Workbook(write_only=True)
ws = wb.create_sheet()

strbun = template.Library()

def inputSearchingUrl(request):
    # 메인 페이지(검색 페이지)
    return render(request, 'index.html', )


global id

@csrf_exempt
@strbun.filter("geturl")
def getCommentsFromYoutube(request):

    geturl_form = request.POST['urlbox']

    context = {
        'url': geturl_form,
    }

    global reviews

    reviews = getComments(geturl_form.split('v=')[1])

    adf = pd.DataFrame(reviews, columns=['Comments'])

    pd_data = {"댓글 내용": adf['Comments']}

    youtube_pd = pd.DataFrame(pd_data)

    id = geturl_form.split('v=')[1]

    # 엑셀 파일 저장
    youtube_pd.to_excel('getCommentFromYoutube/data/%s.xlsx' %(id))

    exec(open('getCommentFromYoutube/predict_views.py', encoding="UTF-8").read())


    # for review in reviews:
    #     print(review)
    #     print()

    return render(request, 'index2.html', context)

def send_reviews() :
    return reviews