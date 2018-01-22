# -*- coding: utf-8 -*-


class Car(object):
    def __init__(self, make, model, year, color, price, miles):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.miles = miles


FEATURED_CARS = [
    {
        'make': 'Subaru',
        'model': 'Forester',
        'year': 2011,
        'color': 'silver',
        'price': 10000,
        'miles': 50000,
    },
    {
        'make': 'Honda',
        'model': 'Civic',
        'year': 2009,
        'color': 'grey',
        'price': 8000,
        'miles': 20000,
    },
    {
        'make': 'Nissan',
        'model': 'Maxima',
        'year': 1992,
        'color': 'white',
        'price': 300,
        'miles': 140000,
    },
    {
        'make': 'Acura',
        'model': 'MDX',
        'year': 2004,
        'color': 'red',
        'price': 12000,
        'miles': 90000,
    }
]


def get_featured_cars(car_ids=None):
    """Returns a copy of the definition of a all featured cars.
    """

    return [Car(**car_definition) for car_definition in FEATURED_CARS]
