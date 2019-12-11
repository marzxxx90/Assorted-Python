from datetime import datetime

def SaveLastValue(strValue):
	f = open("LastValue.txt","w+")
	
	f.write(str(strValue) + "\r\n")
	
def main():
	SaveLastValue('asdfasdf')
	
main()