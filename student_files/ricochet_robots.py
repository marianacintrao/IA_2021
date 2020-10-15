# ricochet_robots.py: Template para implementação do 1º projeto de Inteligência Artificial 2020/2021.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2

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

        # if case == "r":
        #     lst += [nextPo]
        # elif case == "l":
        #     lst += [nextPosition(coord, l)]
        # elif case == "u":
        #     lst += [[coord[0], coord[1]-1]]
        # elif case == "d":
        #     lst += [[coord[0], coord[1]+1]]
        # else:
        #     print("Erro\n")
                
        # self.walls += [lst]
        self.walls += [lst]
    

    def nextPosition(self, coord, direction):
        # print(coord, direction)
        newCoord = ()
        if direction == "r":
            newCoord = (coord[0], coord[1] + 1)
        elif direction == "l":
            newCoord = (coord[0], coord[1] - 1)
        elif direction == "u":
            newCoord = (coord[0] - 1, coord[1])
        elif direction == "d":
            newCoord = (coord[0] + 1, coord[1])
        
        if self.canMove(coord, newCoord):
            return newCoord
        return coord


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
        self.board = board

    def actions(self, state: RRState):
        """ Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento. """
        # TODO
        pass

    def result(self, state: RRState, action):
        """ Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação retornada deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state). """
        # TODO
        # pass
        self.board = state.board
        nextCoord = ()
        while True:
            # print("dentro do while")
            coord = self.board.robots[action[0]]
            nextCoord = self.board.nextPosition(coord, action[1])
            self.board.robots[action[0]] = nextCoord
            if coord == nextCoord:
                # print("dentro do  if do while")
                break
        return self

    def goal_test(self, state: RRState):
        """ Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se o alvo e o robô da
        mesma cor ocupam a mesma célula no tabuleiro. """
        for key in self.board.goal:
            if self.board.robots[key] == self.board.goal[key]:
                return True
        return False

    def h(self, node: Node):
        """ Função heuristica utilizada para a procura A*. """
        # TODO
        pass


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro de input de sys.argv[1],
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass


# parse_instance("i1.txt")
