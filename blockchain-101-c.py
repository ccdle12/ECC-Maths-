import pytest
import math
from pycoin.ecdsa import generator_secp256k1 as g
from binascii import hexlify


# Defining a Curve:
# p = Finite Field Prime Number
# G = Generator Point
# n = Number of Prime Number points in the group

# Bitcoin uses a curve called "secp256k1" - Standards for Efficient Cryptography
# 256 is the number of bits in the prime field
# n is close to p therefore most points on the curve in the group,
# therefore the are 2^256 possible secret keys

# Equation: y^2 = x^3 + 7
# Prime Field (p) = 2^256 - 2^32 - 977
# Base Point / Generator Point (G) = (79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
# 483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
# Order (n) = FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


# Checking points on curve
def is_point_on_ECC(point, p):
    x, y = unpack_point(point)

    return y ** 2 % p == (x ** 3 + 7) % p


def unpack_point(point):
    x = point[0]
    y = point[1]

    return x, y


def lazy_check_all_points_on_curve(public_keys, p):
    results = list(map(lambda x: is_point_on_ECC(x, p), public_keys))

    return results


# Generating Public Keys from Private Keys
def generate_public_key(secret):
    x, y = (secret * g).pair()

    return x, y


def lazy_generate_public_key(private_keys):
    public_keys = list(map(lambda x: generate_public_key(x), private_keys))

    return public_keys


# Getting compressed and uncompressed public keys
def get_uncompressed_public_key(point_public_key):
    x, y = unpack_point(point_public_key)

    x_formatted, y_formatted = format_x_y_points(x, y)

    uncompressed_public_key = "0x04" + x_formatted + y_formatted
    public_key = hex(int(uncompressed_public_key, 16))

    return public_key


def format_x_y_points(x, y):
    return format(x, 'x'), format(y, 'x')


def get_compressed_public_key(point_public_key):
    x, y = unpack_point(point_public_key)

    x_formatted, y_formatted = format_x_y_points(x, y)

    last_hex_value = int(y_formatted[-1:], 16)

    if last_hex_value % 2 == 0:
        compressed_public_key = "0x02" + x_formatted
    else:
        compressed_public_key = "0x03" + x_formatted

    public_key = hex(int(compressed_public_key, 16))

    return public_key


# # Getting original y value from compressed public key
def get_uncompressed_x_from_compressed_key(compressed_public_key):
    return int(compressed_public_key[3::], 16)

def get_uncompressed_y_from_compressed_key(compressed_public_key, p):
    uncompressed_x = get_uncompressed_x_from_compressed_key(compressed_public_key)

    x_side_of_equation = (uncompressed_x**3 + 7) % p
    print(x_side_of_equation)
    uncompressed_y = math.sqrt(x_side_of_equation) % p
    print(uncompressed_y)

    return uncompressed_y

secret = 123
pub_key = generate_public_key(secret)
print(pub_key)
x = pub_key[0]
y = pub_key[1]
p = 2 ** 256 - 2 ** 32 - 977

print("x: {0}".format(x))
print("y: {0}".format(y))

y_in_bitcoin_equation = (y**2) % p
x_in_bitcoin_equation = (x**3 + 7) % p
print("y in bitcoin equation: {0}".format(y_in_bitcoin_equation))
print("x in bitcoin equation: {0}".format(x_in_bitcoin_equation))

reverse_y_in_equation = math.sqrt(y_in_bitcoin_equation)
print("Reversed in equation: {0}".format(reverse_y_in_equation))

compressed_key = get_compressed_public_key(pub_key)
print(compressed_key)




class TestClass:
    def test_is_point_on_ECC(self):
        expected = True
        x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
        point = (x, y)
        p = 2 ** 256 - 2 ** 32 - 977
        result = is_point_on_ECC(point, p)

        assert expected == result

    # This test is failing
    def test_generate_public_key(self):
        expected = (0x5CBDF0646E5DB4EAA398F365F2EA7A0E3D419B7E0330E39CE92BDDEDCAC4F9BC,
                    0x6AEBCA40BA255960A3178D6D861A54DBA813D0B813FDE7B5A5082628087264DA)
        secret = 7
        result = generate_public_key(secret)

        assert expected == result

    def test_lazy_test_of_public_key_gen(self):
        expected = [(0x5CBDF0646E5DB4EAA398F365F2EA7A0E3D419B7E0330E39CE92BDDEDCAC4F9BC,
                     0x6AEBCA40BA255960A3178D6D861A54DBA813D0B813FDE7B5A5082628087264DA),
                    (0xC982196A7466FBBBB0E27A940B6AF926C1A74D5AD07128C82824A11B5398AFDA,
                     0x7A91F9EAE64438AFB9CE6448A1C133DB2D8FB9254E4546B6F001637D50901F55),
                    (0x8F68B9D2F63B5F339239C1AD981F162EE88C5678723EA3351B7B444C9EC4C0DA,
                     0x662A9F2DBA063986DE1D90C2B6BE215DBBEA2CFE95510BFDF23CBF79501FFF82),
                    (0x9577FF57C8234558F293DF502CA4F09CBC65A6572C842B39B366F21717945116,
                     0x10B49C67FA9365AD7B90DAB070BE339A1DAF9052373EC30FFAE4F72D5E66D053)]

        private_keys = [7, 1485, 2 ** 128, 2 ** 240 + 2 ** 31]

        result = lazy_generate_public_key(private_keys)

        assert expected == result

    def test_is_points_on_curve(self):
        expected = True
        point = (0x5CBDF0646E5DB4EAA398F365F2EA7A0E3D419B7E0330E39CE92BDDEDCAC4F9BC,
                 0x6AEBCA40BA255960A3178D6D861A54DBA813D0B813FDE7B5A5082628087264DA)
        p = 2 ** 256 - 2 ** 32 - 977
        result = is_point_on_ECC(point, p)

        assert expected == result

    def test_lazy_all_points_on_curve(self):
        expected = [True, True, True, True]
        private_keys = [7, 1485, 2 ** 128, 2 ** 240 + 2 ** 31]
        public_keys = lazy_generate_public_key(private_keys)
        p = 2 ** 256 - 2 ** 32 - 977

        result = lazy_check_all_points_on_curve(public_keys, p)

        assert expected == result

    # Finding the compressed and uncompressed keys
    def test_uncompressed_public_key(self):
        expected = hex(
            0x045CBDF0646E5DB4EAA398F365F2EA7A0E3D419B7E0330E39CE92BDDEDCAC4F9BC6AEBCA40BA255960A3178D6D861A54DBA813D0B813FDE7B5A5082628087264DA)
        point_public_key = 0x5CBDF0646E5DB4EAA398F365F2EA7A0E3D419B7E0330E39CE92BDDEDCAC4F9BC, 0x6AEBCA40BA255960A3178D6D861A54DBA813D0B813FDE7B5A5082628087264DA
        result = get_uncompressed_public_key(point_public_key)

        assert expected == result

    def test_uncompressed_public_key_with_secret_1(self):
        expected = hex(
            0x049D5CA49670CBE4C3BFA84C96A8C87DF086C6EA6A24BA6B809C9DE234496808D56FA15CC7F3D38CDA98DEE2419F415B7513DDE1301F8643CD9245AEA7F3F911F9)
        secret = 999 ** 3
        public_key = generate_public_key(secret)
        result = get_uncompressed_public_key(public_key)

        assert expected == result

    def test_compressed_public_key_with_secret_1(self):
        expected = hex(0x039D5CA49670CBE4C3BFA84C96A8C87DF086C6EA6A24BA6B809C9DE234496808D5)
        secret = 999 ** 3
        public_key = generate_public_key(secret)
        result = get_compressed_public_key(public_key)

        assert expected == result

    def test_uncompressed_public_key_with_secret_2(self):
        expected = hex(
            0x04A598A8030DA6D86C6BC7F2F5144EA549D28211EA58FAA70EBF4C1E665C1FE9B5204B5D6F84822C307E4B4A7140737AEC23FC63B65B35F86A10026DBD2D864E6B)
        secret = 123
        public_key = generate_public_key(secret)
        result = get_uncompressed_public_key(public_key)

        assert expected == result

    def test_compressed_public_key_with_secret_2(self):
        expected = hex(0x03A598A8030DA6D86C6BC7F2F5144EA549D28211EA58FAA70EBF4C1E665C1FE9B5)
        secret = 123
        public_key = generate_public_key(secret)
        result = get_compressed_public_key(public_key)

        assert expected == result

    def test_uncompressed_public_key_with_secret_3(self):
        expected = hex(
            0x04AEE2E7D843F7430097859E2BC603ABCC3274FF8169C1A469FEE0F20614066F8E21EC53F40EFAC47AC1C5211B2123527E0E9B57EDE790C4DA1E72C91FB7DA54A3)
        secret = 42424242
        public_key = generate_public_key(secret)
        result = get_uncompressed_public_key(public_key)

        assert expected == result

    def test_compressed_public_key_with_secret_3(self):
        expected = hex(0x03AEE2E7D843F7430097859E2BC603ABCC3274FF8169C1A469FEE0F20614066F8E)
        secret = 42424242
        public_key = generate_public_key(secret)
        print(public_key)
        result = get_compressed_public_key(public_key)
        print(result)

        assert expected == result

    def test_get_uncompressed_x_from_compressed_key(self):
        expected = 79103343224040496276989510793860639645068431043554805118507923535946530058126
        compressed_public_key = hex(0x03AEE2E7D843F7430097859E2BC603ABCC3274FF8169C1A469FEE0F20614066F8E)
        result = get_uncompressed_x_from_compressed_key(compressed_public_key)

        assert expected == result

    def test_get_uncompressed_x_from_compressed_key_2(self):
        expected = 74901340345789065325870760596348306623878342739272826068162779513906431781301
        compressed_public_key = hex(0x3a598a8030da6d86c6bc7f2f5144ea549d28211ea58faa70ebf4c1e665c1fe9b5)
        result = get_uncompressed_x_from_compressed_key(compressed_public_key)

        assert expected == result

    # def test_get_uncompressed_y_from_compressed_key_2(self):
    #     expected = 14607169553442007236852410049041684566594265431374316230317606814245957553771
    #     compressed_public_key = hex(0x3a598a8030da6d86c6bc7f2f5144ea549d28211ea58faa70ebf4c1e665c1fe9b5)
    #     p = 2 ** 256 - 2 ** 32 - 977
    #     result = get_uncompressed_y_from_compressed_key(compressed_public_key, p)
    #
    #     assert expected == result


    # def test_programming_blockchain_front_page_exercises(self):
    #