import random
<<<<<<< HEAD
def fill_list():
    lists = []
    for _ in range(10):
        lists.append(random.randit(1, 100))
    return lists
=======
import random
def generate_list():
    return [random.randit(1, 100) for _ in range(10)]

>>>>>>> amaizing_new_branch
