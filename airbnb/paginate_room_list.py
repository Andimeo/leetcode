def paginate(num, results):
    if not results:
        return []
    ans = []
    remaining_items = []
    host_set = set()
    num_added = 0
    index_results = 0
    while index_results < len(results):
        if num_added % num == 0:
            host_set.clear()
        added = False
        if len(remaining_items) > 0:
            for item in remaining_items:
                host_id, _, _, _ = item.split(',')
                if host_id not in host_set:
                    ans.append(item)
                    num_added += 1
                    host_set.add(host_id)
                    added = True
                    break
            if added:
                remaining_items.remove(item)
                continue
        if index_results < len(results):
            host_id, _, _, _ = results[index_results].split(',')
            if host_id not in host_set:
                ans.append(results[index_results])
                index_results += 1
                num_added += 1
                host_set.add(host_id)
                added = True
            else:
                remaining_items.append(results[index_results])
                index_results += 1
    for item in remaining_items:
        ans.append(item)
        num_added += 1
    l = []
    for i, item in enumerate(ans):
        if i != 0 and i % num == 0:
            l.append('')
        l.append(item)
    assert num_added == len(results)
    return l


results = [
    '1,28,300.6,San Francisco',
    '4,5,209.1,San Francisco',
    '20,7,203.4,Oakland',
    '6,8,202.9,San Francisco',
    '6,10,199.8,San Francisco',
    '1,16,190.5,San Francisco',
    '6,29,185.3,San Francisco',
    '7,20,180.0,Oakland',
    '6,21,162.2,San Francisco',
    '2,18,161.7,San Jose',
    '2,30,149.8,San Jose',
    '3,76,146.7,San Francisco',
    '2,14,141.8,San Jose',
]
print(paginate(5, results))
