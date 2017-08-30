class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        import collections
        stack = collections.deque()
        period = [0] * n
        last_timestamp = -1
        last_func_id = -1
        last_order = None
        for log in logs:
            func_id, order, timestamp = log.split(':')
            func_id = int(func_id)
            timestamp = int(timestamp)
            if len(stack) == 0:
                stack.append(func_id)
                last_timestamp = timestamp
                last_func_id = func_id
                last_order = order
            else:
                if order == 'start':
                    period[stack[-1]] += timestamp - last_timestamp + (-1 if last_order == 'end' else 0)
                    stack.append(func_id)
                else:
                    assert stack[-1] == func_id
                    period[stack.pop()] += timestamp - last_timestamp + (1 if last_order == 'start' else 0)
                last_timestamp = timestamp
                last_func_id = func_id
                last_order = order
        return period
