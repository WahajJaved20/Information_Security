
# References:
# https://github.com/francisrstokes/githublog/blob/main/2022/6/15/rolling-your-own-crypto-aes.md
# https://csrc.nist.gov/files/pubs/fips/197/final/docs/fips-197.pdf (THE MAIN REFERENCE)
# MISSION ACCOMPLISHED, WE DID IT FINALLY AES ENCRYPTION AND DECRYPTION
# MADE BY WAHAJ JAVED (20K-0208)

import secrets

# Key Size to Rcon Values
keySizeToRconValues = {
    128: ["01000000","02000000","04000000","08000000","10000000","20000000","40000000","80000000","1B000000","36000000","6C000000","D8000000"],
    192: ["01000000","02000000","04000000","08000000","10000000","20000000","40000000","80000000","1B000000","36000000","6C000000"],
    256:["01000000","02000000","04000000","08000000","10000000","20000000","40000000","80000000"]
}

# Key Size to Number of Rounds
keySizeToRounds = {
    128: 10,
    192: 12,
    256: 14
}

# S-Box 
substitutionBox = [
    ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
    ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
    ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
    ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
    ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
    ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],
    ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
    ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
    ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
    ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
    ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
    ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
    ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
    ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],
    ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],
    ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
]

# Inverse S-Box
inverseSubstitutionBox = [
    ["52", "09", "6A", "D5", "30", "36", "A5", "38", "BF", "40", "A3", "9E", "81", "F3","D7", "FB"],
    ["7C", "E3", "39", "82", "9B", "2F", "FF", "87", "34", "8E", "43", "44", "C4", "DE","E9", "CB"],
    ["54", "7B", "94", "32", "A6", "C2", "23", "3D", "EE", "4C", "95", "0B", "42", "FA","C3", "4E"],
    ["08", "2E", "A1", "66", "28", "D9", "24", "B2", "76", "5B", "A2", "49", "6D", "8B","D1", "25"],
    ["72", "F8", "F6", "64", "86", "68", "98", "16", "D4", "A4", "5C", "CC", "5D", "65","B6", "92"],
    ["6C", "70", "48", "50", "FD", "ED", "B9", "DA", "5E", "15", "46", "57", "A7", "8D","9D", "84"],
    ["90", "D8", "AB", "00", "8C", "BC", "D3", "0A", "F7", "E4", "58", "05", "B8", "B3","45", "06"],
    ["D0", "2C", "1E", "8F", "CA", "3F", "0F", "02", "C1", "AF", "BD", "03", "01", "13","8A", "6B"],
    ["3A", "91", "11", "41", "4F", "67", "DC", "EA", "97", "F2", "CF", "CE", "F0", "B4","E6", "73"],
    ["96", "AC", "74", "22", "E7", "AD", "35", "85", "E2", "F9", "37", "E8", "1C", "75","DF", "6E"],
    ["47", "F1", "1A", "71", "1D", "29", "C5", "89", "6F", "B7", "62", "0E", "AA", "18","BE", "1B"],
    ["FC", "56", "3E", "4B", "C6", "D2", "79", "20", "9A", "DB", "C0", "FE", "78", "CD","5A", "F4"],
    ["1F", "DD", "A8", "33", "88", "07", "C7", "31", "B1", "12", "10", "59", "27", "80","EC", "5F"],
    ["60", "51", "7F", "A9", "19", "B5", "4A", "0D", "2D", "E5", "7A", "9F", "93", "C9","9C", "EF"],
    ["A0", "E0", "3B", "4D", "AE", "2A", "F5", "B0", "C8", "EB", "BB", "3C", "83", "53","99", "61"],
    ["17", "2B", "04", "7E", "BA", "77", "D6", "26", "E1", "69", "14", "63", "55", "21","0C", "7D"]
]

# Multiply in GF(2^8) for polynomials
def multiplyInGF(a, b):
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        high_bit_set = a & 0x80  # Check if the high bit of 'a' is set
        a <<= 1
        if high_bit_set:
            a ^= 0x1B  # XOR with 0x1B (the irreducible polynomial in AES)
        b >>= 1
    return result

class AES:
    def __init__(self,plainText, keySize, rounds):
        self.plainText = plainText
        self.key = ""
        self.keySize = keySize
        self.rounds = rounds

    # Convert Plain Text to Hex Representation
    def convertPlainTextToHex(self):
        utf8Bytes = self.plainText.encode('utf-8')
        hexRepresentation = utf8Bytes.hex()
        return hexRepresentation

    # Generate Random Hex Key based on the input Key Size
    def generateHexKey(self):
        byteArray = secrets.token_bytes(self.keySize // 8)
        hexKey = byteArray.hex()
        return hexKey

    # Divide Hex Plain Text into Blocks of 128 bits
    def divideIntoBlocks(self, hexPlainText):
        paddingLength = (32 - len(hexPlainText) % 32) % 32
        paddedHexPlaintext = hexPlainText + '0' * paddingLength
        blocks = [paddedHexPlaintext[i:i + 32] for i in range(0, len(paddedHexPlaintext), 32)]
        return blocks

    # Generate Helper Variables
    # Hex Plain Text -> Call the above hexToPlainText function
    # Hex Key -> Call the above generateHexKey function
    # Blocks -> Call the above divideIntoBlocks function
    def generateHelperVariables(self):
        self.hexPlainText = self.convertPlainTextToHex()
        print("[+] Hex Representation of Plain Text: ", self.hexPlainText)
        self.key = self.generateHexKey()
        print("[+] Hex Representation of Key: ", self.key)
        self.blocks = self.divideIntoBlocks(self.hexPlainText)
        print("[+] Number of Blocks: ", len(self.blocks))

    # Rotate Words for Key expansion
    def rotateWords(self, word):
        # since we are rotating 32-bit (4 byte) word 8 bits to the left.
        # we set the numBits to 8
        numBits = 8
        wordInt = int(word, 16)
        rotatedInt = ((wordInt << numBits) & 0xFFFFFFFF) | (wordInt >> (32 - numBits))
        rotatedHex = format(rotatedInt, '08X')
        return  rotatedHex

    # the function substitutes a word using the S-Box
    def substituteBytes(self, state):
        result = ""
        for i in range(0,len(state),2):
            firstChar = state[i]
            secondChar = state[i+1]
            # firstly convert the hex characters to integers for the S-Box indexing
            integer1 = int(firstChar, base=16)
            integer2 = int(secondChar, base=16)
            result += substitutionBox[integer1][integer2]
        return result

    # the function substitutes a word using the inverse S-Box
    def inverseSubstituteBytes(self, state):
        result = ""
        for i in range(0,len(state),2):
            firstChar = state[i]
            secondChar = state[i+1]
            integer1 = int(firstChar, base=16)
            integer2 = int(secondChar, base=16)
            result += inverseSubstitutionBox[integer1][integer2]
        return result

    # the function xors two words since two strings cant be xored, we first convert
    # them into integers, xor them and convert them back to hex
    def xorWords(self, word1, word2):
        integer1 = int(word1, base=16)
        integer2 = int(word2, base=16)
        xoredInteger = integer1 ^ integer2
        resultHex = hex(xoredInteger)
        # take the string starting from second index to remove the 0x
        resultHex = str(resultHex)[2:]
        # if the xor results in a hex string of length less than 8 for round keys, we pad it with 0s
        if len(resultHex) <= 8:
            resultHex = "0"*(8-len(resultHex)) + resultHex
        # if the xor results in a hex string of length less than 32 for the cipher text, we pad it with 0s
        elif len(resultHex) < 32:
            resultHex = "0"*(32-len(resultHex)) + resultHex
        return resultHex

    # The Key Expansion schedule that generates the round keys
    def keyExpansion(self, key, rounds, keySize):
        roundKeys = []
        # how many words are in the key
        keySizeInWords = keySize // 32
        i = 0
        position = 0
        # the first round key is the key itself
        while i < keySizeInWords:
            roundKeys.append(key[position:position+8])
            i += 1
            position += 8
        # the rest of the round keys are generated from the previous round key
        rcon = keySizeToRconValues[keySize]
        while i < 4*(rounds+1):
            temp = roundKeys[i-1]
            if i % keySizeInWords == 0:
                temp = self.xorWords(self.substituteBytes(self.rotateWords(temp)),rcon[i//keySizeInWords-1])
            elif(keySizeInWords > 6 and i % keySizeInWords == 4):
                temp = self.substituteBytes(temp)
            result = self.xorWords(roundKeys[i-keySizeInWords],temp)
            roundKeys.append(result)
            i += 1
        print("[+] Number of Round Keys: ", len(roundKeys))
        return roundKeys

    # the function merges the round keys into one string so a 128 bit out of 4 32-bit words is generated
    def mergeKeys(self, roundKeys):
        mergedKey = ""
        for key in roundKeys:
            mergedKey += key
        return mergedKey

    # the function shifts the rows the number of times specified by the row number
    def shiftRows(self, hexWord):
        # firstly, we convert the hex string into a 4x4 matrix state in a column major order
        textIndex = 0
        state = [[0 for x in range(4)] for y in range(4)]
        for col in range(4):
            for row in range(4):
                state[row][col] = hexWord[textIndex:textIndex+2]
                textIndex += 2
        # then we perform the shifting
        for row in range(1, 4):
            numShifts = row
            state[row] = state[row][numShifts:] + state[row][:numShifts]
        result = ""
        # finally take the column major order back into a string
        for col in range(4):
            for row in range(4):
                result += state[row][col]
        return result
    
    # the function inversly shifts the rows the number of times specified by the row number
    def inverseShiftRows(self, hexWord):
        # firstly, we convert the hex string into a 4x4 matrix state in a column major order
        textIndex = 0
        state = [[0 for x in range(4)] for y in range(4)]
        for col in range(4):
            for row in range(4):
                state[row][col] = hexWord[textIndex:textIndex+2]
                textIndex += 2
        # then we perform the shifting
        for row in range(1, 4):
            numShifts = 4 - row
            state[row] = state[row][numShifts:] + state[row][:numShifts]
        result = ""
        # finally take the column major order back into a string
        for col in range(4):
            for row in range(4):
                result += state[row][col]
        return result

    # the function mixes the columns for the sake of diffusion
    def mixColumns(self, hexWord):
        # firstly, we convert the hex string into a 4x4 matrix state in a column major order
        textIndex = 0
        state = [[0 for x in range(4)] for y in range(4)]
        for col in range(4):
            for row in range(4):
                state[row][col] = (int(hexWord[textIndex:textIndex+2], base=16))
                textIndex += 2
        result = ""
        newState= []
        # then we perform the mixing using the polynomial multiplication in GF(2^8)
        for row in range(4):
            temp = [0, 0, 0, 0]
            column = [state[0][row], state[1][row], state[2][row], state[3][row]]
            temp[0] = hex(multiplyInGF(2, column[0]) ^ multiplyInGF(3, column[1]) ^ column[2] ^ column[3])
            temp[1] = hex(column[0] ^ multiplyInGF(2, column[1]) ^ multiplyInGF(3, column[2]) ^ column[3])
            temp[2] = hex(column[0] ^ column[1] ^ multiplyInGF(2, column[2]) ^ multiplyInGF(3, column[3]))
            temp[3] = hex(multiplyInGF(3, column[0]) ^ column[1] ^ column[2] ^ multiplyInGF(2, column[3]))
            newState.append(temp)
        # finally take the column major order back into a string
        for row in range(4):
            for col in range(4):
                temp = str(newState[row][col])
                if len(temp) == 3:
                    result += "0" + temp[len(temp)-1:]
                else:
                    result += temp[len(temp)-2:]
        return result

    # the function inversly mixes the columns for the sake of resolving the diffusion
    def inverseMixColumns(self, hexWord):
        # firstly, we convert the hex string into a 4x4 matrix state in a column major order
        textIndex = 0
        state = [[0 for x in range(4)] for y in range(4)]
        for col in range(4):
            for row in range(4):
                state[row][col] = (int(hexWord[textIndex:textIndex+2], base=16))
                textIndex += 2
        result = ""
        newState= []
        # then we perform the inverse mixing using the polynomial multiplication in GF(2^8)
        for row in range(4):
            temp = [0, 0, 0, 0]
            column = [state[0][row], state[1][row], state[2][row], state[3][row]]
            temp[0] = hex(multiplyInGF(0x0E, column[0]) ^ multiplyInGF(0x0B, column[1]) ^ multiplyInGF(0x0D, column[2]) ^ multiplyInGF(0x09, column[3]))
            temp[1] = hex(multiplyInGF(0x09, column[0]) ^ multiplyInGF(0x0E, column[1]) ^ multiplyInGF(0x0B, column[2]) ^ multiplyInGF(0x0D, column[3]))
            temp[2] = hex(multiplyInGF(0x0D, column[0]) ^ multiplyInGF(0x09, column[1]) ^ multiplyInGF(0x0E, column[2]) ^ multiplyInGF(0x0B, column[3]))
            temp[3] = hex(multiplyInGF(0x0B, column[0]) ^ multiplyInGF(0x0D, column[1]) ^ multiplyInGF(0x09, column[2]) ^ multiplyInGF(0x0E, column[3]))
            newState.append(temp)
        # finally take the column major order back into a string
        for row in range(4):
            for col in range(4):
                temp = str(newState[row][col])
                if len(temp) == 3:
                    result += "0" + temp[len(temp)-1:]
                else:
                    result += temp[len(temp)-2:]
        return result

    # the function merges the blocks into one string as a final step towards creating cipher/plain text
    def mergeBlocks(self, blocks):
        joinedBlocks = ""
        for block in blocks:
            joinedBlocks += block
        return joinedBlocks

    # the function encrypts the plain text using AES-128/192/256
    def encrypt(self):
        print("[+] Encrypting... ")
        # generate the helper variables i.e: hex plain text, hex key, blocks
        self.generateHelperVariables()
        # generate the round keys
        roundKeys = self.keyExpansion(self.key, self.rounds, self.keySize)
        # for each block, perform the encryption
        for j in range(0,len(self.blocks)):
            # the first round key is xored with the plaintext
            plaintext = self.blocks[j]
            mergedKey = self.mergeKeys(roundKeys[0:4])
            ciphertext = self.xorWords(plaintext, mergedKey)
            # for the intermediate rounds, we perform the following steps
            for i in range(1, self.rounds):
                # substitute bytes
                ciphertext = self.substituteBytes(ciphertext)
                # shift rows
                ciphertext = self.shiftRows(ciphertext)
                # mix columns
                ciphertext = self.mixColumns(ciphertext)
                # xor the round key
                mergedKey = self.mergeKeys(roundKeys[4*i:4*i+4])
                ciphertext = self.xorWords(ciphertext, mergedKey)
            # for the last round, we perform the following steps
            # substitute bytes
            ciphertext = self.substituteBytes(ciphertext)
            # shift rows
            ciphertext = self.shiftRows(ciphertext)
            # xor the round key
            mergedKey = self.mergeKeys(roundKeys[len(roundKeys)-4:])
            ciphertext = self.xorWords(ciphertext, mergedKey)
            # the encrypted block is stored back in the blocks array
            self.blocks[j] = ciphertext
        # the cipher text is generated by merging the blocks
        cipherText = self.mergeBlocks(self.blocks)
        print("[+] Cipher Text: ",cipherText)
        return cipherText

    def decrypt(self, ciphertext):
        print("[+] Decrypting... ")
        # divide the cipher text into blocks
        cipherBlocks = self.divideIntoBlocks(ciphertext)
        # generate the round keys
        roundKeys =  self.keyExpansion(self.key, self.rounds, self.keySize)
        # for each block, perform the decryption
        for j in range(0,len(cipherBlocks)):
            ciphertext = cipherBlocks[j]
            # for the first round, we perform the following steps
            # xor the round key
            mergedKey =  self.mergeKeys(roundKeys[len(roundKeys)-4:])
            plainText =  self.xorWords(ciphertext, mergedKey)
            # for the intermediate rounds, we perform the following steps
            for round in range(self.rounds-1, 0, -1):
                # inverse shift rows
                plainText =  self.inverseShiftRows(plainText)
                # inverse substitute bytes
                plainText =  self.inverseSubstituteBytes(plainText)
                # xor the round key
                mergedKey =  self.mergeKeys(roundKeys[4*round:4*round+4])
                plainText =  self.xorWords(plainText, mergedKey)
                # inverse mix columns
                plainText =  self.inverseMixColumns(plainText)
            # for the last round, we perform the following steps
            # inverse shift rows
            plainText =  self.inverseShiftRows(plainText)
            # inverse substitute bytes
            plainText =  self.inverseSubstituteBytes(plainText)
            # xor the round key
            mergedKey =  self.mergeKeys(roundKeys[0:4])
            plainText =  self.xorWords(plainText, mergedKey)
            # the decrypted block is stored back in the blocks array
            cipherBlocks[j] = plainText
        # the plain text is generated by merging the blocks
        plainText = self.mergeBlocks(cipherBlocks)
        # convert the hex plain text to ascii
        bytesObject = bytes.fromhex(plainText)
        plainText = bytesObject.decode("ASCII")
        print("[+] Plaintext: ", plainText)

def main():
    print("[+] AES encryption")
    print("[+] Made by Wahaj Javed (20K-0208)")
    plainText = input("[+] Enter plaintext: ")
    keySize = int(input("[+] Enter Key Size (128, 192, 256): "))
    if(keySize not in keySizeToRounds):
        print("Invalid Key Size... ")
        print("[-] Using Default Key Size (256)")
        keySize = 256
    aes = AES(plainText, keySize, keySizeToRounds[keySize])
    cipherText = aes.encrypt()
    aes.decrypt(cipherText)

if __name__ == "__main__":
    main()
