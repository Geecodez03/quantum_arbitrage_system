# Quantum-secure random generator
import quantumrandom


class QuantumRNG:
    def __init__(self):
        self.cache = []

    def get_random(self) -> float:
        """Fetch from ANU quantum random number generator"""
        try:
            return (
                quantumrandom.random()
            )  # Generate a quantum random float in range [0, 1]
        except AttributeError:
            raise RuntimeError(
                "quantumrandom module does not have a 'random' attribute."
            )
