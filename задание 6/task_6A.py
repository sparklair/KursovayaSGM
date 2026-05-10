from math import sin, pi

#ROUND_CHARS = 4
h = 0.1
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
count_x = len(x)
y = [1]

def f(x: float, y: float):
	return 1 + 0.8*y*sin(x*pi/180) - 2*y*y

for i in range(count_x):
	k0 = f(x[i], y[i])
	print(f'\nПосчитано k0 для i={i}: {k0:.4f}')
	k1 = f(x[i] + h/2, y[i] + h/2 * k0)
	print(f'Посчитано k1 для i={i}: {k1:.4f}')
	k2 = f(x[i] + h/2, y[i] + h/2 * k1)
	print(f'Посчитано k2 для i={i}: {k2:.4f}')
	k3 = f(x[i] + h, y[i] + h * k2)
	print(f'Посчитано k3 для i={i}: {k3:.4f}')
	y1 = y[i] + h/6 * (k0 + 2*k1 + 2*k2 + k3)
	print(f'Y для i={i} равен -> {y1:.4f}')
	y.append(y1)
	
input("\nНажмите любую кнопку, чтобы выйти...")