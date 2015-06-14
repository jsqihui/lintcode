class Solution:
    # @param {string[]} tokens The Reverse Polish Notation
    # @return {int} the value
    def evalRPN(self, tokens):
        # Write your code here
        # use stack
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                ret = self.eval(t, num2, num1)
                stack.append(ret)
        return int(stack[0])
        
    def eval(self, op, num1, num2):
        if op == "+":
            return num1 + num2
        elif op == "*":
            return num1 * num2
        elif op == "-":
            return num1 - num2
        elif op == "/":
            return int((1.0 * num1) / num2)
        else:
            return None

