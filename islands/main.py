#!/usr/bin/env python
# Imagine a 2D array of non-negative integers representing a map.
# 0 values are water and non-0 values are land. The land forms
# islands (contiguous cells vertically or horizontally).
# The value of an island is the sum of all of its tiles.
# Efficiently output the size of the highest-valued island.


def dfs(i, j, graph):
  value, visited = graph[i][j]
  #print "Visiting: " + str(i) + " " + str(j)
  #print str(graph[i][j])
  if visited:
    return 0
  graph[i][j] = (value, True)
  if value == 0:
    return 0
  count = value
  if i - 1 >= 0:
    count += dfs(i-1, j, graph)
  if j - 1 >= 0:
    count += dfs(i, j-1, graph)
  if i + 1 < len(graph):
    count += dfs(i+1, j, graph)
  if j + 1 < len(graph[j]):
    count += dfs(i, j+1, graph)
  return count

def dfs_non_recursive(graph, start):
  stack = [start]
  values = []
  while stack:
    i,j = stack.pop()
    value, visited = graph[i][j]
    if visited:
      continue
    values.append(value)
    graph[i][j] = (value, True)
    if i - 1 >= 0:
      v,_ = graph[i-1][j]
      if v != 0:
        stack.append((i-1, j))
    if j - 1 >= 0:
      v,_ = graph[i][j-1]
      if v != 0:
        stack.append((i, j-1))
    if i + 1 < len(graph):
      v,_ = graph[i+1][j]
      if v != 0:
        stack.append((i+1, j))
    if j + 1 < len(graph[j]):
      v,_ = graph[i][j+1]
      if v != 0:
        stack.append((i, j+1))
  return sum(values)

def find_the_largest_non_recursive(arr):
  carr = []
  for l in range(0, len(arr)):
    carr.append(list())
    for item in arr[l]:
      carr[l].append((item, False))
  print "Input"
  for item in arr:
    print str(item)

  print ""

  output = []
  for i in range(0, len(carr)):
    for j in range(0, len(carr[i])):
      value, visited = carr[i][j]
      if value == 0:
        carr[i][j] = (value, True)
        continue
      if not visited:
        land_value = dfs_non_recursive(carr, (i, j))
        output.append(land_value)
        print "DFS non recursive start: " + str(i) + " " + str(j) + " land value: " + str(land_value)
        print "Display current status of the board"
        for item in carr:
          print str(item)
        print ""
  print "The highest value of the land: " + str(max(output))

def find_the_largest(arr):
  carr = []
  for l in range(0, len(arr)):
    carr.append(list())
    for item in arr[l]:
      carr[l].append((item, False))
  print "Input"
  for item in arr:
    print str(item)

  print ""

  output = []
  for i in range(0, len(carr)):
    for j in range(0, len(carr[i])):
      value, visited = carr[i][j]
      if value == 0:
        carr[i][j] = (value, True)
        continue
      if not visited:
        count = 0
        land_value = dfs(i,j,carr)
        output.append(land_value)
        print "DFS start: " + str(i) + " " + str(j) + " land value: " + str(land_value)
        print "Display current status of the board"
        for item in carr:
          print str(item)
        print ""
  print "The highest value of the land: " + str(max(output))


def main():
  arr = [None] * 5
  arr[0] = [0,2,1,0,0]
  arr[1] = [1,1,1,0,0]
  arr[2] = [0,0,0,1,1]
  arr[3] = [1,1,0,0,1]
  arr[4] = [2,3,0,0,1]

  find_the_largest(arr)
  find_the_largest_non_recursive(arr)

if __name__ == "__main__":
    main()
