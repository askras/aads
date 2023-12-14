class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash_function_sum(self, key):
        return sum(map(ord, key)) % self.size

    def hash_function_square(self, key, attempt):
        return (sum(map(ord, key)) + attempt**2) % self.size

    def hash_function_double(self, key, attempt):
        return (sum(map(ord, key)) + attempt * (7 - (sum(map(ord, key)) % 7))) % self.size

    def insert_linear(self, key, value):
        attempt = 0
        index = self.hash_function_sum(key)

        while self.table[index] is not None:
            attempt += 1
            index = (index + 1) % self.size

            if attempt == self.size:
                break

        self.table[index] = (key, value)

    def insert_quadratic(self, key, value):
        attempt = 0
        index = self.hash_function_square(key, attempt)

        while self.table[index] is not None:
            attempt += 1
            index = self.hash_function_square(key, attempt)

            if attempt == self.size:
                break

        self.table[index] = (key, value)

    def insert_double(self, key, value):
        attempt = 0
        index = self.hash_function_double(key, attempt)

        while self.table[index] is not None:
            attempt += 1
            index = self.hash_function_double(key, attempt)

            if attempt == self.size:
                break

        self.table[index] = (key, value)

    def search(self, key, method):
        attempt = 0

        if method == 'linear':
            index = self.hash_function_sum(key)
        elif method == 'quadratic':
            index = self.hash_function_square(key, attempt)
        elif method == 'double':
            index = self.hash_function_double(key, attempt)

        while self.table[index] is not None:
            current_key, current_value = self.table[index]
            if current_key[:3] == key[:3]:
                return current_value

            attempt += 1

            if method == 'linear':
                index = (index + 1) % self.size
            elif method == 'quadratic':
                index = self.hash_function_square(key, attempt)
            elif method == 'double':
                index = self.hash_function_double(key, attempt)

            if attempt == self.size:
                break

        return None

    def display(self):
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")


hash_table = HashTableOpenAddressing(11)

with open("tel.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 2):
        name = lines[i].strip()
        number = lines[i + 1].strip()
        hash_table.insert_linear(name, number)
        hash_table.insert_quadratic(name, number)
        hash_table.insert_double(name, number)

# hash_table.display()

search_key = "Куз"
result_linear = hash_table.search(search_key, 'linear')
result_quadratic = hash_table.search(search_key, 'quadratic')
result_double = hash_table.search(search_key, 'double')

print(f"Найденный номер для {search_key} (линейный): {result_linear}")
print(f"Найденный номер для {search_key} (квадратичный): {result_quadratic}")
print(f"Найденный номер для {search_key} (двойное хеширование): {result_double}")
