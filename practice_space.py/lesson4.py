# A TRAVEL WEATHER PLANNER 
distance_mi = 3
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

if bool(distance_mi) is False:
    print(False)
elif distance_mi <= 1:
    if is_raining != True:
        print(True) 
    else:
        print(False)

elif distance_mi > 1 and distance_mi <= 6:
    if has_bike and is_raining != True:
        print(True)
    else:
        print(False)
elif distance_mi > 6:
    if has_ride_share_app or has_car:
        print(True)
    else:
        print(False)

