'''
Created on May 1, 2017

@author: bastian
'''
from timeit import default_timer as timer
import json

from aimacode.search import (
    breadth_first_search, astar_search, breadth_first_tree_search,
    depth_first_graph_search, uniform_cost_search,
    greedy_best_first_graph_search, depth_limited_search,
    recursive_best_first_search)
from my_air_cargo_problems import air_cargo_p1, air_cargo_p2, air_cargo_p3
from run_search import PROBLEMS,  PrintableProblem, show_solution

SEARCHES = [
    ["breadth_first_search", breadth_first_search, ""],
    ['depth_first_graph_search', depth_first_graph_search, ""],
    ['uniform_cost_search', uniform_cost_search, ""],
    ['astar_search', astar_search, 'h_1'],
    ['astar_search', astar_search, 'h_ignore_preconditions'],
    ['astar_search', astar_search, 'h_pg_levelsum'],
]


def run_search(search, problem):
    print('Search algo: {}-{}, Problem: {}'.format(
        search[0], search[2], problem[0]))
    start = timer()
    ip = PrintableProblem(problem[1]())
    if search[2] != "":
        h = getattr(ip, search[2])
        node = search[1](ip, h)
    else:
        node = search[1](ip)
    end = timer()
    result = dict()
    result["Expansions"] = ip.succs
    result["Goal tests"] = ip.goal_tests
    result["New nodes"] = ip.states
    result["Time elapsed"] = end - start
    result["Plan length"] = len(node.solution())
    result["Plan"] = "\n".join(
        ['{}{}'.format(a.name, a.args) for a in node.solution()])
    return result


if __name__ == '__main__':
    s_result = dict()
    for s in SEARCHES:
        p_result = dict()
        for p in PROBLEMS:
            p_result[p[0]] = run_search(s, p)

        s_result['{}-{}'.format(s[0], s[2])] = p_result

    with open('search_result.json', 'w') as fp:
        json.dump(s_result, fp)
