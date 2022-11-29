'''
Basic Assumptions
1. 차량은 station에서 대기한다.
2. 사람은 station에서 탈 수도 있지만, 원하는 도로지점에서 차량을 부를 수 있다.
3. 불러진 스쿠터를 사람이 탈 때는 자율주행이 아니라, 사람이 운전을 한다.
4. 사람이 운전할 때는 stations을 제외한 곳들에서도 내릴 수 있다. 
5. 차량이 내린 후에는 스스로 자율주행으로 station에 와야한다.
6. 차량의 배터리 용량은 학교 내에서 가장 먼 지점을 왕복할 정도로 충전되어있다.
7. 차량이 station에 대기할때는 새로운 배터리로 갈아낄 수 있어, 바로 출발 가능하다.
8. 자율주행 중인 차량은 지나가는 길에 dial-a-ride가 있어도 가지 않는다. 충전해야하기 때문에.
9. 차량들은 전부 homogenous하다. 같은 cost를 가진다. 
10. Node와 Node를 연결하는 길은 하나이다. 
'''
# 1. edge map 과 node map을 지정.
import csv
import numpy as np
import random
nodd = list()
f = open('kaist_node.csv','r')
n = csv.reader(f)
for row in n:
    nodd.append(row)
node = np.array(nodd[1:])

Node=node[:,0]
Node_yx = node[:,1:3]
Node_road_count = node[:,3]
f.close

# ! kaist_edge.csv했을 때 name이 깨진다. 
nodd = list()
ff = open('kaist_edge.csv','r',encoding='utf-8')
n = csv.reader(ff)
for row in n:
    nodd.append(row)
edge = np.array(nodd[1:])

edge_u = edge[:,0]
edge_v = edge[:,1]
edge_len = edge[:,2]
edge_reversed = edge[]
f.close

'''
2. Station 지정해주기 <- special node일 뿐
일단 8개로 결정. 창의관, 기계동, 정문, N1, 희망관, 쪽문, 신뢰관, 도서관
Station : staion들의 정보를 모아둔 것.
'''
num = 8 # Stations number
idx = np.random.choice(len(Node),num)
stations = Node[idx]
stations_yx = Node_yx[idx]
stations_road_count = Node_road_count[idx]

# LIST 1. 수요 예측하는 list 만들기

T = 10
# Scoopter number is 20
N = 20 
Dem = []
Demand = []
for i in range(T):
    for j in range(num):
        demands = N * np.random.default_rng().dirichlet(np.ones(num),size=1)
        demands = [np.round(v) for v in demands]
        Dem.append(demands)
    Dem_ = np.asarray(Dem).reshape(-1,8)
    Dem = []
    Demand.append(Dem_)
Demand = np.array(Demand)
# 시간대에 따른 수요 <- 재배치에 쓰일 예정
print(Demand[2])

# 3. node에 연결된 edge 찾는 함수 만들기
def linked_edge(osmid):
    # osmid에 해당하는 index number
    edge_idx = np.where(edge_u == osmid)
    edge_idx = list(edge_idx)
    return edge_idx
print(np.random.choice(Node,1))
idx = linked_edge(Node[1])
Node_destination = edge_v[idx]
print(Node_destination)

# 3.5. distance 함수짜기, node와 node 사이에 연결된 edge를 따라서.
def distance_nodes(osmid1,osmid2):
    # osmid1 : start node
    # osmid2 : destination node
    # edge_idx : edges between start node and destination node
    start_idx = np.where(Node == osmid1)
    start_yx = Node_yx[start_idx]
    end_idx = np.where(Node == osmid2)
    end_yx = Node_yx[end_idx]
    distance = start_yx - end_yx
    return distance

''' 
4. 위치 지정하는 함수 만들기 
1) Node를 random하게 결정.
2) Node에서 연결된 edge를 random하게 결정
3) 그 edge들에서 parameter를 random하게 결정 [0,1]
'''

def sample_location():
    rand_node = np.random.choice(Node,1)
    rand_edge = np.random.choice(linked_edge(rand_node),1)
    rand_destination_node = edge_v[rand_edge]
    rand_alpha = random.random()
    sample_location =  rand_node + rand_alpha * distance_nodes(rand_node,rand_destination_node)
    return sample_location

'''
Frameworks

1. 초기 수요에(LIST 1) 맞게 station들에 스쿠터를 배치
2. Dial-a-ride 일때, 함수 4 써서 부른 사람의 위치 지정
3. 가장 가까운 station에서 dial-a-ride한 사람에게 차량을 배치
4. 사람이 수동주행, 함수 4 써서 도착점 정하기
5. 도착지점 정한 후에, Benefit 함수를 사용하여, 차량이 돌아갈 station을 결정하기
6. Repeat 2-5 until it reaches maximum time.

'''
def cost():
    for i in len(edge):

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
    #여기서 가장 benefit이 높은 목적지 P를 정한다. 
    P = []
    for j in len(목적지들의 list):
        pp = argmax(benefit(i,j))
        P.append(pp)

    for _ in len(P):
        cand = rand.uniform.([current_vehicle(i)]) #<- 재배치될 차량의 후보
        Go(cand,J)
