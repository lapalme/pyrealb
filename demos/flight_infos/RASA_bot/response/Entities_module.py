from typing import Union

flight_fields: list[str] = [
    "cost_relative", "fare_amount", "economy","compartment",
    "flight_time", "flight_mod", "flight_days", "flight_stop",
    "round_trip", "connect", "class_type", "mod", "day_name","period_of_day"
]

class Entity:
    def __init__(self,data:dict[str,Union[int,str]]):
        self.value=data["value"]
        self.entity=data["entity"]
        self.role=data.get("role")

    def __str__(self):
        return ((self.role+".") if self.role is not None else "") \
                + self.entity+":"+self.value

    def has_entity_role(self, otherEntity:str, otherRole:str=None):
        return self.entity==otherEntity and self.role==otherRole

    def get_value(self):
        return self.value

    def get_entity(self):
        return self.entity

    def get_role(self):
        return self.role

class Entities:
    def __init__(self,data:list[Entity]) -> None:
        if len(data)==0 or type(data[0]) is Entity:
            self.entities = data
        else:
            self.entities = [Entity(datum) for datum in data]

    def __str__(self) -> str:
        # produce a "compact" representation of the entities ignoring positions
        return "{ "+", ".join(map(str,self.entities))+" }"

    def __len__(self) -> int:
        return len(self.entities)

    def __getitem__(self,i:int) -> Entity :
        return self.entities[i]

    def pop(self,n:int=None) -> Entity:
        return self.entities.pop(n)

    def split(self,sep:str) -> list[list[Entity]]:
        # split entities into lists at entity named "sep"
        ess=[]
        es=[]
        while len(self.entities)>0:
            e=self.entities.pop(0)
            if e.has_entity_role(sep):
                ess.append(Entities(es))
                es=[]
            else:
                es.append(e)
        if len(es)>0:
            ess.append(Entities(es))
        # for es in ess:
        #     print(es)
        return ess

    # Get the value of a field
    # If the entity is not found return an empty string
    # If more than one entity is found, return all of them separated with a comma
    def get_value(self, field:str, role:str=None) -> str:
        return ", ".join(e.get_value() for e in self.entities if e.has_entity_role(field, role))

    # Get the value of field and remove it from the entities
    # If the entity with an optional role is not found return an empty string
    # If more than one entity is found, return all of them separated with a comma
    def grab_value(self, field:str, role:str=None) -> str:
        res=[]
        i=0
        # cannot use a for loop because the list might be changed during iteration
        while i<len(self.entities):
            if self.entities[i].has_entity_role(field, role):
                res.append(self.entities[i].get_value())
                del self.entities[i]
            else:
                i+=1
        return ", ".join(res)

    # get all values, ignoring their names and clear the list
    def grab_values(self) -> list[str]:
        values = ", ".join(e.get_value() for e in self.entities)
        self.entities.clear()
        return values

    # check if an entity appears in the entities
    def has_entity(self, field:str, role:str=None) -> bool:
        return any(e.has_entity_role(field, role) for e in self.entities)

    # check if any entity has a given role
    def has_role(self,role:str) -> bool:
        return any(e.get_role() == role for e in self.entities)
