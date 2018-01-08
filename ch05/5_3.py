#操作CSV
import csv
headers=['ID','Username','Password','Age','Country']
rows=[(1001,"A","a_pass",20,"China"),
      (1002,"B","b_pass",21,"USA"),
      (1003,"C","c_pass",22,"UK"),]
with open('lichar.csv','w') as fp:
    fp_csv=csv.writer(fp)
    fp_csv.writerow(headers)
    fp_csv.writerows(rows)
'''
the content of lichar.csv: 
ID,Username,Password,Age,Country
1001,A,a_pass,20,China
1002,B,b_pass,21,USA
1003,C,c_pass,22,UK

'''
#or

rows_dict=[{'ID':1004,'Username':"D",'Password':"d_pass",'Age':"24",'Country':"Canada"}]
with open('lichar.csv','a')as fp:  #追加改模式就好了
    fp_csv_dict=csv.DictWriter(fp,headers)
    # fp_csv_dict.writeheader()
    fp_csv_dict.writerows(rows_dict)
