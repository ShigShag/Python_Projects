list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [3, 4, 5, 6]
list.append(3)                      #Am Ende einfügen
list.insert(0, 1)                   #An einem Index einfügen   geht auch mit Liste
list.extend(list2)                  #Liste in Liste einfügen
list.remove(4)                      #Removed die Zahl
del list[1]                         #Removed den Index
pop = list.pop()                    #Removed den letzten Eintrag / Kann auch in einer Variable gespeichert werden
list.reverse()                      #Reversed Liste
list.sort()                         #Sorted Liste      Was auch geht hash_liste.sort(reverse=True)
sorted_list = sorted(list)          #Return sorted to variable
print(min(list))                    #Minimum der Liste
print(max(list))                    #Maximum der Liste
print(sum(list))                    #Summe der Liste
print(list.index(2))                #Index der Zahl 2
print(3 in list)                    #Boolean obitem in der liste ist



print(list)




print(list[::-2])
#hash_liste[start:end:step]

string = 'Helloiamdog1'
print(string[-1:-5:-1])

