import fdb 
import os
import requests
import time
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(['172.16.100.32'])# IP Server --------->Source

FBTEST_HOST = 'localhost'
FBTEST_USER = 'SYSDBA'
FBTEST_PASSWORD = 'masterkey'
DIRPATH = os.getcwd()

#con = fdb.connect(dsn='D:\Installer\Database\DMMHost.fdb',user=FBTEST_USER, password=FBTEST_PASSWORD)
con = fdb.connect(dsn='D:\Installer\Database\DMMHost.fdb',user='sysdba', password='masterkey')
def intToBranch(br):
	br = int (br)
	if br == 1:
		return "Tupi"
	if br == 2:
		return "Polomolok"
	if br == 3:
		return "Tantangan"
	if br == 4:
		return "Santiago"
	
	return "Others:" + str(br)

def SaveLastValue(strValue):
	f = open("LastValue.txt","w+")
	
	f.write(str(strValue) + "\r\n")
	
def ReadLastValue():
	f = open("demofile.txt", "r")
	return f.read()

def main():
	#con = fdb.connect(dsn=FBTEST_HOST + ':' + DIRPATH + '\\SMSHost.fdb'
	#,user=FBTEST_USER, password=FBTEST_PASSWORD)
	
	#Create a Cursor object that operates in the context of Connection con:
	cur = con.cursor()
	# Execute the SELECT statement:

	strSqlDemand = '''Select * From (
                    Select 
                    Case Substring(SAFACCOUNTNUMBER from 3 for 3)
                    When 00001 Then 'Tupi'
                    When 00002 Then 'Polomolok'
                    When 00003 Then 'Tantangan'
                    When 00004 Then 'Santiago'
                    When 00005 Then 'Koronadal'
                    When 00006 Then 'Tacurong'
                    When 00007 Then 'Calumpang'
                    When 00008 Then 'Isulan'
                    When 00009 Then 'Panabo'
                    When 00010 Then 'Tagum'
                    When 00011 Then 'Digos'
                    When 00012 Then 'AsFortuna'
                    When 00013 Then 'Talisay'
                    When 00014 Then 'Kidapawan'
                    When 00015 Then 'Fishport'
                    When 00016 Then 'Robinsons'
                    When 00017 Then 'Valencia'
                    When 00018 Then 'Cogon'
                    When 00019 Then 'Lapu-lapu'
                    When 00020 Then 'SB Cabahub'
                    When 00021 Then 'Puerto'
                    When 00022 Then 'Magallanes'
                    When 00023 Then 'Jaro'
                    When 00024 Then 'Zamboanga'
                    When 00025 Then 'Pagadian'
                    When 00026 Then 'Buhangin'
                    When 00027 Then 'Punta'
                    When 00028 Then 'Ozamiz'
                    When 00029 Then 'Ipil'
                    When 00030 Then 'Cebu'
                    When 00031 Then 'RD Plaza'
                    When 00032 Then 'Surallah'
                    end as "Branch",
                    Case Substring(SAFACCOUNTNUMBER from 6 for 3)
                    when 100 then 'Regular Passbook Savings Account'
                    When 101 then 'Penny Kiddie Savings Deposit'
                    When 102 then 'Savings Deposit - Premier'
                    When 103 then 'Mini-Savings Deposit'
                    When 200 then 'Checking Account'
                    When 300 then 'Regular Time Deposit Account'
                    When 301 then 'Special Savings Deposit Account'
                    end as "ServiceType", SAFACCOUNTNUMBER as AccountNumber, SAFDATEFORWARDED as DateForwarded,
                    SafOutStandingBalance as OutStandingBalance
                    From DMMSAFORWARDEDBALANCE
                    Union
                    Select 
                    Case Substring(CafAccountNumber from 3 for 3)
                    When 00001 Then 'Tupi'
                    When 00002 Then 'Polomolok'
                    When 00003 Then 'Tantangan'
                    When 00004 Then 'Santiago'
                    When 00005 Then 'Koronadal'
                    When 00006 Then 'Tacurong'
                    When 00007 Then 'Calumpang'
                    When 00008 Then 'Isulan'
                    When 00009 Then 'Panabo'
                    When 00010 Then 'Tagum'
                    When 00011 Then 'Digos'
                    When 00012 Then 'AsFortuna'
                    When 00013 Then 'Talisay'
                    When 00014 Then 'Kidapawan'
                    When 00015 Then 'Fishport'
                    When 00016 Then 'Robinsons'
                    When 00017 Then 'Valencia'
                    When 00018 Then 'Cogon'
                    When 00019 Then 'Lapu-lapu'
                    When 00020 Then 'SB Cabahub'
                    When 00021 Then 'Puerto'
                    When 00022 Then 'Magallanes'
                    When 00023 Then 'Jaro'
                    When 00024 Then 'Zamboanga'
                    When 00025 Then 'Pagadian'
                    When 00026 Then 'Buhangin'
                    When 00027 Then 'Punta'
                    When 00028 Then 'Ozamiz'
                    When 00029 Then 'Ipil'
                    When 00030 Then 'Cebu'
                    When 00031 Then 'RD Plaza'
                    When 00032 Then 'Surallah'
                    end as "Branch",
                    'Demand' as ServiceType, CafAccountNumber as AccountNumber, CafDateForwarded as DateForwarded,
                    CafOutStandingBalance as OutStandingBalance
                    From DMMCaForwardedBalance
                    Union
                    Select 
                    Case Substring(TDFACCOUNTNUMBER from 3 for 3)
                    When 00001 Then 'Tupi'
                    When 00002 Then 'Polomolok'
                    When 00003 Then 'Tantangan'
                    When 00004 Then 'Santiago'
                    When 00005 Then 'Koronadal'
                    When 00006 Then 'Tacurong'
                    When 00007 Then 'Calumpang'
                    When 00008 Then 'Isulan'
                    When 00009 Then 'Panabo'
                    When 00010 Then 'Tagum'
                    When 00011 Then 'Digos'
                    When 00012 Then 'AsFortuna'
                    When 00013 Then 'Talisay'
                    When 00014 Then 'Kidapawan'
                    When 00015 Then 'Fishport'
                    When 00016 Then 'Robinsons'
                    When 00017 Then 'Valencia'
                    When 00018 Then 'Cogon'
                    When 00019 Then 'Lapu-lapu'
                    When 00020 Then 'SB Cabahub'
                    When 00021 Then 'Puerto'
                    When 00022 Then 'Magallanes'
                    When 00023 Then 'Jaro'
                    When 00024 Then 'Zamboanga'
                    When 00025 Then 'Pagadian'
                    When 00026 Then 'Buhangin'
                    When 00027 Then 'Punta'
                    When 00028 Then 'Ozamiz'
                    When 00029 Then 'Ipil'
                    When 00030 Then 'Cebu'
                    When 00031 Then 'RD Plaza'
                    When 00032 Then 'Surallah'
                    end as "Branch",
                    'TimeDeposit' as ServiceType, TDFACCOUNTNUMBER as AccountNumber, TDFDATEFORWARDED as DateForwarded, 
                    TDFOUTSTANDINGBALANCE as OutStandingBalance
                    From DMMTDFORWARDEDBALANCE
                    )
                    Where DateForwarded = '12/01/19' '''
					
	cur.execute(strSqlDemand)
	
	# Retrieve all rows as a sequence and print that sequence:
	for row in cur:

		#branch = intToBranch(row[0][0:5])
		
		doc = {
			'Branch': row[0],
			'ServiceType': row[1],
			'AccountNumber': row[2],
            'DateForwarded': row[3],
            'OutStandingBalance': row[4]
            
		}
		#print(str(row[0]))
		#time.sleep(3)
		res = es.index(index="test-01", doc_type='cbs', body=doc)
		print(res['result'])
		
	#cur.execu("")

	print("Please see output")
	
main()
#mainyak()