import pickle

updates = {}
updates = pickle.load(open('updates.obj', 'rb'))

updateList = []
for file, count in updates.items():
    updateList.append((file,count))
updateList = sorted(updateList,key=lambda x: x[1], reverse=False)

for update in updateList:
    print(update)
