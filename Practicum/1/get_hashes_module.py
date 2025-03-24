import numpy as np
import math

def get_hashes(item, size_arr, count=1):
    # Преобразуем входной элемент в строку и затем в число (например, используя хеш Python)
    seed_value = hash(item) % 442
    hashes = []

    def truncate_to_power_of_two(arr):
        # Находим максимальную степень двойки, не превышающую длину массива
        length = len(arr)
        power = math.floor(math.log2(length))
        
        # Обрезаем массив до найденной длины
        return str(arr[:power]) 

    # Создаем три разных хеша с разными seed-ами
    def generate_binary_hash(seed, length=size_arr):
        np.random.seed(seed)  # Задаем seed для детерминированности
        binary_string = ''.join(str(np.random.randint(0, 2)) for _ in range(length))

        return truncate_to_power_of_two(binary_string)
    
    # Генерируем три разных хеша
    for i in range(count):
        hashes.append(generate_binary_hash(seed_value + i))

    return hashes