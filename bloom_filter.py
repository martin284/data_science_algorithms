import ctypes

class BloomFilter():
    def __init__(self, filter_array_length, allowed_data):
        self.filter_array_length = filter_array_length
        self.allowed_data = allowed_data
        self.filter_array = self.create_filter_array()

    def hash_function(self, element, filter_array_length):
        return ctypes.c_size_t(hash(element)).value % filter_array_length

    def create_filter_array(self):
        filter_array = self.filter_array_length * [0]
        for id in self.allowed_data:
            hash_value = self.hash_function(id, self.filter_array_length)
            filter_array[hash_value] = 1
        return filter_array

    def check_element(self, element):
        hash_index = self.hash_function(element, self.filter_array_length)
        if self.filter_array[hash_index] == 1:
             return True
        return False
