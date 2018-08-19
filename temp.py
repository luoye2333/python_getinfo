import datetime
today=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
import csv
csv_file=open("./"+today+"_steam_recommend.csv","w",newline="",encoding="utf-8")
writer=csv.writer(csv_file)
writer.writerow([1,2])
csv_file.close()
