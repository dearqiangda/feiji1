import pygame
import time
from pygame.locals import *
import random

class Base(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name).convert() 

class BasePlant(Base):
    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self,screen_temp, x, y, image_name)
        self.bullet_list = []#存储发射的子弹
    
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():#判断子弹是否越界
                self.bullet_list.remove(bullet)

class BaseBullet(Base):
    def display(self):
        self.screen.blit(self.image,(self.x, self.y))
            

class HeroPlant(BasePlant):
    def __init__(self,screen_temp):
        BasePlant.__init__(self, screen_temp, 105, 350, "./feiji/hero1.png")
        
           
    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class EnemyPlant(BasePlant):
    def __init__(self,screen_temp):
        BasePlant.__init__(self, screen_temp, 0, 0, "./feiji/enemy0.png")

        self.direction = "right"#默认敌机移动方向
    

    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x > 240 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"


    def fire(self):
        random_num = random.randint(0,100)
        if random_num == 8 or random_num == 80:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))

class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+40, y-20, "./feiji/bullet.png")

    def move(self):
        self.y -= 10

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False
class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+25, y+40, "./feiji/bullet1.png")

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 426:
            return True
        else:
            return False

def key_control(hero_temp):
    #获取事件，比如按键等
    for event in pygame.event.get():

        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()

            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()

            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()



def main():

    #创建一个窗口来显示内容,
    screen = pygame.display.set_mode((240,426),0,32)

    #创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png").convert()
    #创建飞机对象
    hero = HeroPlant(screen)

    #创建敌机对象
    enemy = EnemyPlant(screen)

    #把背景图片放到窗口中显示
    while True:

        #设置需要显示的背景图
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        #更新需要显示的内容
        pygame.display.update()
        key_control(hero)

        time.sleep(0.02)


if __name__ == "__main__":
    main()
