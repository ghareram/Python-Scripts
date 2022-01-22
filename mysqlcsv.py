import MySQLdb as dbapi
import sys
import csv

QUERY='SELECT distinct(category) FROM details_urls_meta_vivanuncios'

db=dbapi.connect(host='localhost',user='hare',passwd='Ram@1234',database='AMXTEST')

cur=db.cursor()
cur.execute(QUERY)
result=cur.fetchall()
import pdb; pdb.set_trace()


for i in result:

    i = ''.join(i).strip('/n,')

    decoding='utf-8'
    oupf = open('vivancious_{}.csv'.format(i), 'w+')


    headerlist =["title", "category", "sub_category", "estacionamientos", "price"]
    writer = csv.writer(oupf)
    writer.writerow(headerlist)
    
       
   
    todays_excel_file = csv.writer(oupf)
    sel_qry = 'select title, category, sub_category, estacionamientos, price from details_urls_meta_vivanuncios where category="{}"' .format(i) 
    cur.execute(sel_qry)
    result=cur.fetchall()
    
    for record in result:
        title, category, sub_category, estacionamientos, price=record
        values = [title, category, sub_category, estacionamientos, price]
        todays_excel_file.writerow(values)


