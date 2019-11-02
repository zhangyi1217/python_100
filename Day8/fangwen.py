class shuxingfangwen():
    def __init__(self,foo):
        self.__foo = foo #加两个下划线表示私有属性

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = shuxingfangwen('hello')
    test.__bar()
    print(test.__foo)   #此处因为__bar是私有的，所以调用的时候没有这个属性

if __name__ == '__main__':
    main()