import sympy as sp
import numpy as np

# Определяем функцию и её производную аналитически
x_sym = sp.symbols('x')
f_expr = 3*x_sym**4 + 4*x_sym**3 - 12*x_sym**2 - 5
f_prime_expr = sp.diff(f_expr, x_sym)

f_num = sp.lambdify(x_sym, f_expr, 'numpy')
f_prime_num = sp.lambdify(x_sym, f_prime_expr, 'numpy')

# Аналитическое отделение корней
print("\n[Аналитическое отделение корней]")
print(f"f(x) = {f_expr}")
print(f"f'(x) = {f_prime_expr}")
print("Находим критические точки (f'(x) = 0):")
    
critical_points = sp.nroots(f_prime_expr, n=4)
cp_floats = [float(cp) for cp in critical_points]
print(f"Критические точки: {cp_floats}")

print("Проверяем знаки f(x) на интервалах:")
test_points = [-3, -2, -0.5, 0.5, 1.5, 3]
f_vals = [float(f_num(t)) for t in test_points]
for t, val in zip(test_points, f_vals):
    print(f"  f({t:.2f}) = {val:.5f}")

print("Наблюдаем смену знака на интервалах: (-3, -2) и (1, 3)")
a, b = 1, 3
print("Выбираем корень на интервале [1, 3]")
print(f"f(1) = {f_num(1.0):.5f} (< 0), f(3) = {f_num(3.0):.5f} (> 0)")

# Метод касательных
print("\n[Метод касательных]")
print("Начальное приближение x0 = 2.0")
print("Условие остановки: |x_n - x_{n-1}| < 0.001")

x_prev = 2.0
eps = 0.001
newton_data = []
iteration = 0
max_iter = 20

while iteration < max_iter:
    fx = f_num(x_prev)
    fpx = f_prime_num(x_prev)
    if abs(fpx) < 1e-12:
        print("Производная близка к нулю, метод может расходиться.")
        break
    x_next = x_prev - fx / fpx
    err = abs(x_next - x_prev)
    newton_data.append([iteration, x_prev, fx, fpx, err])
    if err < eps:
        break
    x_prev = x_next
    iteration += 1

# Вывод таблицы итераций
print(f"{'iter':<5} | {'x_n':<12} | {'f(x_n)':<12} | {'f\'(x_n)':<12} | {'|x_{n+1} - x_n|':<15}")
print("-" * 70)
for row in newton_data:
    print(f"{row[0]:<5} | {row[1]:<12.6f} | {row[2]:<12.6f} | {row[3]:<12.6f} | {row[4]:<15.6f}")
print("-" * 70)

final_x = newton_data[-1][1] if newton_data else x_prev
print(f"Корень: x ≈ {final_x:.5f} (с точностью до 0.001)")
print("=" * 70)