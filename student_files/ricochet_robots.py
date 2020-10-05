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

    robots = {}
    goal = {}
    walls = []

    def __init__(self, n):
        self.n = n

    def robot_position(self, robot: str):
        """ Devolve a posição atual do robô passado como argumento. """
        # TODO
        pass

    # TODO: outros metodos da classe
    def addRobot(self, robotInput: list):
        robots[robotInput[0]] =  [ int(x) for x in robotInput[1:] ]
        
    def addGoal(self, goalInput)
        goal[goalInput[0]] = [ int(x) for x in goalInput[1:] ]

[[1,1]]  + [[2,1]]
[[1,1],[2,1]]

    def addWall(self, wallInput) # por acabar
        coord1 = [ int(x) for x in wallInput[-2:] ]
        lst = [coord1]
        # key = wallInput[:-2]
        switch (wallInput[-1]):
            case "r":
                lst += [[coord1[0]+1, coord[1]]]
                break
            case "l":
                lst += [[coord1[0]-1, coord[1]]]
                break
            case "u":
                lst += [[coord1[0], coord[1]-1]]
                break
            case "d":
                lst += [[coord1[0], coord[1]+1]]
                break
        
def parse_instance(filename: str) -> Board:
    """ Lê o ficheiro cujo caminho é passado como argumento e retorna
    uma instância da classe Board. """
    # TODO
    inputFile = open(filename, 'r')
    n = inputFile.readLine()
    board = Board(n)

    """ Coordenadas dos Robots  """
    for i in range(4):
        robot = inputFile.readLine().split()
        board.addRobot(robot)

    """ Alvo """
    goal = inputFile.readLine().split()
    board.addGoal(goal)
    
    """ Paredes """
    n = inputFile.readLine()
    for i in range(n):
        wall = inputFile.readLine().split()
        board.addWall(wall)
        

class RicochetRobots(Problem):
    def __init__(self, board: Board):
        """ O construtor especifica o estado inicial. """
        # TODO: self.initial = ...
        pass

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
        pass

    def goal_test(self, state: RRState):
        """ Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se o alvo e o robô da
        mesma cor ocupam a mesma célula no tabuleiro. """
        # TODO
        pass

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
