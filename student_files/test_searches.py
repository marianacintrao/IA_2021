import time
from ricochet_robots import *
from search import *

if __name__ == "__main__":

    # parse board input
    board = parse_instance(sys.argv[1])

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)

    # print("=== testing file:", sys.argv[1], "===\n");

    print("--- start bfs search ---")

    # init running time
    start_time = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem, problem.h)
    # solution_node = greedy_search(problem, problem.h)
    # solution_node = depth_first_graph_search(problem)
    # solution_node = breadth_first_graph_search(problem)


    print("depois do astar")

    # print and format solution
    string = ""
    actions = 0
    if (solution_node):
        while (solution_node.parent):
            string = solution_node.action[0] + " " + solution_node.action[1] + '\n' + string
            solution_node = solution_node.parent
            actions += 1
    
    # gerados = solution_node.GERADOS
    # expandidos = solution_node.EXPANDIDOS
    string = str(actions) + '\n' + string[:-1]
    print(string)
    
    # get running time
    print("--- %s seconds ---" % (time.time() - start_time))
