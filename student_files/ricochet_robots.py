# ricochet_robots.py: Template para implementação do 1º projeto de Inteligência Artificial 2020/2021.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 98:
# 92510 Lúcia Silva
# 93737 Mariana Cintrão

from search import Problem, Node, astar_search, breadth_first_tree_search, \
    depth_first_tree_search, greedy_search
import sys


class RRState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = RRState.state_id
        RRState.state_id += 1

    def __lt__(self, other):
        """ Este método é utilizado em caso de empate na gestão da lista
        de abertos nas procuras informadas. """
        return self.id < other.id


class Board:
    """ Representacao interna de um tabuleiro de Ricochet Robots. """

    def __init__(self, n):
        self.n = n
        self.robots = {}
        self.goal = {}
        self.walls = []

    def robot_position(self, robot: str):
        """ Devolve a posição atual do robô passado como argumento. """
        return self.robots[robot]


    def addRobot(self, robotInput):
        self.robots[robotInput[0]] = (int(robotInput[1]), int(robotInput[2]))
        
    def addGoal(self, goalInput):
        self.goal[goalInput[0]] = (int(goalInput[1]), int(goalInput[2]))

    def addWall(self, wallInput): 
        coord = (int(wallInput[0]), int(wallInput[1]))
        lst = [coord]
        direction = wallInput[-1]
        lst += [self.nextPosition(coord, direction)]
        self.walls += [lst]


        
    
    
    def nextPosition(self, coord, direction, wall = None):
        newCoord = ()
        if direction == "r":
            newCoord = (coord[0], coord[1] + 1)
        elif direction == "l":
            newCoord = (coord[0], coord[1] - 1)
        elif direction == "u":
            newCoord = (coord[0] - 1, coord[1])
        elif direction == "d":
            newCoord = (coord[0] + 1, coord[1])      
        return newCoord


    def canMove(self, coord1, coord2): 
        if (self.n + 1 in coord2) or (0 in coord2) :
            return False
        for lst in self.walls:
            if coord1 in lst and coord2 in lst:
                return False
        for key in self.robots:
            if self.robots[key] == coord2:
                return False
        return True


def parse_instance(filename: str) -> Board:
    """ Lê o ficheiro cujo caminho é passado como argumento e retorna
    uma instância da classe Board. """
    # TODO
    fileInput = []
    # i = 1 
    with open(filename) as f:
        fileInput = [line.rstrip('\n') for line in f]
    
    board = Board(int(fileInput[0]))

    """ Coordenadas dos Robots  """
    for i in range(1, 5):
        robot = fileInput[i].split()
        board.addRobot(robot)

    """ Alvo """
    goal = fileInput[5].split()
    board.addGoal(goal)

    """ Paredes """ 
    n = int(fileInput[6])
    for i in range(7, 7 + n):
        wall = fileInput[i].split()
        board.addWall(wall)
    
    return board


class RicochetRobots(Problem):
    def __init__(self, board: Board):
        """ O construtor especifica o estado inicial. """
        self.initial = RRState(board)
        

    def actions(self, state: RRState):
        """ Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento. """
        s = RRState(state.board)
        actions = []
        directions = ('r', 'l', 'd', 'u')
        nextCoord = ()
        for robot in s.board.robots:
            for direction in directions:
                action = (robot, direction)
                coord = s.board.robots[robot]
                nextCoord = s.board.nextPosition(coord, direction)
                if s.board.canMove(coord, nextCoord):
                    actions += (action,)
        return actions
                
                        
    def result(self, state: RRState, action):
        """ Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação retornada deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state). """
        s = RRState(state.board)
        actions = self.actions(state)
        if action in actions:
            while True:
                coord = s.board.robots[action[0]]
                nextCoord = s.board.nextPosition(coord, action[1])
                if not s.board.canMove(coord, nextCoord):
                    break
                s.board.robots[action[0]] = nextCoord
        return s


    # def path_cost(self, c, state1, action, state2):
    #     return Problem.path_cost(self, c, state1, action, state2)
    
    
    def goal_test(self, state: RRState):
        """ Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se o alvo e o robô da
        mesma cor ocupam a mesma célula no tabuleiro. """
        for key in self.initial.board.goal:
            if self.initial.board.robots[key] == state.board.goal[key]:
                return True
        return False

    def h(self, node: Node):
        """ Função heuristica utilizada para a procura A*. """
        return 1
        


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro de input de sys.argv[1],
    # Usar uma técnica de procura para resolver a instância,
    # Retirar astara solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.

    board = parse_instance(sys.argv[1])

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    print(problem.initial.board.walls)

    # print(problem.initial.board.robots)
    # initial_state = RRState(board)
    # initial_node = Node(initial_state)

    # Obter o nó solução usando a procura A*:
    # solution_node = astar_search(problem, problem.h(initial_node))
    solution_node = astar_search(problem, problem.h)

    if (solution_node):
        # print("solution node existe!")
        # action_list = solution_node.solution()
        # print(action_list)
        # print(solution_node.state.board.robots)
        if solution_node.parent and problem.goal_test(solution_node.state):
            print("YES!")
        else:
            print(":((((((((")
        while (solution_node.parent):
            print(solution_node.action)
            solution_node = solution_node.parent
    





