def distance_from_zero(wok):
    if type(wok) == int or type(wok) == float:
        return abs(wok)
    else:
        return "nope"


print(distance_from_zero(-12))


def rental_car_cost(days):
    car_cost = 40 * days

    # if days >