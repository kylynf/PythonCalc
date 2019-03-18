from graphics import *
import math

class Stack:
    def __init__(self):
        self.mStack = []

    def push(self, operator):
        self.mStack.append(operator)

    #pop removes at index
    def pop(self):
        return self.mStack.pop()

    def isEmpty(self):
        if len(self.mStack) == 0:
            return True
        return False

    def top(self):
        return self.mStack[-1]

def insertExpression():
    print("Please think of the expression that you would like to calculate. ")
    print("A valid expression consists of single digit integers, the variable x,")
    print("and the operators: + (plus), - (minus), * (multiply), / (divide), ( (open parentheses) and ) (close parentheses).")
    infixExpression = input("Please input your expression now: ")
    return infixExpression

def InfixToPostfix(infixExpression):
    stackList = Stack()
    postfix = ""
    for c in infixExpression:
        if c in "0123456789x":
            postfix += c
        elif c in "+-":
            while not stackList.isEmpty() and stackList.top() in "+-/*":
                postfix += stackList.pop()
            stackList.push(c)
        elif c in "*/":
            while not stackList.isEmpty() and stackList.top() in "/*":
                postfix += stackList.pop()
            stackList.push(c)
        elif c == "(":
            stackList.push(c)
        elif c == ")":
            while not stackList.isEmpty() and stackList.top() != "(":
                postfix += stackList.pop()
            stackList.pop()
        else:
            print("Unexpected Character ", c)
    while not stackList.isEmpty():
        postfix += stackList.pop()
    return postfix

def EvaluatePostfix(postfixExpression, x):
    stackList = Stack()
    right = 0
    left = 0
    answer = 0
    for k in postfixExpression:
        if k in "0123456789":
            stackList.push(k)
        if k == "+":
            right = float(stackList.pop())
            left = float(stackList.pop())
            answer = left + right
            stackList.push(answer)
        elif k == "-":
            right = float(stackList.pop())
            left = float(stackList.pop())
            answer = left - right
            stackList.push(answer)
        elif k == "*":
            right = float(stackList.pop())
            left = float(stackList.pop())
            answer = left * right
            stackList.push(answer)
        elif k == "/":
            right = float(stackList.pop())
            left = float(stackList.pop())
            answer = left / right
            stackList.push(answer)
        elif k == "x":
            stackList.push(float(x))
    final = stackList.pop()
    return final


def main():
    expression = insertExpression()
    postfix = InfixToPostfix(expression)
    win = GraphWin("My Circle", 500, 500)
    XLOW = -10.0
    XHIGH = +10.0
    YLOW = -10.0
    YHIGH = +10.0
    win.setCoords(XLOW, YLOW, XHIGH, YHIGH)

    # Store the curve points in xpoints and ypoints
    xpoints = []
    ypoints = []
    x = -10.0
    while x < 11:
        y = EvaluatePostfix(postfix, x)
        xpoints.append(x)
        ypoints.append(y)
        x += .1

    # Draw the curve
    for i in range(len(xpoints)-1):
        p1 = Point(xpoints[i], ypoints[i])
        p2 = Point(xpoints[i+1], ypoints[i+1])
        line = Line(p1, p2)
        line.setOutline("blue")
        line.setWidth(3)
        line.draw(win)

    # Draw Axes
    line = Line(Point(XLOW, (YLOW+YHIGH)//2), Point(XHIGH,(YLOW+YHIGH)//2 ))
    line.setOutline("red")
    line.draw(win)
    line = Line(Point( (XLOW+XHIGH)//2, YLOW), Point( (XLOW+XHIGH)//2, YHIGH) )
    line.setOutline("red")
    line.draw(win)


    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
