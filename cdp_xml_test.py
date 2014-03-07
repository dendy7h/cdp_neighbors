#!/usr/bin/python2
import re
import lxml.etree as etree
import sys

def clean_up_xml(text):
    ''' this function takes the xml tags or text as input and returns a pretty version '''
    # removes the {cdpd} in each xml tag
    if re.search('{cdpd}', text):
        #print(re.split('{.*}', text)[1])
        return(re.split('{.*}', text)[1])
    # removes the dns suffix on a hostname
    elif re.search('netapp.com', text):
        #print(re.split('\..*', text)[0])
        return(re.split('\..*', text)[0])
    # removes the serial numbers on nexus devices
    else:
        #print(re.split('\(.*', text)[0]) 
        return(re.split('\(.*', text)[0]) 


#def device_type():


if __name__ == '__main__':
    # This will ultimately be a list of dictionaries
    cdp_neigh = []
    # import the xml file
    root = etree.parse(sys.argv[1]).getroot()
    ''' create an incrementer to keep up with the number of items in the list cdp_neigh and
        set it to -1 b/c ROW is in CDP neighbors output before the device info '''
    row_increment = -1
    
    for child in root.getiterator():
        tag = clean_up_xml(child.tag)
        text = clean_up_xml(child.text)
        # assigns the values needed into the list
        if re.search('_id', tag):
            # appends the values to the current dictionary
            cdp_neigh[row_increment][tag] =  text
        elif re.search('capability', tag):
            cdp_neigh[row_increment][tag].append(text)
        elif re.search('ROW', tag): 
            row_increment  += 1
            # creates a new dictionary in the list
            cdp_neigh.append({})
            cdp_neigh[row_increment]['capability'] = []
   
    for x in cdp_neigh:
        print x
#    print("interface %s" % (x['intf_id']))
#    print(" description %s:%s" % (x['device_id'], x['port_id']))
