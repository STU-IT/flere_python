def taxi_fare(km):
    grundpris = 4.00
    kmpris    = 0.25 / 0.140    # 25 cent pr 140 meter

    if km > 0:
        turpris = grundpris + km * kmpris
    else:
        turpris = grundpris
    return turpris

print(taxi_fare(1))
print(taxi_fare(3.36))
print(taxi_fare(10))
print(taxi_fare(0.01))



print(taxi_fare(-1))
print(taxi_fare(-3.36))
print(taxi_fare(-10))
print(taxi_fare(0))

