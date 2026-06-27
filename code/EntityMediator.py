from xml.dom.minidom import Entity

from code.enemy import Enemy
from code.entity import entity


class EntityMediator:
    @classmethod
    def __verify_collision_window(cls, test_entity):
        pass

    @classmethod
    def __verify_collision_window(cls, test_entity):
        pass

    @classmethod
    def __verify_collision_window(cls, test_entity):
        pass


class entityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
           


    

    @staticmethod
    def verify_collision(entity_list: list[entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
            
            
   


def verify_collision(entity_list):
    return None


def verify_health(entity_list):
    return None