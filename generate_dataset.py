import random
import csv

# Настройки датасета
num_rows = 100000
filename = 'dataset.csv'

# Возможные значения для категориальных признаков
categories = ['IT', 'Finance', 'Marketing', 'HR', 'Sales']
regions = ['North', 'South', 'East', 'West', 'Central']
education_levels = ['Bachelor', 'Master', 'PhD', 'College']

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Заголовок таблицы (6+ признаков, минимум 3 типа данных)
    # id: int
    # age: int
    # salary: float
    # category: string (categorical)
    # score: float
    # is_active: boolean
    # region: string (categorical)
    # experience_years: int
    writer.writerow(['id', 'age', 'salary', 'category', 'score', 'is_active', 'region', 'experience_years'])
    
    for i in range(num_rows):
        # Генерация случайных данных
        user_id = i + 1
        age = random.randint(20, 65)
        
        # Зарплата зависит от категории и опыта для реалистичности
        base_salary = random.uniform(30000, 150000)
        if random.choice(categories) == 'IT':
            base_salary *= 1.5
        
        salary = round(base_salary, 2)
        
        category = random.choice(categories)
        score = round(random.uniform(0, 100), 2)
        is_active = random.choice([True, False])
        region = random.choice(regions)
        experience_years = random.randint(0, 40)
        
        # Запись строки
        writer.writerow([
            user_id, 
            age, 
            salary, 
            category, 
            score, 
            is_active, 
            region, 
            experience_years
        ])

print(f"Датасет '{filename}' успешно создан! Строк: {num_rows}")