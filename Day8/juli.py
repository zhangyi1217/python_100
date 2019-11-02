from math import sqrt
class Point(object):
    def __init__(self,x, y):
        """初始化方法
        :param x:横坐标
        ：:param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self,x, y):
        """移动到指定位置
        :param x:新的横坐标
        :param y:新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self,dx, dy):
        """移动的增量
        :param dx:横坐标的增量
        :param dy:纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离
        :param other:另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx*dx + dy*dy)

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))

def main():
    p1 = Point(0, 1)
    p2 = Point(0, 2)
    print(p1)
    print(p2)
    p2.move_by(0, 0)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()