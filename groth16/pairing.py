from groth16.classes import *

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


def pairing_addition(p1: G1Point, p2: G1Point) -> G1Point:
    """
    the sum of two points of G1
    """
    # TODO black magic addition
    return G1Point(0, 0)


def pairing_scalar_mul(p: G1Point, s: int) -> G1Point:
    """
    returns the product of a point p on G1 and a scalar s, i.e.
    p == p.scalar_mul(1) and p.addition(p) == p.scalar_mul(2) for all points p.
    """
    # TODO black magic scalar mul
    return G1Point(0, 0)


def pairing_pairing(p1: List[G1Point], p2: List[G2Point]) -> bool:
    """
    return the result of computing the pairing check
    e(p1[0], p2[0]) *  .... * e(p1[n], p2[n]) == 1
    For example pairing([P1(), P1().negate()], [P2(), P2()]) should
    return true.
    """
    # TODO black magic pairing check
    return False


def pairing_prod_2(a1: G1Point, a2: G2Point, b1: G1Point, b2: G2Point) -> bool:
    """
    Convenience method for a pairing check of two pairs
    """
    return pairing_pairing([a1, b1], [a2, b2])


def pairing_prod_3(
    a1: G1Point, a2: G2Point, b1: G1Point, b2: G2Point, c1: G1Point, c2: G2Point
) -> bool:
    """
    Convenience method for a pairing check of three pairs
    """
    return pairing_pairing([a1, b1, c1], [a2, b2, c2])


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
    return pairing_pairing([a1, b1, c1, d1], [a2, b2, c2, d2])
