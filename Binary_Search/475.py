def findRadius(houses, heaters):
    houses.sort()
    heaters.sort()

    radius = 0

    for house in houses:
        # manual binary search: first heater >= house
        left, right = 0, len(heaters) - 1
        pos = len(heaters)  # default if all heaters < house

        while left <= right:
            mid = (left + right) // 2
            if heaters[mid] >= house:
                pos = mid
                right = mid - 1
            else:
                left = mid + 1

        # distance to right heater
        right_dist = float('inf')
        if pos < len(heaters):
            right_dist = heaters[pos] - house

        # distance to left heater
        left_dist = float('inf')
        if pos > 0:
            left_dist = house - heaters[pos - 1]

        nearest = min(left_dist, right_dist)
        radius = max(radius, nearest)

    return radius
