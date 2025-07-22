from pyamaze import maze, COLOR, agent

# 미로 크리 설정

MAZE_ROWS = 10
MAZE_COLS = 10

m = maze(MAZE_ROWS, MAZE_COLS)
m.CreateMaze(theme=COLOR.light)
a=agent(m, filled=True, footprints=True)
m.tracePath({a:m.path})


# 벽 따라가기 알고리즘 구현


# main.
def main():
    m.run()

# 프로그램 실행

if __name__ == "__main__":
    main()
