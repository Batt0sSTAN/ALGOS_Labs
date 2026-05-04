import time, random

def task2(arr): #поиск второго максимального элемента в массиве
    max1 = arr[0]
    max2 = arr[0]
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
    return max2

def generate_array(n): #генерация массива
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def measure_time(func, data): #измерение времени
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(task2, arr)
        print(f"{n} {t:.6f}")