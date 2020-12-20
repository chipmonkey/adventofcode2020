import itertools
import re
import time

from collections import Counter
import builtins as __builtin__

DEBUG = False

def print(*args, **kwargs):
    if DEBUG:
        return __builtin__.print(*args, **kwargs)
    else:
        return 0

class data:

    def __init__(self, filename):
        self.rules = {}
        self.text = []
        f = open(filename, 'r')
        # row = 0
        for row, line in enumerate(f):
            # print(f"parsing line {row}: {line}")
            if re.match(r'\d+\:', line):
                thing = line.strip()
                stuff = thing.split(': ')
                self.rules[stuff[0]] = stuff[1] # .replace('"', '')
            elif re.match(r'\w+', line):
                self.text.append(line.strip())
        print(f"rules: {self.rules}")
        print(f"text: {self.text}")
        print(f"----")
        # print(f"input: {self.lines} with {len(self.lines)} rows")
        # self.replaceEmAll()

    def recurse(self, ruleID, line, myDepth = 0):
        rule = self.rules[ruleID]
        remaining = []
        print(f"recursing into rule: '{rule}' for text: {line} at depth: {myDepth}")
        if len(rule) == 3:  # Atomic i.e. "a"
            if not line:
                return []
            if line[0] == rule[1]:  # If we match the first character, pop the rest of the line off
                return [line[1:]]
            return []
        for myRule in rule.split('|'):
            alt_remaining = [line]
            print(f"alt_remaining: {alt_remaining}")
            for part in myRule.split():
                print(f"part: {part}")
                alt_remaining = [new_chars for mychars in alt_remaining for new_chars in self.recurse(part, mychars, myDepth + 1)]
                if not alt_remaining:
                    break
            remaining += alt_remaining
        return remaining

    def _replaceRules(self, oldStr, newStr):
        print(f"replacing {oldStr} with {newStr}")
        for ruleId, ruleText in self.rules.items():
            # Surely there's a better way than these four rules... should have tokenized
            if re.match(rf'^{oldStr}$', ruleText) or \
                re.search(rf'^{oldStr} ', ruleText) or \
                re.search(rf' {oldStr}$', ruleText) or \
                re.search(rf' {oldStr} ', ruleText):
                print(f"{ruleText} matched {oldStr}")
                self.rules[ruleId] = self.rules[ruleId].replace(oldStr, newStr)
            else:
                print(f"{ruleText} does not match {oldStr}")
    
    def replaceEmAll(self):
        """ Try to simplify rules from the bottom of the tree upwards
        i.e. 8: "a" and 10: 8 9 becomes just 10: b 9
        """
        iSaySo = True
        while iSaySo:
            iSaySo = False
            rulesCopy = {k: v for k, v in self.rules.items()}
            for ruleID, ruleText in rulesCopy.items():
                print(f"rule[{ruleID}]: {ruleText}")
                if re.match(r'^[abx ]+$', ruleText):
                    print(f"ab matched {ruleText}")
                    # All letters
                    self._replaceRules(str(ruleID), ruleText)
                    del self.rules[ruleID]
                    iSaySo = True
                
                if re.match(r'^a \| b$', ruleText) or \
                    re.match(r'^b \| a$', ruleText):
                    print(f"x marks the spot for {ruleID}: {ruleText}")
                    self._replaceRules(str(ruleID), 'x')
                    del self.rules[ruleID]
                    iSayso = True


class machine:

    def __init__(self, filename):
        self.data = data(filename)

        # Comment out these two lines for Part 1
        self.data.rules['8'] = '42 | 42 8'
        self.data.rules['11'] = '42 31 | 42 11 31'
    
    def runProgram(self):
        test = self.data.recurse('0', self.data.text[0])
        print(f'test: {test}')
        total = sum(1 for line in self.data.text if '' in self.data.recurse('0', line))
        return total
        # total = sum([self._checkRuleI(x, 0) for x in self.data.text])
        # return total

    def _checkRuleText(self, line, ruleText):
        print(f"hello")


    def _checkRuleI(self, line, i):
        print(f"Checking rule {i} against {line}")
        rule = self.data.rules[i]
        ruleText = rule.split(': ')[1]
        print(f'rule text: {ruleText}')

        if ('|') in ruleText:
            subRules = ruleText.split(' | ')
            lValue = self._checkRuleText(line, subRules[0])
            rValue = self._checkRuleText(line, subRules[1])
            if lValue or rValue:
                return True
            else:
                return False

        if ('"') in ruleText:
            value = ruleText.replace('"', '')
            value = value.replace(' ', '')
            if line == value:
                return True, value[1:]
            else:
                return False, ''
        
        numberedRules = ruleText.split(' ')
        rValue = True
        remainingText = ruleText
        ruleIndex = 0
        while ruleText != '' and rValue:
            rValue, remainingText = self._checkRuleI(remainingText, numberedRules[ruleIndex])
        print(f"numbered Rules: {numberedRules}")

        exit("Unhandled path")


# input = data('testinput.txt')
# print("-----------------")

myMachine = machine('testinput.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")

# myMachine = machine('testinput2.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")

myMachine = machine('input.txt')
finalState = myMachine.runProgram()
__builtin__.print(f"Final State: {finalState}")
