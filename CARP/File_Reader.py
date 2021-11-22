
INF = 0x3f3f3f3f

class File_Reader:
    def __init__(self, File_Name):
        self.File_Name = File_Name
        self.Vertices_Number = 0
        self.Depot = 0
        self.Tasks_Number = 0
        self.Non_Tasks_Number = 0
        self.Vehicles_Number = 0
        self.Capacity = 0
        self.Total_Cost = 0
        self.Name = None
        self.distance = None
        self.ori_distance = None
        self.demand = None
        self.Demand_List = []
    def Read_FIle(self):
        with open(self.File_Name) as read:
            i = 0
            for line in read.readlines():
                line = line.strip()
                input = line.split(' : ')
                if i == 9:
                    if line == 'END':
                        break
                    a, b, c, d = map(int, line.split())
                    self.distance[a][b] = c
                    self.distance[b][a] = c
                    self.demand[a][b] = d
                    self.demand[b][a] = d
                    self.ori_distance[a][b] = c
                    self.ori_distance[b][a] = c
                    if d > 0:
                        self.Demand_List.append((a,b))
                        self.Demand_List.append((b,a))
                    continue
                if input[0] == 'NAME':
                    self.Name = input[1]
                    i += 1
                    continue
                if input[0] == 'VERTICES':
                    self.Vertices_Number = int(input[1])
                    i += 1
                    continue
                if input[0] == 'DEPOT':
                    self.Depot = int(input[1])
                    i += 1
                    continue
                if input[0] == 'REQUIRED EDGES':
                    self.Tasks_Number = int(input[1])
                    i += 1
                    continue
                if input[0] == 'NON-REQUIRED EDGES':
                    self.Non_Tasks_Number = int(input[1])
                    i += 1
                    continue
                if input[0] == 'VEHICLES':
                    self.Vehicles_Number = int(input[1])
                    self.distance = [[INF for i in range(self.Vertices_Number + 1)] for i in range(self.Vertices_Number + 1)]
                    self.demand = [[0 for i in range(self.Vertices_Number + 1)] for i in range(self.Vertices_Number + 1)]
                    self.ori_distance = [[INF for i in range(self.Vertices_Number + 1)] for i in range(self.Vertices_Number + 1)]
                    i += 1
                    continue
                if input[0] == 'CAPACITY':
                    self.Capacity = int(input[1])
                    i += 1
                    continue
                if input[0] == 'TOTAL COST OF REQUIRED EDGES':
                    self.Total_Cost = int(input[1])
                    i += 1
                    continue
                if input[0] == 'NODES       COST         DEMAND':
                    i +=1
                    continue
            self.floyd()
    def floyd(self):
        for i in range(1,self.Vertices_Number+1):
            self.distance[i][i] = 0
        for k in range(1,self.Vertices_Number+1):
            for i in range(1,self.Vertices_Number + 1):
                for j in range(1,self.Vertices_Number + 1):
                    if self.distance[i][j] > self.distance[i][k] + self.distance[k][j]:
                        self.distance[i][j] = self.distance[i][k] + self.distance[k][j]


