from typing import List, Tuple


class Ride:

    def __init__(self, row_start, col_start, row_finish, col_finish, earlyest_start, latest_finish):
        self.row_start = row_start
        self.col_start = col_start
        self.row_finish = row_finish
        self.col_finish = col_finish
        self.earlyest_start = earlyest_start
        self.latest_finish = latest_finish


class Vehicle:

    def __init__(self):
        self.rides_ids = []
        self.cur_col = 0
        self.cur_row = 0
        self.cur_step = 0

    def assign_ride(self, ride_id: int):
        self.rides_ids.append(ride_id)


def main():
    file_name = 'c_no_hurry.in'
    with open(f'in/{file_name}') as file:
        row, cols, vehicle_count, ride_count, bonus, step_count = [int(val) for val in file.readline().split()]
        rides = list()
        for i in range(ride_count):
            row_start, col_start, row_finish, col_finish, earlyest_start, latest_finish = [int(val) for val in
                                                                                           file.readline().split()]
            ride = Ride(row_start, col_start, row_finish, col_finish, earlyest_start, latest_finish)
            rides.append(ride)
        final_score = 0
        vehicles: List[Vehicle] = []
        for i in range(vehicle_count):
            vehicle = Vehicle()
            vehicles.append(vehicle)

        remain_ride_ids = set(range(ride_count))
        cnt = 0
        while remain_ride_ids:

            best_rate: int = 0
            best_combo: Tuple[int, int] = tuple()
            spent_time_of_best_combo = 0
            score_of_best_combo = 0
            for remain_ride_id in remain_ride_ids:
                for vehicle_id in range(vehicle_count):
                    score = 0
                    vehicle: Vehicle = vehicles[vehicle_id]
                    ride: Ride = rides[remain_ride_id]
                    distance_to_start: int = abs(ride.col_start - vehicle.cur_col) + abs(
                        ride.row_start - vehicle.cur_row)
                    step_to_arrive = vehicle.cur_step + distance_to_start
                    ride_distance = abs(ride.col_start - ride.col_finish) + abs(ride.row_start - ride.row_finish)
                    if step_to_arrive <= ride.earlyest_start:
                        score = bonus + ride_distance
                    else:
                        if step_to_arrive + ride_distance <= ride.latest_finish:
                            score = ride_distance

                    spent_time = distance_to_start + ride_distance
                    rate = score / spent_time
                    if rate >= best_rate:
                        spent_time_of_best_combo = spent_time
                        best_rate = rate
                        best_combo = (remain_ride_id, vehicle_id)
                        score_of_best_combo = score

            remain_ride_ids.remove(best_combo[0])
            vehicles[best_combo[1]].assign_ride(best_combo[0])
            vehicles[best_combo[1]].cur_row = ride.row_finish
            vehicles[best_combo[1]].cur_col = ride.col_finish
            vehicles[best_combo[1]].cur_step = spent_time_of_best_combo
            final_score += score_of_best_combo

            if cnt % 10 == 0:
                print(len(remain_ride_ids), '!!!!!!!!')
            cnt += 1

        print(final_score)


if __name__ == '__main__':
    main()
