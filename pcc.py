'''My solution (so far) to pythonchallenge.com'''
def pc(serial):
    '''Call it with a porblem number to get a solution'''
    if serial==0:
        '''274877906944=map'''
        print 2**38
    elif serial==1:
        '''ocr'''
        k = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
        print "".join(filter(bool, map(lambda x: "a"<=x<="z" and ((x=="y" and "a") or (x=="z" and "b") or chr(ord(x)+2)) or x, k)))
    elif serial==2:
        '''equality'''
        k="equality"#Get it from source
        print "".join(filter(bool, map(lambda x: "a"<=x<="z" and ((x=="y" and "a") or (x=="z" and "b") or chr(ord(x)+2)) or x, k)))
    elif serial==3:
        '''linkedlist'''
        import re
        k = "OOOlOOOiOOOnOOOkOOOeOOOdOOOlOOOiOOOsOOOt"
        print "".join(filter(bool, map(lambda x: x[4], re.findall(r'[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]', k))))
    elif serial==4:
        '''peak'''
        import urllib2
        base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
        nothing  = "66831"#"8022"#"12345"
        while True:
            try:
                response = urllib2.urlopen(base+nothing)
                nothing = response.read().split()[-1]
                print nothing
            except: break
    elif serial==5:
        '''channel'''
        def print_arr(arr):
            '''Prints each section of each line of the given array'''
            for line in arr:
                print("".join(line))
        import cPickle
        # file = open("C:\\Users\\User\\Downloads\\banner.p", "r")
        # k = "".join(file.readlines())
        import urllib2
        k = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
        arr = cPickle.loads(k)
        print_arr(map(lambda x:map(lambda y:y[0]*y[1], x), arr))
    elif serial==6:
        '''oxygen'''
        import zipfile
        myZip = zipfile.ZipFile("C:\\Users\\User\\Downloads\\channel.zip", "r")
        nothing  = "90052"
        print myZip.getinfo(nothing+".txt").comment
        tot = ""
        while True:
            try:
                something = myZip.read(nothing+".txt")
                #print something
                nothing = something.split()[-1]
                tot += myZip.getinfo(nothing+".txt").comment
            except: 
                print tot
                break
pc(6)