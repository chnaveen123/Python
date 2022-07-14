import re

url = "www.google.com / search='%new hindi movies?' % / get_data2019 / fetch_data frm_1 / imdb? %hindi%movies$& / result = page1.aspx"

res = re.findall(r'(/^.*//)', url)

if res:


    print("Match founded")
    print(f"String that did't match : {url[:res.start()]}")
    print(f"string that matched :  {url[res.start():res.end()]}")
    print(f"string that is not checked :{url[res.end():]}")

else:
    print("Match not found")


    9492487489