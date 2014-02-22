#! /usr/bin/python
#coding:UTF-8
'''
    @author: neptune
    @time: 2014-02-20
    @descript: 主要记录Pyhon中一些常用的东西.建议宽屏阅读使用
'''
import sys


def demo_help():
    print "快速查找:利用编辑的查找功能查找@关键字。"
    print "\t例如：查找list相关的东西：输入@list"
    print "\t查看运行结果:shell$ ./man.py list"
    print "输入./man.py -m list 可以查看list的API帮助"
    
def demo_api(datatype,spacing=15,collapse=1):
    """Print methods and doc-strings wtih object"""

    methodList = [method for method in dir(datatype) if callable(getattr(datatype,method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)

    print "\n".join(["%s %s" % 
        (method.ljust(spacing),processFunc(str(getattr(datatype,method).__doc__)))
        for method in methodList]);

#===========================================================================================================
#@list
#    演示list相关的用法
#===========================================================================================================
def demo_list():
    "演示list相关的用法"
    print "list类型：属于一种集合类型，它非常灵活，支持在源处修改，可按需增长缩短，可以包含任何类型的对象亦可嵌套"
    
    #define list variable 定义list类型的变量
    li1 = [];
    li2 = [1,2,3,4,5]   
    li3 = [1,2,3,'4',5]
    li4 = [1,'snakeam',['am','pm'],'fun']
    li5 = list("list-variable")
    li6 = list(range(-4,4))
    print "li1:",type(li1),"+\t",li1
    print "li2:",type(li1),"+\t",li2
    print "li3:",type(li1),"+\t",li3
    print "li4:",type(li1),"+\t",li4
    print "li5:",type(li1),"+\t",li5
    print "li6:",type(li1),"+\t",li6
    
    #index  form 0-index
    print li2[0]
    print li3[3]
    print li4[1][1]
    
    #split
    print li2[:3]       #取前三个元素，返回list
    print li3[3:]       #取第三个以后的元素，返回list
    print li3[2:4]      #从第三个开始取到第五个但不包括5
    print li3[-1:]      #取最后一个
    
    #add or del
    li1.append("hello")
    print li1
    li1.insert(0, "xcx")
    print li1
    li1[0:0] =['hmj']
    print li1
    li1[1:1] =['zxy']
    print li1
    li1[len(li1):1]=['world']
    print li1
    li1[-1] =['!','wan an']
    print li1
    
    del li1[0]
    print li1
    li1.remove(li1[0])
    print li1
    li1[2][0:1]=['I']
    print li1
    li1.pop()
    print li1
    
    #len
    print "li1's length",len(li1)
    
    #iterator
    listdemo = [x** 2 for x in li2]
    print listdemo
    
    
    for x in li2:print x*2
    #filter element : if expresstion
    li = [x *2 for x in li1 if x > 2]
    print li
    #
    #         list的方法
    #         L.append(var) #追加元素
    #         L.insert(index,var)
    #         L.pop(var) #返回最后一个元素，并从list中删除之
    #         L.remove(var) #删除第一次出现的该元素
    #         L.count(var) #该元素在列表中出现的个数
    #         L.index(var) #该元素的位置,无则抛异常
    #         L.extend(list) #追加list，即合并list到L上
    #         L.sort() #排序
    #         L.reverse() #倒序
    #         list 操作符:,+,*，关键字del
    #         a[1:] #片段操作符，用于子list的提取
    #         [1,2]+[3,4] #为[1,2,3,4]。同extend()
    #         [2]*4 #为[2,2,2,2]
    #         del L[1] #删除指定下标的元素
    #         del L[1:3] #删除指定下标范围的元素
    #         list的复制
    #         L1 = L #L1为L的别名，用C来说就是指针地址相同，对L1操作即对L操作。函数参数就是这样传递的
    #         L1 = L[:] #L1为L的克隆，即另一个拷贝。
#===========================================================================================================
#@dict
#    演示dict相关的用法
#===========================================================================================================
def demo_dict():
    """演示dict的常用操作"""
    #静态的创建一个字典
    d1 = {}                                      #创建一个空字典
    print d1
    d2 = {'name':'snakeam','skill':'decode'}     #创建有俩想的字典
    print d2
    d3 = {'food':{'ham':1,'egg':2}}              #字典的嵌套
    #Python 3.x
    #d4 = dict(name='xcx',skill='god'）
    print d3
    # print d4
    #动态构造一个字典
    #在Python3.x和Python2.x中字典可以用字典解析来创建。
    #字典解析运行一个隐士循环，根据每次迭代的收集表达式键/值结果来填充一个新的字典
    #动态初始化一个字典的标准方法都是：将其键和值对应起来传递个dict调用
    #zip函数是在一个单个调用中从键和值的列表来构建一个字典的方式之一
    li =['a','b','c']
    li2 =[1,2,3,4]
    d5 = dict(zip(li,li2))
    print d5
    
    #演示dict字典的取值
    print d2['name']
    print d3['food']['egg']
    #dict.get(key,0) 如果没有则返回默认值，[key]方式没有则抛出异常
    print d2.get('age',100)
    
    #成员关系：键是否存在测试
    print ('ham' in d3)
    #has_key(key)判断字典是否包含莫个键
    print d2.has_key('age')
    
    
    #Python2.x
    list_key = d5.keys()
    print "type=>",type(list_key)       #list
    print list_key                      #['a','b','c']
    
    list_value = d5.values()
    print "type=>",type(list_value)     #list
    print list_value                    #[1,2,3]
    
    list_item = d5.items()
    print "type=>",type(list_item)      #list
    print list_item                     #[('a',1),('b',2),('c',3)]
    #python3.x
    #keys,values,items都返回试图对象，而不向Python2.x中返回实际的结果集列表
    #视图对象是可迭代。这就意味着每次产生一个结果集项，而不是在内存中直接生存列表
    #视图保存了字典的最初顺，但他们不支持索引和列表的sort等方法。打印时也不现实自己的项
    
    #add  mondify
    d2['age']=100                   #为d2新增{'age':100}
    print d2
    d2['age']=20                    #修改age
    print d2
    del d2['name']                  #删除name建值对
    print(d2.pop('age'))
    print(d2.popitem())
    #字典合并
    d1.update(d2)
    print d1
    
    #字典遍历
    print d5
    for (k,v) in d5.items(): print "%s:%s" % (k,v) 
    #最笨的方法 
    for d in d5: print "%s:%s" % (d,d5[d])
    for k,v in zip(d5.iterkeys(),d5.itervalues()): print "%s:%s" % (k,v)
    #for k,v in zip(d5.keys(),d5.values()): print "%s:%s" % (k,v)
    #效率最高的
    for k,v in d5.iteritems(): print "%s:%s" % (k,v)
    
#===========================================================================================================
#@tuple
#    演示元组的使用
#===========================================================================================================
def demo_tuple():
    """元组tuple。元组由简单的对象构成，元组与列表非常类似，但元组不能在原处修改，因为它是不可变的。而且通常写成
        园括号而不是方括号中的一系列项。元组不支持任何方法调用，但元组具有列表的大多数属性。

        任意对象的有序集合
            与字符串和列表类似，元组是一个位置有序的对象集合，与列表相同，可以嵌入到任何类别的对象中
        通过偏移存取
            同字符串，列表一样，在元组中的元素通过偏移来访问，它们支持所有基于偏移的操作。
        不可变序列类型
            类似于字符串，元组是不可变的。它们不支持应用在列表中任何原处修改的操作。
        固定长度，异构，任意嵌套
            元组因为是不可变的，在不生成一个拷贝的情况下不能增长或缩短。另一方面，元组可以包含其他的符号对象，
        对象引用的数组
            与列表相似，元组最好看做是对象引用的数组。元组存储指向其他对象的存储点
    """
    #定义元组
    ()                      #定义个空元组
    T = (0,)                #定义一个元素的元组，注意逗号不能少
    print T
    T = (1,'snake',2,3,4)
    print T
    T = 0,'ni',1,2,3
    print T
    T = ('snakeam',('java','c','web','asm'),'python')
    print T
    T1 = tuple("poseido")       #一个可迭代对象元组
    print T1
    
    #进行索引
    print T[1]
    print T[1][1]
    #分片
    print T[1:2]
    #合并
    print T+T1
    #重复
    print T *3
    #迭代
    for x in T:print x
    for x in T1:print x
    #成员关系
    print T.index('python')
    print T1.index('s')
    #计数
    print (T * 3).count('python')
    
    #tuple 和list相互转换
    li1 = list(T)
    print "type=>",type(li1),'\n',li1
    li1.sort()
    print li1
    T = tuple(li1)
    print "type=>",type(T),'\n',T
#===========================================================================================================
#@string
#    演示字符串的使用
#===========================================================================================================    
def demo_string():
    """
        Python中字符串的定义：一个有序的字符的集合，用来存储和表现基于文件的信息。
        Python中的字符串与其他语言中的字符串一样扮演着重要的角色。
        严格的说Python中字符串要算是不可变的序列这一类别。意味着这些字符从所包含的字符存在从左至右的顺序
        并且它们不可以在源处修改。
    """
    #下面是一些常用的字符串常量和表达式的定义
    S = ""              #空字符串
    print S
    S = "i'am chinese people!"  #双引号和单引号相同
    print S
    S = 's\np\ta\x00m'          #转意
    print S
    S = """
            可以包含多行字符串
        """
    print S
    S = r"\temp\span"           #Raw字符串
    print S
    S = b'spam'                 #Python中的字节字符串
    print S
    S = u"测试"               #2.x中使用的unicode字符串
    print S
    
    #字符串的一些常用操作
    print   S +"this's a String"    #字符串合并
    strs =   " xcx hmj zxy " *3        #重复3次
    print strs
    #索引
    print strs[1]
    #分片
    print strs[1:4]
    #求长度
    print len(strs)
    #字符从格式化表达式
    print "a %s skill" % "super"
    print "a {0} skill".format("super")
    
    #字符串搜索
    print strs.find("x")
    #移除空格
    print strs.strip()
    print strs.rstrip()
    print strs.lstrip()
    #用制定的字符进行分割
    li = strs.split(" ")
    print "li's type=>",type(li)
    print li
    print "内容测试：",strs.isdigit()
    print "大小写转换",strs.upper()
    print "是否是以制定的字符结尾",strs.endswith(" ")
    print "<|>".join(list("snakeam"))
    print strs.encode("latin-1")
    #成员关系
    print "xcx" in strs
    #迭代
    for x in strs:print x*2
    print [ord(x) for x in strs]
    
    
#===========================================================================================================
if __name__ == "__main__":
    #print sys.argv
    if len(sys.argv) >=2:
        selfMod = __import__(__name__)
        if sys.argv[1] == '-m':
            return_function = getattr(selfMod,"demo_api")
            if(callable(selfMod.return_function) and callable(selfMod.return_function)):
                return_function(sys.argv[2])
        else:
            return_function = getattr(selfMod,"demo_%s" % sys.argv[1])
            if(callable(selfMod.return_function) and callable(selfMod.return_function)):
                return_function()
    else:
        demo_help()