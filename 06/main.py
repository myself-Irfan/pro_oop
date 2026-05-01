from parking_spot import ParkingSpot


def attempt(action: str, func, *args):
    try:
        func(*args)
        print(f'Success: {action}')
    except ValueError as e:
        print(f'Failed: {action} → {e}')


def main():
    slot = ParkingSpot()
    print(f'Initial state: {slot}\n')

    attempt('Parking ABC-1234', slot.park, 'ABC-1234')
    print(f'{slot}\n')

    attempt('Parking XYZ-9876', slot.park, 'XYZ-9876')
    print(f'{slot}\n')

    attempt('Unparking', slot.unpark)
    print(f'{slot}\n')

    attempt('Unparking', slot.unpark)
    print(f'{slot}\n')

    attempt('Parking with "" vehicle', slot.park, '')
    print(f'{slot}\n')

    attempt('Park with None', slot.park, None)
    print(f'{slot}\n')

    attempt('Parking DEF-5678', slot.park, 'DEF-5678')
    print(f'{slot}\n')


if __name__ == '__main__':
    main()
