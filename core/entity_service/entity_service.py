from entities.static_entity.config import ENTITIES_PARAM
from entities.static_entity.static_entity import StaticEntity


class EntityService:
    def __init__(self, entities: list[dict]) -> None:
        self.entities = list()
        self.set_entities(entities)

    @property
    def entity_objs(self):
        return self.entities

    def set_entities(self, entities: list[dict]) -> None:
        self.entities.clear()
        for obj in entities:
            self.entities.append(StaticEntity(ENTITIES_PARAM[obj['id']], obj['pos']))

    def update_entity_pos(self, id: int, pos: tuple[float, float]) -> None:
        self.entities[id].update_pos(pos)
