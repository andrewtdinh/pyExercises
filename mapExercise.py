students = 'Andrew Dinh Byron Dong Joe Doe Jane Enuf'
names = students.split(' ')
fnames = map(lambda name: names.index(name) % 2 == 0, names)
lnames = map(lambda name: names.index(name) % 2, names)
names = [x, y for x in fnames]