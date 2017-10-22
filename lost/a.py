import requests
import json
from django import template
from django.shortcuts import render
from .my_api_key import api_key_OA123, api_key_OA124  # set your own key here


wb_code = {
    "버스": "b1",
    "마을버스": "b2",
    "법인택시": "t1",
    "개인택시": "t2",
    "지하철(1~4)": "s1",
    "지하철(5~8)": "s2",
    "코레일": "s3",
    "지하철(9)": "s4"
}

cate = {
    "전체": "전체",
    "가방": "가방",
    "배낭": "베낭",
    "서류봉투": "서류봉투",
    "쇼핑백": "쇼핑백",
    "옷": "옷",
    "지갑": "지갑",
    "책": "책",
    "파일": "파일",
    "핸드폰": "핸드폰",
    "기타": "기타",
}

def lost_update(request):
    s = requests.Session()
    for lost_type in wb_code.itervalues():
        url = "http://openAPI.seoul.go.kr:8088/%s/json/ListLostArticleService/%d/%d/%s/" % (
            api_key_OA124, page_start, page_end, lost_type)
        r = s.get(url)
        lost_data = json.loads(r.text)
    return render(request, 'lost/lost_list_OA124.html', context)

def lost_list(request):
    lost_type = request.GET.get("lost_type", "b1")
    lost_cate = request.GET.get("lost_cate", "전체")
    page_start = int(request.GET.get("start", 1))
    page_end = int(request.GET.get("end", 10))
    keyword = request.GET.get("keyword", "")

    if lost_cate == "전체" and not keyword:
        #lost_data = 
        context = {
            "lost_data": lost_data,
            "page_start": page_start,
            "page_end": page_end,
            "wb_code": wb_code,
            "lost_type": lost_type,
            "cate": cate,
            "lost_cate": lost_cate
        }
        return render(request, 'lost/lost_list_OA124.html', context)
    else:
        #lost_data = 
        context = {
            "lost_data": lost_data,
            "page_start": page_start,
            "page_end": page_end,
            "wb_code": wb_code,
            "lost_type": lost_type,
            "cate": cate,
            "lost_cate": lost_cate,
            "keyword": keyword
        }
        return render(request, 'lost/lost_list_OA123.html', context)


def lost_search(request):
    context = {
        "wb_code": wb_code,
        "cate": cate,
        "page_start": 1,
        "page_end": 10,
    }
    return render(request, 'lost/search.html', context)
