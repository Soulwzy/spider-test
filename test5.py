# 可视化爬取结果
import requests
from bs4 import BeautifulSoup  # 从bs4引入BeautifulSoup
from pyecharts import Page, Pie, Bar  # 引入绘图需要的模块

#请求网页
url = "https://movie.douban.com/cinema/later/chengdu/"
response = requests.get(url)

soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')

all_movies = soup.find('div', id="showing-soon")  # 先找到最大的div

# 先把所有的数据存到这个list里面
all_movies_info = []
for each_movie in all_movies.find_all('div', class_="item"):  # 从最大的div里面找到影片的div
    # print(each_movie)  # 输出每个影片div的内容
    all_a_tag = each_movie.find_all('a')
    all_li_tag = each_movie.find_all('li')
    movie_name = all_a_tag[1].text
    moive_href = all_a_tag[1]['href']
    movie_date = all_li_tag[0].text
    movie_type = all_li_tag[1].text
    movie_area = all_li_tag[2].text
    movie_lovers = all_li_tag[3].text.replace('人想看', '') #  去掉除了数字之外的字
    # 把电影数据添加到list
    all_movies_info.append({'name': movie_name, 'date': movie_date, 'type': movie_type, 
                            'area': movie_area, 'lovers': movie_lovers})
    # print('名字：{}，日期：{}，类型：{}，地区：{}， 关注者：{}'.format(
        # movie_name, movie_date, movie_type, movie_area, movie_lovers))
print(all_movies_info)  # 输出一下检查数据是否传递成功
# 绘制关注者排行榜图

# i['name'] for i in all_movies_info 这个是Python的快捷方式，
# 这一句的作用是从all_movies_info这个list里面依次取出每个元素，
# 并且取出这个元素的 name 属性
sort_by_lovers = sorted(all_movies_info, key=lambda x: int(x['lovers']))
all_names = [i['name'] for i in sort_by_lovers]
all_lovers = [i['lovers'] for i in sort_by_lovers]

lovers_rank_bar = Bar('电影关注者排行榜')  # 初始化图表，给个名字
# all_names是所有电影名，作为X轴, all_lovers是关注者的数量，作为Y轴。二者数据一一对应。
# is_convert=True设置x、y轴对调,。is_label_show=True 显示y轴值。 label_pos='right' Y轴值显示在右边
lovers_rank_bar.add('', all_names, all_lovers, is_convert=True, is_label_show=True, label_pos='right')
lovers_rank_bar.render("aaa.html")
# 绘制电影类型占比图
all_types = [i['type'] for i in all_movies_info]
type_count = {}
for each_types in all_types:
    # 把 爱情 / 奇幻 这种分成[爱情, 奇幻]
    type_list = each_types.split(' / ')
    for e_type in type_list:
        if e_type not in type_count:
            type_count[e_type] = 1
        else:
            type_count[e_type] += 1
# print(type_count) # 检测是否数据归类成功

type_pie = Pie('上映类型占比', title_top=40,width=1024,height=768)  # 因为类型过多影响标题，所以标题向下移20px
# 直接取出统计的类型名和数量并强制转换为list。
type_pie.add('', list(type_count.keys()), list(type_count.values()), is_label_show=True)
type_pie.render("bbb.html")  # jupyter下直接显示