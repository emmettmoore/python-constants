# -*- coding: utf-8 -*-

import datetime

from bad_car import get_featured_cars


def get_cars_to_display():
    featured_cars = get_featured_cars()
    if datetime.datetime.today().weekday() == 2:  # Tuesday!
        for featured_car in featured_cars:
            featured_car.price *= 1.05
    return featured_cars
