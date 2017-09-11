def print_terrains(terrains, waters):
    max_height = max(terrains)
    for height in range(max_height, -1, -1):
        for i in range(len(terrains)):
            if terrains[i] >= height:
                print('+', end='')
            elif terrains[i] + waters[i] >= height:
                print('w', end='')
            else:
                print(' ', end='')
        print()


def pour_water(terrains, location, water):
    waters = [0] * len(terrains)
    print_terrains(terrains, waters)
    while water > 0:
        left = location - 1
        while left >= 0 and terrains[left] + waters[left] <= terrains[left + 1] + waters[left + 1]:
            left -= 1

        if terrains[left + 1] + waters[left + 1] < terrains[location] + waters[location]:
            location_to_pour = left + 1
        else:
            right = location + 1
            while right < len(terrains) and terrains[right] + waters[right] <= terrains[right - 1] + waters[right - 1]:
                right += 1
            if terrains[right - 1] + waters[right - 1] < terrains[location] + waters[location]:
                location_to_pour = right - 1
            else:
                location_to_pour = location
        waters[location_to_pour] += 1
        water -= 1
    print_terrains(terrains, waters)


pour_water([5, 4, 2, 1, 2, 3, 2, 1, 0, 1, 2, 4], 5, 14)
