# Description:The program takes the inputs, turns into floating points and assign them to the attributes of the object created. Then the boolean method is called to check and the results will be outputed by calling the methods created.
class LinearEquation:
    def __init__(self):
        self.p1 = (0,0)
        self.p2 = (0,0)
        self.p3 = (0,0)
        self.p4 = (0,0)
    def count_a(self):
        return self.p1[1] - self.p2[1]
    def count_b(self):
        return self.p2[0] - self.p1[0]
    def count_c(self):
        return self.p3[1] - self.p4[1]
    def count_d(self):
        return self.p4[0] - self.p3[0]
    def count_e(self):
        return (self.p1[1] - self.p2[1])*self.p1[0] + (self.p2[0] - self.p1[0])*self.p1[1]
    def count_f(self):
        return (self.p3[1] - self.p4[1])*self.p3[0] + (self.p4[0] - self.p3[0])*self.p3[1]
    def __str__(self) -> str:
        ps = ''
        a = self.count_a()
        b = self.count_b()
        c = self.count_c()
        d = self.count_d()
        e = self.count_e()
        f = self.count_f()
        ps += f'The equation of the first line with points {self.p1} and {self.p2} is:\n{a}x + {b}y = {e}\n'
        ps += f'The equation of the second line with points {self.p3} and {self.p4} is:\n{c}x + {d}y = {f}\n'
        print(ps)
    def check(self):
        return bool((self.count_a()*self.count_d() - self.count_b()*self.count_c()) != 0)
    def x_inter(self):
        a = self.count_a()
        b = self.count_b()
        c = self.count_c()
        d = self.count_d()
        e = self.count_e()
        f = self.count_f()
        return round((e*d-b*f)/(a*d-b*c),1)
    def y_inter(self):
        a = self.count_a()
        b = self.count_b()
        c = self.count_c()
        d = self.count_d()
        e = self.count_e()
        f = self.count_f()
        return round((a*f-e*c)/(a*d-b*c),1)
def main():
    point_1 = input('Enter the x and y coordinates of point1: ').split()
    point_2 = input('Enter the x and y coordinates of point2: ').split()
    point_3 = input('Enter the x and y coordinates of point3: ').split()
    point_4 = input('Enter the x and y coordinates of point4: ').split()
    p_1 = [float(value) for value in point_1]
    p_2 = [float(value) for value in point_2]
    p_3 = [float(value) for value in point_3]
    p_4 = [float(value) for value in point_4]
    intersection = LinearEquation()
    intersection.p1 = tuple(p_1)
    intersection.p2 = tuple(p_2)
    intersection.p3 = tuple(p_3)
    intersection.p4 = tuple(p_4)
    intersection.__str__()
    if intersection.check():
        print(f'\nThe intersection point is: ({intersection.x_inter()},{intersection.y_inter()})')
    else:
        print('\nThe two lines do not intersect.')
main()



    