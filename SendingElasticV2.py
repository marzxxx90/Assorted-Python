import fdb 
import os
import requests
import time
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(['192.168.1.176'])

FBTEST_HOST = 'localhost'
FBTEST_USER = 'SYSDBA'
FBTEST_PASSWORD = 'masterkey'
DIRPATH = os.getcwd()

con = fdb.connect(dsn='D:\Installer\Database\LMMHost.fdb',user=FBTEST_USER, password=FBTEST_PASSWORD)

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
	
def mainYak():
	savelastvalue(str('asdf asdf'))

def main():
	#con = fdb.connect(dsn=FBTEST_HOST + ':' + DIRPATH + '\\SMSHost.fdb'
	#,user=FBTEST_USER, password=FBTEST_PASSWORD)
	
	#Create a Cursor object that operates in the context of Connection con:
	cur = con.cursor()
	# Execute the SELECT statement:
	
	
	cur.execute("Select ALRLOANACCOUNTNO, ALRDATEENTERED, (ALRDEBITAMOUNT + ALRCREDITAMOUNT) as TotalAmt From LMMAIRLEDGER Where ALRDATEENTERED Between '1/1/2019' And '12/31/2019'")
	
	# Retrieve all rows as a sequence and print that sequence:
	for row in cur:

		branch = intToBranch(row[0][0:5])
		
		doc = {
			'timestamp': row[1],
			'loan_amt': row[2],
			'branch': branch
		}
		
		#time.sleep(3)
		res = es.index(index="test-01", doc_type='cbs', body=doc)
		print(res['result'])

	print("Please see output")
	
#main()
mainyak()