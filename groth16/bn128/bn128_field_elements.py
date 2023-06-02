from opshin.prelude import *

# The prime modulus of the field
field_modulus = (
    21888242871839275222246405745257275088696311157297823662689037894645226208583
)
# See, it's prime!
# assert pow(2, field_modulus, field_modulus) == 2

# The modulus of the polynomial in this representation of FQ12
FQ12_modulus_coeffs = [82, 0, 0, 0, 0, 0, -18, 0, 0, 0, 0, 0]  # Implied + [1]

# Extended euclidean algorithm to find modular inverses for
# integers
def inv(a, n):
    if a == 0:
        return 0
    lm, hm = 1, 0
    low, high = a % n, n
    while low > 1:
        r = high // low
        nm, new = hm - lm * r, high - low * r
        lm, low, hm, high = nm, new, lm, low
    return lm % n


# A class for field elements in FQ. Wrap a number in this class,
# and it becomes a field element.
FQ = int


def fq_init(n: int) -> FQ:
    return n % field_modulus


def fq_add(self: FQ, other: FQ) -> FQ:
    return fq_init(self + other)


def fq_mul(self: FQ, other: FQ) -> FQ:
    return fq_init(self * other)


def fq_sub(self: FQ, other: FQ) -> FQ:
    return fq_init(self - other)


def fq_div(self: FQ, other: FQ) -> FQ:
    return fq_init(self * inv(other, field_modulus))


def fq_pow(self: FQ, other: FQ) -> FQ:
    if other == 0:
        return 1
    elif other == 1:
        return self
    elif other % 2 == 0:
        return fq_pow(fq_mul(self, self), fq_div(other, 2))
    else:
        return fq_mul(fq_pow(fq_mul(self, self), fq_div(other, 2)), self)


def fq_eq(self: FQ, other: FQ) -> bool:
    return self == other


def fq_ne(self: FQ, other: FQ) -> bool:
    return self != other


def fq_neg(self: FQ):
    return fq_init(-self)


def fq_one() -> FQ:
    return 1


def fq_zero() -> FQ:
    return 0


# Utility methods for polynomial math
def deg(p: List[int]) -> int:
    """
    degree of a polynomial
    """
    d = len(p) - 1
    while p[d] == 0 and d:
        d -= 1
    return d


def poly_rounded_div(a: List[int], b: List[int]) -> List[int]:
    # TODO implement with immutable list
    dega = deg(a)
    degb = deg(b)
    temp = [x for x in a]
    o = [0 for x in a]
    for i in reversed(range(dega - degb + 1)):
        o[i] += temp[degb + i] / b[degb]
        for c in range(degb + 1):
            temp[c + i] -= o[c]
    return o[: deg(o) + 1]


# A class for elements in polynomial extension fields
@dataclass
class FQP(PlutusData):
    coeffs: List[FQ]
    # The coefficients of the modulus, without the leading [1]
    modulus_coeffs: List[int]
    # The degree of the extension field
    degree: int


def fqp_add(self: FQP, other: FQP) -> FQP:
    return FQP(
        [fq_add(x, y) for x, y in zip(self.coeffs, other.coeffs)],
        self.modulus_coeffs,
        self.degree,
    )


def fqp_sub(self: FQP, other: FQP) -> FQP:
    return FQP(
        [x - y for x, y in zip(self.coeffs, other.coeffs)],
        self.modulus_coeffs,
        self.degree,
    )

    def __mul__(self, other):
        if isinstance(other, (FQ, int, long)):
            return self.__class__([c * other for c in self.coeffs])
        else:
            assert isinstance(other, self.__class__)
            b = [FQ(0) for i in range(self.degree * 2 - 1)]
            for i in range(self.degree):
                for j in range(self.degree):
                    b[i + j] += self.coeffs[i] * other.coeffs[j]
            while len(b) > self.degree:
                exp, top = len(b) - self.degree - 1, b.pop()
                for i in range(self.degree):
                    b[exp + i] -= top * FQ(self.modulus_coeffs[i])
            return self.__class__(b)

    def __rmul__(self, other):
        return self * other

    def __div__(self, other):
        if isinstance(other, (FQ, int, long)):
            return self.__class__([c / other for c in self.coeffs])
        else:
            assert isinstance(other, self.__class__)
            return self * other.inv()

    def __truediv__(self, other):
        return self.__div__(other)

    def __pow__(self, other):
        if other == 0:
            return self.__class__([1] + [0] * (self.degree - 1))
        elif other == 1:
            return self.__class__(self.coeffs)
        elif other % 2 == 0:
            return (self * self) ** (other // 2)
        else:
            return ((self * self) ** int(other // 2)) * self

    # Extended euclidean algorithm used to find the modular inverse
    def inv(self):
        lm, hm = [1] + [0] * self.degree, [0] * (self.degree + 1)
        low, high = self.coeffs + [0], self.modulus_coeffs + [1]
        while deg(low):
            r = poly_rounded_div(high, low)
            r += [0] * (self.degree + 1 - len(r))
            nm = [x for x in hm]
            new = [x for x in high]
            assert (
                len(lm)
                == len(hm)
                == len(low)
                == len(high)
                == len(nm)
                == len(new)
                == self.degree + 1
            )
            for i in range(self.degree + 1):
                for j in range(self.degree + 1 - i):
                    nm[i + j] -= lm[i] * r[j]
                    new[i + j] -= low[i] * r[j]
            lm, low, hm, high = nm, new, lm, low
        return self.__class__(lm[: self.degree]) / low[0]

    def __repr__(self):
        return repr(self.coeffs)

    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        for c1, c2 in zip(self.coeffs, other.coeffs):
            if c1 != c2:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        return self.__class__([-c for c in self.coeffs])

    @classmethod
    def one(cls):
        return cls([1] + [0] * (cls.degree - 1))

    @classmethod
    def zero(cls):
        return cls([0] * cls.degree)


# The quadratic extension field
class FQ2(FQP):
    def __init__(self, coeffs):
        self.coeffs = [FQ(c) for c in coeffs]
        self.modulus_coeffs = [1, 0]
        self.degree = 2
        self.__class__.degree = 2


# The 12th-degree extension field
class FQ12(FQP):
    def __init__(self, coeffs):
        self.coeffs = [FQ(c) for c in coeffs]
        self.modulus_coeffs = FQ12_modulus_coeffs
        self.degree = 12
        self.__class__.degree = 12
