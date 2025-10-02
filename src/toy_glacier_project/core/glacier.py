from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime



class Glacier:
    """
    A class representing a glacier with a name and mass.

    Parameters
    ----------
    name : str
        The name of the glacier.
    mass : int
        The initial mass of the glacier.
    """

    def __init__(self, name: str, mass: int, id: UUID = None):
        self.name = name
        self.mass = mass
        self.id = id if id is not None else uuid4()
        self.version:int = 0

    def can_ablate(self, ablate_amount: int) -> bool:
        """
        Check if the glacier can lose the specified mass without going negative or to zero.

        Parameters
        ----------
        ablate_amount : int
            The amount of mass to potentially ablate.

        Returns
        -------
        bool
            True if the glacier can lose the specified mass, False otherwise.
        """
        return self.mass >= ablate_amount  # .qty

    def accumulate(self, accum_amount: int):
        """
        Simulate accumulation by increasing the glacier's mass.

        Parameters
        ----------
        accum_amount : int
            The mass to add to the glacier.
        """
        self.mass += accum_amount
        self.version += 1

    def ablate(self, ablate_amount: int):
        """
        Simulate ablation by decreasing the glacier's mass.

        Parameters
        ----------
        ablate_amount : int
            The amount of mass to remove from the glacier.

        Raises
        ------
        ValueError
            If the glacier does not have enough mass to ablate the specified amount.
        """
        if self.can_ablate(ablate_amount):
            self.mass -= ablate_amount  # .qtz
            self.version += 1
        else:
            raise ValueError("Glacier has disappeared, no more mass to lose.")


def make_glacier(name: str, mass: int):
    """
    Create a Glacier object.

    Parameters
    ----------
    name : str
        The name of the glacier.
    mass : int
        The initial mass of the glacier.

    Returns
    -------
    Glacier
        A new Glacier object with the specified name and mass.
    """
    glacier = Glacier(name=name, mass=mass, id=uuid4())
    return glacier
