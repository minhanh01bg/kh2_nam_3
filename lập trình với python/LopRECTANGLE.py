class Rectangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def perimeter(self):
        return self.x * 2 + self.y * 2

    def area(self):
        return self.x*self.y

    def color(self):
        return self.z.capitalize()


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
        t -= 1
