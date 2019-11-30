if 0 == False:
    print('what the fuck')
a = [0, 240, 480, 720, 1200, 1440, 1680]
b = [0, 240, 480, 720, 960, 1440, 1680]
c = [0, 240, 480, 720, 960, 1200, 1440]
d = [240, 480, 720, 960, 1200, 1440, 1680]

def inserter (list, element, index):

    if str(index) == 'none':
        value = 0

        if int(element) < int(list[0]):
            list.insert(0,int(element))
            return 0
        elif int(element) > int(list[int(len(list) - 1)]):
            list.append(int(element))
            return int(len(list) - 1)

        while value <= int(len(list) - 1):
            if int(element) >= int(list[value]) and int(element) <= int(list[value + 1]):
                list.insert(int(value + 1),int(element))
                return value
            value +=1



# print(inserter(a, 960, 'none')) # 3
# print a
# print(inserter(b, 1200, 'none')) # 4
# print b
# print(inserter(c, 1680, 'none')) # 7
# print c
# print(inserter(d, 0, 'none')) # 0
# print d
# print (' ')


f = [[0, 0],
[0.375, 42, 24, 0.28125],
[0.375, 54, 28, 0.28125],
[0.75, 42, 24, 0.28125],
[0.75, 54, 28, 0.28125],
[1.125, 54, 28, 0.28125],
[1.125, 42, 24, 0.28125]]

e = [0, 0, 0.0015625, 0.0016129041666666669, 0.0015243895833333334, 0.0015527958333333332, 0.0016129041666666669, 0.0019083979166666667, 0.0024038458333333333, 0.00471698125, 0.0012886604166666667, 0.00125628125, 0.0011627916666666666, 0.0012019229166666666]

g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 47, 48, 44, 45]

mt = [[0, 0], [0.0015625, 0.0]]

note_on = [[240, 63, 0.0015625]]
con = [[0.0, 0.0], [240, 0.375]]

def finder (elem, index, list): #in order to make this function work you must input an element with the index of the list you are checking for it, in
    value = 0
    if str(index) == 'none':
        for k in reversed(list):
            if float(k) == float(elem):
                value = int(len(list) - 1) - int(value)
                return value
            else:
                value += 1
    else:
        for k in reversed(list):
            if float(elem) == float(k[index]):
                value = int(len(list) - 1) - int(value)
                return value
            else:
                value += 1
    return False



print(finder(240, 0, con))
# print(finder(63, 1, note_on))
# print(finder(75, 1, note_on))
# print(finder(240, 'none', mt)) # = 2
# print(finder(37, 'none', mt)) # = False
# print(finder(78, 1, f)) # = 49
# print(finder(0.0015625, 'none', e)) # = 2
# print(finder(44, 'none', g)) # = 37
# print(finder(4080, 'none', mt)) # = 17
# print(finder(83, 1, note_on)) # = 2

        # print(' ')
        # print('this is list f:' + str(f))
        # print('this is list note_on: ' + str(note_on))
        # print(' ')
        # if int(tempo_start) > int(mt[-1]): #this is done to compensate for the difference in time btwn the last note and the new tempo start
        #     tb = float(time)
        #     time = (float(tempo_start) - float(mt[-1])) * float(e[-1]) + float(tb)
        #
        # index = finder(motor, 1, f)
        # print('TIME CHECK')
        # print(' ')
        # if float(f[index][0]) == float(f[index - 1][0]):
        #     print('it is the case that: ' + str(f[index][0]) + ' == ' + str(f[index - 1][0]))
        #     j = 0
        #     while f[index][0] == f[index - j][0]:
        #         j += 1
        #
        #     if finder(f[index][0], 'none', mt) == False:
        #         print('it is the case that ' + str(f[index][0]) + ' IS NOT IN list mt: ' + str(mt) )
        #         tb = float(time)
        #         time = (float(f[index][0]) - float(mt[-1])) * float(epsilon) + float(tb)
        #         print('this is what you just did: ' + str(time) + ' = ' + '(' + str(f[index][0]) + ' - ' + str(mt[-1]) + ')' + ' * ' + str(epsilon) + ' + ' + str(tb))
        #         print(' ')
        #         print(' ')
        #         inserter(f[index][0], 'none', mt)
        #         print('this is the list mt now: ' + str(mt))
        #         while j != 0:
        #             f[index - (j - 1)][0] = float(time)
        #             g.append(index - (j - 1))
        #             j -= 1
        #         print('this is list g: ' + str(g))
        #     else:
        #         print('is it the case that ' + str(f[index][0]) + ' is in list mt ')
        #         new_index = finder(f[index][0], 'none', mt)
        #         tb = float(time)
        #         time = (float(mt[new_index]) - float(mt[new_index - 1])) * float(epsilon) + float(tb)
        #         print('this is what you just did: ' + str(time) + ' = ' + '(' + str(mt[new_index]) + ' - ' + str(mt[new_index - 1]) + ')' + ' * ' + str(epsilon) + ' + ' + str(tb))
        #
        # elif finder(index, 'none', g) == (False or 0) :
        #     print('it is the case that ' + str(index) + ' NOT IN list g ' + str(g))
        #     new_index = inserter(f[index][0], 'none', mt)
        #     tb = float(time) #make sure that the backwards order of appending here is uniform among all midi files
        #     t1 = float(mt[new_index]) - float(mt[new_index - 1])
        #     time = float(t1) * float(epsilon) + float(tb)
        #     f[index][0] = float(time)
        #     print('this is what you just did: ' + str(time) + ' = ' + '(' + str(mt[new_index]) + ' - ' + str(mt[new_index - 1]) + ')' + ' * ' + str(epsilon) + ' + ' + str(tb))
        #
        # print(' ')
        # print(' ')
        # print(' ')
        # print(' ')
        # print('OVER')
        # print(' ')
        # print(' ')
        # print(' ')
        # print(' ')

        # def inserter (element, index, list):
        #     value = 0
        #     if str(index) == 'none':
        #         if int(element) < int(list[0]):
        #             list.insert(0,int(element))
        #             return 0
        #         elif int(element) > int(list[int(len(list) - 1)]):
        #             list.append(int(element))
        #             return int(len(list) - 1)
        #
        #         while value <= int(len(list) - 1):
        #             if int(element) >= int(list[value]) and int(element) <= int(list[value + 1]):
        #                 list.insert(int(value + 1),int(element))
        #                 return value + 1
        #             value +=1
