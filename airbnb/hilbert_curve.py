def hc(x, y, n):
    if n == 0: return 0

    border_len = 2 ** (n - 1)
    area_points = 4 ** (n - 1)

    if x < border_len and y < border_len:
        return area_points + hc(x, y, n - 1)
    elif x < border_len and y >= border_len:
        return hc(border_len - 1 - (y - border_len), border_len - 1 - x, n - 1)
    elif x >= border_len and y < border_len:
        return 2 * area_points + hc(x - border_len, y, n - 1)
    else:
        return 3 * area_points + hc(y - border_len, x - border_len, n - 1)
