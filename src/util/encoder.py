import numpy as np
import json

CHAR_SET = {"idx_to_char": {"1": " ", "2": "!", "3": "\"", "4": "#", "5": "$", "6": "%", "7": "&", "8": "'", "9": "(","10": ")", "11": "*", "12": "+", "13": ",", "14": "-", "15": ".", "16": "/", "17": "0", "18": "1", "19": "2", "20": "3", "21": "4", "22": "5", "23": "6", "24": "7", "25": "8", "26": "9", "27": ":", "28": ";", "29": "=", "30": "?", "31": "A", "32": "B", "33": "C", "34": "D", "35": "E", "36": "F", "37": "G", "38": "H", "39": "I", "40": "J", "41": "K", "42": "L", "43": "M", "44": "N", "45": "O", "46": "P", "47": "Q", "48": "R", "49": "S", "50": "T", "51": "U", "52": "V", "53": "W", "54": "X", "55": "Y", "56": "Z", "57": "[", "58": "]", "59": "_", "60": "`", "61": "a", "62": "b", "63": "c", "64": "d", "65": "e", "66": "f", "67": "g", "68": "h", "69": "i", "70": "j", "71": "k", "72": "l", "73": "m", "74": "n", "75": "o", "76": "p", "77": "q", "78": "r", "79": "s", "80": "t", "81": "u", "82": "v", "83": "w", "84": "x", "85": "y", "86": "z", "87": "|", "88": "~", "89": "\u00a3", "90": "\u00a7", "91": "\u00a8", "92": "\u00ab", "93": "\u00ac", "94": "\u00ad", "95": "\u00b0", "96": "\u00b2", "97": "\u00b4", "98": "\u00b7", "99": "\u00ba", "100": "\u00bb", "101": "\u00bc", "102": "\u00bd", "103": "\u00be", "104": "\u00c0", "105": "\u00c2", "106": "\u00c4", "107": "\u00c7", "108": "\u00c8", "109": "\u00c9", "110": "\u00ca", "111": "\u00d4", "112": "\u00d6", "113": "\u00dc", "114": "\u00df", "115": "\u00e0", "116": "\u00e1", "117": "\u00e2", "118": "\u00e4", "119": "\u00e6", "120": "\u00e7", "121": "\u00e8", "122": "\u00e9", "123": "\u00ea", "124": "\u00eb", "125": "\u00ec", "126": "\u00ee", "127": "\u00ef", "128": "\u00f1", "129": "\u00f2", "130": "\u00f3", "131": "\u00f4", "132": "\u00f6", "133": "\u00f8", "134": "\u00f9", "135": "\u00fa", "136": "\u00fb", "137": "\u00fc", "138": "\u00ff", "139": "\u0142", "140": "\u0152", "141": "\u0153", "142": "\u0393", "143": "\u0396", "144": "\u03a4", "145": "\u03ac", "146": "\u03ae", "147": "\u03b1", "148": "\u03b4", "149": "\u03b5", "150": "\u03b7", "151": "\u03b9", "152": "\u03ba", "153": "\u03bb", "154": "\u03bc", "155": "\u03bd", "156": "\u03be", "157": "\u03bf", "158": "\u03c0", "159": "\u03c1", "160": "\u03c4", "161": "\u03c5", "162": "\u03c7", "163": "\u03c8", "164": "\u03c9", "165": "\u03cc", "166": "\u03ce", "167": "\u0406", "168": "\u2012", "169": "\u2013", "170": "\u2014", "171": "\u2020", "172": "\u2021", "173": "\u2030", "174": "\u2039", "175": "\u203a", "176": "\u2082", "177": "\u20a4", "178": "\u2114", "179": "\u2153", "180": "\u2154", "181": "\u2155", "182": "\u2156", "183": "\u2157", "184": "\u2158", "185": "\u2159", "186": "\u215a", "187": "\u215b", "188": "\u2206", "189": "\u2207", "190": "\u222b", "191": "\u2260", "192": "\u25a1", "193": "\u2640", "194": "\u2642", "195": "\u2713", "196": "\uff46"},
            "char_to_idx": {"\u203a": 175, "\u2014": 170, "\u25a1": 192, " ": 1, "\u00a3": 89, "$": 5, "\u00a7": 90, "(": 9, "\u00ab": 92, "\u2206": 188, ",": 13, "\u03b1": 147, "0": 17, "\u03b5": 149, "4": 21, "\u00b7": 98, "\u03b9": 151, "8": 25, "\u00bb": 100, "\u03bd": 155, "\u03c1": 159, "\u2640": 193, "\u0142": 139, "\u03c5": 161, "D": 34, "\u00c7": 107, "\u2260": 191, "\u03c9": 164, "H": 38, "L": 42, "P": 46, "\u0152": 140, "T": 50, "\u2156": 182, "X": 54, "\u215a": 186, "\u00df": 114, "`": 60, "d": 64, "\u00e7": 120, "h": 68, "\u00eb": 124, "l": 72, "\u00ef": 127, "p": 76, "\u00f3": 130, "t": 80, "x": 84, "\u00fb": 136, "|": 87, "\u00ff": 138, "\u2207": 189, "\u2153": 179, "\u2013": 169, "\u0396": 143, "#": 4, "\u20a4": 177, "'": 8, "\u00a8": 91, "+": 12, "\u00ac": 93, "/": 16, "\u03ae": 146, "\u00b0": 95, "3": 20, "\u00b4": 97, "7": 24, ";": 28, "\u03ba": 152, "\u00bc": 101, "?": 30, "\u03be": 156, "\u00c0": 104, "C": 33, "\u00c4": 106, "G": 37, "\u2020": 171, "\u00c8": 108, "K": 41, "O": 45, "\u03ce": 166, "S": 49, "\u2155": 181, "\u00d4": 111, "W": 53, "\u2159": 185, "[": 57, "\u00dc": 113, "_": 59, "\u00e0": 115, "c": 63, "\u00e4": 118, "g": 67, "\u00e8": 121, "k": 71, "\u00ec": 125, "o": 75, "s": 79, "\u00f4": 131, "w": 83, "\u00f8": 133, "\u2021": 172, "\u00fc": 137, "\u2030": 173, "\u0406": 167, "\u0393": 142, "\u2012": 168, "\u2114": 178, "\"": 3, "&": 7, "*": 11, "\u00ad": 94, ".": 15, "2": 19, "\u03b7": 150, "6": 23, "\u03bb": 153, ":": 27, "\u00bd": 102, "\u03bf": 157, "B": 32, "\u03c7": 162, "F": 36, "\u00c9": 109, "J": 40, "N": 44, "R": 48, "\u2154": 180, "V": 52, "\u2158": 184, "Z": 56, "\u00e1": 116, "b": 62, "\u2039": 174, "f": 66, "\u00e9": 122, "j": 70, "n": 74, "\u00f1": 128, "r": 78, "v": 82, "\u00f9": 134, "z": 86, "~": 88, "\u2082": 176, "\u2713": 195, "\u2642": 194, "!": 2, "%": 6, "\u03a4": 144, ")": 10, "\uff46": 196, "-": 14, "\u03ac": 145, "1": 18, "\u00b2": 96, "5": 22, "\u03b4": 148, "9": 26, "\u00ba": 99, "=": 29, "\u03bc": 154, "\u00be": 103, "A": 31, "\u03c0": 158, "\u00c2": 105, "E": 35, "\u03c4": 160, "I": 39, "\u03c8": 163, "\u00ca": 110, "M": 43, "\u03cc": 165, "Q": 47, "\u0153": 141, "U": 51, "\u2157": 183, "\u00d6": 112, "Y": 55, "\u215b": 187, "]": 58, "a": 61, "\u00e2": 117, "e": 65, "\u00e6": 119, "i": 69, "\u00ea": 123, "m": 73, "\u00ee": 126, "q": 77, "\u00f2": 129, "u": 81, "\u00f6": 132, "y": 85, "\u00fa": 135, "\u222b": 190}
            }


class Encoder:
    """
    Encoder

    Responsible for mapping characters to indices and indices to characters. This mapping
    is necessary to get labels into a format that can be used in the TensorFlow model.
    """

    def __init__(self, char_set_path=None, max_sequence_size=128, blank_character=0):
        """
        Accepts a json file with the corresponding character set. The json file
        should eventually map to python dictionaries, idx_to_char and char_to_idx.
        These will be used to encode/decode characters and indices.

        :param char_set_path: The filepath to the char_set file. Must be in format: {'idx_to_char: {"1": " ", "2": "!", ... }, "char_to_idx": {" ": "1", "!": "2"}}
        :param max_sequence_size: The maximum length of a line
        :param blank_character: The blank character index
        """

        if char_set_path is not None:
            with open(char_set_path) as file:
                self.char_set = json.load(file)
        else:
            self.char_set = CHAR_SET

        self.max_sequence_size = max_sequence_size
        self.blank_character = blank_character

    @staticmethod
    def remove_duplicates(idxs):
        """
        When we do decoding, our index tensor will have repeating characters.
        With best-path decoding, we remove the repeating elements. If a word
        actually contains repeating characters, there should be a blank in-between.

        :param idxs:
        :return:
        """
        new_idxs = []

        for i in range(len(idxs)):
            # Only append if the next character in the sequence is not
            # identical to the current character. If we're at the end of
            # the sequence, add it.
            if i + 1 == len(idxs) or idxs[i] != idxs[i + 1]:
                new_idxs.append(idxs[i])

        return new_idxs

    def idx_to_char(self, idx):
        """
        Convert an index to a character

        :param idx: A single integer index representing a character
        :return: A single character
        """
        if idx == self.blank_character:
            return ''  # Return empty string for the blank character
        else:
            return self.char_set['idx_to_char'][str(int(idx))]

    def char_to_idx(self, char):
        """
        Convert a character to an index

        :param char: A single character
        :return: A single integer index representing the character
        """
        return int(self.char_set['char_to_idx'][char])

    def str_to_idxs(self, string):
        """
        Convert a string to a list of indices

        :param string: The label string
        :return: The label as a list of indices
        """
        idxs = []

        zeros = np.full(self.max_sequence_size, self.blank_character)
        for char in string:
            idxs.append(self.char_to_idx(char))

        # Pad the array to the max sequence size
        idxs = np.concatenate((idxs, zeros))[:self.max_sequence_size]

        return idxs

    def idxs_to_str(self, idxs, remove_duplicates=True):
        """
        Convert a list of indices to a string

        :param idxs: The label as indices
        :param remove_duplicates: T/F - Whether or not repeating characters should be removed.
                                  This can be helpful if decoding the target label value and
                                  blank characters have not been introduced.
        :return: The label as a string
        """
        string = ''

        if remove_duplicates:
            idxs = Encoder.remove_duplicates(idxs)

        for idx in idxs:
            string += self.idx_to_char(idx)

        return string

    def str_to_idxs_batch(self, batch):
        """
        Convert a list of strings to a list of indices

        :param batch: The list of strings
        :return: A list of lists of indices
        """
        idxs = []

        for string in batch:
            idx = self.str_to_idxs(string)
            idxs.append(idx)

        return idxs

    def idxs_to_str_batch(self, batch, remove_duplicates=True):
        """
        Convert a list of indices to a list of strings

        :param batch: The list of lists of indices
        :param remove_duplicates: T/F - Whether or not repeating characters should be removed
        :return: A list of strings
        """
        strings = []

        for idxs in batch:
            strings.append(self.idxs_to_str(idxs, remove_duplicates=remove_duplicates))

        return strings
