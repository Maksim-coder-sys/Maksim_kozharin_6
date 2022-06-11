from sys import argv
print(argv)
with open("bakery.csv",'r',encoding = "utf-8") as all:
    n=0
    f=0
    for i in range(int(argv[2])):
        rez = all.readline().replace('\n','')
        n+=1
        f=f+len(rez)+2
        if int(argv[1]) <= n <= int(argv[2]):
            all.seek ( f -len(rez)-2)
            print(all.readline().replace('\n',''))

    # all.close()