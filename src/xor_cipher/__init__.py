"""Simple, reusable and optimized XOR ciphers in Python."""

__description__ = "Simple, reusable and optimized XOR ciphers in Python."
__url__ = "https://github.com/GDPSApp/xor-cipher-python"

__title__ = "xor_cipher"
__author__ = "GDPS App"
__license__ = "MIT"
__version__ = "5.0.0"

from xor_cipher.python import cyclic_xor, cyclic_xor_in_place, xor, xor_in_place

__all__ = ("cyclic_xor", "cyclic_xor_in_place", "xor", "xor_in_place")

try:
    from xor_cipher.core import cyclic_xor, cyclic_xor_in_place, xor, xor_in_place

except ImportError:  # pragma: no cover
    pass
