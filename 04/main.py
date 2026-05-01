from bank_account import BankAccount


def main():
    acc_1 = BankAccount(
        number=1212,
        name='IA',
        balance=100.00
    )
    acc_1.get_account_info()

    acc_2 = BankAccount(
        number=1312,
        name='AA',
        balance=100.00
    )
    acc_2.get_account_info()

    acc_2.transfer(
        amount=20,
        other_account=acc_1
    )

    acc_1.get_account_info()
    acc_2.get_account_info()


if __name__ == '__main__':
    main()
