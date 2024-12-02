import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {
    'номер': [1, 2, 3, 4, 5],
    'месяц': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май'],
    'фио': ['Иванов И.И.', 'Петров П.П.', 'Сидоров С.С.', 'Кузнецов К.К.', 'Смирнов С.С.'],
    'номер телефона': ['1234567890', '0987654321', '1122334455', '2233445566', '3344556677'],
    'льгота': [0, 1, 2, 0, 1],
    'оплата': [1000, 1000, 1000, 1000, 1000],
    'внесено': [1000, 750, 500, 1000, 750]
}


df = pd.DataFrame(data)


def calculate_payment(row):
    if row['льгота'] == 0:
        return row['оплата']
    elif row['льгота'] == 1:
        return row['оплата'] * 0.75
    elif row['льгота'] == 2:
        return row['оплата'] * 0.50

df['оплата'] = df.apply(calculate_payment, axis=1)


df['долг'] = df['оплата'] - df['внесено']


paid = df['внесено'].sum()
debt = df['долг'].sum()


average_debt = df['долг'].mean()


count_above_average_debt = (df['долг'] > average_debt).sum()


min_debt = df['долг'].min()
max_debt = df['долг'].max()


debt_by_fio = df.groupby('фио')['долг'].sum().reset_index()


monthly_summary = df.groupby('месяц').agg({'оплата': 'sum', 'внесено': 'sum'}).reset_index()


print("Общая сумма внесенной оплаты:", paid)
print("Общая сумма долга:", debt)
print("Среднее значение долга:", average_debt)
print("Количество абонентов с долгом больше среднего:", count_above_average_debt)
print("Минимальный долг:", min_debt)
print("Максимальный долг:", max_debt)
print("\nСумма долга по каждой фамилии:\n", debt_by_fio)
print("\nСумма начисленной и внесенной оплаты по месяцам:\n", monthly_summary)


monthly_summary.set_index('месяц').plot(kind='bar', figsize=(10, 6))
plt.title('Сумма начисленной и внесенной оплаты по месяцам')
plt.ylabel('Сумма')
plt.xlabel('Месяц')
plt.xticks(rotation=45)
plt.legend(['Оплата', 'Внесено'])
plt.tight_layout()
plt.show()