import urllib
import re
symbolslist = ["aapl","spy","goog","nflx","baba","agnc","msft","jd"]
i =0
while i<len(symbolslist):
    url = "https://finance.yahoo.com/q;_ylt=AqOBWk3KURVrY1XkSOQ_FM33qsAF?uhb=uhb2&fr=uh3_finance_vert_gs&type=2button&s="+symbolslist[i]
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_'+symbolslist[i]+'">(.+?)</span>'
    regex2 = '<span id="yfs_p43_'+symbolslist[i]+'">(.+?)</span>'
    regex3 = '<span id="yfs_v53_'+symbolslist[i]+'">(.+?)</span>'
    pattern = re.compile(regex)
    pattern2 = re.compile(regex2)
    pattern3 = re.compile(regex3)
    price = re.findall(pattern,htmltext)
    change = re.findall(pattern2,htmltext)
    volume = re.findall(pattern3,htmltext)
    
    print "the price of" , symbolslist[i] , "is" ,price, " current change is" ,change, "Volume is" , volume
    i+=1
