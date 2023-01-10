import random
from bottle import route, abort, run
import mathgenerator


@route('/api/gen/n/<num:int>/ids/<ids>')
def generate_problems(num, ids):
    if not (1 <= num <= 1000):
        abort(400, "Invalid Request")
    func_ids = ids.split("-")
    results = []
    for _ in range(num):
        func_id = int(random.choice(func_ids))
        problem, solution = mathgenerator.genById(func_id)
        results.append({"f": func_id, "q": problem, "a": solution})
    return {'data': results}
