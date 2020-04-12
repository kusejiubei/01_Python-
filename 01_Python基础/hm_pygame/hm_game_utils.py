import pygame

# 每次移动的距离
PER_SPACE = 1
# 屏幕矩阵rect
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 游戏刷新频率
FRESH_PER_SECOND = 60
# 定义用户事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = CREATE_ENEMY_EVENT + 1


def key_click(event, hero_rect):
    """
    键盘操作
    :param event:
    :param hero_rect:
    :return:
    """
    if event.dict["key"] == pygame.K_RIGHT:  # 275 有常量的，开始不知道
        hero_rect.x += PER_SPACE * 2
    elif event.dict["key"] == 276:
        hero_rect.x -= PER_SPACE * 2
    elif event.dict["key"] == 274:
        hero_rect.y += PER_SPACE * 2
    elif event.dict["key"] == 273:
        hero_rect.y -= PER_SPACE * 2
    else:
        print(event)


def key_press(key_press, hero_rect):
    """
    键盘专有操作
    :param event:
    :param hero_rect:
    :return:
    """
    if key_press[pygame.K_RIGHT]:  # 275 有常量的，开始不知道
        hero_rect.x += PER_SPACE * 2
    elif key_press[pygame.K_LEFT]:
        hero_rect.x -= PER_SPACE * 2
    elif key_press[pygame.K_DOWN]:
        hero_rect.y += PER_SPACE * 2
    elif key_press[pygame.K_UP]:
        hero_rect.y -= PER_SPACE * 2
    else:
        pass


def mouse_move(event, hero_rect):
    """
    鼠标移动
    :param event:
    :param hero_rect:
    :return:
    """
    x_ = event.dict["pos"][0]
    y_ = event.dict["pos"][1]
    if 0 < x_ < SCREEN_RECT.width and 0 < y_ < SCREEN_RECT.height:
        hero_rect.x = x_ - 50
        hero_rect.y = y_ - 43


def mouse_button(event, again, over):
    print("+" * 10, event, again, SCREEN_RECT.right, SCREEN_RECT.left, SCREEN_RECT.top, SCREEN_RECT.bottom)
    if again.rect.left < event.pos[0] < again.rect.right and again.rect.top < event.pos[1] < again.rect.bottom:
        return 1
    elif over.rect.left < event.pos[0] < over.rect.right and over.rect.top < event.pos[1] < over.rect.bottom:
        return 2
    else:
        return 3
