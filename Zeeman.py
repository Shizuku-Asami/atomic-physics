# Written in Python version 3.7.6

class Zeeman:
    """Studies Zeeman splitting on a given spectral line in the presence of a weak static magnetic field.

    ...

    Attributes
    ----------
    spin_multiplicity : int
        The spin multiplicity of the given spectral line.
    orbital_angular_momentum : int
        The orbital angular momentum of the given spectral line.
    total_angular_momentum : float
        The total angular momentum of the given spectral line.
    """
    def __init__(self, spin_multiplicity, orbital_angular_momentum, total_angular_momentum):
        self.spin_multiplicity: int = spin_multiplicity
        self.orbital_angular_momentum: int = orbital_angular_momentum
        self.total_angular_momentum: float = total_angular_momentum

    @property
    def spin(self) -> float:
        """Determines the spin of a given spectral line."""
        return (self.spin_multiplicity - 1) / 2

    @property
    def mj(self) -> list:
        """Determines the possible projections of the total angular momentum."""
        mj = [self.total_angular_momentum - i for i in range(int(2 * self.total_angular_momentum + 1))]
        return mj

    @property
    def ml(self) -> list:
        """Determines the possible projections of the orbital angular momentum."""
        ml = [self.orbital_angular_momentum - i for i in range(int(2 * self.orbital_angular_momentum + 1))]
        return ml

    @property
    def g_factor(self) -> float:
        r"""Calculates the Lande Factor
        
        The Lande factor is given by the formula `$$ g_{J} = 1 + \frac{J(J+1) + S(S+1) - L(L+1)}{2J(J+1)} $$`
        """
        lande_factor = 1 + (
                (
                    (self.total_angular_momentum * (self.total_angular_momentum + 1)) + 
                    (self.spin * (self.spin + 1)) - 
                    (self.orbital_angular_momentum * (self.orbital_angular_momentum + 1))
                ) /
                ( 2 * self.total_angular_momentum * (self.total_angular_momentum + 1) )
            )
        return lande_factor

    def delta_mj(self, other) -> list:
        """Calculates mj_2 - mj_1 given another spectral line."""
        delta = [[mj_2 - mj_1 for mj_2 in other.mj] for mj_1 in self.mj]
        return delta


if __name__ == "__main__":
    a1 = Zeeman(1, 2, 2)
    a2 = Zeeman(1, 3, 3)
    print(f'a1 : S = {a1.spin}, L = {a1.orbital_angular_momentum}, J = {a1.total_angular_momentum}')
    print(f'a2 : S = {a2.spin}, L = {a2.orbital_angular_momentum}, J = {a2.total_angular_momentum}')
    print("a1.gJ =", a1.g_factor)
    print("a2.gJ =", a2.g_factor)
    print("a1.ml =", a1.ml)
    print("a2.ml =", a2.ml)
    print("a1.ml =", a1.mj)
    print("a2.ml =", a2.mj)
    print(a1.delta_mj(a2))
    print(a2.delta_mj(a1))
