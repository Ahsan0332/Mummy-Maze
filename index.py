import movement
import algo
import time
import pygame 
pygame.init()
pygame.display.init()

height = width = 512
dimension = 8
sqSize =  height // dimension
font_1 = pygame.font.SysFont('Courier New', 15)
this_sentence=font_1.render('Write text here',True,(0,0,0))
images = {}

l = [[0]*8 for i in range(8)]

for row in range(dimension):
    # print(row)
    for col in range(dimension):
        # print(row)
        # print(col)
        l[row][col] = (algo.Node('n' + str(row) + str(col)))

for row in range(8):
    for col in range(8):

        if row == 0:
            if col == 0:
                l[row][col].add_neighbor(l[row + 1][col])
                l[row][col].add_neighbor(l[row][col + 1])
            elif col == 7:
                l[row][col].add_neighbor(l[row + 1][col])
                l[row][col].add_neighbor(l[row][col - 1])
            else:
                l[row][col].add_neighbor(l[row + 1][col])
                l[row][col].add_neighbor(l[row][col - 1])
                l[row][col].add_neighbor(l[row][col + 1])
        
        elif row == 7:
            if col == 0:
                l[row][col].add_neighbor(l[row - 1][col])
                l[row][col].add_neighbor(l[row][col + 1])
            elif col == 7:
                l[row][col].add_neighbor(l[row - 1][col])
                l[row][col].add_neighbor(l[row][col - 1])
            else:
                l[row][col].add_neighbor(l[row - 1][col])
                l[row][col].add_neighbor(l[row][col - 1])
                l[row][col].add_neighbor(l[row][col + 1])

        else:
            if col == 0:
                l[row][col].add_neighbor(l[row - 1][col])
                l[row][col].add_neighbor(l[row + 1][col])
                l[row][col].add_neighbor(l[row][col + 1])
            elif col == 7:
                l[row][col].add_neighbor(l[row - 1][col])
                l[row][col].add_neighbor(l[row + 1][col])
                l[row][col].add_neighbor(l[row][col - 1])

            else:
                l[row][col].add_neighbor(l[row - 1][col])
                l[row][col].add_neighbor(l[row + 1][col])
                l[row][col].add_neighbor(l[row][col - 1])
                l[row][col].add_neighbor(l[row][col + 1])


def loadImages():
        images['mummy'] = pygame.transform.scale(pygame.image.load("images/mummy.jpeg") , (sqSize , sqSize))
        images['player'] = pygame.transform.scale(pygame.image.load("images/player.jpeg") , (sqSize , sqSize))

def main(): 
    global screen
    screen = pygame.display.set_mode((height,width))
    clock = pygame.time.Clock() 

    mummyPos = movement.index_2d(movement.board , 'mummy')
    print(mummyPos)
    playerPos = movement.index_2d(movement.board , 'player')
    print(playerPos)
    running = True

    while running:    
        screen.fill((0,0,0))
        drawBoard(movement.board)
        defeatCheck = movement.index_2d(movement.board , "player")

        if  defeatCheck[0] == -1 or defeatCheck[1] == -1 :
            print("----------DEFEAT--------")
            time.sleep(2)
            break

        if movement.index_2d(movement.board , "player") == [7,1]:   
            print("--------VICTORY--------")
            time.sleep(2)
            break    

        prevPlayerPos = movement.index_2d(movement.board , 'player')  
        prevMummyPos = movement.index_2d(movement.board , 'mummy')

        for e in pygame.event.get():          
            if e.type == pygame.QUIT:
                running = False            
            if e.type == pygame.KEYDOWN:    
                if e.key == pygame.K_LEFT:
                    movement.moveLeft()
                elif e.key == pygame.K_RIGHT:
                    movement.moveRight()
                elif e.key == pygame.K_UP:
                    movement.moveUp()
                elif e.key == pygame.K_DOWN:
                    movement.moveDown()

                playerPos = movement.index_2d(movement.board , 'player')
                print("player" , playerPos)
                mummyPos = movement.index_2d(movement.board , 'mummy')
                print("mummy" , mummyPos)

                movement.mummyMovement(algo.ShortestPath(l[prevMummyPos[0]][prevMummyPos[1]] , l[playerPos[0]][playerPos[1]]).bfs())
                
                print("Entering loop")
                
            for row in range(8):
                for col in range(8):
                    l[row][col].visited = False
                                      
        pygame.display.flip()   
        clock.tick(30)
        
def drawBoard(board):

    loadImages()
    colors = [pygame.Color("grey") ,pygame.Color("black")]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[(r+c) % 2]
            pygame.draw.rect(screen , color , pygame.Rect(c*sqSize , r*sqSize , sqSize , sqSize)  )

            piece = board[r][c]
            if piece != "--":
                screen.blit(images[piece] , pygame.Rect(c*sqSize ,r*sqSize  , sqSize , sqSize))
    
main()

