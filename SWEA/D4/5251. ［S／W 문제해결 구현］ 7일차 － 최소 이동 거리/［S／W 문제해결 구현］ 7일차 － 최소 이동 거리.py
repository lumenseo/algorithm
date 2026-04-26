# 우선순위 큐(힙) 기능을 사용하기 위한 모듈 불러오기
from heapq import heappush, heappop 

# 전체 테스트 케이스의 개수 입력받기
T = int(input()) 

# 각 테스트 케이스마다 반복 실행
for tc in range(1, T + 1): 
    # N: 마지막 노드 번호 (총 노드는 0번부터 N번까지 N+1개)
    # E: 간선(도로)의 개수
    N, E = map(int, input().split())

    # 각 노드에 연결된 간선 정보를 저장할 빈 2차원 리스트(인접 리스트) 생성
    road = [[] for _ in range(N + 1)]

    # 간선의 개수(E)만큼 반복하면서 간선 정보 입력받기
    for _ in range(E):
        # s: 시작점, e: 도착점, w: 가중치(거리)
        s, e, w = map(int, input().split()) 
        # 일방통행이므로 s에서 e로 가는 경로만 추가 
        # (힙에서 가중치 기준으로 정렬하기 위해 w를 튜플의 첫 번째에 둠)
        road[s].append((w, e))

    # 0번부터 N번까지 다른 모든 노드로 가는 최단 거리를 무한대(inf)로 초기화
    distance = [float('inf')] * (N + 1)
    
    # 시작점(0번 노드) 자기 자신까지의 거리는 항상 0으로 설정
    distance[0] = 0

    # 다익스트라에 사용할 빈 힙(우선순위 큐) 리스트 생성
    H = [] 
    
    # 시작점 정보를 힙에 삽입: (누적 거리 0, 시작 노드 0)
    heappush(H, (0, 0))

    # 힙에 검사할 노드가 남아있는 동안 계속 반복
    while H: 
        # 힙에서 가장 누적 거리가 짧은 노드의 (현재 누적 거리, 현재 노드 번호)를 꺼냄
        currentweight, currentnode = heappop(H)

        # [최적화 1] 꺼낸 거리가 이미 테이블에 기록된 최단 거리보다 길다면, 과거의 찌꺼기 데이터이므로 무시
        if distance[currentnode] < currentweight:
            continue

        # [최적화 2] 목적지인 N번 노드에 도달했다면 이미 최단 거리가 확정된 것이므로 탐색 중단
        if currentnode == N:
            break

        # 현재 노드와 인접한(연결된) 다음 노드들을 하나씩 확인
        for weight, nextnode in road[currentnode]:
            # 현재 노드를 거쳐서 다음 노드로 가는 총 거리(cost) 계산
            cost = currentweight + weight
            
            # 계산한 거리가 기존에 알고 있던 다음 노드까지의 최단 거리보다 짧다면 갱신!
            if cost < distance[nextnode]:
                # 더 짧은 거리로 최단 거리 테이블 업데이트
                distance[nextnode] = cost 
                # 갱신된 거리와 노드 정보를 다시 힙에 넣어 주변 탐색을 이어가게 함
                heappush(H, (cost, nextnode))

    # 모든 탐색이 끝나면, 목적지인 N번 노드까지의 최종 최단 거리 출력
    print(f"#{tc} {distance[N]}")