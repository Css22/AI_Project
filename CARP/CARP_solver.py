
import time
import sys
import random
from File_Reader import File_Reader
INF = 0x3f3f3f3f



def Filp(File_Reader , Result,all_cost,sharking):
    index = random.randint(0, len(Result) - 1)
    EndPoint = File_Reader.Depot
    new_cost = all_cost
    test = all_cost
    test2 = Result[index].copy()
    do = False
    for i in range(0, len(Result[index])):
        if i != len(Result[index]) - 1:
            new_cost = all_cost + File_Reader.distance[EndPoint][Result[index][i][1]] + \
                       File_Reader.distance[Result[index][i][0]][Result[index][i + 1][0]] - \
                       File_Reader.distance[EndPoint][Result[index][i][0]] - \
                       File_Reader.distance[Result[index][i][1]][Result[index][i + 1][0]]
        else:
            new_cost = all_cost + File_Reader.distance[EndPoint][Result[index][i][1]] + \
                       File_Reader.distance[Result[index][i][0]][File_Reader.Depot] - \
                       File_Reader.distance[EndPoint][Result[index][i][0]] - \
                       File_Reader.distance[Result[index][i][1]][File_Reader.Depot]
        if new_cost < all_cost or sharking:
            do = True
            a = Result[index]
            Result[index][i] = (Result[index][i][1],Result[index][i][0])
            all_cost = new_cost
        EndPoint = Result[index][i][1]
    if do:
        return all_cost
    else:
        return test
# 在选取插入的问题上存在问题
def Single_insertion(File_Reader,Result,Q_array):
    while True :
        index1 = random.randint(0, len(Result) - 1)
        while len(Result[index1]) <= 1 :
            index1 = random.randint(0, len(Result) - 1)
        index2 = random.randint(0, len(Result[index1]) - 1)
        index3 = random.randint(0, len(Result) - 1)
        index4 = random.randint(0, len(Result[index3]))

        # 对随机结果为同一序列的处理,相等于进行swap的过程
        if index1 == index3:
            index2 = random.randint(0, len(Result[index1]) - 1)
            index4 = random.randint(0, len(Result[index3]) - 1)
            while index2 == index4:
                index2 = random.randint(0, len(Result[index1]) - 1)
                index4 = random.randint(0, len(Result[index3]) - 1)
            change = 0
            if index2 - index4 == 1 or index4 - index2 == 1:
                if index2 > index4:
                    a = index4
                    index4 = index2
                    index2 = a
                if index2 == 0 and index4 == len(Result[index3]) -1:
                    change = change - (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                                         File_Reader.distance[Result[index1][index2][1]][Result[index3][index4][0]] + File_Reader.distance[Result[index3][index4][1]][File_Reader.Depot]) \
                              + (File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]] +
                                 File_Reader.distance[Result[index3][index4][1]][Result[index1][index2 ][0]] +
                                 File_Reader.distance[Result[index1][index2][1]][File_Reader.Depot])

                if index2 == 0 and index4 != len(Result[index3]) -1:
                    change = change - (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                                       File_Reader.distance[Result[index1][index2][1]][Result[index3][index4][0]] +
                                       File_Reader.distance[Result[index3][index4][1]][Result[index3][index4+1][0]]) \
                             + (File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]] +
                                File_Reader.distance[Result[index3][index4][1]][Result[index1][index2][0]] +
                                File_Reader.distance[Result[index1][index2][1]][Result[index3][index4 + 1][0]])

                if index2 != 0 and index4 == len(Result[index3]) -1:
                    change = change - (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                                       File_Reader.distance[Result[index1][index2][1]][Result[index3][index4][0]] +
                                       File_Reader.distance[Result[index3][index4][1]][File_Reader.Depot]) \
                             + (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index3][index4][0]] +
                                File_Reader.distance[Result[index3][index4][1]][Result[index1][index2][0]] +
                                File_Reader.distance[Result[index1][index2][1]][File_Reader.Depot])
                if index2 != 0 and index4 != len(Result[index3]) -1:
                    change = change - (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                                       File_Reader.distance[Result[index1][index2][1]][Result[index3][index4][0]] +
                                       File_Reader.distance[Result[index3][index4][1]][Result[index3][index4 + 1][0]]) \
                             + (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index3][index4][0]] +
                                File_Reader.distance[Result[index3][index4][1]][Result[index1][index2][0]] +
                                File_Reader.distance[Result[index1][index2][1]][Result[index3][index4 + 1][0]])

                new_cost = change
                if new_cost < 0:
                    a = Result[index1][index2]
                    Result[index1][index2] = Result[index3][index4]
                    Result[index3][index4] = a
                    return new_cost
            else:
                change1 = 0
                change2 = 0
                if index2 == 0:
                    change1 = change1 - (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                                         File_Reader.distance[Result[index1][index2][1]][Result[index1][index2 + 1][0]]) \
                              + (File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]] +
                                 File_Reader.distance[Result[index3][index4][1]][Result[index1][index2 + 1][0]])
                elif index2 == len(Result[index1]) - 1:
                    change1 = change1 - (
                                File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                                File_Reader.distance[Result[index1][index2][1]][File_Reader.Depot]) \
                              + (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index3][index4][0]] +
                                 File_Reader.distance[Result[index3][index4][1]][File_Reader.Depot])
                elif index2 != 0 and index2 != len(Result[index1]) - 1:
                    change1 = change1 - (
                                File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                                File_Reader.distance[Result[index1][index2][1]][Result[index1][index2 + 1][0]]) \
                              + (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index3][index4][0]] +
                                 File_Reader.distance[Result[index3][index4][1]][Result[index1][index2 + 1][0]])

                if index4 == 0:
                    change1 = change1 - (File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]] +
                                         File_Reader.distance[Result[index3][index4][1]][Result[index3][index4 + 1][0]]) \
                              + (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                                 File_Reader.distance[Result[index1][index2][1]][Result[index3][index4 + 1][0]])
                elif index4 == len(Result[index3]) - 1:
                    change1 = change1 - (
                                File_Reader.distance[Result[index3][index4 - 1][1]][Result[index3][index4][0]] +
                                File_Reader.distance[Result[index3][index4][1]][File_Reader.Depot]) \
                              + (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                                 File_Reader.distance[Result[index1][index2][1]][File_Reader.Depot])
                elif index4 != 0 and index4 != len(Result[index3]) - 1:
                    change1 = change1 - (
                                File_Reader.distance[Result[index3][index4 - 1][1]][Result[index3][index4][0]] +
                                File_Reader.distance[Result[index3][index4][1]][Result[index3][index4 + 1][0]]) \
                              + (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                                 File_Reader.distance[Result[index1][index2][1]][Result[index3][index4 + 1][0]])

                new_cost = change2 + change1
                if new_cost < 0:
                    a = Result[index1][index2]
                    Result[index1][index2] = Result[index3][index4]
                    Result[index3][index4] = a
                    return new_cost

        else:
            change1 = 0
            change2 = 0
            if index2 == 0 and index2 != len(Result[index1]) - 1:
                change1 = change1 - (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                                     File_Reader.distance[Result[index1][index2][1]][Result[index1][index2 + 1][0]]) + (
                          File_Reader.distance[File_Reader.Depot][Result[index1][index2 + 1][0]])
            elif index2 == len(Result[index1]) - 1 and index2 != 0:
                change1 = change1 - (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                                     File_Reader.distance[Result[index1][index2][1]][File_Reader.Depot]) + (
                          File_Reader.distance[Result[index1][index2 - 1][1]][File_Reader.Depot])
            elif index2 != 0 and index2 != len(Result[index1]) - 1:
                change1 = change1 - (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                                     File_Reader.distance[Result[index1][index2][1]][Result[index1][index2 + 1][0]]) + (
                          File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2 + 1][0]])


            if index4 == 0:
                change2 = change2 + (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                                     File_Reader.distance[Result[index1][index2][1]][Result[index3][index4][0]]) - (
                          File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]])
            elif index4 == len(Result[index3]):
                change2 = change2 + (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                                     File_Reader.distance[Result[index1][index2][1]][File_Reader.Depot]) - (
                          File_Reader.distance[Result[index3][index4 - 1][1]][File_Reader.Depot])
            else:
                change2 = change2 + (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                                     File_Reader.distance[Result[index1][index2][1]][Result[index3][index4][0]]) - (
                          File_Reader.distance[Result[index3][index4 - 1][1]][Result[index3][index4][0]])

            new_cost = change2 + change1
            if new_cost < 0:
                Result[index3].insert(index4, Result[index1][index2])
                Result[index1].remove(Result[index1][index2])
                return new_cost
def Double_insertion(File_Reader,Result ,max_length,Q_array,sharking):
    n = random.randint(1, max_length)
    index1 = random.randint(0, len(Result) - 1)
    while len(Result[index1]) <= n:
        index1 = random.randint(0, len(Result) - 1)
    index2 = random.randint(0, len(Result[index1]) - 1 - (n - 1))
    index3 = random.randint(0, len(Result) - 1)
    index4 = random.randint(0, len(Result[index3]))

    if index1 == index3:
        index4 = random.randint(0, len(Result[index3]) - 1)
        while index2 == index4 or (index2 < index4 and index2 + n - 1 >= index4) or index2 + n == index4:
            index2 = random.randint(0, len(Result[index1]) - 1 - (n - 1))
            index4 = random.randint(0, len(Result[index3]) - 1)

        if index2 - index4 == 1:
            change = 0
            if index4 == 0 and index2 + n - 1 == len(Result[index3]) - 1:
                change = change - (File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]] +
                                   File_Reader.distance[Result[index3][index4][1]][Result[index1][index2][0]] +
                                   File_Reader.distance[Result[index1][index2 + n - 1][1]][File_Reader.Depot]) \
                         + (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                            File_Reader.distance[Result[index1][index2 + n - 1][1]][Result[index3][index4][0]] +
                            File_Reader.distance[Result[index3][index4][1]][File_Reader.Depot])

            if index4 == 0 and index2 + n - 1 != len(Result[index3]) - 1:
                change = change - (File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]] +
                                   File_Reader.distance[Result[index3][index4][1]][Result[index1][index2][0]] +
                                   File_Reader.distance[Result[index1][index2 + n - 1][1]][
                                       Result[index1][index2 + n - 1 + 1][0]]) \
                         + (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                            File_Reader.distance[Result[index1][index2 + n - 1][1]][Result[index3][index4][0]] +
                            File_Reader.distance[Result[index3][index4][1]][Result[index1][index2 + n - 1 + 1][0]])

            if index4 != 0 and index2 + n - 1 == len(Result[index3]) - 1:
                change = change - (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index3][index4][0]] +
                                   File_Reader.distance[Result[index3][index4][1]][Result[index1][index2][0]] +
                                   File_Reader.distance[Result[index1][index2 + n - 1][1]][File_Reader.Depot]) \
                         + (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                            File_Reader.distance[Result[index1][index2 + n - 1][1]][Result[index3][index4][0]] +
                            File_Reader.distance[Result[index3][index4][1]][File_Reader.Depot])
            if index4 != 0 and index2 + n - 1 != len(Result[index3]) - 1:
                change = change - (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index3][index4][0]] +
                                   File_Reader.distance[Result[index3][index4][1]][Result[index1][index2][0]] +
                                   File_Reader.distance[Result[index1][index2 + n - 1][1]][
                                       Result[index1][index2 + n - 1 + 1][0]]) \
                         + (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                            File_Reader.distance[Result[index1][index2 + n - 1][1]][Result[index3][index4][0]] +
                            File_Reader.distance[Result[index3][index4][1]][Result[index1][index2 + n - 1 + 1][0]])

            new_cost = change
            if new_cost < 0 or sharking :
                a = Result[index1][index2: index2 + n]
                for i in range(0, n):
                    Result[index1].remove(a[i])
                for i in range(0, n):
                    if index2 > index4:
                        Result[index1].insert(index4 + i, a[i])
                    else:
                        Result[index1].insert(index4 + i - n, a[i])
                return new_cost
            else:
                return 0
        else:
            change1 = 0
            change2 = 0
            if index2 == 0 and index2 + n - 1 != len(Result[index1]) - 1:
                change1 = change1 - (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                                     File_Reader.distance[Result[index1][index2 + n - 1][1]][
                                         Result[index1][index2 + n - 1 + 1][0]]) + (
                              File_Reader.distance[File_Reader.Depot][Result[index1][index2 + n - 1 + 1][0]])
            elif index2 + n - 1 == len(Result[index1]) - 1 and index2 != 0:
                change1 = change1 - (
                        File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                        File_Reader.distance[Result[index1][index2 + n - 1][1]][File_Reader.Depot]) + (
                              File_Reader.distance[Result[index1][index2 - 1][1]][File_Reader.Depot])
            elif index2 != 0 and index2 + n - 1 != len(Result[index1]) - 1:
                change1 = change1 - (
                        File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                        File_Reader.distance[Result[index1][index2 + n - 1][1]][
                            Result[index1][index2 + n - 1 + 1][0]]) + (
                              File_Reader.distance[Result[index1][index2 - 1][1]][
                                  Result[index1][index2 + n - 1 + 1][0]])

            if index4 == 0:
                change2 = change2 + (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                                     File_Reader.distance[Result[index1][index2 + n - 1][1]][
                                         Result[index3][index4][0]]) - (
                              File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]])
            elif index4 == len(Result[index3]):
                change2 = change2 + (
                        File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                        File_Reader.distance[Result[index1][index2 + n - 1][1]][File_Reader.Depot]) - (
                              File_Reader.distance[Result[index3][index4 - 1][1]][File_Reader.Depot])
            else:
                change2 = change2 + (
                        File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                        File_Reader.distance[Result[index1][index2 + n - 1][1]][Result[index3][index4][0]]) - (
                              File_Reader.distance[Result[index3][index4 - 1][1]][Result[index3][index4][0]])

            new_cost = change2 + change1
            if new_cost < 0 or sharking:
                a = Result[index1][index2: index2 + n]
                for i in range(0, n):
                    Result[index1].remove(a[i])
                for i in range(0, n):
                    if index2 > index4:
                        Result[index1].insert(index4 + i, a[i])
                    else:
                        Result[index1].insert(index4 + i - n, a[i])
                return new_cost
            else:
                return 0
    else:
        Add_load = 0
        for i in range(0, n):
            Add_load = Add_load + File_Reader.demand[Result[index1][index2 + i][0]][
                Result[index1][index2 + i][1]]
        if Q_array[index3] + Add_load > File_Reader.Capacity:
            return 0
        change1 = 0
        change2 = 0
        if index2 == 0 and index2 + n - 1 != len(Result[index1]) - 1:
            change1 = change1 - (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                                 File_Reader.distance[Result[index1][index2 + n - 1][1]][
                                     Result[index1][index2 + n - 1 + 1][0]]) + (
                          File_Reader.distance[File_Reader.Depot][Result[index1][index2 + n - 1 + 1][0]])
        elif index2 + n - 1 == len(Result[index1]) - 1 and index2 != 0:
            change1 = change1 - (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                                 File_Reader.distance[Result[index1][index2 + n - 1][1]][File_Reader.Depot]) + (
                          File_Reader.distance[Result[index1][index2 - 1][1]][File_Reader.Depot])
        elif index2 != 0 and index2 + n - 1 != len(Result[index1]) - 1:
            change1 = change1 - (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                                 File_Reader.distance[Result[index1][index2 + n - 1][1]][
                                     Result[index1][index2 + n - 1 + 1][0]]) + (
                          File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2 + n - 1 + 1][0]])

        if index4 == 0:
            change2 = change2 + (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                                 File_Reader.distance[Result[index1][index2 + n - 1][1]][Result[index3][index4][0]]) - (
                          File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]])
        elif index4 == len(Result[index3]):
            change2 = change2 + (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                                 File_Reader.distance[Result[index1][index2 + n - 1][1]][File_Reader.Depot]) - (
                          File_Reader.distance[Result[index3][index4 - 1][1]][File_Reader.Depot])
        else:
            change2 = change2 + (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                                 File_Reader.distance[Result[index1][index2 + n - 1][1]][Result[index3][index4][0]]) - (
                          File_Reader.distance[Result[index3][index4 - 1][1]][Result[index3][index4][0]])

        new_cost = change2 + change1
        if new_cost < 0 or sharking:
            for i in range(0, n):
                Result[index3].insert(index4 + i, Result[index1][index2 + i])
            a = Result[index1][index2: index2 + n]
            for i in a:
                Result[index1].remove(i)
            Q_array[index3] += Add_load
            Q_array[index1] -= Add_load
            return new_cost
        else:
            return 0

def Swap(File_Reader,Result,Q_array,sharking):
    index1 = random.randint(0, len(Result) - 1)
    index2 = random.randint(0, len(Result[index1]) - 1)
    index3 = random.randint(0, len(Result) - 1)
    while index3 == index1:
        index3 = random.randint(0, len(Result) - 1)
    index4 = random.randint(0, len(Result[index3]) - 1)
    if (Q_array[index1] - File_Reader.demand[Result[index1][index2][0]][Result[index1][index2][1]] \
                          + File_Reader.demand[Result[index3][index4][0]][Result[index3][index4][1]] > File_Reader.Capacity) \
        or (Q_array[index3] + File_Reader.demand[Result[index1][index2][0]][Result[index1][index2][1]] \
                          - File_Reader.demand[Result[index3][index4][0]][Result[index3][index4][1]] > File_Reader.Capacity):
        return 0
    change1 = 0
    change2 = 0
    if index2 == 0 and index2 != len(Result[index1]) - 1:
        change1 = change1 - (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                             File_Reader.distance[Result[index1][index2][1]][Result[index1][index2 + 1][0]]) \
                  + (File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]] +
                     File_Reader.distance[Result[index3][index4][1]][Result[index1][index2 + 1][0]])
    elif index2 == 0 and index2 == len(Result[index1]) - 1:
        change1 = change1 - (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                             File_Reader.distance[Result[index1][index2][1]][File_Reader.Depot]) \
                  + (File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]] +
                     File_Reader.distance[Result[index3][index4][1]][File_Reader.Depot])
    elif index2 != 0 and index2 == len(Result[index1]) - 1:
        change1 = change1 - (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                             File_Reader.distance[Result[index1][index2][1]][File_Reader.Depot]) \
                  + (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index3][index4][0]] +
                     File_Reader.distance[Result[index3][index4][1]][File_Reader.Depot])
    elif index2 != 0 and index2 != len(Result[index1]) - 1:
        change1 = change1 - (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                             File_Reader.distance[Result[index1][index2][1]][Result[index1][index2 + 1][0]]) \
                  + (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index3][index4][0]] +
                     File_Reader.distance[Result[index3][index4][1]][Result[index1][index2 + 1][0]])

    if index4 == 0 and index4 != len(Result[index3]) - 1:
        change2 = change2 - (File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]] +
                             File_Reader.distance[Result[index3][index4][1]][Result[index3][index4 + 1][0]]) \
                  + (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                     File_Reader.distance[Result[index1][index2][1]][Result[index3][index4 + 1][0]])
    elif index4 == 0 and index4 == len(Result[index3]) - 1:
        change2 = change2 - (File_Reader.distance[File_Reader.Depot][Result[index3][index4][0]] +
                             File_Reader.distance[Result[index3][index4][1]][File_Reader.Depot]) \
                  + (File_Reader.distance[File_Reader.Depot][Result[index1][index2][0]] +
                     File_Reader.distance[Result[index1][index2][1]][File_Reader.Depot])
    elif index4 != 0 and index4 != len(Result[index3]) - 1:
        change2 = change2 - (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index3][index4][0]] +
                             File_Reader.distance[Result[index3][index4][1]][Result[index3][index4 + 1][0]]) \
                  + (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                     File_Reader.distance[Result[index1][index2][1]][Result[index3][index4 + 1][0]])
    elif index4 != 0 and index4 == len(Result[index3]) - 1:
        change2 = change2 - (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index3][index4][0]] +
                             File_Reader.distance[Result[index3][index4][1]][File_Reader.Depot]) \
                  + (File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]] +
                     File_Reader.distance[Result[index1][index2][1]][File_Reader.Depot])

    new_cost = change2 + change1
    if new_cost < 0 or sharking:
        Q_array[index1] = Q_array[index1] - File_Reader.demand[Result[index1][index2][0]][Result[index1][index2][1]] \
                          + File_Reader.demand[Result[index3][index4][0]][Result[index3][index4][1]]
        Q_array[index3] = Q_array[index3] + File_Reader.demand[Result[index1][index2][0]][Result[index1][index2][1]] \
                          - File_Reader.demand[Result[index3][index4][0]][Result[index3][index4][1]]
        a = Result[index1][index2]
        Result[index1][index2] = Result[index3][index4]
        Result[index3][index4] = a
        return new_cost
    else:
        return 0
def two_opt_single(File_Reader,Result,all_cost,sharking):
    index = random.randint(0, len(Result) - 1)
    while len(Result[index]) == 1:
        index = random.randint(0, len(Result) - 1)
    max = len(Result[index])
    n = random.randint(1,max-1)
    i = random.randint(0,len(Result[index]) - 1 - (n - 1))
    new_cost = 0
    if i + n - 1 == len(Result[index]) - 1:
        new_cost = all_cost - (File_Reader.distance[Result[index][i - 1][1]][Result[index][i][0]] +
                               File_Reader.distance[Result[index][i + n - 1][1]][File_Reader.Depot]) \
                   + (File_Reader.distance[Result[index][i - 1][1]][Result[index][i + n - 1][1]]+
                      File_Reader.distance[Result[index][i][0]][File_Reader.Depot])
    elif i == 0:
        new_cost = all_cost - (File_Reader.distance[File_Reader.Depot][Result[index][i][0]] +
                               File_Reader.distance[Result[index][i + n - 1][1]][Result[index][i+n-1+1][0]]) \
                   + (File_Reader.distance[File_Reader.Depot][Result[index][i + n - 1][1]] +
                      File_Reader.distance[Result[index][i][0]][Result[index][i+n-1+1][0]])
    else:
        new_cost = all_cost - (File_Reader.distance[Result[index][i - 1][1]][Result[index][i][0]] +
                               File_Reader.distance[Result[index][i + n - 1][1]][Result[index][i + n - 1 + 1][0]]) \
                   + (File_Reader.distance[Result[index][i - 1][1]][Result[index][i + n - 1][1]] +
                      File_Reader.distance[Result[index][i][0]][Result[index][i + n - 1 + 1][0]])
    if new_cost < all_cost or sharking:
        a = Result[index][i : i+n]
        for k in range(0,n):
            a[k] = (a[k][1],a[k][0])
        a = list(reversed(a))
        for k in range(0,n):
            Result[index][k+i] = (a[k][0],a[k][1])
        return  new_cost
    else:
        return all_cost
def two_opt_double(File_Reader,Result,Q_array):
    index1 = random.randint(0,len(Result) - 1)
    while len(Result[index1]) <= 2:
        index1 = random.randint(0, len(Result) - 1)
    index2 = random.randint(1,len(Result[index1]) - 1)
    index3 = random.randint(0,len(Result) -1 )
    while index3 == index1 or len(Result[index3]) <= 2:
        if len(Result) == 2:
            return 0
        index3 = random.randint(0,len(Result) - 1)
    index4 = random.randint(1,len(Result[index3]) - 1)

    path1 = Result[index1][0:index2]
    path2 = Result[index1][index2:len(Result[index1])]
    path3 = Result[index3][0:index4]
    path4 = Result[index3][index4:len(Result[index3])]

    load1 = 0
    load2 = 0
    load3 = 0
    load4 = 0
    if index2 < len(Result[index1])/2:
        for i in range(0,index2):
            load1 = load1 + File_Reader.demand[Result[index1][i][0]][Result[index1][i][1]]
        load2 = Q_array[index1] - load1
    else:
        for i in range(index2, len(Result[index1])):
            load2 = load2 + File_Reader.demand[Result[index1][i][0]][Result[index1][i][1]]
        load1 = Q_array[index1] - load2

    if index4 < len(Result[index3])/2:
        for i in range(0,index4):
            load3 = load3 + File_Reader.demand[Result[index3][i][0]][Result[index3][i][1]]
        load4 = Q_array[index3] - load3
    else:
        for i in range(index4, len(Result[index3])):
            load4 = load4 + File_Reader.demand[Result[index3][i][0]][Result[index3][i][1]]
        load3 = Q_array[index3] - load4

    cost1 = 0
    cost2 = 0

    # 两种交换方法进行交换，同时求出最小的COST
    # path1 path3            path2 path4 该方法需要反转path3  path2 同时修改他们的顺序
    if(load1 + load3 <= File_Reader.Capacity and load2 + load4 <= File_Reader.Capacity):
        cost1 = - (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                   File_Reader.distance[Result[index3][index4 - 1][1]][Result[index3][index4][0]]) \
                + (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index3][index4 -1][1]] +
                   File_Reader.distance[Result[index1][index2][0]][Result[index3][index4][0]])
    # path1 path4            path2 path3
    if (load1 + load4 <= File_Reader.Capacity and load2 + load3 <= File_Reader.Capacity):
        cost2 = - (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index1][index2][0]] +
                   File_Reader.distance[Result[index3][index4 - 1][1]][Result[index3][index4][0]]) \
                + (File_Reader.distance[Result[index1][index2 - 1][1]][Result[index3][index4][0]] +
                   File_Reader.distance[Result[index3][index4 - 1][1]][Result[index1][index2][0]])
    if cost2 < cost1 and cost2 < 0:
        for i in range(0,len(path4)):
            path1.append(path4[i])
        for i in range(0,len(path2)):
            path3.append(path2[i])
        Result[index1] = path1
        Result[index3] = path3
        Q_array[index1] = load1 + load4
        Q_array[index3] = load2 + load3
        return cost2
    elif cost1 < cost2 and cost1 < 0:
        for i in range(0,len(path3)):
            path3[i] = (path3[i][1],path3[i][0])
        path3 = list(reversed(path3))
        for i in range(0,len(path3)):
            path1.append(path3[i])
        for i in range(0, len(path2)):
            path2[i] = (path2[i][1], path2[i][0])
        path2 = list(reversed(path2))
        for i in range(0, len(path4)):
            path2.append(path4[i])
        Result[index1] = path1
        Result[index3] = path2
        Q_array[index1] = load1 + load3
        Q_array[index3] = load2 + load4
        return cost1
    else:
        return 0
def Path_Scanning(File_Reader):
    free = File_Reader.Demand_List
    Result = []
    all_cost = 0
    while len(free) != 0 :
        path = []
        cost = 0
        load = 0
        Q = File_Reader.Capacity
        EndPoint = File_Reader.Depot
        EndPoint2 = EndPoint
        while True :
            min_distance = INF
            chosen = (EndPoint, EndPoint)
            for i in free:
                if File_Reader.demand[i[0]][i[1]] + load > Q:
                    continue
                if File_Reader.distance[EndPoint][i[0]] + File_Reader.ori_distance[i[0]][i[1]] < min_distance:
                    min_distance = File_Reader.distance[EndPoint][i[0]] + File_Reader.ori_distance[i[0]][i[1]]
                    chosen = i
                    EndPoint2 = i[1]
                elif min_distance == File_Reader.distance[EndPoint][i[0]] + File_Reader.ori_distance[i[0]][i[1]]:
                    if load <= Q/2:
                        if File_Reader.distance[EndPoint][File_Reader.Depot] < File_Reader.distance[i[1]][File_Reader.Depot]:
                            chosen = i
                            EndPoint2 = i[1]
                    else:
                        if File_Reader.distance[EndPoint][File_Reader.Depot] > File_Reader.distance[i[1]][File_Reader.Depot]:
                            chosen = i
                            EndPoint2 = i[1]
            if min_distance == INF or len(free) == 0:
                break
            else:
                path.append(chosen)
                cost = cost + File_Reader.distance[EndPoint][chosen[0]] + File_Reader.ori_distance[chosen[0]][chosen[1]]
                EndPoint = EndPoint2
                free.remove((chosen[0],chosen[1]))
                free.remove((chosen[1],chosen[0]))
                load = load + File_Reader.demand[chosen[0]][chosen[1]]
        cost = cost + File_Reader.distance[EndPoint][File_Reader.Depot]
        all_cost = all_cost + cost
        Result.append(path)
    return all_cost,Result
def VNS(File_Reader , all_cost , Result , Q_array, numbers,length,s):
    i = 0
    # if length /File_Reader.Vehicles_Number > 22:
    #
    #     s = 2000
    # elif length /File_Reader.Vehicles_Number > 30:
    #     s = 500
    # else:
    #     s = 5000
    while i < numbers:
        out_cost = all_cost
        sharking = random.randint(0, 3)
        Result1 = []
        for l in Result:
            Result1.append(l.copy())
        Q_array1 = []
        for l in Q_array:
            Q_array1.append(l)
        if sharking == 0:
            change_cost = two_opt_single(File_Reader, Result1, all_cost , True)
            out_cost = change_cost
        if sharking == 1:
            max = 0
            for tt in range(0, len(Result1)):
                if max < len(Result1[tt]):
                    max = tt
            change_cost = Double_insertion(File_Reader, Result1, max, Q_array1,True)
            out_cost = out_cost + change_cost
        if sharking == 2:
            change_cost = Swap(File_Reader, Result1, Q_array1,True)
            out_cost = out_cost + change_cost
        if sharking == 3:
            change_cost = Filp(File_Reader, Result1, out_cost,True)
            out_cost = change_cost
        # 这里将执行sharking操作
        j = 0
        while j <= 4:
            # if j == sharking:
            #     j = j + 1
            #     continue
            Good = False
            t = 0
            if j==0:

                while t <= s:
                    change_cost = two_opt_double(File_Reader, Result1, Q_array1)
                    if change_cost < 0:
                        j = 0
                        Good = True
                        out_cost = out_cost + change_cost
                        t = 0
                    else:
                        t = t + 1
            if j==1:
                while t <= s:
                    change_cost = two_opt_single(File_Reader, Result1, out_cost,False)
                    if change_cost < out_cost:
                        j = 0
                        out_cost = change_cost
                        Good = True
                        break
                    else:
                        t = t + 1
            if j==2:
                while t <= s:
                    max = 0
                    for tt in range(0, len(Result)):
                        if max < len(Result[tt]):
                            max = tt
                    change_cost = Double_insertion(File_Reader, Result1,max, Q_array1,False)
                    if change_cost < 0:
                        j = 0
                        out_cost = out_cost + change_cost
                        Good = True
                        break
                    else:
                        t = t + 1
            if j==3:
                while t <= s:
                    change_cost = Swap(File_Reader, Result1, Q_array1,False)
                    if change_cost < 0:
                        j = 0
                        out_cost = out_cost + change_cost
                        Good = True
                        break
                    else:
                        t = t + 1
            if j==4:
                while t <= s:
                    change_cost = Filp(File_Reader, Result1, out_cost,False)
                    if change_cost < out_cost:
                        j = 0
                        out_cost = change_cost
                        Good = True
                        break
                    else:
                        t = t + 1
            if not Good :
                j = j+1
        if all_cost > out_cost:
            Result.clear()
            for l in Result1:
                Result.append(l.copy())
            Q_array.clear()
            for l in Q_array1:
                Q_array.append(l)
            all_cost = out_cost
        i = i + 1
    return all_cost
if __name__ == '__main__':
    start = time.time()
    filename = sys.argv[1]
    timelimit = int(sys.argv[3])
    seed = int(sys.argv[5])
    File_Reader = File_Reader(filename)
    File_Reader.Read_FIle()
    length = len(File_Reader.Demand_List)
    test = File_Reader.Demand_List.copy()
    Result = None
    cost , Result = Path_Scanning(File_Reader)
    max = 0
    Q_array = []
    for i in Result :
        load = 0
        for  k in i:
            load = load + File_Reader.demand[k[0]][k[1]]
        Q_array.append(load)
    for i in range(0,len(Result)):
        if max < len(Result[i]):
            max = i
    # test2 = test.copy()
    # cost2 = 0
    # cost4 = 0
    numbers = 2000
    if length/File_Reader.Vehicles_Number > 21:
        s = 1000
        numbers = 500
    elif length/File_Reader.Vehicles_Number < 10:
        s  = 200
        numbers = 4000
    else:
        s = 500
        numbers = 2000
    cost3 = VNS(File_Reader, cost, Result, Q_array, numbers, length , s)


    # for i in Result:
    #     last = File_Reader.Depot
    #     for j in i:
    #         cost2 = cost2 + File_Reader.distance[last][j[0]]
    #         cost2 = cost2 + File_Reader.ori_distance[j[0]][j[1]]
    #         last = j[1]
    #     cost2 = cost2 + File_Reader.distance[last][File_Reader.Depot]
    # for i in Result:
    #     load = 0
    #     for k in i:
    #         test2.remove((k[0], k[1]))
    #         test2.remove((k[1], k[0]))
    #         load = load + File_Reader.demand[k[0]][k[1]]
    #     if load > File_Reader.Capacity:
    #         print(load)
    #         print('超出容量')
    # if len(test2) != 0:
    #     print('解错误')
    # if cost3 != cost2:
    #     print(cost2)
    print('s', end=' ')
    for i in Result:
        print('0', end=',')
        for j in i:
            print('(', end='')
            print(j[0], end=',')
            print(j[1], end=')')
            print(',', end='')
        if i != Result[-1]:
            print('0', end=',')
        else:
            print('0')
    print('q', end=' ')
    print(cost3)
    run_time = (time.time() - start)
    # print(run_time)