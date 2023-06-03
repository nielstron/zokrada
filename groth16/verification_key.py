from groth16.classes import *

# this corresponds to verification.key output of zokrates

"""
vk.alpha = Pairing.G1Point(uint256(0x0883dd2110a0acf58cc1032b3681e5f4386e84a30ec8a22160dfcd0e92bf1ea7), uint256(0x21197c06356e16c2406935b2b0ad57aed377297228aeef52d31bcf5c147dcd74));
vk.beta = Pairing.G2Point([uint256(0x29598a27d11a6807cc1b326874532df22260a655356a847f261f1e6e40073174), uint256(0x0df45eb59937a7dad714dc6022320664882cb69342db69c335cb742bb3d7a081)], [uint256(0x0e7e1a53834ec94ae0f7b4b7856d67e31aad61376e901c8f34fefae3c54063f4), uint256(0x2680e2d4722da50dabc025a3ac53288cd2711542cb05483f5608dd6662bd848b)]);
vk.gamma = Pairing.G2Point([uint256(0x23d4e43c0727ed061b8af8732fab673ae04ec2c1540ef5029e16d175721caf9e), uint256(0x1e3ea2ce2ae7a2c2367f4c3f6fd91dffaf192b51896b7336598589ab83dbdf13)], [uint256(0x27d24877409eaad596acb92b6606bcdc294b7ad1f23ac2a4ac201570a8646824), uint256(0x17907aa7e3f0c74c7eb446c97bd02333c14afc47de9a278a6db244e884989510)]);
vk.delta = Pairing.G2Point([uint256(0x1cb83f0b35793808cdca387c6ea3518d944355e099aa29b68d3e8b898538a26d), uint256(0x1b27613433af4e97e3ad31aa5e7c9cd266fd9641a5aebb89128e36c2e075dfd3)], [uint256(0x1d639afab7b7c8711b5256a4ed559f50dbef4ef4f8931ac001458aa7bc29b4c8), uint256(0x27cc92be78978d9b18820e275454fc2a707e8e239d7ab394d358001d7207a354)]);
vk.gamma_abc = new Pairing.G1Point[](2);
vk.gamma_abc[0] = Pairing.G1Point(uint256(0x0a05f8f76a5b2b1dc4d6536e75c88160830fb1c7409f50e2bc48d048aaf6696a), uint256(0x0c1c8c7815a6c62baa6639739b7e9f8e55057a3f4a9afcf1b07c42fe1bd465ff));
vk.gamma_abc[1] = Pairing.G1Point(uint256(0x1e360b79fc2d8dc4cd8fda1330002f646cde6ae6847149af13498951e22d66f0), uint256(0x280a602cab10fa27cc711c1e44131b522aac715ebc5d78acee1266bd9cb53205));
"""

verifying_key = VerifyingKey(
    G1Point(
        0x0883DD2110A0ACF58CC1032B3681E5F4386E84A30EC8A22160DFCD0E92BF1EA7,
        0x21197C06356E16C2406935B2B0AD57AED377297228AEEF52D31BCF5C147DCD74,
    ),
    G2Point(
        0x29598A27D11A6807CC1B326874532DF22260A655356A847F261F1E6E40073174,
        0x0DF45EB59937A7DAD714DC6022320664882CB69342DB69C335CB742BB3D7A081,
        0x0E7E1A53834EC94AE0F7B4B7856D67E31AAD61376E901C8F34FEFAE3C54063F4,
        0x2680E2D4722DA50DABC025A3AC53288CD2711542CB05483F5608DD6662BD848B,
    ),
    G2Point(
        0x23D4E43C0727ED061B8AF8732FAB673AE04EC2C1540EF5029E16D175721CAF9E,
        0x1E3EA2CE2AE7A2C2367F4C3F6FD91DFFAF192B51896B7336598589AB83DBDF13,
        0x27D24877409EAAD596ACB92B6606BCDC294B7AD1F23AC2A4AC201570A8646824,
        0x17907AA7E3F0C74C7EB446C97BD02333C14AFC47DE9A278A6DB244E884989510,
    ),
    G2Point(
        0x1CB83F0B35793808CDCA387C6EA3518D944355E099AA29B68D3E8B898538A26D,
        0x1B27613433AF4E97E3AD31AA5E7C9CD266FD9641A5AEBB89128E36C2E075DFD3,
        0x1D639AFAB7B7C8711B5256A4ED559F50DBEF4EF4F8931AC001458AA7BC29B4C8,
        0x27CC92BE78978D9B18820E275454FC2A707E8E239D7AB394D358001D7207A354,
    ),
    [
        G1Point(
            0x0A05F8F76A5B2B1DC4D6536E75C88160830FB1C7409F50E2BC48D048AAF6696A,
            0x0C1C8C7815A6C62BAA6639739B7E9F8E55057A3F4A9AFCF1B07C42FE1BD465FF,
        ),
        G1Point(
            0x1E360B79FC2D8DC4CD8FDA1330002F646CDE6AE6847149AF13498951E22D66F0,
            0x280A602CAB10FA27CC711C1E44131B522AAC715EBC5D78ACEE1266BD9CB53205,
        ),
    ],
)

print(verifying_key.to_json())
