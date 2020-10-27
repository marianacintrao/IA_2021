import time
from ricochet_robots import *

if __name__ == "__main__":

    # parse board input
    board = parse_instance(sys.argv[1])

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)

    print("=== testing file:", sys.argv[1], "===\n");

    print("--- start astar search ---")

    # init running time
    start_time = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem, problem.h)

    # print and format solution
    string = ""
    actions = 0
    if (solution_node):
        while (solution_node.parent):
            string = solution_node.action[0] + " " + solution_node.action[1] + '\n' + string
            solution_node = solution_node.parent
            actions += 1
    string = str(actions) + '\n' + string[:-1]
    print(string)
    
    # get running time
    print("--- %s seconds ---\n" % (time.time() - start_time))

    print("--- start dfs search ---")

    # init running time
    start_time = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem, problem.h)

    # print and format solution
    string = ""
    actions = 0
    if (solution_node):
        while (solution_node.parent):
            string = solution_node.action[0] + " " + solution_node.action[1] + '\n' + string
            solution_node = solution_node.parent
            actions += 1
    string = str(actions) + '\n' + string[:-1]
    print(string)
    
    # get running time
    print("--- %s seconds ---\n" % (time.time() - start_time))

    print("--- start greddy search ---")

    # init running time
    start_time = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = greedy_search(problem, problem.h)

    # print and format solution
    string = ""
    actions = 0
    if (solution_node):
        while (solution_node.parent):
            string = solution_node.action[0] + " " + solution_node.action[1] + '\n' + string
            solution_node = solution_node.parent
            actions += 1
    string = str(actions) + '\n' + string[:-1]
    print(string)

    # get running time
    print("--- %s seconds ---\n" % (time.time() - start_time))