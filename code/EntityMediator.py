# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot
from code.Enemy import Enemy
from code.EnemyShoot import EnemyShot

class EntityMediator:

    @classmethod
    def __verify_collision_window(cls, ent: Entity):
        # CORREÇÃO: Removido o 'list[Entity]' do argumento porque aqui avaliamos uma entidade por vez
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
    def __verify_collision_entity(cls, ent1: Entity, ent2: Entity):
        valid_interaction = False

        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True

        if isinstance(ent2, Player) and isinstance(ent1, Enemy):
            valid_interaction = True
        elif isinstance(ent2, Player) and isinstance(ent1, EnemyShot):
            valid_interaction = True
        elif isinstance(ent2, Enemy) and isinstance(ent1, PlayerShot):
            valid_interaction = True

        if valid_interaction:
            if ent1.rect.colliderect(ent2.rect):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @classmethod
    def __give_score(cls, enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @classmethod
    def verify_collision(cls, entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            cls.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                cls.__verify_collision_entity(entity1, entity2)

    @classmethod
    def verify_health(cls, entity_list: list[Entity]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    cls.__give_score(ent, entity_list)
                entity_list.remove(ent)

