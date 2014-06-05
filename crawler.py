GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None
ANDROID_ID = None
DOWNLOAD_PATH = '/Users/dflower/Program/googleplay/'

from googleplay import  GooglePlayAPI
import sys
import os
import urlparse
from helpers import sizeof_fmt, print_header_line, print_result_line
from config import *

def getCategories(api):
    response = api.browse()
    return response

def getApps(api,category,subcategory,number,offset):
    ret = []
    try:
        message = api.list(category, subcategory, number, offset)
    except:
        print "Error: HTTP 500 - one of the provided parameters is invalid"

    if (subcategory is None):
        print SEPARATOR.join(["Subcategory ID", "Name"])
        for doc in message.doc:
            print SEPARATOR.join([doc.docid.encode('utf8'), doc.title.encode('utf8')])
    else:
        print_header_line()
        doc = message.doc[0]
        for c in doc.child:
            try:
                print_result_line(c)
                package = c.docid
                name = c.title
            
                length = c.details.appDetails.installationSize
                if length>1024*1024*50:
                    print 'too large, skip'
                    continue
            
                folder = DOWNLOAD_PATH + category
                if not os.path.exists(folder):
                    os.mkdir(folder)
                filename = folder + '/' + name + '.apk'
                if not os.path.isfile(filename):
                    downloadApps(api,package,filename)
            
                ret.append(package)
            except:
                continue
    return ret  

def downloadApps(api,packagename,filename):
    # Get the version code and the offer type from the app details
    m = api.details(packagename)
    doc = m.docV2
    vc = doc.details.appDetails.versionCode
    ot = doc.offer[0].offerType

    # Download
    print "Downloading %s..." % sizeof_fmt(doc.details.appDetails.installationSize),
    data = api.download(packagename, vc, ot)
    open(filename, "wb").write(data)
    print "Done"      
    

if __name__ == '__main__':
    #get categories
    api = GooglePlayAPI(ANDROID_ID)
    api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)
    
    #getApps(api,'GAME','apps_topselling_free','100',None)
    #getApps(api,'BOOKS_AND_REFERENCE','apps_topselling_free','100',None)
    #getApps(api,'BUSINESS','apps_topselling_free','3','100')
    #getApps(api,'COMICS','apps_topselling_free','10','100')
    #getApps(api,'COMMUNICATION','apps_topselling_free','2','100')
    #getApps(api,'EDUCATION','apps_topselling_free','100',None)
    #getApps(api,'ENTERTAINMENT','apps_topselling_free','30','100')
    #getApps(api,'FINANCE','apps_topselling_free','10','290')
    #getApps(api,'HEALTH_AND_FITNESS','apps_topselling_free','5','125')
    #getApps(api,'LIBRARIES_AND_DEMO','apps_topselling_free','20','120')
    #getApps(api,'LIFESTYLE','apps_topselling_free','50','200')
    #getApps(api,'APP_WALLPAPER','apps_topselling_free','100','100')
    #getApps(api,'MEDIA_AND_VIDEO','apps_topselling_free','10','100')
    #getApps(api,'NEWS_AND_MAGAZINES','apps_topselling_free','50','220')
    #getApps(api,'MEDICAL','apps_topselling_free','30','220')
    #getApps(api,'MUSIC_AND_AUDIO','apps_topselling_free','20','100')
    #getApps(api,'PERSONALIZATION','apps_topselling_free','10','100')
    #getApps(api,'PHOTOGRAPHY','apps_topselling_free','10','100')
    #getApps(api,'PRODUCTIVITY','apps_topselling_free','10','100')
    #getApps(api,'SHOPPING','apps_topselling_free','50','100')
    #getApps(api,'SOCIAL','apps_topselling_free','100','100')
    #getApps(api,'SPORTS','apps_topselling_free','30','100')
    #getApps(api,'TOOLS','apps_topselling_free','3','110')
    #getApps(api,'TRANSPORTATION','apps_topselling_free','5','110')
    #getApps(api,'TRAVEL_AND_LOCAL','apps_topselling_free','15','115')
    #getApps(api,'WEATHER','apps_topselling_free','5','100')
    #getApps(api,'APP_WIDGETS','apps_topselling_free','30','200')
    
    print 'google play crawler by dflower'