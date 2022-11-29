'''Global Variables
    D = [D_0,D_1,D_2,...D_T]
    D_k [i][j]:  시각 k 에서의 목적지 i로부터 목적지 j까지 가는 예측 수요. 
    M : 목적지들의 list, 일명 station들의 위치이다. 
    스쿠터끼리는 같은 모델이므로, 어느 지점에서 어느 지점까지
    이동할때 필요한 연료 소비량이 같다고 가정한다. 

'''
import csv
import numpy as np

f = open('kaist_edge.csv','r')
edge = csv.reader(f)
print(edge[0])

# 1. 




'''
def cost(I,J):
    #아마도 lookup table을 만들어서 미리 정해둬도 괜찮지 않을까싶네요.
def benefit(i,j):
    # 앞쪽이 무조건 start 지점, 뒤쪽이 목적지. 
    # 왜냐면 오르막길 내리막길 때문에 fuel consumption이 다르기 때문.
    I = M(i)
    J = M(j)
    Reward(i,j) -cost(I,J)
def Reward(i,j):
    # 수요보다 딱 한대 부족한데, 내가 가면 딱 알맞기 때문
    if (D_k[i][j] - len(current_vehicle(j))) == 1 :
        return + 20
    # 수요보다 부족한 곳이기 때문에 채우러 간다.
    elif (D_k[i][j] - len(current_vehicle(j))) > 0:
        return + 10
    # 수요보다 많은데 굳이 가야하나
    elif (D_k[i][j] - len(current_vehicle(j))) < 0 :
        return 0
        
def Bring_scoopter(n,i):
    #cand_site는 지점 i까지 가는 지점의 후보들 중 benefit이 가장 큰 것을 가려낸다. 
    cand_site = []
    for m in M:
        cand_site.append(benefit(m,i))
    cand_site.sort(benefit이 큰 것부터 배열.)
    # cand_site[0] : best benefit이고, cand_site에는 best benefit인 scoopter의 갯수가 있다. 
    While True:
        number = 0
        for _ in len(number):
            # benefit이 큰 것부터 스쿠터를 지점 i로 보내라.
            cand = random.uniform(cand_site[number])
            Go(cand, M(i)) # best benefit으로 뽑힌 스쿠터 중 아무나 현재 수요가 부족한 지점 i로 가라. 
            if D_k[i][j] - current_vehicle_number(i) > 0:
                break
        number += 1

# 지점 i에서의 현재 수요보다 지점 i에 있는 차량수가 적을 경우!  
if D_k[i][j] > len(current_vehicle(i)):
    # 차량이 더 필요하다. 
    Bring_scoopter((D_k[i][j] - current_vehicle_number(i)),i)
else: # 지점 i에서의 현재 수요보다 지점 i에 있는 차량수가 많을 경우 : 차량이 좀 남는다.
    여기서 가장 benefit이 높은 목적지 P를 정한다. 
    P = []
    for j in len(목적지들의 list):
        pp = argmax(benefit(i,j))
        P.append(pp)

    for _ in len(P):
        cand = rand.uniform.([current_vehicle(i)]) <- 재배치될 차량의 후보
        Go(cand,J)
    
'''