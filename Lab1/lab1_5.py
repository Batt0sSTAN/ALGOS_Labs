import time, random, sys, tracemalloc

def task5(arr): #Сортировка пузырьком
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def generate_array(n): #генерация массива
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    arr.sort()
    return arr

def measure_memory(func, data):
    tracemalloc.start()
    func(data)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak

def measure_time(func, data):#измерение времени
    start = time.perf_counter() 
    result = func(data)
    end = time.perf_counter()
    return end - start


if __name__ == '__main__':
    sizes = [10000]
    for n in sizes:
        arr = generate_array(n)
        t, mem = measure_time(task5, arr), measure_memory(task5, arr)
        print(f"{n}     {t:.6f}    {mem}")