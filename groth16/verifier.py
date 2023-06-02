from groth16.classes import *


def verify(verifying_key: VerifyingKey, input: List[int], proof: Proof) -> bool:
    snark_scalar_field = (
        21888242871839275222246405745257275088548364400416034343698204186575808495617
    )
    vk = verifying_key


# the cardano validator for groth16 zksnarks onchain verifier is a parameterized script
def validator(verifying_key: VerifyingKey, input_length: int, proof: Proof, input: List[int], context: ScriptContext) -> None:
    assert len(input) == input_length, "Length of input must be " + str(input_length)
    assert verify(verifying_key, input, proof), "Proof could not be verified"
