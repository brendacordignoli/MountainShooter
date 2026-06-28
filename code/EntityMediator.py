from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShoot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @classmethod
    def __verify_collision_window(cls, ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        elif isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        elif isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0


    @classmethod
    def __verify_collision_entity(cls, ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @classmethod
    def __give_score(cls: Enemy, entity_list: list[Entity]):
        if cls.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += cls.score
        elif cls.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += cls.score

    @classmethod
    def verify_collision(cls: list[Entity]):
        for i in range(len(cls)):
            entity1 = cls[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(cls)):
                entity2 = cls[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @classmethod
    def verify_health(cls, entity_list):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)


def verify_collision(entity_list):
    return None

def verify_health(entity_list):
    return None