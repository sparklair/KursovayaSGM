import sympy as sp
import numpy as np

# Определяем функцию и её производную аналитически
x_sym = sp.symbols('x')
f_expr = sp.exp(x_sym) - 3*x_sym - 2
f_prime_expr = sp.diff(f_expr, x_sym)

f_num = sp.lambdify(x_sym, f_expr, 'numpy')
f_prime_num = sp.lambdify(x_sym, f_prime_expr, 'numpy')

# Аналитическое отделение корней
print("\n[Аналитическое отделение корней]")
print(f"f(x) = {f_expr}")
print(f"f'(x) = {f_prime_expr} = 0")

critical_point = sp.nsolve(f_prime_expr, 1)
cp_float = float(critical_point)
print(f"Критическая точка (минимум): x0 ≈ {cp_float:.5f}")
print(f"Значение f в точке минимума: f(x0) ≈ {float(f_num(cp_float)):.5f}")

test_points = [-2, -0.5, 1, 2.5]
f_vals = [float(f_num(t)) for t in test_points]
for t, val in zip(test_points, f_vals):
    print(f"  f({t:.2f}) = {val:.5f}")

# Выбираем интервал для корня (2-й корень между 1.5 и 2.5)
a, b = 1.5, 2.5
print("Вывод: два интервала, содержащих корни.")
print(f"Выбираем корень на интервале [{a}, {b}]")
print(f"f({a}) = {f_num(a):.5f} (< 0), f({b}) = {f_num(b):.5f} (> 0)")

# Метод половинного деления
print("\n[Метод половинного деления]")
print("Условие остановки: |b - a| < 0.001")

eps = 0.001
iter_data = []
a_curr, b_curr = a, b
iteration = 0
max_iter = 50

while (b_curr - a_curr) >= eps and iteration < max_iter:
    x_mid = (a_curr + b_curr) / 2
    f_mid = f_num(x_mid)
    iter_data.append([
        iteration, a_curr, b_curr,
        f_num(a_curr), f_num(b_curr),
        x_mid, f_mid, b_curr - a_curr
    ])
    if f_num(a_curr) * f_mid < 0:
        b_curr = x_mid
    else:
        a_curr = x_mid
    iteration += 1

# Вывод таблицы итераций
print(f"{'iter':<5} | {'a':<10} | {'b':<10} | {'f(a)':<12} | {'f(b)':<12} | {'x':<10} | {'f(x)':<12} | {'|b-a|':<10}")
print("-" * 95)
for row in iter_data:
    print(f"{row[0]:<5} | {row[1]:<10.6f} | {row[2]:<10.6f} | {row[3]:<12.6f} | {row[4]:<12.6f} | "
          f"{row[5]:<10.6f} | {row[6]:<12.6f} | {row[7]:<10.6f}")
print("-" * 95)

final_x = (a_curr + b_curr) / 2
print(f"Корень: x ≈ {final_x:.3f} (с точностью до 0.001)")
print("=" * 70)
input("\nНажмите любую кнопку, чтобы выйти...")