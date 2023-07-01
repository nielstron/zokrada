from zokrada.verification_key import verifying_key
from zokrada.verifier import validator
from zokrada.classes import Proof, G1Point, G2Point

print(
    validator(
        verifying_key,
        1,
        [0x000000000000000000000000000000000000000000000000000000000001bba1],
        Proof(
            a=G1Point(
                0x1c858cb03a0fcb232603a0c7904720569281f526db360c6fb824247b897b32d4,
                0x25e44239433a2d19637ed88a542aa38410575cc7695de5b59127b941f4a59da4,
            ),
            b=G2Point(
                0x21baff07c22b088ea45331440de0dea827e292930a5db29d5ab560b501ccce79,
                0x14a398c3c04e3bf81a816ad8936b5cc156f32e4a9cab08904ac506ef6a82b957,
                0x04c0616f2225e40dc3d344fc7016982ffdf505fa140d126cba9f6b981d3ab8f1,
                0x0d8c667ff78c80e252c25d3b31c27005b9b01fca505a801c18837b43575bcf46,
            ),
            c=G1Point(
                0x2469cd8d8ded3b16d166e7d829aad98cb8479a2d792d576e933661dd995971c1,
                0x1e6de4c64b9c9c460a6b8a03ff5ffc4ffb98c2a7cb15c2598be3ab358d71c426,
            ),
        ),
        None,
    )
)
