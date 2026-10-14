import math

def parking_fee(minutes):
    if minutes < 0:
        raise ValueError("Час не може бути негативним")
    if minutes <= 15:
        return 0
    if minutes > 480: 
        return 80
    hours = math.ceil(minutes / 60)
    return hours * 10