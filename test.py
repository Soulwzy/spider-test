import requests
url = "https://movie.douban.com/cinema/later/chengdu/"
response = requests.get(url)
print(response.content.decode('utf-8'))
# 保存网页到本地
# file_obj = open('douban.html', 'w')  # 以写模式打开名叫 douban.html的文件
# 如果打开网页显示的是乱码那么就用下一行代码
# file_obj = open('douban.html', 'w', encoding="utf-8")  # 以写模式打开名叫 douban.html的文件，指定编码为utf-8
# file_obj.write(response.content.decode('utf-8'))  # 把响应的html内容
# file_obj.close()  # 关闭文件，结束写入