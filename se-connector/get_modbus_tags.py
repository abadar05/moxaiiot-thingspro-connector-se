#!/usr/bin/env python

import requests
import json


tagList = []
equipmentNameList = []

def get_mx_api_token():
    f = open('/etc/mx-api-token', 'r')
    token = f.readline()
    print "mx-api-token :", token
    return token


def getModbusTags():
    
    """
    Configuration
    """
    with open("/home/moxa/config.json") as json_data_file:
        cfg = json.load(json_data_file)
        
    """
    Header
    """    
    headers = {"mx-api-token": cfg["things-pro"]["mx_api_token"]}   
    
    """
    GET 
    """    
    r = requests.get(
        'https://localhost/api/v1/mxc/equipments',
        headers=headers,
        verify=False)
        
    print ("Return code :", r.status_code)
    data = r.json()
   
    
    """
    Parser
    """
    for dictionary in data:
        get_keys_list = (dictionary.keys())
       
        get_equipmentName =  dictionary['equipmentName']  
       
        equipmentNameList.append(get_equipmentName) 

        if dictionary['equipmentName'] == cfg["things-pro"]["device_name"]:
              
            get_equipmentTags = dictionary['equipmentTags']
  
            for nested_tag in get_equipmentTags:
                get_nested_equipmentTags = nested_tag
                
                get_tagName = get_nested_equipmentTags['name']
                 
                tagList.append(get_tagName)
    
    return tagList, equipmentNameList
