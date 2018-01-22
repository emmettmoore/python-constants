# -*- coding: utf-8 -*-


class Car(object):
    def __init__(self, make=None, model=None, year=None,
    color=None, miles=None, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.miles = miles
        self.price = price


FEATURED_CARS = [
    Car(
        make='Subaru',
        model='Forester',
        year=2011,
        color='silver',
        miles=50000,
        price=10000,
    ),
    Car(
        make='Honda',
        model='Civic',
        year=2009,
        color='grey',
        miles=20000,
        price=8000,
    ),
    Car(
        make='Nissan',
        model='Maxima',
        year=1992,
        color='white',
        miles=140000,
        price=900,
    ),
    Car(
        make='Acura',
        model='MDX',
        year=2004,
        color='red',
        miles=90000,
        price=12000,
    )
]


def get_featured_cars():
    return [car for car in FEATURED_CARS]
