import fdb
import os
import requests
import time
import logging
import configparser
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(['172.16.100.32'])  # IP Server --------->Source

FBTEST_HOST = 'localhost'
FBTEST_USER = 'SYSDBA'
FBTEST_PASSWORD = 'masterkey'
DIRPATH = os.getcwd()

# con = fdb.connect(dsn='D:\Installer\Database\DMMHost.fdb',user=FBTEST_USER, password=FBTEST_PASSWORD)
con = fdb.connect(dsn='D:\Installer\Database\DMMHost.fdb',user ='sysdba', password='masterkey')

def SetKeysValue(strSection, strKeys, strValue):
    config.set(strSection, strKeys, strValue)

def ReturnValueConfig(strSection, strKeys):
    return config.get(strSection, strKeys) 
    
def SaveSuccessRow(strValue):
    f = open("DMMSuccessRow.txt","w+")
    f.write(str(strValue) + "\r\n")  
    
def main():
    # Create a Cursor object that operates in the context of Connection con:
    cur = con.cursor()
    # Execute the SELECT statement:
    IntStartRows = 1
    IntEndRows = 500

    strSql = "Select "
    strSql +="Case Substring(SAFACCOUNTNUMBER from 3 for 3) "
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
    strSql +="When 00032 Then 'Surallah' "
    strSql +="end as Branch, "
    strSql +="Case Substring(SAFACCOUNTNUMBER from 6 for 3) "
    strSql +="when 100 then 'Regular Passbook Savings Account' "
    strSql +="When 101 then 'Penny Kiddie Savings Deposit' "
    strSql +="When 102 then 'Savings Deposit - Premier' "
    strSql +="When 103 then 'Mini-Savings Deposit' "
    strSql +="When 200 then 'Checking Account' "
    strSql +="When 300 then 'Regular Time Deposit Account' "
    strSql +="When 301 then 'Special Savings Deposit Account' "
    strSql +="end as ServiceType, SAFACCOUNTNUMBER as AccountNumber, SAFDATEFORWARDED as DateForwarded, "
    strSql +="SafOutStandingBalance as OutStandingBalance "
    strSql +="From DMMSAFORWARDEDBALANCE "
    strSql +="Where SAFDATEFORWARDED = '"+ "12/01/19" +"'"

    cur.execute(strSql)
	# Retrieve all rows as a sequence and print that sequence:
    RowCount = 0
    for row in cur:
        doc = {
            'Branch': row[0],
            'ServiceType': row[1],
            'AccountNumber': row[2],
            'DateForwarded': row[3],
            'OutStandingBalance': row[4]}
            
        RowCount += 1
        time.sleep(1)
        res = es.index(index="DMM-" + datetime.today().strftime('%Y%m%d'), doc_type='cbs', body=doc)
        print(res['result'])
        SaveSuccessRow('Success Row: ' + str(RowCount))

    print("Please see output")
	
main()