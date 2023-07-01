from zokrada.classes import *
from opshin.bridge import wraps_builtin

@wraps_builtin
def bn256_add(x: Anything, y: Anything) -> Anything:
    pass


@wraps_builtin
def bn256_mul(x: Anything, y: int) -> Anything:
    pass


@wraps_builtin
def bn128_pairing(x: List[Anything], y: List[Anything]) -> bool:
    pass

# Generator of G1
P1 = G1Point(1, 2)
# Generator of G2
P2 = G2Point(
    10857046999023057135944570762232829481370756359578518086990519993285655852781,
    11559732032986387107991004021392285783925812861821192530917403151452391805634,
    8495653923123431417604973247489272438418190587263600148770280649306958101930,
    4082367875863433681332203403145435568316851327593401208105741076214120093531,
)

# prime q in the base field F_q for G1
q = 21888242871839275222246405745257275088696311157297823662689037894645226208583


def pairing_negate(p: G1Point) -> G1Point:
    """
    Negation of p i.e. addition(p, negation(p)) == 0
    """
    if p.x == 0 and p.y == 0:
        return G1Point(0, 0)
    return G1Point(p.x, q - (p.y % q))

pairing_check = bn128_pairing
pairing_addition = bn256_add
pairing_scalar_mul = bn256_mul

def pairing_prod_2(a1: G1Point, a2: G2Point, b1: G1Point, b2: G2Point) -> bool:
    """
    Convenience method for a pairing check of two pairs
    """
    return pairing_check([a1, b1], [a2, b2])


def pairing_prod_3(
    a1: G1Point, a2: G2Point, b1: G1Point, b2: G2Point, c1: G1Point, c2: G2Point
) -> bool:
    """
    Convenience method for a pairing check of three pairs
    """
    return pairing_check([a1, b1, c1], [a2, b2, c2])


def pairing_prod_4(
    a1: G1Point,
    a2: G2Point,
    b1: G1Point,
    b2: G2Point,
    c1: G1Point,
    c2: G2Point,
    d1: G1Point,
    d2: G2Point,
) -> bool:
    """
    Convenience method for a pairing check of four pairs
    """
    return pairing_check([a1, b1, c1, d1], [a2, b2, c2, d2])
