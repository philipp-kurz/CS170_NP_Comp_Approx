import pickle
position = {}
with open('leaderboard.txt', 'r') as file:
    data = file.read().replace('\n', '')
    occs = data.split("<tr><td>")[1:]
    for occ in occs:
        a = occ.split("\'")
        name = a[1]
        pos = (a[2].split("</td></tr>")[-2]).split("</td><td>")[-1]
        position[name] = int(pos)
avg = 0
first = 0
firstPos = set()
for file, pos in position.items():

    avg += pos
    if pos == 1:
        first += 1
        print(file, pos)
        firstPos.add(file)
avg /= len(position)
print("Average position: " + str(avg))
print("Number of first place positions: " + str(first))
pickle.dump(firstPos, open('firstPositions.obj', 'wb'))


