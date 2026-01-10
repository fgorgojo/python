from ImportEngine.Cat import Cat

cats=[]
with open('tmp/c.txt', 'r') as f:
    data = f.read()
    print(data)
    rows = data.split()
    for row in rows:
        lrow = row.split(',')
        new_cat = Cat(lrow[0], int(lrow[1]), bool(lrow[2]))
        cats.append(new_cat)   

print(cats )