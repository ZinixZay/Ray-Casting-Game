from entities.static_entity.static_entity import StaticEntity
from settings import ENTITIES_PARAM
from statuses.status_entities import STATUS_ENTITIES


class EntityService:
    def __init__(self, entities: list[dict]) -> None:
        self.entities = list()
        self.set_entities(entities)

    @property
    def entity_objs(self) -> list:
        return self.entities

    @property
    def entity_vulnerable(self) -> list:
        return [ent for ent in filter(lambda x: x.health_point > 0, self.entities)]

    @property
    def entity_packs(self) -> list:
        return [ent for ent in filter(lambda x: x.type in [
            STATUS_ENTITIES.HEALTH_PACK, STATUS_ENTITIES.ARMOR_PACK, STATUS_ENTITIES.BULLET_PACK
        ], self.entities)]

    def set_entities(self, entities: list[dict]) -> None:
        self.entities.clear()
        for obj in entities:
            self.entities.append(StaticEntity(ENTITIES_PARAM[obj['id']], obj['pos']))

    def update_entity_pos(self, id: int, pos: tuple[float, float]) -> None:
        self.entities[id].update_pos(pos)

    def update_entity_angle(self, id: int, angle: int) -> None:
        self.entities[id].update_angle(angle)
