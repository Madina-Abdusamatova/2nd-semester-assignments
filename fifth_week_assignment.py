from abc import ABC, abstractmethod
class Rule(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def test(self, value):
        pass
    
    def evaluate(self, value):
        if self.test(value):
            print(f"[PASS] {self.name}: {value}")
            return True
        print(f"[FAIL] {self.name}: {value}")
        return False
    
class MinLengthRule(Rule):
    def __init__(self, min_len):
        super().__init__(f"MinLength({min_len})")
        self.min_len = min_len

    def test(self, value):
        return len(value) >= self.min_len
    
class HasUppercaseRule(Rule):
    def __init__(self):
        super().__init__("HasUppercase")

    def test(self, value):
        for c in value:
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
               return True
        return False

class HasSpecialCharRule(Rule):
    def __init__(self):
        super().__init__("HasSpecialChar")

    def test(self, value):
        for c in value:
            if c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                return True
        return False

class NoRepeatingCharsRule:
    def __init__(self):
        self.name = "NoRepeatingChars"

    def test(self, value):
        for i in range(len(value)-1):
            if value[i] == value[i+1]:
                return False
        return True
        
    def evaluate(self, value):
        if self.test(value):
            print(f"[PASS] {self.name}: {value}")
            return True
        print(f"[FAIL] {self.name}: {value}")
        return False
    
class StrengthReport:
    def __init__(self):
        self.entries = []

    def add(self, rule_name, value, passed):
        self.entries.append((rule_name, value, passed))

    def summary(self):
        total = len(self.entries)
        passed_count = 0
        for _, _, p in self.entries:
            if p:
                passed_count = passed_count+1
        failed = total - passed_count
        print(f"Total: {total}, Passed: {passed_count}, Failed: {failed}") 
    
class PasswordField:
    def __init__(self, field_name):
        self.field_name = field_name
        self.rules = []
        self.report = StrengthReport()

    def add_rule(self, rule):
        self.rules.append(rule)

    def check(self, value):
        print(f'Checking {self.field_name}: "{value}"')
        all_passed = True
        for rule in self.rules:
            passed = rule.evaluate(value)
            self.report.add(rule.name, value, passed)
            if not passed:
                all_passed = False
        return all_passed
    
    def show_report(self):
        print(f"--- Report for {self.field_name} ---")
        self.report.summary
       
password_field = PasswordField('password')
password_field.add_rule(MinLengthRule(8))
password_field.add_rule(HasUppercaseRule())
password_field.add_rule(HasSpecialCharRule())
password_field.add_rule(NoRepeatingCharsRule())

valid1 = password_field.check('Str0ng!Pw')
print(f'Valid: {valid1}')
print()

valid2 = password_field.check('short')
print(f'Valid: {valid2}')
print()

valid3 = password_field.check('aabbccdd!!')
print(f'Valid: {valid3}')
print()

password_field.show_report()

try:
    r = Rule('test')
except TypeError:
    print('Cannot instantiate abstract class')
           



    