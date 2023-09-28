from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Pikachu.png')


def handle_events():
    global running, dir, action, frame, jump_x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a: #좌
                if dir != 1: frame = 0
                dir, action = 1, 1

            elif event.key == SDLK_d: #우
                if dir != 2: frame = 0
                dir, action = 2, 1

            elif event.key == SDLK_w: #상
                if dir != 3: frame = 0
                dir, action = 3, 1

            elif event.key == SDLK_s: #하
                if dir != 4: frame = 0
                dir, action = 4, 1

            elif event.key == SDLK_ESCAPE: #종료
                running = False

            elif event.key == SDLK_SPACE: #점프
                jump_x, frame = 0, 0
                action = 2

            elif event.key == SDLK_e: #전기
                jump_x, frame = 0, 0
                action = 3

        elif event.type == SDL_KEYUP:
            if (dir == 1 and event.key == SDLK_a) or (dir == 2 and event.key == SDLK_d) or (dir == 3 and event.key == SDLK_w) or (dir == 4 and event.key == SDLK_s):
                frame, action = 0, 0



def paint_pikachu(w, h, poition, cnt):
    global x, y, dir, frame
    if dir % 2 == 1:
        character.clip_draw(frame * w, 597 - poition, w, h, x, y, w * 2, h * 2)
    else:
        character.clip_composite_draw(frame * w, 597 - poition, w, h, 0, 'h', x, y, w * 2, h * 2)
    frame = (frame + 1) % cnt



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame, action, jump_x, dir = 0, 0, 0, 1
jump_width = [47, 46, 55, 42, 36, 33, 50, 49, 46, 40, 67, 37, 50, 51, 46, 48, 51, 65, 63, 61, 52]

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    # 정지
    if action == 0:
        paint_pikachu(51, 48, 48, 8)

    # 뛰기
    elif action == 1:
        if dir == 1:
            x -= 10
        elif dir == 2:
            x += 10
        elif dir == 3:
            y += 10
        elif dir == 4:
            y -= 10

        if x - 57 >= 0 and x + 57 <= TUK_WIDTH and y - 48 >= 0 and y + 48 <= TUK_HEIGHT:
            paint_pikachu(57, 47, 145, 5)

        else:
            if x - 57 < 0 or x + 57 > TUK_WIDTH:
                if x - 57 < 0:
                    x = 57
                    character.clip_draw(0, 597 - 96, 57, 47, x, y, 57 * 2, 47 * 2)

                elif x + 57 > TUK_WIDTH:
                    x = TUK_WIDTH - 57
                    character.clip_composite_draw(0, 597 - 96, 57, 47, 0, 'h', x, y, 57 * 2, 47 * 2)

            elif y - 48 < 0 or y + 48 > TUK_HEIGHT:
                if y - 48 < 0: y = 48
                elif y + 48 > TUK_HEIGHT: y = TUK_HEIGHT - 48

                paint_pikachu(57, 47, 145, 5)

    # 점프
    elif action == 2:
        if dir % 2 == 1:
            character.clip_draw(jump_x, 597 - 247, jump_width[frame], 100, x, y + 20, jump_width[frame] * 2, 100 * 2)
        else:
            character.clip_composite_draw(jump_x, 597 - 247, jump_width[frame], 100, 0, 'h', x, y + 20, jump_width[frame] * 2, 100 * 2)
        jump_x += jump_width[frame]
        frame = (frame + 1) % 21
        if frame == 0:
            action = 0

    # 전기
    elif action == 3:
        paint_pikachu(53, 45, 295, 17)
        if frame == 0:
            action = 0
        pass

    update_canvas()
    handle_events()

    delay(0.05)


close_canvas()

