a = 1
print(a) # 1
def func1():
    global a
    print(a) # 1

def func2():
    a = 3
    def func3():
        nonlocal a
        print(a) # 3
    func3()

func1()
func2()