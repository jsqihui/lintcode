class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here

        for i in range(len(string)):
            if string[i] == " ":
                string = string[:i] + ["%", "2". "0"] + string[i+1:]
        
        return len(string)

