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
con = fdb.connect(dsn=r"C:\Users\HQMIS05\Desktop\DesktopDat\LMMHost.fdb",user ='sysdba', password='masterkey')

def SaveSuccessRow(strValue):
    f = open("LMMSuccessRow.txt","w+")
    f.write(str(strValue) + "\r\n")  
    
def GetSuccessRow():
    f = open("LMMSuccessRow.txt","r+")
    
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
    
    strSql = "Select "
    strSql +="Case Substring(LFBLoanAccountNo from 3 for 3) "
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
    strSql +="Case Substring(LFBLOANACCOUNTNO from 6 for 3) "
    strSql +="When 101 then 'Commercial Loans P10 Million And Above' "
    strSql +="When 102 then 'Industrial Loans P10 Million And Above' "
    strSql +="When 103 then 'Domestic Bills Purchased' "
    strSql +="When 104 then 'Receivable Discounting' "
    strSql +="When 201 then 'Commercial Loans Up to 10 Million' "
    strSql +="When 202 then 'Industrial Loans Up to P10 Million' "
    strSql +="When 203 then 'Truck And Equipment Financing P3 Million to P10 Million' "
    strSql +="When 204 then 'Domestic Bill Purchased' "
    strSql +="When 205 then 'Receivable Discounting' "
    strSql +="When 206 then 'Quick Loan Jewelry' "
    strSql +="When 207 then 'Smart Business Loan' "
    strSql +="When 301 then 'Small and Medium Business Loans Up to 3 Million' "
    strSql +="When 302 then 'Truck and Equipment Financing' "
    strSql +="When 303 then 'Agricultural Loan' "
    strSql +="When 304 then 'Agricultural Loans Equipment Financing' "
    strSql +="When 305 then 'Domestic Bills Purchased' "
    strSql +="When 306 then 'Receivable Discounting' "
    strSql +="When 307 then 'Smart Business Loan' "
    strSql +="When 401 then 'Housing Loans' "
    strSql +="When 402 then 'Quick Loans Pension Loans' "
    strSql +="When 403 then 'Quick Loans Jewelry' "
    strSql +="When 404 then 'Salary Loans' "
    strSql +="When 405 then 'Auto Loans' "
    strSql +="When 406 then 'Pencycle' "
    strSql +="end as Loan_Product_Code, "
    strSql +="case LFBLOANSTATUS "
    strSql +="When 01 then 'Current Loan' "
    strSql +="When 02 then 'Past Due Loan' "
    strSql +="When 03 then 'Item in Litigation (ITL)' "
    strSql +="When 04 then 'Delinquent Loan' "
    strSql +="When 07 then 'Acquired Asset' "
    strSql +="When 08 then 'Write Off' "
    strSql +="When 09 then 'Closed Account' "
    strSql +="When 10 then 'Cancelled (for cancelled newly released loan)' "
    strSql +="When 11 then 'Forfeited Loan Account' "
    strSql +="end as LoanStatus, "
    strSql +="LFBDateForwarded as DateForwarded, Sum(LFBPRINCIPALBALANCE) as PrincipalBal , "
    strSql +="Sum(LFBLoanAmount) as LoanAmount, " 
    strSql +="Case "
    strSql +="When Substring(LFBLoanAccountNo from 3 for 3) In (00004, 00031, 00015, 00007, 00002) Then 'Business Center I' "
    strSql +="When Substring(LFBLoanAccountNo from 3 for 3) In (00001, 00005, 00003, 00008, 00032, 00006) Then 'Business Center II' "
    strSql +="When Substring(LFBLoanAccountNo from 3 for 3) In (00011, 00010, 00009, 00022, 00026, 00014) Then 'Business Center III' "
    strSql +="When Substring(LFBLoanAccountNo from 3 for 3) In (00017, 00025, 00028, 00029, 00021, 00018, 00024) Then 'Business Center IV' "
    strSql +="When Substring(LFBLoanAccountNo from 3 for 3) In (00012, 00020, 00030, 00027, 00013, 00019, 00016, 00023) Then 'Business Center V' "
    strSql +="End as Cluster "
    strSql +="From LMMFORWARDINGBALANCE "
    strSql +="Where LFBDateForwarded Between '12/01/19' And '12/31/19' "
    strSql +="Group By Substring(LFBLoanAccountNo from 3 for 3), Substring(LFBLOANACCOUNTNO from 6 for 3) , LFBLOANSTATUS, LFBDateForwarded "
    
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
    
    bar = IncrementalBar(' Progress', index = RowCount, max = cnt)
    
    strSql +="Rows " + str(IntStartRows) + " to " + str(IntEndRows)

    cur.execute(strSql)
	# Retrieve all rows as a sequence and print that sequence:
    
    for row in cur:
        doc = {
            'Branch': row[0],
            'ServiceType': row[1],
            'LoanStatus' : row[2],
            'DateForwarded': row[3],
            'PrincipalBal': row[4],
            'LoanAmount': row[5],
            'BusinessCenter': row[6],
            'PostingDate': row[3],
            'DocType': "LMM"}
            
        RowCount += 1
        # time.sleep(1)
        res = es.index(index="frontier-" + datetime.today().strftime('%Y%m%d'), doc_type='cbs', body=doc, request_timeout=30)
        #print(res['result'])
        if res['result'] != "created":
            time.sleep(3)
            res = es.index(index="frontier-" + datetime.today().strftime('%Y%m%d'), doc_type='cbs', body=doc, request_timeout=30)
            
        bar.next()
        SaveSuccessRow(str(RowCount))
    
    SaveSuccessRow(str(0))
    bar.finish()
    print("Last Rows Count: " + str(RowCount))
    print("Please see output")
	
main()
