#Students mark management program


def students(n) :
    d={}
    for i in range (n) :
        while True :
            name = input(f"Enter Student {i+1} name : ")
            if name in d :
                print("Name already exist , try different name..")
            else :
                break
        while True :
            mark = float(input(f"Enter student {i+1} mark : "))
            if mark < 0 :
                print("Mark sholud not be negative.")
            else :
                break
        d[name] = mark
    return d

def toppers(d) :
    s = sorted(d.items(), key = lambda items: items[1] , reverse=True)
    top = s[:3]
    print("Top 3 Rank holders are :")
    i = 1
    for key, value in s :
        print(f"Rank {i} : {key}\t{value} marks")
        i += 1

n = int(input("Enter number of Students : "))
a = students(n)
b = toppers(a)
