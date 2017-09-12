def doesCircleExist(commands):
    results = []
    for command in commands:
        initial_x, initial_y = 0, 0
        x, y = 0, 0
        direction = 0
        for c in command:
            if c == 'L':
                direction = (direction + 1) % 4
            elif c == 'R':
                direction = (direction - 1 + 4) % 4
            else:
                if direction == 0:
                    y += 1
                elif direction == 1:
                    x -= 1
                elif direction == 2:
                    y -= 1
                else:
                    x += 1
        if direction == 0 and (x != initial_x or y != initial_y):
            results.append('NO')
        else:
            results.append('YES')
    return results
