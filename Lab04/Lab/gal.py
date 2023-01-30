with open("./Lab04/Lab/Lab04-1.gal", "r",encoding="utf-8") as f:
  f.readline()
  gal = dict()
  for line in f:
    line = line.strip().split()
    print('length'+str(len(line)))
    # print('this line'+str(line))
    # print('this is the line '+ gal[line[0]])
    # print()
    gal[line[0]] = f.readline().strip().split()
    print(line[0])
    print(gal[line[0]])
    # line = line.strip().split()
    # gal[line[0]] = str(line)
    # print(len(gal[line[0]]))

    
# f = open("./Lab04/Lab/Lab04-1.gal", "r",encoding="utf-8")

  


  # print('this is the '+ gal[line[0]]+ ' and the '+line[1])




