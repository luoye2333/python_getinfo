from selenium import webdriver
from selenium.webdriver.chrome.options import Options


opt=Options()
opt.add_argument("--headless")

driver=webdriver.Chrome(chrome_options=opt)
driver.set_window_size(width=1920,height=200)
#设置宽度 否则太小显示不出来东西
driver.get("https://store.steampowered.com/")
print("connect successful")
data=driver.find_elements_by_css_selector("#home_maincap_v7 > div.carousel_items > a")

import time
recommend=[]
for i in data:
    #game_name=data[i].find_element_by_class_name("info").\
    #find_element_by_class_name("app_name").find_element_by_css_selector("div").text
    game_name=i.find_element_by_css_selector("div:nth-child(2) >div:nth-child(1)>div").text
    while game_name=="":
        print("wait")

        time.sleep(2)
        #等待steam自动切换
        game_name=i.find_element_by_css_selector("div:nth-child(2) >div:nth-child(1)>div").text
    game_id=i.get_attribute("data-ds-appid")
    recommend.append([game_name,game_id])
    print([game_name,game_id])

import datetime
today=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
import csv
with open("./"+today+"_steam_recommend.csv","w",newline="",encoding="utf-8") as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow(["游戏名称","游戏id"])
    for i in recommend:
        writer.writerow(i)


driver.close()