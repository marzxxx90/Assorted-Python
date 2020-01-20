import fdb
import os
import requests
import time
import logging
import configparser
from datetime import datetime
from elasticsearch import Elasticsearch
from progress.bar import IncrementalBar
es = Elasticsearch(['172.16.100.32'])  # IP Server --------->Source

FBTEST_HOST = 'localhost'
FBTEST_USER = 'SYSDBA'
FBTEST_PASSWORD = 'masterkey'
DIRPATH = os.getcwd()

# con = fdb.connect(dsn='D:\Installer\Database\DMMHost.fdb',user=FBTEST_USER, password=FBTEST_PASSWORD)
con = fdb.connect(dsn='D:\Installer\Database\GLMHost.fdb',user ='sysdba', password='masterkey')
 
def SaveSuccessRow(strValue):
    f = open("GLMSuccessRow.txt","w+")
    f.write(str(strValue) + "\r\n")  
    
def GetSuccessRow():
    f = open("GLMSuccessRow.txt","r+")
    
    tmp = f.read()
    return int(tmp)
    
def GetCountRecord(strSql):
    cur = con.cursor()    
    
    cur.execute("Select Count(*) From (" + strSql + " )")
    for row in cur:
        tmpCount = row[0]
    return int(tmpCount)
  
def main():
    # Create a Cursor object that operates in the context of Connection con:
    cur = con.cursor()
    # Execute the SELECT statement:
    
    strSql = "Select DBA.CADPostingDate, " 
    strSql +="Case DBA.CADBRANCHCODE "
    strSql +="When 00001 Then 'Tupi' "
    strSql +="When 00002 Then 'Polomolok' "
    strSql +="When 00003 Then 'Tantangan' "
    strSql +="When 00004 Then 'Santiago' "
    strSql +="When 00005 Then 'Koronadal' "
    strSql +="When 00006 Then 'Tacurong' "
    strSql +="When 00007 Then 'Calumpang' "
    strSql +="When 00008 Then 'Isulan' "
    strSql +="When 00009 Then 'Panabo' "
    strSql +="When 00010 Then 'Tagum' "
    strSql +="When 00011 Then 'Digos' "
    strSql +="When 00012 Then 'AsFortuna' "
    strSql +="When 00013 Then 'Talisay' "
    strSql +="When 00014 Then 'Kidapawan' "
    strSql +="When 00015 Then 'Fishport' "
    strSql +="When 00016 Then 'Robinsons' "
    strSql +="When 00017 Then 'Valencia' "
    strSql +="When 00018 Then 'Cogon' "
    strSql +="When 00019 Then 'Lapu-lapu' "
    strSql +="When 00020 Then 'SB Cabahub' "
    strSql +="When 00021 Then 'Puerto' "
    strSql +="When 00022 Then 'Magallanes' "
    strSql +="When 00023 Then 'Jaro' "
    strSql +="When 00024 Then 'Zamboanga' "
    strSql +="When 00025 Then 'Pagadian' "
    strSql +="When 00026 Then 'Buhangin' "
    strSql +="When 00027 Then 'Punta' "
    strSql +="When 00028 Then 'Ozamiz' "
    strSql +="When 00029 Then 'Ipil' "
    strSql +="When 00030 Then 'Cebu' "
    strSql +="When 00031 Then 'RD Plaza' "
    strSql +="When 00032 Then 'Surallah' End as Branch, "
    strSql +="DBA.CADChartOfAccount, Sum(DBA.CADBeginningBalance) as BeginningBalance, "
    strSql +="Sum(DBA.CADEndingBalance) as EndingBalance, CA.COAACCOUNTDESCRIPTION "
    strSql +="From GLMCOADAILYBALANCE DBA "
    strSql +="Inner Join GLMChartOfAccount CA On DBA.CADChartOfAccount = CA.COAACCOUNTCODE "
    strSql +="Where DBA.CADPostingDate Between '12/01/19' And '12/06/19' "
    strSql +="Group by DBA.CADBRANCHCODE, DBA.CADPostingDate, DBA.CADChartOfAccount, CA.COAACCOUNTDESCRIPTION "
   
    scRow = GetSuccessRow()
    cnt = GetCountRecord(strSql)
    
    
    IntStartRows = 1
    IntEndRows = cnt


    if scRow != 0:
        IntStartRows = scRow
        IntEndRows = cnt       
        
    RowCount = IntStartRows -1
    

    
    print("Rows Start: " + str(scRow))
    print("Record Count: " + str(cnt))
    
    bar = IncrementalBar(' Progress', index = 1, max = cnt)
    
    strSql +="Rows " + str(IntStartRows) + " to " + str(IntEndRows)
 
    cur.execute(strSql)
    # Retrieve all rows as a sequence and print that sequence:
    RowCount = 0
    for row in cur:
        doc = {
            'PostingDate': row[0],
            'Branch': row[1],
            'ChartOfAccount': row[2],
            'BeginningBalance': row[3],
            'EndingBalance': row[4],
            'AcountDescription': row[5],
            'DocType': "GLM"}
            
        RowCount += 1
        # time.sleep(1)
        res = es.index(index="frontier-" + datetime.today().strftime('%Y%m%d'), doc_type='cbs', body=doc)
        #print(res['result'])
        bar.next()
        SaveSuccessRow(str(RowCount))
        
    SaveSuccessRow(str(0))
    bar.finish()
    print("Last Rows Count: " + str(RowCount))
    print("Please see output")
	
main()