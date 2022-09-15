"""Task 4.10 from PYTHON-09"""

from collections import defaultdict, deque

def task_manager(task_list: list) -> defaultdict:
    """Function returns queues for each server.

    Args:
        task_list (list): includes corteges
                        (<number of task>,
                        <name of server>,
                        <task prioity: False or True>)

    Returns:
        defaultdict: key - name of server,
                     value - deque of server's queue
    """

    result = defaultdict(deque)
    for task in task_list:
        if task[2]:
            result[task[1]].appendleft(task[0])
        else:
            result[task[1]].append(task[0])
    return result

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

print(task_manager(tasks))
