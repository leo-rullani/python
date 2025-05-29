import curses
from random import randint

def main(stdscr):
    # Cursor ausblenden
    curses.curs_set(0)
    
    # Spielfeldhöhe und -breite
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # Initiale Position der Snake
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    # Erstes Futter
    food = [randint(1, sh - 2), randint(1, sw - 2)]
    w.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # Neue Kopfposition
        head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            head[0] += 1
        if key == curses.KEY_UP:
            head[0] -= 1
        if key == curses.KEY_LEFT:
            head[1] -= 1
        if key == curses.KEY_RIGHT:
            head[1] += 1

        snake.insert(0, head)

        # Game Over Bedingungen
        if (
            head[0] in [0, sh] or
            head[1] in [0, sw] or
            head in snake[1:]
        ):
            msg = "GAME OVER! Drücke eine Taste."
            w.addstr(sh // 2, (sw - len(msg)) // 2, msg)
            w.nodelay(0)
            w.getch()
            break

        # Futter fressen
        if head == food:
            food = None
            while food is None or food in snake:
                food = [randint(1, sh - 2), randint(1, sw - 2)]
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

curses.wrapper(main)
