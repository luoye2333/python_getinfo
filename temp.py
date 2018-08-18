import csv
import numpy as np

node=[]
with open("node","r",newline="",encoding="utf-8") as file_node:
    reader_node=csv.reader(file_node)
    rowcount=0
    for row in reader_node:
        rowcount += 1
        if rowcount == 1:continue
        node.append(row)

print(node)       
