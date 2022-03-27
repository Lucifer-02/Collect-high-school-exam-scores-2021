from requests import get
from re import search
from concurrent import futures
#  from bs4 import BeautifulSoup
import test_hoang


def scrap(index):
    #  sbd = index * 1000000 # from 10
    sbd = index * 1000000  # from 1 to 9

    check_final = 0

    # results were saved to data dir to and check dir to check error
    file_check = open(
        "/run/media/lucifer/STORAGE/IMPORTANTS/CODE/DS/diem_thi_2021/check/" + str(index) + "_check.txt", "a")
    file = open("/run/media/lucifer/STORAGE/IMPORTANTS/CODE/DS/diem_thi_2021/data/" +
                str(index) + ".csv", "a")

    # clean previous data
    file_check.truncate(0)
    file.truncate(0)

    # write head title
    file.write("SBD;Toan;Van;Li;Hoa;Sinh;Su;Dia;GDCD;Ngoai ngu (N1);Ngoai ngu (N2);Ngoai ngu (N3);Ngoai ngu (N4);Ngoai ngu (N5);Ngoai ngu (N6)\n")

    # use join a list instead of string mapulation to better performance for pypy3 (but I won't use pypy3 because it slower in this case and I this this implement code not effect to cpython performance)
    final_data = []
    check_data = []
    while True:
        sobaodanh = "0" + str(sbd) # from 1 to 9
        #  sobaodanh = str(sbd) # from 10
        url = "https://vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt/?y=2021&sbd=" + \
            sobaodanh
        content = get(url, headers=headers).content.decode('UTF-8')

        if(search("Không Tìm thấy", content) != None):
            check_data.append("".join([sobaodanh, ": Khong tim thay\n"]))
            check_final += 1
        else:
            final_data.append(
                "".join([sobaodanh, ";", test_hoang.sum_as_string(content)]))
            check_final = 0
            print("so bao danh: " + sobaodanh) # from 1 to 9
            #  print("so bao danh: " + sobaodanh) # from 10
        sbd += 1

        if(check_final == 10):
            break

    file.write("".join(final_data))
    file_check.write("".join(check_data))
    file.close()
    file_check.close()

# for use case beautifulsoup
#  def filter(f) -> str:
#      objects = {"Toán":"", "Văn":"", "Lí":"","Hóa":"","Sinh":"","Sử":"", "Địa":"","GDCD":"", "N1":"",  "N2":"",  "N3":"",  "N4":"",  "N5":"",  "N6":""}
#      doc = BeautifulSoup(f, "html.parser")
#      datas = doc.find_all(["div"], class_="d-flex justify-content-between search-result-line py-3 px-3")
#
#      for data in datas:
#          mon = data.find_all("div")[0].string
#          diem = data.find_all("div")[1].string
#          if(mon == None):
#              mon = data.find_all("span")[0].string
#          objects[mon] = diem
#
#      output = ""
#      for value in objects.values():
#          if(value == ""):
#              output += "-1;"
#          else:
#              output += value + ";"
#      output += "\n"
#      return output


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.76'}

#  records = [1,2,3,4,5,6,7,8,9]
#
#  with futures.ThreadPoolExecutor() as executor:
#      result = [executor.submit(scrap, record) for record in records]
scrap(2)
