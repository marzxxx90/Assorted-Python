import fdb 
import os
import requests
import time

FBTEST_HOST = 'localhost'
FBTEST_USER = 'SYSDBA'
FBTEST_PASSWORD = 'masterkey'
DIRPATH = os.getcwd()

con = fdb.connect(dsn='208.1.1.93:SMSHost.fdb',user=FBTEST_USER, password=FBTEST_PASSWORD)


def main():
	#con = fdb.connect(dsn=FBTEST_HOST + ':' + DIRPATH + '\\SMSHost.fdb'
	#,user=FBTEST_USER, password=FBTEST_PASSWORD)
	
	#Create a Cursor object that operates in the context of Connection con:
	cur = con.cursor()
	# Execute the SELECT statement:
	cur.execute("Select * from tbl_SMSLogs Where Status = 0")

	# Retrieve all rows as a sequence and print that sequence:
	for row in cur:
		SMS_SendFunction(row[0],row[2],row[4])
		time.sleep(3)
		#print(row[0], row[2], row[4])
		#Update_SMS_Logs(row[0])
	pass
	
def Update_SMS_Logs(IntID):
	#Create a Cursor object that operates in the context of Connection con:
	cur = con.cursor()
	
	sql = "Update tbl_SMSLogs Set Status = '1' Where ID = " + str(IntID)
	print(sql)
	cur.execute(sql)
	
	con.commit()
	pass
	
def SMS_SendFunction(ID, strNum, strMessage):
	url = 'https://devapi.globelabs.com.ph/smsmessaging/v1/outbound/21588120/requests'
	myparams = {'address': strNum, 'passphrase':'XEcS6yMXf7','app_id':'7naxFr4RyeHzaiX9q7cR65Hnqny4FE7n',
	'app_secret':'dc05f0161945d4bb5d40bdbfa671e84f7ad7747946931cc1ef406f566529d141',
	'message':strMessage}

	try:
		response = requests.post(url, data = myparams)
		#print(response.text)
		#if response.status_code == '201':
		Update_SMS_Logs(ID)
		requests.session().close()
	except requests.ConnectionError as e:
		print(str(e))
	except requests.Timeout as e:
		print(str(e))
	except requests.RequestException as e:
		print(str(e))
	
main()