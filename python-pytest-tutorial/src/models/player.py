from dataclasses import dataclass, field
from typing import List, Iterable
from models.guardian import Guardian


@dataclass
class Player:
    first_name: str
    last_name: str
    guardians: List[Guardian] = field(default_factory=list)

    def add_guardian(self, guardian: Guardian):
        self.guardians.append(guardian)

    # def add_guardians(self, guardians: list[Guardian]):
    # Iterable generic to List and Tuple
    def add_guardians(self, guardians: Iterable[Guardian]):
        self.guardians.extend(guardians)

    @property
    def primary_guardian(self):
        return self.guardians[0]
