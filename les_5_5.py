out_f = open("lesson_5_5.txt", "w")
for num in range(0,101):
    print(num,  end = ' ', file = out_f)
out_f.close()

inp_f = open("lesson_5_5.txt", "r")
content = inp_f.readline()
lst = [int(x) for x in content.split()]
print(sum(lst))
inp_f.close()

