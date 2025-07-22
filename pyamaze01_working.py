# pyamaze 라이브러리 설치 필요: pip install pyamaze
from pyamaze import maze, agent, COLOR
import time

MAZE_ROWS = 10
MAZE_COLS = 10

def truly_working_maze_solver(maze_obj):
    """재귀 DFS 백트래킹"""
    start = (maze_obj.rows, maze_obj.cols)
    goal = (1, 1)
    
    directions = {
        'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)
    }
    
    def get_neighbors(pos):
        neighbors = []
        for direction, (dr, dc) in directions.items():
            if pos in maze_obj.maze_map and maze_obj.maze_map[pos][direction] == 1:
                next_pos = (pos[0] + dr, pos[1] + dc)
                if (1 <= next_pos[0] <= maze_obj.rows and 
                    1 <= next_pos[1] <= maze_obj.cols):
                    neighbors.append(next_pos)
        return neighbors
    
    def manhattan_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def dfs_solve(current_pos, path, visited):
        if current_pos == goal:
            return True
        
        visited.add(current_pos)
        
        neighbors = get_neighbors(current_pos)
        unvisited_neighbors = [n for n in neighbors if n not in visited]
        unvisited_neighbors.sort(key=lambda x: manhattan_distance(x, goal))
        
        for next_pos in unvisited_neighbors:
            path[current_pos] = next_pos
            
            if dfs_solve(next_pos, path, visited):
                return True
            
            if current_pos in path:
                del path[current_pos]
        
        visited.remove(current_pos)
        return False
    
    print(f"재귀 DFS 백트래킹 실행...")
    start_time = time.time()
    path = {}
    visited = set()
    
    success = dfs_solve(start, path, visited)
    total_time = time.time() - start_time
    
    if success:
        print(f"🎉 재귀 DFS 성공! ({len(path)}단계, {total_time:.3f}초)")
        return path, True
    else:
        print(f"❌ 재귀 DFS 실패! ({total_time:.3f}초)")
        return {}, False

def iterative_backtracking_solver(maze_obj):
    """반복문 백트래킹"""
    start = (maze_obj.rows, maze_obj.cols)
    goal = (1, 1)
    
    directions = {
        'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)
    }
    
    def get_neighbors(pos):
        neighbors = []
        for direction, (dr, dc) in directions.items():
            if pos in maze_obj.maze_map and maze_obj.maze_map[pos][direction] == 1:
                next_pos = (pos[0] + dr, pos[1] + dc)
                if (1 <= next_pos[0] <= maze_obj.rows and 
                    1 <= next_pos[1] <= maze_obj.cols):
                    neighbors.append(next_pos)
        return neighbors
    
    def manhattan_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    print(f"반복문 백트래킹 실행...")
    start_time = time.time()
    
    stack = [(start, {}, set([start]))]
    step_count = 0
    max_steps = MAZE_ROWS * MAZE_COLS * 50
    
    while stack and step_count < max_steps:
        current_pos, current_path, current_visited = stack.pop()
        step_count += 1
        
        if current_pos == goal:
            total_time = time.time() - start_time
            print(f"🎉 반복문 백트래킹 성공! ({len(current_path)}단계, {step_count}회 시도, {total_time:.3f}초)")
            return current_path, True
        
        neighbors = get_neighbors(current_pos)
        unvisited_neighbors = [n for n in neighbors if n not in current_visited]
        unvisited_neighbors.sort(key=lambda x: manhattan_distance(x, goal), reverse=True)
        
        for next_pos in unvisited_neighbors:
            new_path = current_path.copy()
            new_path[current_pos] = next_pos
            new_visited = current_visited.copy()
            new_visited.add(next_pos)
            stack.append((next_pos, new_path, new_visited))
    
    total_time = time.time() - start_time
    print(f"❌ 반복문 백트래킹 실패! ({step_count}회 시도, {total_time:.3f}초)")
    return {}, False

def enhanced_greedy_solver(maze_obj):
    """향상된 단순 탐욕 - 실패해도 경로 반환"""
    start = (maze_obj.rows, maze_obj.cols)
    goal = (1, 1)
    
    directions = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    current_pos = start
    path = {}
    visited = set()
    
    def manhattan_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    step_count = 0
    max_steps = MAZE_ROWS * MAZE_COLS * 3
    
    print("향상된 단순 탐욕 실행...")
    start_time = time.time()
    
    while current_pos != goal and step_count < max_steps:
        visited.add(current_pos)
        
        possible_moves = []
        for direction, (dr, dc) in directions.items():
            if (current_pos in maze_obj.maze_map and 
                maze_obj.maze_map[current_pos][direction] == 1):
                next_pos = (current_pos[0] + dr, current_pos[1] + dc)
                if (1 <= next_pos[0] <= maze_obj.rows and 
                    1 <= next_pos[1] <= maze_obj.cols and
                    next_pos not in visited):
                    possible_moves.append(next_pos)
        
        if not possible_moves:
            # 막혔을 때: 가장 가까운 방문하지 않은 곳 찾기 (제한적 백트래킹)
            all_moves = []
            for direction, (dr, dc) in directions.items():
                if (current_pos in maze_obj.maze_map and 
                    maze_obj.maze_map[current_pos][direction] == 1):
                    next_pos = (current_pos[0] + dr, current_pos[1] + dc)
                    if (1 <= next_pos[0] <= maze_obj.rows and 
                        1 <= next_pos[1] <= maze_obj.cols):
                        all_moves.append(next_pos)
            
            if not all_moves:
                break
                
            # 방문한 곳이라도 목표에 가장 가까운 곳으로
            possible_moves = all_moves
        
        # 목표에 가장 가까운 위치 선택
        best_move = min(possible_moves, key=lambda x: manhattan_distance(x, goal))
        path[current_pos] = best_move
        current_pos = best_move
        step_count += 1
    
    total_time = time.time() - start_time
    success = current_pos == goal
    
    if success:
        print(f"🎉 단순 탐욕 성공! ({step_count}단계, {total_time:.3f}초)")
        print(f"   최종 위치: {current_pos}")
        return path, True
    else:
        print(f"❌ 단순 탐욕 실패! ({step_count}단계, {total_time:.3f}초)")
        print(f"   최종 위치: {current_pos} (목표: {goal})")
        print(f"   도달 거리: {manhattan_distance(current_pos, goal)}칸 남음")
        return path, False  # 실패해도 지금까지의 경로는 반환!

def main():
    # 미로 생성
    m = maze(MAZE_ROWS, MAZE_COLS)
    m.CreateMaze(loopPercent=0, theme=COLOR.light)
    
    print("=" * 70)
    print("🧠 모든 알고리즘 시도 결과 비교 (실패해도 표시)")
    print("=" * 70)
    
    # 1. 재귀 DFS 백트래킹
    print("\n🎯 1. 재귀 DFS 백트래킹:")
    recursive_path, recursive_success = truly_working_maze_solver(m)
    
    # 2. 반복문 백트래킹  
    print("\n🔄 2. 반복문 백트래킹:")
    iterative_path, iterative_success = iterative_backtracking_solver(m)
    
    # 3. 향상된 단순 탐욕
    print("\n🏃 3. 향상된 단순 탐욕:")
    greedy_path, greedy_success = enhanced_greedy_solver(m)
    
    print("\n" + "=" * 70)
    print("📊 결과 비교:")
    print(f"재귀 백트래킹:   {len(recursive_path):3d}단계 {'🎉' if recursive_success else '❌'}")
    print(f"반복문 백트래킹: {len(iterative_path):3d}단계 {'🎉' if iterative_success else '❌'}")  
    print(f"단순 탐욕:       {len(greedy_path):3d}단계 {'🎉' if greedy_success else '❌'}")
    
    if hasattr(m, 'path') and m.path:
        print(f"최적 경로:       {len(m.path):3d}단계 ⭐")
    
    print("\n🎨 시각화 결과:")
    
    # 시각화 - 성공/실패 관계없이 모든 경로 표시
    if recursive_path:
        agent1 = agent(m, footprints=True, color=COLOR.blue, filled=True, shape='arrow')
        m.tracePath({agent1: recursive_path}, delay=20)
        status = "성공!" if recursive_success else "실패"
        print(f"🔵 파란 화살표: 재귀 백트래킹 ({status})")
    
    if iterative_path:
        agent2 = agent(m, footprints=True, color=COLOR.red, filled=False, shape='square')  
        m.tracePath({agent2: iterative_path}, delay=20)
        status = "성공!" if iterative_success else "실패"
        print(f"🔴 빨간 사각형: 반복문 백트래킹 ({status})")
    
    if greedy_path:  # 이제 실패해도 경로가 있으면 표시!
        agent3 = agent(m, footprints=True, color=COLOR.cyan, filled=True, shape='square')
        m.tracePath({agent3: greedy_path}, delay=20)
        status = "성공!" if greedy_success else "실패 (부분 경로)"
        print(f"🟦 청록 사각형: 단순 탐욕 ({status})")
    
    if hasattr(m, 'path') and m.path:
        optimal_agent = agent(m, color=COLOR.green, filled=False, shape='square')
        print(f"🟢 초록 사각형: 최적 경로")
    
    print(f"\n💡 해석:")
    print(f"   - 백트래킹 알고리즘들은 해가 있으면 반드시 찾습니다")
    print(f"   - 단순 탐욕은 빠르지만 막다른 길에서 멈출 수 있습니다")
    print(f"   - 실패한 경로도 '어디까지 갔는지' 보여줍니다")
    
    print("\n🎮 미로 실행 중... 창을 닫으면 종료됩니다.")
    m.run()

if __name__ == "__main__":
    print("🚀 모든 알고리즘 시도 결과 비교!")
    print("=" * 50)
    print("성공하든 실패하든 모든 경로를 보여줍니다!")
    print("=" * 50)
    main()