class MagneticField:
    def __init__(self, induction: int): # induction vector is [0, 0, induction], perpendicular to the game board
        self.induction = induction

    def apply(self, speed: tuple[int, int], charge: int, mass: int, time: int):
        # apply Lorentz force
        force = (charge * speed[1] * self.induction, -(charge * speed[0] * self.induction)) # sin = 1, because vectors are perpendicular
        new_speed = (force[0] / mass * time, force[1] / mass * time)
        return (speed[0] + new_speed[0], speed[1] + new_speed[1])