# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если
# фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли
# к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

profit = input("Укажите сколько выручки в этом месяце:\n>>>")
costs = input("Укажите сколько издержек в этом месяце:\n>>>")
number_employees = input("Укажите количество сотрудников в фирме:\n>>>")

if profit.isdigit() and costs.isdigit() and number_employees.isdigit():
    profit = float(profit)
    costs = float(costs)

    if profit > costs:
        difference = profit - costs
        profitability = int(difference / profit * 100)
        profit_employee = int(difference / int(number_employees))
        print(f"В этом месяце фирма отработала с прибылью {difference}.")
        print(f"Рентабельность фирмы равна {profitability}%.")
        print(f"Прибыль фирмы в расчете на одного сотрудника составляет {profit_employee}.")
    elif profit == costs:
        print("В этом месяце фирма отработала с нулевой прибылью.")
    else:
        print("В этом месяце фирма отработала в убыток.")
else:
    print("Ошибка: введенные данные не являются числами.")
