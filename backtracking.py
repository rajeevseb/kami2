

import collections

adjacencyMap = { 

'v1' : ['v2' , 'v12' , 'v13']  , 

'v2' : ['v1' , 'v3' , 'v13' ,'v15'] , 

'v3' : ['v2' , 'v4' , 'v15'] , 

'v4' : ['v3' , 'v5' , 'v6' , 'v15' , 'v9', 'v7'] , 

'v5' : ['v4'] , 

'v6' : ['v4'] , 

'v7' : ['v4' , 'v8' , 'v9'] ,

'v8' : ['v7' , 'v11' , 'v9'] ,

'v9' : ['v7'  , 'v11' ,'v4' , 'v8' , 'v15'] ,

'v10' : ['v11' ] ,

'v11' : ['v12' ,  'v13' , 'v15' , 'v10' , 'v8' , 'v9' ] ,

'v12' : ['v1' , 'v13' , 'v11'] ,

'v13' : ['v1' , 'v2' , 'v15','v14' , 'v11' , 'v12'] ,

'v14' : ['v13'] ,

'v15' : ['v2' , 'v3' , 'v4','v17' , 'v16' , 'v13' , 'v11' ,'v9' ] ,

'v16' : ['v15'] ,

'v17' : ['v15'] ,


}




vertexColor = {
'v1' : 'R' , 
'v2' :  'B' ,
'v3' :  'O' , 
'v4' :  'B', 
'v5' :  'R' ,
'v6' :  'O' ,
'v7' :  'R' ,
'v8' :  'B', 
'v9' :  'C', 
'v10' :  'B',
'v11' :  'O' ,
'v12' :  'B' ,
'v13' :  'C',
'v14' :  'R',
'v15' :  'R' ,
'v16' :  'O',
'v17' :  'O' }

candidateColors = ['R', 'O', 'C', 'B']

answer =[]

i = 4

def changeColor(vertex, color,vertexColor,adjacencyMap) :

  #print("Original %s" %(''.join(vertexColor.values())))

  #print("Changing vertex %s color to %s" %(vertex,color))   

  previousColor = vertexColor[vertex]

  vertexColor[vertex] = color;

  adjacentVertices = adjacencyMap[vertex];

  for v in adjacentVertices :

     if(vertexColor[v] == previousColor):

      vertexColor[v] = color
      adjacencyMap[vertex] = list(set(adjacencyMap[vertex]).union(set(adjacencyMap[v])))
  #print("Changed %s"%(''.join(vertexColor.values())))

 

def isGoal(vertexColor) :

  vertcolors = ''.join(vertexColor.values())

  length = collections.Counter(vertcolors).most_common()[0][1]

  if len(vertcolors) == length :

    return True

  else :

    return False




  

def solve(vertexColor, numberOfMoves, vertex, color,adjacencyMap):

    if(numberOfMoves == 0) :

      if(isGoal(vertexColor)) :

        #print("Vertex: %s Color :%s" % (vertex, color))

        return True

      else :

        return False

    else :

      for v in vertexColor :

        for c in candidateColors :

          currentvertexcolor = vertexColor.copy()
          currentadjancencyMap = adjacencyMap.copy()

          #print "move Number %s"%(numberOfMoves)

          changeColor(v, c,currentvertexcolor,currentadjancencyMap)

          if(solve(currentvertexcolor.copy(), numberOfMoves - 1, v, c,currentadjancencyMap.copy()) == True):

            answer.append(' vertex: ' + v + ' color: ' + c )

            #print("moveNumber %s Vertex: %s Color :%s" % (numberOfMoves,v, c))

            return True

      return False




numberOfMoves = 4




if(solve(vertexColor.copy(), numberOfMoves, 'v7', 'B',adjacencyMap.copy()) == False):

    print "NO solution found"

else :

    answer.reverse()

    print answer    

    

    




 
