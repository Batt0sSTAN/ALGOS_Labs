import time, random, sys

def task5(arr): #Бинарный поиск
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

def measure_time(func, data): #измерение времени
    start = time.perf_counter()
    result = func(data)
    end = time.perf_counter()
    time_t = end - start

    mem = sys.getsizeof(result)
    for item in result:
        mem += sys.getsizeof(item)
    return time_t, mem


if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t, mem = measure_time(task5, arr)
        print(f"{n}     {t:.6f}    {mem}")