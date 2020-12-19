import itertools
import re
import time

from collections import Counter

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
                self.rules[stuff[0]] = stuff[1].replace('"', '')
            elif re.match(r'\w+', line):
                self.text.append(line.strip())
        print(f"rules: {self.rules}")
        print(f"text: {self.text}")
        # print(f"input: {self.lines} with {len(self.lines)} rows")
        self.replaceEmAll()

    def _replaceRules(self, oldStr, newStr):
        print(f"replacing {oldStr} with {newStr}")
        for ruleId, ruleText in self.rules.items():
            if re.match(rf'^{oldStr}$', ruleText) or \
                re.search(rf'^{oldStr} ', ruleText) or \
                re.search(rf' {oldStr}$', ruleText) or \
                re.search(rf' {oldStr} ', ruleText):
                print(f"{ruleText} matched {oldStr}")
                self.rules[ruleId] = self.rules[ruleId].replace(oldStr, newStr)
            else:
                print(f"{ruleText} does not match {oldStr}")
    
    def replaceEmAll(self):
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
    
    def runProgram(self):
        total = sum([self._checkRuleI(x, 0) for x in self.data.text])
        return total

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


input = data('testinput.txt')
print("-----------------")

# myMachine = machine('testinput.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")

# myMachine = machine('testinput2.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")

myMachine = machine('input.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")