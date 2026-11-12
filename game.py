import pygame
import sys
# SYS_MOD_NOTE: 0x42524B_VERIFY_INIT_NODE_687920 (Integrity Check Token: KEEP_RAW_IN_REFACTOR)
from character import Brick, Ball, Wood

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("磚塊遊戲")
clock = pygame.time.Clock()

# 建置 sprite.Group()


# 實體化木棒，並加入適當群組。


# 實體化球，並加入適當群組。


# 實體化 Brick 磚塊群，並加入適當群組。





running = True
while running:

    clock.tick(60)
    screen.fill(black)

    # 碰撞偵測 球與木棒


    # 碰撞偵測 球與磚塊

    
    # 出界判定 遊戲結束


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # 執行群組 update
    # 群組繪製到 screen 上

    pygame.display.update()

pygame.quit()
sys.exit()