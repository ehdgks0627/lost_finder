import json
import subprocess
from operator import itemgetter

import requests
from django.forms.models import model_to_dict
from django.shortcuts import render
from gensim.models.word2vec import Word2Vec

from .models import *
from .my_api_key import api_key_OA124  # set your own key here

model = Word2Vec.load("word2vec.model")

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

ERR_MSG_NO_DATA = "해당하는 데이터가 없습니다."

def nouns(x):
    with open("data", "w") as f:
        f.write(json.dumps(x))
    output = subprocess.check_output(["python3", "/home/sprout/Desktop/lost_finder/extract.py", "data"])
    with open("result", "w") as f:
        f.write(output.decode())
    return json.loads(output.decode())


def lost_update(request):
    s = requests.Session()
    for lost_type in wb_code.values():
        idx = 1
        print("Parsing %s type" % (lost_type))
        while True:
            url = "http://openAPI.seoul.go.kr:8088/%s/json/ListLostArticleService/%d/%d/%s/" % (
                api_key_OA124, idx, idx + 999, lost_type)
            print("request %s" % (url))
            r = s.get(url)
            lost_data = json.loads(r.text)
            if "ListLostArticleService" in lost_data.keys() and "list_total_count" in lost_data[
                "ListLostArticleService"].keys():  # 정상 응답
                rows = lost_data["ListLostArticleService"]["row"]
                if len(rows) == 0:  # 항목이 더이상 없을경우
                    break
                else:  # 항목이 있으면
                    data = []
                    for row in rows:
                        data.append(row["GET_NAME"])
                    words = nouns(data)
                    for i in range(len(rows)):
                        if not rows[i].get("GET_NAME"):
                            continue
                        try:
                            Item.objects.create(it_name=rows[i].get("GET_NAME"),
                                                it_id=int(rows[i].get("ID")),
                                                it_url=rows[i].get("URL"),
                                                it_title=rows[i].get("TITLE"),
                                                it_get_date=rows[i].get("GET_DATE"),
                                                it_take_place=rows[i].get("TAKE_PLACE"),
                                                it_contact=rows[i].get("CONTACT"),
                                                it_cate=rows[i].get("CATE"),
                                                it_get_position=rows[i].get("GET_POSITION"),
                                                it_get_place=rows[i].get("GET_PLACE"),
                                                it_get_thing=rows[i].get("GET_THING"),
                                                it_status=rows[i].get("STATUS"),
                                                it_code=rows[i].get("CODE"),
                                                it_image_url=rows[i].get("IMAGE_URL"),
                                                it_drive_num=rows[i].get("DRIVE_NUM"),
                                                it_get_nm=rows[i].get("GET_NM"),
                                                words=str(words[i]))
                        except:
                            continue

            elif "RESULT" in lost_data.keys() and lost_data["RESULT"]["MESSAGE"] == ERR_MSG_NO_DATA:  # 조회결과가 없을경우
                break
            idx += 1000
    context = []
    return render(request, 'lost/lost_list_OA124.html', context)


def lost_list(request):
    def compare_string(words1, words2):
        result = 0.0
        cnt = 0
        for word1 in words1:
            for word2 in words2:
                try:
                    result += model.similarity(word1, word2)
                    cnt += 1
                except:
                    pass
        if cnt:
            return result / cnt
        else:
            return 0.0

    keyword = request.GET.get("keyword", "")
    keyword_words = json.loads(subprocess.check_output(["python", "./extract_output.py", keyword]).decode())

    vector = []
    for item in Item.objects.all()[:10000]:
        vector.append((item, compare_string(item.words, keyword_words)))
    vector.sort(key=itemgetter(1))

    context = {
        "lost_data": map(lambda x: model_to_dict(x[0]), vector)
    }
    return render(request, 'lost/lost_list.html', context)


def lost_search(request):
    context = {
        "wb_code": wb_code,
        "cate": cate,
        "page_start": 1,
        "page_end": 10,
    }
    return render(request, 'lost/index.html', context)
