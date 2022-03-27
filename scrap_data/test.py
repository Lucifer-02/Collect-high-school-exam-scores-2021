from re import search
from requests import get

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'}


def scrap():

    for sbd in range(13_000_000, 13_000_100):
        url = "https://vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt/?y=2021&sbd=" + \
            str(sbd)
        content = get(url, headers=headers).content.decode('UTF-8')

        if(search("Không Tìm thấy", content) != None):
            print(str(sbd) + ": khong tim thay")
        else:
            print(str(sbd) + ": tim thay")
        print(type(content))


scrap()
