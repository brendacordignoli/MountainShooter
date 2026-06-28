from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShoot import EnemyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class EntityMediator:

    @classmethod
    def __verify_collision_window(cls: Entity):
        if isinstance(cls, Enemy):
            if cls.rect.right <= 0:
                cls.health = 0
        if isinstance(cls, PlayerShot):
            if cls.rect.left >= WIN_WIDTH:
                cls.health = 0
        if isinstance(cls, EnemyShot):
            if cls.rect.right <= 0:
                cls.health = 0


    @classmethod
    def verify_collision(cls: list[Entity], entity_list=None):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window()

    @classmethod
    def verify_health(cls: list[Entity], entity_list=None):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)


def verify_collision(entity_list):
    return None

def verify_health(entity_list):
    return None