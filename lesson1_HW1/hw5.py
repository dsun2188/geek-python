# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым
# результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчете на одного сотрудника.

revenue = int(input("Введите сумму выручки:"))
costs = int(input("Введите сумму издержек:"))

profit = revenue - costs

if profit:
    profitability = profit / revenue
    print(f"Прибыль = {profit}, рентабельность = {profitability}")

    workers_count = int(input("Укажите кол-во сотрудников:"))

    profit_per_worker = profit / workers_count
    print(f"Прибыль на одного сотрудника = {profit_per_worker}")
else:
    print(f"Убыток = {profit}")
