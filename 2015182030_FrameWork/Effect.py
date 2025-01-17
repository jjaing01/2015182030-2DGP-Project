from pico2d import *
import main_state
import game_framework

time = 0.0


class CEffect:
    image = [None, None, None]

    def __init__(self, PosX, PosY, CX, CY, Speed, IsSingleEffect, IsAnimationEndDead, MaxFrame, LifeTime, ScaleX, ScaleY, FileName):
        self.IsDead = False
        self.x = PosX
        self.y = PosY
        self.cx = CX
        self.cy = CY
        self.speed = Speed
        self.frame = 1
        self.max_frame = MaxFrame
        self.lifetime = LifeTime
        self.scaleX = ScaleX
        self.scaleY = ScaleY
        self.filename = FileName
        self.isSingleEffect = IsSingleEffect
        self.isAnimationEndDead = IsAnimationEndDead
        self.m_bIsMeteo = False

        if CEffect.image[0] is None:
            CEffect.image[0] = load_image("Tengai/Resource/UI/Explode/Explode.png")
        if CEffect.image[1] is None:
            CEffect.image[1] = load_image("Tengai/Resource/UI/Effect5/Effect5.png")
        if CEffect.image[2] is None:
            CEffect.image[2] = load_image("Tengai/Resource/UI/PSkill/PSkill.png")
            pass

    def Handle_Events(self):
        pass

    def update(self):
        if self.IsDead:
            return -1

        # Animation
        if not self.isSingleEffect:
            self.frame = (self.frame + self.speed)
        if self.frame >= self.max_frame:
            if self.isAnimationEndDead:
                self.IsDead = True
            else:
                self.frame = 0

        # LifeTime
        global time
        time += 0.1
        if time >= self.lifetime:
            self.IsDead = True
            time = 0.0

        if self.filename == "PSkill.png" and self.m_bIsMeteo == False:
            main_state.m_ObjectMgr.Add_Object("FIRE_BALL", None, 500, 600)
            main_state.m_ObjectMgr.Add_Object("FIRE_BALL", None, 300, 580)
            main_state.m_ObjectMgr.Add_Object("FIRE_BALL", None, 700, 510)
            main_state.m_ObjectMgr.Add_Object("FIRE_BALL", None, 800, 600)
            main_state.m_ObjectMgr.Add_Object("FIRE_BALL", None, 400, 500)
            main_state.m_ObjectMgr.Add_Object("FIRE_BALL", None, 100, 550)
            main_state.m_ObjectMgr.Add_Object("FIRE_BALL", None, 200, 700)
            main_state.m_ObjectMgr.Add_Object("FIRE_BALL", None, 150, 650)
            main_state.m_ObjectMgr.Add_Object("FIRE_BALL", None, 70, 450)
            main_state.m_ObjectMgr.Add_Object("FIRE_BALL", None, 50, 350)
            self.m_bIsMeteo = True

        return 0
        pass

    def draw(self):
        index = 0

        if not self.IsDead:
            if self.filename == "Explode.png":
                index = 0

            elif self.filename == "Effect5.png":
                index = 1

            elif self.filename == "PSkill.png":
                index = 2

            if not self.isSingleEffect:
                self.image[index].clip_draw(int(self.frame) * self.cx, 0, self.cx, self.cy, self.x, self.y, self.scaleX,
                                            self.scaleY)
            else:
                self.image[index].draw(self.x, self.y, self.scaleX, self.scaleY)

        pass

    def Dead_Object(self):
        self.IsDead = True
        pass

    pass