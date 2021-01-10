def nearest_square(limit):
    i = 0
    while (i+1)**2 <= limit:
        i += 1
    return i ** 2
