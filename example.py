# -*- coding: utf-8 -*-


class Car(object):
    def __init__(self, make, model, year, color, num_seats):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_seats = num_seats


FEATURED_CARS = {
    'car1': {
        'make': 'Subaru',
        'model': 'Forester',
        'year': 2011,
        'color': 'silver',
        'num_seats': 5,
        'transmission': 'manual',

    },
}


def get_featured_car_simple(car_id):
    return FEATURED_CARS[car_id]


def get_featured_car(car_id):
    return Car(id=car_id, **FEATURED_CARS[car_id])
