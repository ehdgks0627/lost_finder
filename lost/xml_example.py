import xml.etree.ElementTree as ET
import requests
from my_api_key import api_key_OA124  # set your own key here

s = requests.Session()
types = {
    "bus": "b1",
    "village bus": "b2",
    "taxi": "t1",
    "personal taxi": "t2",
    "subway1~4": "s1",
    "subway5~8": "s2",
    "korail": "s3",
    "subway9": "s4"
}

page_start = 1
page_end = 5
url = "http://openAPI.seoul.go.kr:8088/%s/xml/ListLostArticleService/%d/%d/%s/" % (
api_key_OA124, page_start, page_end, types["taxi"])
r = s.get(url)
data = r.text

tree = ET.fromstring(data)
print("총 데이터 건수 : %s" % (tree.find("list_total_count").text if tree.find("list_total_count").text else ""))
result = tree.find("RESULT")
print("요청결과 코드 : %s" % result.find("CODE").text if result.find("CODE").text else "")
print("요청결과 메세지 : %s" % result.find("MESSAGE").text if result.find("MESSAGE").text else "")
print()
print("물품 내역")
for row in tree.iter("row"):
    print("분실물 ID : %s" % (row.find("ID").text if row.find("ID").text else ""))
    print("습득물품명 : %s" % (row.find("GET_NAME").text if row.find("GET_NAME").text else ""))
    print("원문링크주소(지하철) : %s" % (row.find("URL").text if row.find("URL").text else ""))
    print("습득물분류 : %s" % (row.find("TITLE").text if row.find("TITLE").text else ""))
    print("습득일자 : %s" % (row.find("GET_DATE").text if row.find("GET_DATE").text else ""))
    print("수령가능장소 : %s" % (row.find("TAKE_PLACE").text if row.find("TAKE_PLACE").text else ""))
    print("수령가능장소연락처 : %s" % (row.find("CONTACT").text if row.find("CONTACT").text else ""))
    print("습득물분류 : %s" % (row.find("CATE").text if row.find("CATE").text else ""))
    print("습득위치_회사명 : %s" % (row.find("GET_POSITION").text if row.find("GET_POSITION").text else ""))
    print("습득위치(지하철) : %s" % (row.find("GET_PLACE").text if row.find("GET_PLACE").text else ""))
    print("습득물품_상세 : %s" % (row.find("GET_THING").text if row.find("GET_THING").text else ""))
    print("분실물상태 : %s" % (row.find("STATUS").text if row.find("STATUS").text else ""))
    print("습득물품코드 : %s" % (row.find("CODE").text if row.find("CODE").text else ""))
    print("이미지 URL : %s" % (row.find("IMAGE_URL").text if row.find("IMAGE_URL").text else ""))
    print()
    print()
