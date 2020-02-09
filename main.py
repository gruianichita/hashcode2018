class Ride:

    def __init__(self, row_start, col_start, row_finish, col_finish, earlyest_start, latest_start):
        self.row_start = row_start
        self.col_start = col_start
        self.row_finish = row_finish
        self.col_finish = col_finish
        self.earlyest_start = earlyest_start
        self.latest_start = latest_start


def main():
    file_name = 'b_should_be_easy.in'
    with open(f'in/{file_name}') as file:
        row, cols, vehicle_count, ride_count, bonus, step_count = file.readline().split()
        rides = list()
        for i in range(ride_count):
            row_start, col_start, row_finish, col_finish, earlyest_start, latest_start = file.readline().split()
            ride = Ride(row_start, col_start, row_finish, col_finish, earlyest_start, latest_start)
            rides.append(ride)


if __name__ == '__main__':
    main()
