from konlpy.tag import Twitter
import sys
import json

twitter = Twitter()
print(str(twitter.nouns(sys.argv[1])).replace("'",'"'))
