import time, random

def task4(n): #Построение таблицы умножения
    table=[]
    for i in range(1, n+1):
        row=[]
        for j in range(1, n+1):
            row.append(i*j)
        table.append(row)
    return table

def measure_time(func, n): #измерение времени
    start = time.perf_counter()
    func(n)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        t = measure_time(task4, n)
        print(f"{n} {t:.6f}")