# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys

_, work_hrs, hr_cost, prem = sys.argv

salary = (float(hr_cost) * float(work_hrs)) + float(prem)

print(f"Зарплата = {salary}")
