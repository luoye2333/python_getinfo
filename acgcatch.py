from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

url="https://music.163.com/#/discover/playlist/?cat=ACG&order=hot"
opt=Options()
opt.add_argument("--headless")

driver=webdriver.Chrome(chrome_options=opt)

csv_file=open("acg","w",newline="",encoding="utf-8")
writer=csv.writer(csv_file)
writer.writerow(["标题","播放数","链接"])

while url !="javascript:void(0)":
    driver.get(url)
    driver.switch_to.frame("contentFrame")

    data=driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
    for i in range(len(data)):
        playnumber=data[i].find_element_by_class_name("nb").text
        if "万" in playnumber:
            if int(playnumber.split("万")[0])>500:
                msk=data[i].find_element_by_class_name("msk")
                title=msk.get_attribute("title")
                link=msk.get_attribute("href")
                writer.writerow([title,playnumber,link])
    #一页结束
    nexturl=driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute("href")
    url=nexturl
csv_file.close()
driver.close()





