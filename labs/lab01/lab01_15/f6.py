import dependencies


def f6(n):
    min = dependencies.vector[0]
    for i in dependencies.vector[:n]:
        if i < min:
            min = i
    return min


func = dependencies.get_usage_time(ndigits=5)(f6)

items = range(1, 500001, 500)
times = [func(i) for i in items]
for i in range(2):
    for j in range(len(items)):
        times[j] += func(items[j])
for i in range(len(times)):
    times[i] /= 3



fig = dependencies.plt.plot(items, times, 'r-', linewidth = 0.5)
dependencies.plt.title('Поиск минимума простым перебором')
ax = dependencies.plt.gca()
ax.set_xlabel('Объем входных данных')
ax.set_ylabel('Время')
dependencies.plt.savefig('graph6.png')