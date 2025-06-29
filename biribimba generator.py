#Biribimba generators

import random

first_array = ["biri","bara","biro","bima","brita","birso","pary","bipi","blim"]
second_array = ["bimba","srimba","primba","grimba","blimba","bymba","pumba", "brimba", "da",
                "pirimba", "babibma", "ЗА ДОНБІМБА", "Сама такая", "dabimba", "mirimba",
                "ganbimba", "bara bara biri biri biri", "medalka"]

first_number = random.randint(0, len(first_array)-1)
second_number = random.randint(0, len(second_array)-1)
print(first_array[first_number] + second_array[second_number])

input()
