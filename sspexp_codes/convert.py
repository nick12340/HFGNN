f = open("USA-road-t.BAY.gr")
output = open("bay-t","w")
n = 0
for line in f:
    n = n + 1
    if n%2 != 1:
        continue
    tokens = line.split(" ")
    u = int(tokens[1]) - 1
    v = int(tokens[2]) - 1
    d = int(tokens[3]) 
    output.write(str(u) + " " + str(v) + " " + str(d)+"\n")
output.close()
f.close()