class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''


    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix.__str__(self)


my_Matrix1 = Matrix([[2, 5, 4], [6, 8, 1], [2, 4, 8], [1, 0, -1]])
my_Matrix2 = Matrix([[3, 5, 10], [11, 8, 0], [-2, 0, 4], [6, 2, 9]])
print(my_Matrix1.__add__(my_Matrix1))