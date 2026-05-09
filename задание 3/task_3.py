import numpy as np

# Интегрируемая функция
def f(x):
    return (1 + 0.9 * x**2) / (1.5 + np.sqrt(0.4 * x**2 + 0.7))

# Пределы интегрирования
a = 1.3
b = 3.46

# Формула трапеций (n = 20)
n_trap = 20
h_trap = (b - a) / n_trap

x_trap = np.linspace(a, b, n_trap + 1)
y_trap = f(x_trap)

sum_trap = (y_trap[0] + y_trap[-1]) / 2 + np.sum(y_trap[1:-1])
I_trap = h_trap * sum_trap

# Вывод таблицы для трапеций
print("="*70)
print("а) Формула трапеций (n = 20)")
print("="*70)
print("-"*30)
print(f"h = {h_trap:.4f}")
print(f"{'i':>4} | {'x_i':>10} | {'y_i':>10}")
print("-"*30)
for i in range(len(x_trap)):
    print(f"{i:4} | {x_trap[i]:10.4f} | {y_trap[i]:10.4f}")
print("-"*30)
print(f"Результат: I ≈ {I_trap:.3f} (с тремя десятичными знаками)")
print("="*70)

# Формула Симпсона (n = 8)
n_simp = 8
h_simp = (b - a) / n_simp

x_simp = np.linspace(a, b, n_simp + 1)
y_simp = f(x_simp)

sum_simp = y_simp[0] + y_simp[-1]
for i in range(1, n_simp):
    if i % 2 == 1:
        sum_simp += 4 * y_simp[i]
    else:
        sum_simp += 2 * y_simp[i]
I_simp = (h_simp / 3) * sum_simp

# Вывод таблицы для Симпсона
print("\n\n" + "="*70)
print("б) Формула Симпсона (n = 8)")
print("="*70)
print(f"h = {h_simp:.4f}")
print("-"*45)
print(f"{'i':>4} | {'x_i':>10} | {'y_i':>10} | {'Коэф.':>6}")
print("-"*45)
for i in range(len(x_simp)):
    coef = 1 if i == 0 or i == n_simp else (4 if i % 2 == 1 else 2)
    print(f"{i:4} | {x_simp[i]:10.4f} | {y_simp[i]:10.4f} | {coef:6}")
print("-"*45)
print(f"Результат: I ≈ {I_simp:.4f} (с четырьмя десятичными знаками)")
print("="*70)
input("\nНажмите любую кнопку, чтобы выйти...")
