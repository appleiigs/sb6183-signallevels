import time
import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser


statusURL = "http://192.168.100.1/RgConnect.asp"
logFileName = "sb6183log.csv"


def url_get_contents(url):
    # Opens a website and read its binary contents (HTTP Response Body)
    # making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    #reading contents of the website
    return f.read()


try:
    xhtml = url_get_contents(statusURL).decode('utf-8')
except:
    print("Exception occured in request.")
    exit()

# Defining the HTMLTableParser object
p = HTMLTableParser()
# feed the html contents in the # HTMLTableParser object
p.feed(xhtml)

#now parse downstream signal levels table
#labels (row 1):
# ['Channel','Lock Status','Modulation','Channel ID','Frequency','Power','SNR','Corrected','Uncorrectables']
#content (starts at row 2):
#['1', 'Locked','QAM256','13','477000000 Hz','13.9 dBmV','42.3 dB','474','324']
#16 channels total

channel=range(16)
chData=[]
maxChannel=16-1               #take care of 0-indexing
empty=["","","","","","","","",""]
downOutput=""

try:
    for ch in channel:
        chData.append(p.tables[2][ch+2])
except:
    maxChannel=ch-1            #could be cases where <16 channels are locked and/or have data

for ch in channel:
    if ch<=maxChannel:
        data=chData[ch]
    else:
        data=empty
    downOutput=downOutput+",".join(data)

#now parse upstream signal levels table
#labels (row 1):
#['Channel','Lock Status','US Channel Type','Channel ID','Symbol Rate','Frequency','Power']
#content (starts at row 2):
#format ['1', 'Locked', 'ATDMA', '4', '5120 Ksym/sec', '35600000 Hz', '54.0 dBmV']
#4 channels

channel=range(4)
chData=[]
maxChannel=4-1                #take care of 0-indexing
empty=["","","","","","",""]
upOutput=""

try:
    for ch in channel:
        chData.append(p.tables[3][ch+2])
except:
    maxChannel=ch-1           #could be cases where <4 channels are locked and/or have data

for ch in channel:
    if ch<=maxChannel:
        data=chData[ch]
    else:
        data=empty
    upOutput=upOutput+",".join(data)

sampleTime=time.strftime("%m/%d/%y,%H:%M:%S,")

outputFileName="signallevels.csv"
f=open(outputFileName, "a")
f.write(sampleTime)
f.write(downOutput)
f.write(upOutput)
f.write("\n")
f.close()

exit()
