# -*- coding: utf-8 -*-
#给car赋值100
cars = 100
#给车内空间赋值为4
space_in_a_car = 4
#给司机赋值为30
drivers = 30
#给乘客赋值为90
passengers = 90
#空车等于没有司机的车
cars_not_driven = cars - drivers
#能开的车等于司机
cars_driven = drivers
#总共能搭载的乘客数等于所有能开的车乘以每辆车的空间
carpool_capacity = cars_driven * space_in_a_car
#每辆车上的人等于乘客除以总共的车数
average_passengers_per_car = passengers / cars_driven


print "there are",cars, "cars available."
print "there are only",drivers,"drivers available."
print "there will be",cars_not_driven,"empty cars today."
print "we can transport", carpool_capacity,"people today."
print "we have", passengers, "to carpool today."
print "we need to put about",average_passengers_per_car,"in each car"

