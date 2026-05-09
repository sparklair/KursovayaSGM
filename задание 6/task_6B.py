from math import cos, sin, pi

h = 0.1
x0 = 0
y0 = 1
x_end = 1


def f(x, y):
    return 1 - sin((1.75*x + y) * pi / 180) + (0.1 * y) / (x + 2)


n = int(round((x_end - x0) / h))
x = [x0 + i * h for i in range(n + 1)]

y = [y0]
f_vals = []
q = []
dy = []
dq = []
d2q = []
d3q = []

# Метод Эйлера
for i in range(min(3, n)):
    fi = f(x[i], y[i])
    f_vals.append(fi)
    qi = h * fi
    q.append(qi)
    y_next = y[i] + h * fi
    y.append(y_next)
    dy.append(y_next - y[i])

    if i >= 1:
        dq.append(q[i] - q[i-1])
    if i >= 2:
        d2q.append(dq[i-1] - dq[i-2])
    if i >= 3:
        d3q.append(d2q[i-2] - d2q[i-3])

# для последней точки(i=2)
if n >= 3:
    f3 = f(x[3], y[3])
    f_vals.append(f3)
    q3 = h * f3
    q.append(q3)
    dq.append(q[3] - q[2])
    d2q.append(dq[2] - dq[1])
    d3q.append(d2q[1] - d2q[0])

# Метод Адамса
for i in range(3, n):
    delta_y = q[i] + 0.5 * dq[i-1] + (5/12) * d2q[i-2] + (3/8) * d3q[i-3]
    dy.append(delta_y)
    y_next = y[i] + delta_y
    y.append(y_next)

    f_next = f(x[i+1], y_next)
    f_vals.append(f_next)
    q_next = h * f_next
    q.append(q_next)

    dq.append(q_next - q[i])
    d2q.append(dq[i] - dq[i-1])
    d3q.append(d2q[i-1] - d2q[i-2])

# Вывод таблицы
print('\n' + '='*100)
print('Таблица приближённых значений интеграла дифференциального уравнения')
print('='*100)
print(f'{'i':>2} | {'x':>8} | {'y':>9} | {'Δy':>9} | {'y\'=f(x,y)':>12} | {'q=h*y\'':>9} | {'Δq':>9} | {'Δ²q':>9} | {'Δ³q':>9}')
print('-'*100)

for i in range(len(x)):
    xi = x[i]
    yi = y[i] if i < len(y) else None
    dyi = dy[i] if i < len(dy) else None
    fi = f_vals[i] if i < len(f_vals) else None
    qi = q[i] if i < len(q) else None
    dqi = dq[i-1] if i-1 < len(dq) and i >= 1 else None
    d2qi = d2q[i-2] if i-2 < len(d2q) and i >= 2 else None
    d3qi = d3q[i-3] if i-3 < len(d3q) and i >= 3 else None

    def fmt(val):
        if val is None:
            return '-'.center(9)
        return f'{val:9.4f}'
    
    row = (f'{i:2} | {xi:8.4f} | {fmt(yi)} | {fmt(dyi)} | {fmt(fi)} | {fmt(qi)} | {fmt(dqi)} | {fmt(d2qi)} | {fmt(d3qi)}')
    print(row)
print('='*100)
