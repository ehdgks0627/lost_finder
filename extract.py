from konlpy.tag import Twitter
import sys
import json

twitter = Twitter()
with open(sys.argv[1]) as f:
    datas = json.loads(f.read())
result = []
for data in datas:
    result.append(twitter.nouns(data))
print(str(result).replace("'",'"'))
