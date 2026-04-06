import matplotlib.pyplot as plt
import numpy as np

# Данные из твоих экспериментов
experiments = ["3 DN\nBase", "3 DN\nOpt", "1 DN\nBase", "1 DN\nOpt"]
times = [29.91, 20.59, 19.75, 22.08]

# Цвета для столбцов
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

plt.figure(figsize=(10, 6))
bars = plt.bar(experiments, times, color=colors, edgecolor='black')

# Добавление значений на столбцы
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}s', 
             ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.title('Сравнение времени выполнения Spark приложений\n(Hadoop Cluster)', fontsize=14)
plt.ylabel('Время выполнения (секунды)', fontsize=12)
plt.xlabel('Конфигурация эксперимента', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, max(times) + 5) # Немного места сверху для цифр

# Сохранение графика
plt.savefig('results/comparison_chart.png', dpi=300, bbox_inches='tight')
plt.show()

print("График сохранен в results/comparison_chart.png")