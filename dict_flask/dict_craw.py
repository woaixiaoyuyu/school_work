import requests
import re
from bs4 import BeautifulSoup

browser = requests.Session()


def build_url(data):
    a = 0
    if re.search('^[A-Za-z].*', data):
        a = 1
    data = data.encode()
    data = (str(data).replace(r'\x', '%'))[2:-1]
    return data, a


def CH_EN(addr):
    list = []  # 存放结果
    url = 'http://dict.cn/'+addr
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Geck    o) '
                          'Chrome/70.0.3538.77 Safari/537    .36'}
    response = browser.get(url, headers=headers)
    dic = BeautifulSoup(response.text.replace('<br>', '').replace('<br/>', ''), 'html.parser')
    CH_label = dic.find('h1', class_='keyword')   # 中文标签
    print(CH_label.get_text())
    list.append(CH_label.get_text())
    # 基本释义
    EN_meaning = dic.find_all('a',href=re.compile(r'http://dict.cn/[a-z]'))
    print('------------')
    list.append('------------')
    print("基本释义")
    list.append("基本释义")
    for mean in EN_meaning:
        # print(mean['href'])
        result = re.search('/dir/', mean['href'])
        result2 = re.search('/jp/', mean['href'])
        result3 = re.search('/de/', mean['href'])
        result4 = re.search('/fr/', mean['href'])
        result5 = re.search('/kr/', mean['href'])
        result6 = re.search('/es/', mean['href'])
        result7 = re.search('/it/', mean['href'])
        result8 = re.search('/ru/', mean['href'])
        result9 = re.search('/list/yinbiao', mean['href'])
        # print(result)
        if result or result2 or result3 or result4 or result5 or result6 or result7 or result8 or result9:
            continue
        else:
            print((mean.get_text()).strip())
            list.append((mean.get_text()).strip())

    # 例句
    print('------------')
    list.append('------------')
    print("例句")
    list.append("例句")
    EX_sentence = dic.find_all('ol',slider='2')
    for each in EX_sentence:
        each_2 = each.find_all('li')
        for each_3 in each_2:
            response = each_3.string
            key = re.findall('(?<=\t\t\t\t\t)(.*)(?=\t\t\t\t\t)', response)
            for i in key:
                print(i)
                list.append(i)

    return list


def EN_CH(addr):
    list = []  # 存放结果
    fp = open("C:/Users/Lou wen/Desktop/python3.5.2/dict/templates/result.txt", "w")
    # browser=requests.Session()
    # http://dict.cn/%E8%8B%B9%E6%9E%9C  apple
    # http://dict.cn/%E6%B0%B4%E6%9E%9C  fruit
    url = 'http://dict.cn/' + addr
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Geck    o) '
                      'Chrome/70.0.3538.77 Safari/537    .36'
    }

    response = browser.get(url, headers=headers)
    dic = BeautifulSoup(response.text.replace('<br>', '').replace('<br/>', ''), 'html.parser')

    en_label = dic.find('h1', class_='keyword')  # 英文标签
    print(en_label.get_text())
    list.append(en_label.get_text())
    fp.writelines(str(en_label.get_text()))

    # 释义
    print('------------')
    list.append('------------')
    fp.writelines('------------')
    list.append("释义")
    print("释义")
    fp.writelines("释义")
    mean = dic.find_all('li')
    for each in mean:
        each_2 = each.find('span')
        each_3 = each.find('strong')
        if not each_2:
            break
        else:
            print(each_2.get_text() + '\t' + each_3.get_text())
            fp.writelines(each_2.get_text() + '\t' + each_3.get_text())
            list.append(each_2.get_text() + '\t' + each_3.get_text())

    # 例句
    print('------------')
    list.append('------------')
    fp.writelines('------------')
    print("例句")
    fp.writelines("例句")
    list.append("例句")
    mean = dic.find_all('ol', slider='2')
    for each in mean:
        if not each.string:
            each_2 = each.find_all('li')
            for each_3 in each_2:
                if not each_3.find('strong'):
                    if re.search('^[A-Za-z].*', each_3.string):
                        print(each_3.string + '\n')
                        fp.writelines(each_3.string + '\n')
                        list.append(each_3.string + '\n')

    fp.close()
    return list


