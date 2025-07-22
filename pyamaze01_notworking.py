from pyamaze import maze, COLOR, agent

# 미로 크기 설정

MAZE_ROWS = 10
MAZE_COLS = 10

m = maze(MAZE_ROWS, MAZE_COLS)
m.CreateMaze(theme=COLOR.light)
a=agent(m, filled=True, footprints=True)
m.tracePath({a:m.path})


# 벽 따라가기 알고리즘 구현
def wall_following_algorithm(maze_obj):
    
     
    def can_move_to(from_pos, direction):
    """현재 위치에서 목표점까지 직진할 수 있는지 확인합니다."""
    
    def get_next_position(pos, direction):
    """현재 위치에서 특정 방향으로 이동했을 때의 다음 위치를 반환합니다."""
    
    def can_go_to_goal_directly():
    """현재 위치에서 목표점까지 직진할 수 있는지 확인합니다."""
    
    def get_wall_following_direction():
    """오른손 법칙에 따라 다음 이동 방향을 결정합니다."""
    
    def move_toward_goal():
    """목표점을 향해 직진합니다."""
    
# main.
def main():
    m.run()

# 프로그램 실행

if __name__ == "__main__":
    main()
