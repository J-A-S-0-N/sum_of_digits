def answer(numa, numb):
    number = {
    }

    numa = str(numa)
    numb = str(numb)
    numa_list = list(numa)
    numb_list = list(numb)
    print(numa_list)
    for i in range(0, len(numa_list)):
        number.update({"".format(str(i)):numb_list[i]})
    print(number)
    # suma = numa[0] + 


answer(1776,1492)