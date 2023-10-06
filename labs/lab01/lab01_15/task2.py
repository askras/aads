import dependencies

def task2(n):
    matrix_size = (n, n)
    matrix_a = dependencies.np.random.rand(*matrix_size)
    matrix_b = dependencies.np.random.rand(*matrix_size)
    result = dependencies.np.dot(matrix_a, matrix_b)
    return result


func = dependencies.get_usage_time(ndigits=5)(task2)

items = [i for i in range(1, 10000, 500)]
times = [func(i) for i in range(1, 10000, 500)]
for i in range(2):
    z = 1
    for j in range(len(times)):
        times[j] += func(z)
        z += 10
for i in range(len(times)):
    times[i] /= 3


fig = dependencies.plt.plot(items, times, 'r-', linewidth = 0.5)
dependencies.plt.title('Умножение матриц')
ax = dependencies.plt.gca()
ax.set_xlabel('Объем входных данных')
ax.set_ylabel('Время')
dependencies.plt.savefig('task2.png')