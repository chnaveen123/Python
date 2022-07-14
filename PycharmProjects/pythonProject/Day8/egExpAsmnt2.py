import urllib.parse
url = "www.google.com / search='%new hindi movies?' % / get_data2019 / fetch_data frm_1 / imdb? %hindi%movies$& / result = page1.aspx"
parsed = urllib.parse.urlsplit(url)
print("{}?{}".format(parsed.path.split("/")[0:4], parsed.query))
print("{}?{}".format(parsed.path.split("/")[1:4], parsed.query))
print("{}?{}".format(parsed.path.split("/")[0:4], parsed.query))