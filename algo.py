class Node:
  def __init__(self, name):
    self.name = name
    self.prev = None
    self.neighbors = []
    self.visited = False

  #Method to connect nodes
  def add_neighbor(self, node):
    self.neighbors.append(node)
    node.neighbors.append(self)

  #Node representaion
  def __repr__(self):
    return self.name

class ShortestPath:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def bfs(self):
    #Create queue 
    queue = []
    #Visit and add the start node to the queue
    self.start.visited = True
    queue.append(self.start)
    #BFS until queue is empty
    while queue:
      #Pop a node from queue for search operation
      current_node = queue.pop(0)
      #Loop through neighbors nodes to find the 'end' 
      for node in current_node.neighbors:
        if not node.visited:
          #visit and add neighbors nodes to the queue
          node.visited = True
          queue.append(node)
          #update its preceding node
          node.prev = current_node
          #stop BFS if the visited node is the end node 
          if node == self.end:
            queue.clear()
            break
    #BFS completed, now trareturn self.trace_route()ce the route    
    return self.trace_route()

  #Function to trace the route using preceding nodes
  def trace_route(self):
    node = self.end
    route = []
    #start node has no preceding node
    #so loop until node->prev is null 
   
    while node:
      print("node:" , node)
      route.append(str(node))
      temp = node
      node = node.prev
      temp.prev = None
    #reverse the route bring start to the front
    route.reverse()
    #output route
    return route




# l = [ [0]*8 for i in range(8)]

# for row in range(8):
#     # print(row)
#     for col in range(8):
#         # print(row)
#         # print(col)
#         l[row][col] = (Node('n' + str(row) + str(col)))



# for row in range(8):
#     for col in range(8):

#         if row == 0:
#             if col == 0:
#                 l[row][col].add_neighbor(l[row + 1][col])
#                 l[row][col].add_neighbor(l[row][col + 1])
#             elif col == 7:
#                 l[row][col].add_neighbor(l[row + 1][col])
#                 l[row][col].add_neighbor(l[row][col - 1])
#             else:
#                 l[row][col].add_neighbor(l[row + 1][col])
#                 l[row][col].add_neighbor(l[row][col - 1])
#                 l[row][col].add_neighbor(l[row][col + 1])
        
#         elif row == 7:
#             if col == 0:
#                 l[row][col].add_neighbor(l[row - 1][col])
#                 l[row][col].add_neighbor(l[row][col + 1])
#             elif col == 7:
#                 l[row][col].add_neighbor(l[row - 1][col])
#                 l[row][col].add_neighbor(l[row][col - 1])
#             else:
#                 l[row][col].add_neighbor(l[row - 1][col])
#                 l[row][col].add_neighbor(l[row][col - 1])
#                 l[row][col].add_neighbor(l[row][col + 1])

       


#         else:
#             if col == 0:
#                 l[row][col].add_neighbor(l[row - 1][col])
#                 l[row][col].add_neighbor(l[row + 1][col])
#                 l[row][col].add_neighbor(l[row][col + 1])
#             elif col == 7:
#                 l[row][col].add_neighbor(l[row - 1][col])
#                 l[row][col].add_neighbor(l[row + 1][col])
#                 l[row][col].add_neighbor(l[row][col - 1])

#             else:
#                 l[row][col].add_neighbor(l[row - 1][col])
#                 l[row][col].add_neighbor(l[row + 1][col])
#                 l[row][col].add_neighbor(l[row][col - 1])
#                 l[row][col].add_neighbor(l[row][col + 1])




# print(ShortestPath(l[0][1], l[7][4]).bfs())
