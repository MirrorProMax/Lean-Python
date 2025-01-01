import multiprocessing

def loop():
    while True:
        pass

if __name__ == "__main__":
    for i in range(multiprocessing.cpu_count()-1):#减1是为了给CPU留一个核心
        print("第",i+1,"个CPU核心")
        p = multiprocessing.Process(target=loop)
        p.start()