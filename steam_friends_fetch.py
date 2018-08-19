import selenium.webdriver as wbd
from selenium.webdriver.chrome import options as opt

myopt=opt.Options()
myopt.add_argument("--headless")

browser=wbd.Chrome(chrome_options=myopt)
browser.set_window_size(width=1920,height=1680)
print("open browser")
import csv
#读取原有的节点信息，用于重名检测
node=[]
with open("node","r",newline="",encoding="utf-8") as file_node:
    reader_node=csv.reader(file_node)
    rowcount=0
    for row in reader_node:
        rowcount += 1
        if rowcount == 1:continue
        node.append(row)


#打开文件准备
file_node=open("./node","w",newline="",encoding="utf-8")
file_connection=open("./connection","w",newline="",encoding="utf-8")
writer_node=csv.writer(file_node)
writer_connection=csv.writer(file_connection)
writer_node.writerow(["node_id","name","level","only_url"])

firsturl="https://steamcommunity.com/profiles/76561198236936012/"#luoye
#采用bfs
#每次从队列头弹出一个,添加时从尾部添加
#保证同一级的同时处理
urlqueue=[]
urlqueue.append(firsturl)
count=0
def search(url):
    #在node(list)中查找url
    #如果有 返回node_id
    #没有则返回-1
    node_id=-1
    for i in range(len(node)):
        if url==node[i][4-1]:
            node_id=node[i][0]
            break
    return node_id
def getplayer(url):
    global count
    count+=1
    browser.get(url)
    print(url)
    #打开队列头一个网页
    #获取当前url本人信息
    #获取name
    myname=browser.find_element_by_class_name("actual_persona_name").text
    #获取level
    mylevel=browser.find_element_by_class_name("profile_header_badgeinfo_badge_area")\
    .find_element_by_css_selector("a > div > div > span").text
    #写入node文件
    writer_node.writerow([count,myname,mylevel,url])
    file_node.flush()
    #debug
    print([count,myname,mylevel])

    #之后获取七个好友的信息
    friends_block_data=browser.find_element_by_class_name("profile_rightcol")\
    .find_elements_by_css_selector("div:nth-child(4) > div > div:nth-child(2) > div")
    for i in friends_block_data:
        friend_url=i.find_element_by_css_selector("a").get_attribute("href")
        #if friend_url in node... then continue
        #如果好友在之前已经加入了node表，则之前一定查找过了，跳过
        if search(friend_url)==-1:
            urlqueue.append(friend_url)

        #link(url,friend_url)
        


while (urlqueue!=[])and(count<30):
    getplayer(urlqueue.pop(0))


file_node.close()
file_connection.close()
browser.close()