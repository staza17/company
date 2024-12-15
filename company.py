"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

if __name__ == "__main__":
    departments_titles = []
    employers_names = []
    employers_departments = []
    hundred_salary = []
    eighty_salary = []
    departments_money = []

    dep_sal = []
    dep_avg_sal = 0
    ninety_salary = set()
    female = ["Michelle", "Nicole", "Christina", "Caitlin"]
    fem_avg = {}
    vowels = ["a", "e", "i", "o", "u", "y"]
    vowels_names = set()

    dep_tax = {}
    name_sal_tax = []
    avg_taxes = {}
    dep_tax_list = []
    taxes_sorted = []
    dep_taxes = {}
    oneh_tax = []

    for department in departments:
        dep_tax[department["title"].lower()] = 0

    for tax in taxes:
        if tax["department"] == None:
            for department in dep_tax:
                dep_tax[department] += tax["value_percents"]
        if tax["department"] != None:
            if tax["department"].lower() in dep_tax:
                dep_tax[tax["department"].lower()] += tax["value_percents"]

    for department in departments:
        departments_titles.append(department["title"])
        money = 0
        salary_data = {}
        salary_data["title"] = department["title"]
        max_salary = 0
        fem_salary = 0
        fem_count = 0
        dep_taxes_sum = 0
        for employee in department["employers"]:
            full_name = employee["first_name"] + " " + employee["last_name"]
            employers_names.append(full_name)
            employers_departments.append(f'{full_name}: {department["title"]}')
            if employee["salary_rub"] > 100000:
                hundred_salary.append(full_name)
            elif employee["salary_rub"] < 80000:
                eighty_salary.append(full_name)
            money += employee["salary_rub"]
            tax_count = employee["salary_rub"] * dep_tax[department["title"].lower()] / 100
            if department["employers"].index(employee) == 0:
                min_salary = employee["salary_rub"]
            if max_salary < employee["salary_rub"]:
                max_salary = employee["salary_rub"]
            if min_salary > employee["salary_rub"]:
                min_salary = employee["salary_rub"]
            if employee["salary_rub"] > 90000:
                ninety_salary.add(employee["position"])
            if employee["first_name"] in female:
                fem_salary += employee["salary_rub"]
                fem_count += 1
            if employee["last_name"][-1] in vowels:
                vowels_names.add(full_name)
            dep_taxes_sum += int(tax_count)
            sal_tax = {}
            sal_tax["name"] = full_name
            sal_tax["tax"] = int(employee["salary_rub"] * dep_tax[department["title"].lower()] / 100)
            sal_tax["gross"] = employee["salary_rub"]
            sal_tax["net"] = employee["salary_rub"] - sal_tax["tax"]
            name_sal_tax.append(sal_tax)
        departments_money.append(f'{department["title"]} - {money} рублей в месяц')
        salary_data["avg"] = int(money/len(department["employers"]))
        salary_data["max"] = max_salary
        salary_data["min"] = min_salary
        dep_sal.append(salary_data)
        dep_avg_sal += int(money/len(department["employers"]))
        fem_avg[department["title"]] = int(fem_salary / fem_count)
        avg_taxes[department["title"]] = dep_taxes_sum/len(department["employers"])
        dep_taxes[dep_taxes_sum] = department["title"]
        dep_tax_list.append(dep_taxes_sum)

    dep_tax_list.sort()
    for dep in dep_tax_list:
        taxes_sorted.append(dep_taxes[dep])

    min_tax = name_sal_tax[0]["tax"] * 12
    min_tax_name = name_sal_tax[0]["name"]
    for employee in name_sal_tax:
        if (employee["tax"] * 12) > 100000:
            oneh_tax.append(employee["name"])
        if (employee["tax"] * 12) < min_tax:
            min_tax = employee["tax"] * 12
            min_tax_name = employee["name"]

    print(f'Названия отделов: {", ".join(departments_titles)}')
    print(f'Сотрудники компании: {", ".join(employers_names)}')
    for employee in employers_departments:
        print(employee)
    print(f'Зарплата больше 100к рублей у работников: {", ".join(hundred_salary)}')
    print(f'Зарплата меньше 80к на позициях: {", ".join(eighty_salary)}')
    for department in departments_money:
        print(department)

    for department in dep_sal:
        print(f'Минимальная зарплата в {department["title"]} - {department["min"]}')
    for department in dep_sal:
        print(f'{department["title"]}: минимальная зарплата - {department["min"]}, средняя зарплата - {department["avg"]}, максимальная зарплата - {department["max"]},')
    print(f'Средняя зарплата по всей компании - {int(dep_avg_sal/len(departments))}')
    print(f'Должности, которые получают больше 90к: {", ".join(ninety_salary)}')
    for department, salary in fem_avg.items():
        print(f'Средняя зарплата среди девушек по отделу {department} - {salary} рублей')
    print(f'Имена людей, чьи фамилии заканчиваются на гласную букву: {", ".join(vowels_names)}')

    for dep, tax in avg_taxes.items():
        print(f'Средний налог на сотрудника в {dep}: {int(tax)} рублей')
    for employee in name_sal_tax:
        print(f'{employee["name"]}: зарплата "на руки" - {int(employee["net"])}, зарплата с учётом налогов - {employee["gross"]}')
    print(f'Список отделов по возрастанию месячной налоговой нагрузки: {", ".join(taxes_sorted)}')
    print(f'Сотрудники, за которых компания платит больше 100к налогов в год: {", ".join(oneh_tax)}')
    print(f'Сотрудник, за которого компания платит меньше всего налогов: {min_tax_name}')


