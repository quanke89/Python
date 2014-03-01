#! /usr/bin/python
#coding=utf-8

#@descript: parser url in python
import urlparse,sys

ljust = 15
print "url's standard formart:"
print "\t scheme://username:password@xx.xx.com:port/pathname/filename?query=value#fargment"

def demo_parseurl():
    
    url1 = "http://www.baidu.com"
    print "======================================================"
    print "url:"+url1
    r = urlparse.urlparse(url1)
    print "r's type->",type(r)
    print r
    print "scheme:".ljust(ljust),r.scheme
    print "netloc:".ljust(ljust),r.netloc
    print "path:".ljust(ljust),r.path
    print "params:".ljust(ljust),r.params
    print "query:".ljust(ljust),r.query
    print "fragment:".ljust(ljust),r.fragment
    print "username:".ljust(ljust),r.username
    print "password:".ljust(ljust),r.password
    print "hostname:".ljust(ljust),r.hostname
    print "port:".ljust(ljust),r.port
    
    print "===================================================="
    wsl_url1 = "http://www.baidu.com:login.php@www.qq.com/login.jsp?user=1234&suid=fasfjasklfjw"
    print "url:"+wsl_url1
    wsl = urlparse.urlparse(wsl_url1)
    print "wsl's type->",type(r)
    print wsl
    print "scheme:".ljust(ljust),wsl.scheme
    print "netloc:".ljust(ljust),wsl.netloc
    print "path:".ljust(ljust),wsl.path
    print "params:".ljust(ljust),wsl.params
    print "query:".ljust(ljust),wsl.query
    print "fragment:".ljust(ljust),wsl.fragment
    print "username:".ljust(ljust),wsl.username
    print "password:".ljust(ljust),wsl.password
    print "hostname:".ljust(ljust),wsl.hostname
    print "port:".ljust(ljust),wsl.port
#==========================================================================================
#@join-url
#@descript：由于URL可以分成多个部分，所以有时就需要对URL进行拼接，可以使用urlparse
#模块中的urljoin方法将其进行拼接。urljoin方法有俩个参数，一个是绝对地址，另外一个是相对地址，
#直接调用此函数，将产生一个URL字符串.
#==========================================================================================
def demo_join():
    print "演示如何拼接URL字符串"
    hostname = "http://www.baidu.com"
    pathname = "/v2/?login&tpl=mn"
    url = urlparse.urljoin(hostname,pathname)
    print url
    
    #如果第二个参数及相对地址有指定协议优先使用
    url = urlparse.urljoin("http://www.baidu.com/","ftp://www.baidu.com/index.html")
    print url
#==========================================================================================
#@urlsplit
#urlsplit方法可以用来对于URL进行分解。其函数原型和urlparse类似，也接收一个字符串。
#然后给出一个元组。与urlparse的方法结果相比。这里的结果少了param参数
#==========================================================================================
def demo_split():
    url ="http://zz.xxx.com/tools/admin.php?user=admin&password=xxx"
    res = urlparse.urlsplit(url)
    print res
    print urlparse.urlunsplit(res)
#==========================================================================================
#@encode
#@descript：演示各种URL的加密与解密
#==========================================================================================
def demo_decodeURL():
    import urllib
    print "使用urllib的还函数对url进行编码和解码"
    print "编码:quote/quote_safe"
    print "解码:unquote/unquote_safe"
    print "python 3.0 不支持 urllib.quote()"
    print "改成了下面：编码　：urllib.parse.quote(s)解码 ：urllib.parse.unquote(s)"
    
    host ="http://www.baidu.com/#wd="
    url1= host+urllib.quote("和尚")
    url2= host+urllib.quote("和尚 尼姑")
    url3= host+urllib.quote_plus("和尚  尼姑 ")
    print url1
    print url2
    print url3
    
    unurl1 = urllib.unquote(url1)
    unurl2 = urllib.unquote(url2)
    unurl3 = urllib.unquote(url3)
    unurl4 = urllib.unquote_plus(url3)
    print unurl1
    print unurl2
    print unurl3
    print unurl4
    
    print  "利用urlencode对查询参数进行编码"
    print  "因为list和字典都是无序的所以结果不一样，但是在url请求中的效果是一样的"
    params = [('entryid','10000'),('userid','admin'),('note','python笔记')]
    url_query = urllib.urlencode(params)
    print url_query
    
    params = ({'entryid':'10000','userid':'admin','note':'python笔记'})
    url_query = urllib.urlencode(params)
    print url_query
    
    
    params =[('entryid',['100001','19999','222222'])]
    print urllib.urlencode(params)
    print urllib.urlencode(params,True)
#==========================================================================================
#@handlerUrl
#一个综合的url处理演示
#==========================================================================================
def demo_handlerURL():
    list_res =[]
    list_host =['http://www.baidu.com','http://www.qq.com','http://www.163.com','http://www.jd.com']
    list_admin =['admin.php','admin.jsp','admin.aspx','/admin/admin.php','/admin/admin.jsp']
    
    list_url = []
    for host in list_host:
        for admin in list_admin:
            list_url.append(urlparse.urljoin(host, admin))
        
    for url in list_url:
        scheme,netloc,path,query,fragment =urlparse.urlsplit(url)
        scheme='http'
        list_res.append(urlparse.urlunsplit((scheme,netloc,path,query,fragment)))

    for strs in list_res:
        print strs
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        selfMod =__import__(__name__)
        return_function = getattr(selfMod,"demo_%s" % sys.argv[1])
        if (callable(selfMod.return_function)):
            return_function()
    else:
        print "help:"
        print "self.py parseurl".ljust(30),"演示如何解析url"