# imports
from libsRicerca.searchGeneric import AStarSearcher
from libsRicerca.searchProblem import Arc, Search_problem_from_explicit_graph

# defining the problem
building_problem = Search_problem_from_explicit_graph(
    {   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'},
    [   Arc('A', 'B', 2),
        Arc('A', 'C', 3),
        Arc('A', 'D', 4),
        Arc('B', 'E', 2),
        Arc('B', 'F', 3),
        Arc('C', 'J', 7),
        Arc('D', 'H', 4),
        Arc('F', 'D', 2),
        Arc('H', 'G', 3),
        Arc('J', 'G', 4)],
    start = 'A',
    goals = {'G'},
    hmap = {
        'A': 7,
        'B': 5,
        'C': 9,
        'D': 6,
        'E': 3,
        'F': 5,
        'G': 0,
        'H': 3,
        'J': 4,
    }
)


# defining the solver 
A_Star = AStarSearcher(building_problem)

# solve
for i in range (0,8):
    solution= A_Star.search()
    print(f"Path = {solution}\nCost = {solution.cost}")


