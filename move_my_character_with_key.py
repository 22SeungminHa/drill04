from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Pikachu.png')


def handle_events():
    global running, dir, action, move, frame

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            frame = 0
            if event.key == SDLK_a: #좌
                dir, action = 1, 1
            elif event.key == SDLK_d: #우
                dir, action = 2, 1
            elif event.key == SDLK_w: #상
                dir, action = 3, 1
            elif event.key == SDLK_s: #하
                dir, action = 4, 1
            elif event.key == SDLK_ESCAPE: #종료
                running = False
            elif event.key == SDLK_SPACE: #점프
                action = 2
            elif event.key == SDLK_e: #전기
                action = 3
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a or event.key == SDLK_w or event.key == SDLK_s or event.key == SDLK_d:
                frame, action = 0, 0



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir = 0
action = 0


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)


    update_canvas()
    handle_events()

    delay(0.05)


close_canvas()


close_canvas()

