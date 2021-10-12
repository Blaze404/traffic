import math
class Network:

    def get_network(self):
        return {
                1: {
                    'in': {'left': [], 'right': [], 'straight': []},
                    'out': {'left': [25], 'right': [7], 'straight': [2]},
                    'distance': 3,
                    'capacity': 5
                },
                2: {
                    'in': {'left': [7], 'right': [25], 'straight': []},
                    'out': {'left': [26], 'right': [21], 'straight': [3]},
                    'distance': 8,
                    'capacity': 6
                },
                3: {
                    'in': {'left': [21], 'right': [26], 'straight': [2]},
                    'out': {'left': [27], 'right': [22], 'straight': [4]},
                    'distance': 5,
                    'capacity': 5
                },
                4: {
                    'in': {'left': [22], 'right': [27], 'straight': [3]},
                    'out': {'left': [33], 'right': [23], 'straight': [5]},
                    'distance': 5,
                    'capacity': 5
                },
                5: {
                    'in': {'left': [23], 'right': [33], 'straight': [4]},
                    'out': {'left': [34], 'right': [24], 'straight': [6]},
                    'distance': 3,
                    'capacity': 5
                },
                6: {
                    'in': {'left': [], 'right': [], 'straight': []},
                    'out': {'left': [], 'right': [], 'straight': []},
                    'distance': 1,
                    'capacity': 5
                },
                7: {
                    'out': {'left': [], 'right': [2], 'straight': [25]},
                    'in': {'left': [18], 'right': [], 'straight': [8]},
                    'distance': 3,
                    'capacity': 5
                },
                8: {
                    'out': {'left': [], 'right': [18], 'straight': [7]},
                    'in': {'left': [11], 'right': [], 'straight': [9]},
                    'distance': 3,
                    'capacity': 5
                },
                9: {
                    'out': {'left': [], 'right': [11], 'straight': [8]},
                    'in': {'left': [10], 'right': [], 'straight': []},
                    'distance': 1,
                    'capacity': 5
                },
                10: {
                    'in': {'left': [], 'right': [9], 'straight': []},
                    'out': {'left': [35], 'right': [], 'straight': []},
                    'distance': 21 + 3*20/math.floor(1200/30),
                    'capacity': 15
                },
                11: {
                    'in': {'left': [9], 'right': [8], 'straight': []},
                    'out': {'left': [15], 'right': [], 'straight': [12]},
                    'distance': 8,
                    'capacity': 8
                },
                12: {
                    'in': {'left': [], 'right': [15], 'straight': [11]},
                    'out': {'left': [16], 'right': [], 'straight': [13]},
                    'distance': 5,
                    'capacity': 5
                },
                13: {
                    'in': {'left': [], 'right': [16], 'straight': [12]},
                    'out': {'left': [17], 'right': [], 'straight': [14]},
                    'distance': 5,
                    'capacity': 5
                },
                14: {
                    'in': {'left': [], 'right': [17], 'straight': [13]},
                    'out': {'left': [24], 'right': [35], 'straight': []},
                    'distance': 3,
                    'capacity': 5
                },
                15: {
                    'in': {'left': [12], 'right': [11], 'straight': []},
                    'out': {'left': [18], 'right': [19], 'straight': [21]},
                    'distance': 3,
                    'capacity': 5
                },
                16: {
                    'in': {'left': [13], 'right': [12], 'straight': []},
                    'out': {'left': [19], 'right': [20], 'straight': [22]},
                    'distance': 3,
                    'capacity': 5
                },
                17: {
                    'in': {'left': [14], 'right': [13], 'straight': []},
                    'out': {'left': [20], 'right': [], 'straight': [23]},
                    'distance': 3,
                    'capacity': 5
                },
                18: {
                    'in': {'left': [8], 'right': [7], 'straight': []},
                    'out': {'left': [21], 'right': [15], 'straight': [19]},
                    'distance': 8,
                    'capacity': 8
                },
                19: {
                    'in': {'left': [15], 'right': [21], 'straight': [18]},
                    'out': {'left': [22], 'right': [16], 'straight': [20]},
                    'distance': 5,
                    'capacity': 5
                },
                20: {
                    'in': {'left': [16], 'right': [22], 'straight': [19]},
                    'out': {'left': [23], 'right': [17], 'straight': []},
                    'distance': 5,
                    'capacity': 5
                },
                21: {
                    'in': {'left': [19], 'right': [18], 'straight': [15]},
                    'out': {'left': [2], 'right': [3], 'straight': [26]},
                    'distance': 3,
                    'capacity': 5
                },
                22: {
                    'in': {'left': [20], 'right': [19], 'straight': [16]},
                    'out': {'left': [3], 'right': [4], 'straight': [27]},
                    'distance': 3,
                    'capacity': 5
                },
                23: {
                    'in': {'left': [], 'right': [20], 'straight': [17]},
                    'out': {'left': [4], 'right': [5], 'straight': [33]},
                    'distance': 3,
                    'capacity': 5
                },
                24: {
                    'in': {'left': [], 'right': [14], 'straight': [35]},
                    'out': {'left': [5], 'right': [6], 'straight': [34]},
                    'distance': 6 + 1*20/math.floor(1200/30),
                    'capacity': 6
                },
                25: {
                    'in': {'left': [2], 'right': [], 'straight': [7]},
                    'out': {'left': [], 'right': [28], 'straight': [30]},
                    'distance': 5,
                    'capacity': 5
                },
                26: {
                    'in': {'left': [3], 'right': [2], 'straight': [21]},
                    'out': {'left': [28], 'right': [29], 'straight': []},
                    'distance': 5,
                    'capacity': 5
                },
                27: {
                    'in': {'left': [4], 'right': [3], 'straight': [22]},
                    'out': {'left': [29], 'right': [], 'straight': []},
                    'distance': 5,
                    'capacity': 5
                },
                28: {
                    'in': {'left': [25], 'right': [30], 'straight': []},
                    'out': {'left': [], 'right': [26], 'straight': [29]},
                    'distance': 8,
                    'capacity': 8
                },
                29: {
                    'in': {'left': [26], 'right': [], 'straight': [28]},
                    'out': {'left': [], 'right': [27], 'straight': []},
                    'distance': 5,
                    'capacity': 5
                },
                30: {
                    'in': {'left': [28], 'right': [], 'straight': [25]},
                    'out': {'left': [], 'right': [31], 'straight': []},
                    'distance': 2,
                    'capacity': 5
                },
                31: {
                    'in': {'left': [30], 'right': [], 'straight': []},
                    'out': {'left': [], 'right': [33], 'straight': [32]},
                    'distance': 18 + 2*20/math.floor(1200/30),
                    'capacity': 20
                },
                32: {
                    'in': {'left': [33], 'right': [], 'straight': [31]},
                    'out': {'left': [], 'right': [34], 'straight': []},
                    'distance': 3,
                    'capacity': 5
                },
                33: {
                    'in': {'left': [5], 'right': [4], 'straight': [23]},
                    'out': {'left': [31], 'right': [32], 'straight': []},
                    'distance': 7 + 1*20/math.floor(1200/30),
                    'capacity': 7
                },
                34: {
                    'in': {'left': [6], 'right': [5], 'straight': [24]},
                    'out': {'left': [32], 'right': [], 'straight': []},
                    'distance': 7 + 1*20/math.floor(1200/30),
                    'capacity': 7
                },
                35: {
                    'in': {'left': [], 'right': [10], 'straight': []},
                    'out': {'left': [14], 'right': [], 'straight': [24]},
                    'distance': 1,
                    'capacity': 5
                },
            }
