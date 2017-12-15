import os

def main():
  x = 0
  y = 0
  z = 0
  distances = []
  ws = os.path.dirname(__file__)
  with open(os.path.join(ws, "day11.txt"), 'r') as f:
    dirs = f.read().split(',')
    for dir_ in dirs:
      if dir_ == 'n':
        x += 1
        z -= 1
      elif dir_ == 's':
        x -=1
        z += 1
      elif dir_ == 'ne':
        x += 1
        y -= 1
      elif dir_ == 'sw':
        x -= 1
        y += 1
      elif dir_ == 'nw':
        y += 1
        z -= 1
      elif dir_ == 'se':
        y -= 1
        z += 1
      distances.append(distance(x,y,z))
  print(max(distances))
  print(distance(x,y,z))

def distance(x, y, z):
  return (abs(x) + abs(y) + abs(z)) // 2

if __name__ == '__main__':
  main()