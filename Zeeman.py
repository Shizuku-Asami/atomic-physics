class Zeeman:
    """Studies Zeeman splitting on a given spectral line in the presence of a weak static magnetic field.

    ...

    Attributes
    ----------
    spin_multiplicity : int
        The spin multiplicity of the given spectral line.
    L : int
        The orbital angular momentum of the given spectral line.
    J : float
        The total angular momentum of the given spectral line.
    """
    def __init__(self, spin_multiplicity, L, J):
        self.spin_multiplicity : int = spin_multiplicity
        self.L : int = L
        self.J : float = J

    @property
    def S(self):
        """Determines the spin of a given spectral line."""
        return (self.spin_multiplicity - 1) / 2

    @property
    def MJ(self):
        """Determines the possible projections of the total angular momentum."""
        mj = []
        for i in range(int(2*self.J + 1)):
            mj.append(self.J - i)
        return mj

    @property
    def ML(self):
        """Determines the possible projections of the orbital angular momentum."""
        ml = []
        for i in range(int(2*self.L + 1)):
            ml.append(self.L - i)
        return ml

    @property
    def g_factor(self):
        """Calculates the Lande Factor"""
        return 1 + (( (self.J * (self.J + 1)) + (self.S * (self.S + 1)) - (self.L * (self.L + 1)) )/( 2 * self.J * (self.J + 1) ))

    def delta_MJ(self, other):
        """Calculates MJ_2 - MJ_1 given another spectral line."""
        delta = []
        for MJ_1 in self.MJ:
            _delta = []
            for MJ_2 in other.MJ:
                _delta.append(MJ_2 - MJ_1)
            delta.append(_delta)
        return delta


if __name__ == "__main__":
    a1 = Zeeman(1, 2, 2)
    a2 = Zeeman(1, 3, 3)
    print(f'a1 : S = {a1.S}, L = {a1.L}, J = {a1.J}')
    print(f'a2 : S = {a2.S}, L = {a2.L}, J = {a2.J}')
    print("a1.gJ =", a1.g_factor)
    print("a2.gJ =", a2.g_factor)
    print("a1.ML =", a1.ML)
    print("a2.ML =", a2.ML)
    print("a1.MJ =", a1.MJ)
    print("a2.MJ =", a2.MJ)