import array

class Vector(object):
    
    MAX_DISPLAY = 5

    def __init__(self, data):
        self._data = array.ArrayType('d', data)
    
    def __len__(self):
        return len(self._data)

    def __getitem__(self, position):
        print(position)
        return self._data[position]

    def __repr__(self):
        if len(self._data) < self.MAX_DISPLAY:
            data_str = str(self._data.tolist())
        else:
            data_str = (str(self._data[:self.MAX_DISPLAY].tolist())[: -1] 
                            + ', ...]')
        return 'Vector(%s)' % data_str
