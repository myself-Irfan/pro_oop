from random import randint

def populate_init_list(list_size: int) -> list[int]:
    return [randint(1, 99) for _ in range(list_size)]

def main():
    age_list = populate_init_list(10)

    adult_count = 0
    minor_count = 0

    for age in age_list:
        if age >= 18:
            adult_count += 1
            print(f'user with {age} is adult')
        else:
            minor_count += 1
            print(f'user with {age} is minor')

    print(f"Adults: {adult_count}")
    print(f"Minors: {minor_count}")

if __name__ == '__main__':
    main()
