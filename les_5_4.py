
out_f = open("lesson5_4_out.txt", "w")

with open("lesson5_4.txt") as f_obj:
    for el in f_obj:
        el = el.replace("One", "Один")
        el = el.replace("Two", "Два")
        el = el.replace("Three", "Три")
        el = el.replace("Four", "Четыре")
        print(el, file = out_f)

out_f.close()

