import requests
import os
import xmltodict

def fart():
    userid = int(input("enter the user id of sets to scrape: "))

    #fetch sets of user
    url = "http://www.roblox.com/Game/Tools/InsertAsset.ashx?nsets=20&type=user&userid="+str(userid)
    userSetsXml = requests.get(url).content 
    setCreator = xmltodict.parse(userSetsXml)['List']['Value'][0]['Table']['Entry'][4]['Value']

    if not os.path.exists(setCreator):
            os.makedirs(setCreator)
            
    open(setCreator+"/usersets.xml", "wb").write(userSetsXml)

    #now move on to archiving all the user's sets
    dict = xmltodict.parse(userSetsXml)

    #remove "my models" and "my decals"
    del dict['List']['Value'][0]
    del dict['List']['Value'][0]

    for set in dict['List']['Value']:
        setName = set['Table']['Entry'][0]['Value']
        setId = set['Table']['Entry'][3]['Value']
        setImage = set['Table']['Entry'][5]['Value']
        print 'Saving "' + setName + '" [set ID '+ str(setId) +']',
        
        url = "https://www.roblox.com/Game/Tools/InsertAsset.ashx?sid="+str(setId)
        r = requests.get(url)
        open(setCreator+"/"+str(setId)+" ["+setName+"].xml", "wb").write(r.content)

        #also save the set image because why not
        url = "https://www.roblox.com/asset/?id="+str(setImage)
        r = requests.get(url)
        open(setCreator+"/"+str(setId)+" ["+setName+"].png", "wb").write(r.content)

        print(" ... Done!")

    print("----------------------------------------------------------------")

    fart()

fart()


