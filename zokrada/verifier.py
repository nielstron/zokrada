from zokrada.pairing import *


def verify(verifying_key: VerifyingKey, input: List[int], proof: Proof) -> bool:
    snark_scalar_field = (
        21888242871839275222246405745257275088548364400416034343698204186575808495617
    )
    vk = verifying_key
    assert len(input) + 1 == len(
        verifying_key.gamma_abc
    ), "Length of verifying key and input are incompatible"
    # Compute the linear comnbination vk_x
    vk_x = vk.gamma_abc[0]
    for k in range(len(input)):
        j = vk.gamma_abc[k+1]
        i = input[k]
        assert i < snark_scalar_field, "Input value too large"
        mul_res: G1Point = pairing_scalar_mul(j, i)
        vk_x: G1Point = pairing_addition(vk_x, mul_res)
    # assert is_on_curve((FQ(vk_x.x), FQ(vk_x.y)), b)
    return pairing_prod_4(
        proof.a,
        proof.b,
        pairing_negate(vk_x),
        vk.gamma,
        pairing_negate(proof.c),
        vk.delta,
        pairing_negate(vk.alpha),
        vk.beta,
    )


# the cardano validator for zokrada zksnarks onchain verifier is a parameterized script
def validator(
    verifying_key: VerifyingKey,
    input_length: int,
    input: List[int],
    proof: Proof,
    context: ScriptContext,
) -> None:
    assert len(input) == input_length, "Length of input must be " + str(input_length)
    assert verify(verifying_key, input, proof), "Proof could not be verified"
