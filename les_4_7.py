def fibo_gen():
    priv_el = 1
    for el in range(1, 16):
        yield el * priv_el
        priv_el = el * priv_el

fact = 1
num=1
for el in fibo_gen():
    print(f"факториал числа {num} равен {el}")
    num+=1


print("факториал числа равен ", fact)