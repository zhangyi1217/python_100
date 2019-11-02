class Student(object):
    def __init__(self, name, age):    #这里的_init_是一个特殊的方法用在创建对象时进行初始化操作
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age<18:
            print('%s只能观看《熊出没》'%self.name)
        else:
            print('%s正在观看大电影' %self.name)

def main():
    stu1 = Student('张毅',22)
    stu1.study('python程序设计')
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()

if __name__ == '__main__':
        main()

