class PDController:
    def __init__(self, kp = 0.15, kd = 0.6):
        # Keep gains on the instance so they can be tuned per controller.
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    def reset(self) -> None:
        # Each simulation starts with the specified e[-1] = 0.
        self.previous_error = 0.0

    def compute_action(self, reference, depth) -> float:
        error = reference - depth
        action = self.kp * error + self.kd * (error - self.previous_error)
        self.previous_error = error
        return action