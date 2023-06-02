from opshin.prelude import *

@dataclass
class G1Point(PlutusData):
    x: int
    y: int

@dataclass
class G2Point(PlutusData):
    x1: int
    x2: int
    y1: int
    y2: int

@dataclass
class Proof(PlutusData):
    a: G1Point
    b: G2Point
    c: G1Point

def validator(proof: Proof, input: int, context: ScriptContext):
    pass