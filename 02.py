import csv


def read_csv(filename) -> list[tuple[str, int]]:
    salary_list = []

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            salary_list.append((row['Name'].strip(), int(row['Salary'])))

        return salary_list


def find_max_salary(salary_list: list[tuple[str, int]]) -> list[tuple[str, int]]:
    max_salary = max(salary_list, key=lambda salary: salary[1])[1]
    return [salary for salary in salary_list if salary[1] == max_salary]


def find_min_salary(salary_list: list[tuple[str, int]]) -> list[tuple[str, int]]:
    min_salary = min(salary_list, key=lambda salary: salary[1])[1]
    return [salary for salary in salary_list if salary[1] == min_salary]

def print_salaries(label: str, entries: list[tuple[str, int]]):
    for name, salary in entries:
        print(f'{label}: {name}\t{salary}')


def main():
    salary_list = read_csv('salarysheet.csv')

    print_salaries('Max', find_max_salary(salary_list))
    print_salaries('Min', find_min_salary(salary_list))


if __name__ == '__main__':
    main()
