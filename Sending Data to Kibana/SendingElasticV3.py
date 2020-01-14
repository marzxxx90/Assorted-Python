import fdb 
import os
import requests
import time
import configparser

def UpdateKeysValue(strPath, strSection, strKeys, strValue):
    config = configparser.ConfigParser()
    config.read(strPath)
    sections = config.sections()
    
    config.set(strSection, strKeys, strValue)

def ReturnValueConfig(strPath, strSection, strKeys):
    config = configparser.ConfigParser()
    config.read(strPath)
    tmpVal = config.get(strSection, strKeys)
    return tmpVal

def main():
    #SetKeysValue('Configuration.ini', "Configuration", "StartRows", "100")
    UpdateKeysValue('Configuration.ini', "Configuration", "EndRows", "9000")
    #print(ReturnValueConfig('Configuration.ini',"Configuration", "StartRows"))
    
main()