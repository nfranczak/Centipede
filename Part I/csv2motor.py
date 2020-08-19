import csv
import operator
f = [[0, 0, 0, 0]]
note_on = []
mt = [[0,0]]
time = 0.
con = [[0., 0.]]
tem = []
g = []

def finder (elem, index, list):
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


def instructions (midi_time, motor, attack, epsilon, tempo_start):
    if finder(tempo_start, 1, mt) == False:
        mt.append([float(epsilon), float(tempo_start)])

    if finder(motor, 1, note_on) == False and int(attack) != 0:
        note_on.append([int(midi_time), int(motor), float(epsilon)])
        f.append([int(midi_time), int(motor), int(attack), 0])
    else:
        if len(note_on) == 0:
            pass
        else:
            dur = 0.
            index = finder(motor, 1, note_on)
            if float(note_on[index][2]) == float(epsilon):
                dur = (float(midi_time) - float(note_on[index][0])) * float(epsilon)
                note_on.remove(note_on[index])
            else:
                index1 = finder(float(note_on[index][2]), 0, mt) # finds index of epsilon that was in the original occurance of note
                index2 = finder(float(epsilon), 0, mt) # finds index of epsilon that has occured now
                index_next = int(index1) + 1
                dur = (float(mt[index_next][1]) - float(note_on[index][0])) * float(mt[index1][0]) # the time between the note beginning and the next tempo starting
                index1 = index_next
                index_next += 1
                while int(index_next) < int(index2):
                    tb = float(dur)
                    dur = (float(mt[index_next][1]) - float(mt[index1][1])) * float(mt[index1][0]) + float(tb)
                    index1 = index_next
                    index_next += 1
                if int(index1) != int(index2):
                    tb = float(dur)
                    dur = (float(mt[index2][1]) - float(mt[index1][1])) * float(mt[index1][0]) + float(tb) # calculates the time between the last tempo start and the second to last tempo start
                tb = float(dur)
                dur = (float(midi_time) - float(mt[index2][1])) * float(mt[index2][0]) + float(tb) # calculates the time between when the note is off and the tempo starts
                note_on.remove(note_on[index])
                index = finder(motor, 1, f)
                if int(f[index][3]) == 0:
                    f[index][1] = int(f[index][1]) - 21
                    f[index][3] = float(dur)
            index = finder(motor, 1, f)
            if int(f[index][3]) == 0:
                f[index][1] = int(f[index][1]) - 21
                f[index][3] = float(dur)


with open('new chad.csv', 'r') as csv_file:
    for row in csv_file:
        indicies = list(filter(lambda x: row[x] == ',', range(len(row))))
        if ' Header' in row:
            alpha = row[(indicies[4]+1):len(row)]

        elif ' Tempo' in row:
            beta = row[(indicies[2]+1):len(row)]
            beta1 = int(beta) / 1000000. #the number of seconds per quarter note
            epsilon = float(beta1) / float(alpha) #how long each clock pulse is, in seconds
            tempo_start = row[(indicies[0] + 1):indicies[1]]
            f.append(['tempo', float(epsilon), float(tempo_start)])

        elif ' Note_on_c' in row:
            motor = row[(indicies[3] + 1):indicies[4]]
            midi_time = row[(indicies[0] + 1):indicies[1]]
            attack = row[(indicies[4] + 1):len(row)]

            instructions(midi_time, motor, attack, epsilon, tempo_start)


f.remove(f[0])
for row in f:
    if 'tempo' in row:
        tem.append(row[1]) #epsilon of tempo
        tempo_time = float(row[2]) #time of tempo
        if float(row[2]) != float(tempo_time):
            tt = (float(row[2]) - float(tempo_time)) * float(tem[-2])
            tb = float(time)
            time = (float(tt) - float(tb)) + float(tb)
    else:
        if finder(row[0], 0, con) == False:
            con.append([row[0], 0])
            tb = float(time)
            time = (float(con[-1][0]) - float(con[-2][0])) * float(tem[-1]) + float(tb)
            con[-1][1] = float(time)
            row[0] = float(time)
        elif row[0] == con[-1][0]:
            row[0] = float(con[-1][1])


for row in f:
    if 'tempo' not in row:
        g.append(row)

with open('ready liz_et3.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for row in g:
        writer.writerow(row)

# for i in g:
#     print i
