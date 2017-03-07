import pickle
namefile='name.data'

class AdressBook:
    def __init__(self,name,age,number):
        self.name = name
        self.age = age
        self.number = number
        print('new name :{0},age:{1},number:{2}')\
        .format(self.name,self.age,self.number)
    def tell(self):
        print '{0},{1},{2}'.format(self.name,self.age,self.number)
   

Zhangbao = AdressBook('ZhangBao',28,13822544981)

Mybook = {}
Mybook[Zhangbao.name] ='BeiJing'
f = open (namefile,'wb')
pickle.dump(Mybook,f)
f.close()
fr = open (namefile)
date = fr.readlines()
for eachline in date:
    print eachline,
