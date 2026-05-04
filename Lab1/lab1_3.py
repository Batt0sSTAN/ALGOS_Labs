import time, random

def task3(arr, target): #Бинарный поиск
    right = len(arr) - 1
    left = 0

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            return "Target is found"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "Target was NOT found"

def generate_array(n): #генерация массива
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    arr.sort()
    return arr

def measure_time(func, data, target): #измерение времени
    start = time.perf_counter()
    func(data, target)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(task3, arr, random.randint(0, 10000))
        print(f"{n} {t:.6f}")