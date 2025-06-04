from datetime import date
from pydantic import BaseModel, ConfigDict, computed_field


class AnimalCreate(BaseModel):
    animal_type: str
    animal_breed: str
    name: str
    birth_date: date
    animal_photo: str


class AnimalResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    animal_type: str
    animal_breed: str
    name: str
    birth_date: date
    animal_photo: str

    @computed_field
    @property
    def age(self) -> int:
        today = date.today()
        years = today.year - self.birth_date.year

        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1

        return years
