import hashlib


class HashFinder:
    def __init__(self, secret_key, hash_prefix):
        self.secret_key = secret_key
        self.hash_prefix = hash_prefix

    def compute_hash(self, number):
        md5 = hashlib.md5()
        encoded_str = (self.secret_key + str(number)).encode("utf-8")
        md5.update(encoded_str)
        return md5.hexdigest()

    def has_valid_hash(self, number):
        hash = self.compute_hash(number)
        return hash.startswith(self.hash_prefix)

    def find_lowest_number_with_valid_hash(self):
        number = 0
        while not self.has_valid_hash(number):
            number += 1
        return number


if __name__ == "__main__":
    hash_finder = HashFinder("yzbqklnj", "00000")
    five_zeros_hash = hash_finder.find_lowest_number_with_valid_hash()
    print("five zeros hash: {}".format(five_zeros_hash))

    six_zeros_hash = HashFinder(
        "yzbqklnj", "000000"
    ).find_lowest_number_with_valid_hash()
    print("six zeros hash: {}".format(six_zeros_hash))
