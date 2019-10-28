import ObjectMgr
import math


# 원 충돌 검사.
def Check_Collision(Dst, Src):
    Distance = math.sqrt(pow(Dst.x - Src.x, 2) + pow(Dst.y - Src.y, 2))
    Sum_Radius = Dst.m_Rad + Src.m_Rad

    if Distance <= Sum_Radius:
        return True
    else:
        return False
    pass


# Monster & Player 충돌.
def Collision_Monster_Player(DstLst, SrcLst):
    # DstLst - Monster
    # SrcLst - Player
    pass


# Monster & Player Bullet
def Collision_Monster_PLBullet(DstLst, SrcLst):
    # DstLst - Monster
    # SrcLst - Player Bullet

    for Dst in DstLst:
        for Src in SrcLst:
            if Check_Collision(Dst, Src):
                # Delete Bullet
                Src.Dead_Object()

                # Monster Hp 감소
                Dst.iHp -= Src.m_iAtk
                # Monster 사망 시 Player Exp 증가.
                if Dst.iHp <= 0:
                    Dst.m_bIsDead = True

                    # Monster 사망 Effect
                    # PosX, PosY, CX, CY, Speed, IsSingleEffect, IsAnimationEndDead, MaxFrame, LifeTime, ScaleX, ScaleY, FileName
                    #GameObj = Effect.CEffect(Dst.x, Dst.y, 76, 51, 0.3, False, False, 4, 2.4, 114, 76, "dust.png")
                    #ObjectMgr.Add_GameObject(GameObj, "Effect")
                pass

    return False
    pass
