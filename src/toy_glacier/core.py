class Glacier:
    """
    A class representing a glacier with a name and volume.

    Parameters
    ----------
    name : str
        The name of the glacier.
    volume : int
        The initial volume of the glacier.
    """
    def __init__(self, name: str, volume: int):
        self.name = name
        self.volume = volume

    def can_ablate(self, ablate_amount: int) -> bool:
        """
        Check if the glacier can lose the specified volume without going negative or to zero.

        Parameters
        ----------
        ablate_amount : int
            The amount of volume to potentially ablate.

        Returns
        -------
        bool
            True if the glacier can lose the specified volume, False otherwise.
        """        
        return self.volume >= ablate_amount  # .qty

    def accumulate(self, accum_amount: int):
        """
        Simulate accumulation by increasing the glacier's volume.

        Parameters
        ----------
        accum_amount : int
            The volume to add to the glacier.
        """       
        self.volume += accum_amount 

    def ablate(self, ablate_amount: int):
        """
        Simulate ablation by decreasing the glacier's volume.

        Parameters
        ----------
        ablate_amount : int
            The amount of volume to remove from the glacier.

        Raises
        ------
        ValueError
            If the glacier does not have enough volume to ablate the specified amount.
        """       
        if self.can_ablate(ablate_amount):
            self.volume -= ablate_amount  # .qtz
        else:
            raise ValueError("Glacier has disappeared, no more mass to lose.")


def make_glacier(name: str, glacier_volume: int):
    """
    Create a Glacier object.

    Parameters
    ----------
    name : str
        The name of the glacier.
    glacier_volume : int
        The initial volume of the glacier.

    Returns
    -------
    Glacier
        A new Glacier object with the specified name and volume.
    """   
    glacier = Glacier(name=name, volume=glacier_volume)
    return glacier
   