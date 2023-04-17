from allcode import buggy, serial_comms


def main():
    car = buggy.Buggy(serial_comms.SerialDevice())
    print(f'API Version: {car.api_version()}')
    print(f'{car.battery_voltage()}V')


if __name__ == '__main__':
    main()
