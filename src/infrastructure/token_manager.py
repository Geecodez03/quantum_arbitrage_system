# JWT token service with HSM integration
import jwt
from cryptography.hazmat.primitives import serialization

class TokenManager:
    def __init__(self):
        self.hsm_key = self._load_hsm_key()
    
    def generate_token(self, payload: dict) -> str:
        """Create signed JWT token"""
        return jwt.encode(payload, self.hsm_key, algorithm="RS256")
