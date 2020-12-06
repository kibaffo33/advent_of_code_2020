import data
from dataclasses import dataclass
import re


def load_passports():

    passport_batch = data.load_data("data/day04.txt")

    text_passports = passport_batch.split("\n\n")
    text_passports = list(map(lambda x: x.replace("\n", " "), text_passports))
    text_passports = list(map(lambda x: x.rstrip(), text_passports))

    passports = []

    for passport in text_passports:
        
        p = Passport()

        field_pairs = passport.split(" ")
        for pair in field_pairs:
            key, value = pair.split(":")
            setattr(p, key, value)
        
        passports.append(p)
    
    return passports


def validate_by_regex(value, pattern):
    try:
        match = re.fullmatch(pattern, value)
        return bool(match)
    except TypeError:
        return False

def validate_by_min_max(value, minimum, maximum):
    try:
        value = int(value)
        match = minimum <= value  and value <= maximum
        return match
    except TypeError:
        return False


@dataclass
class Passport:
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None

    def validate(self):
        validation = [            
            self.validate_required_fields(),
            self.validate_byr(),
            self.validate_iyr(),
            self.validate_eyr(),
            self.validate_hgt(),
            self.validate_hcl(),
            self.validate_ecl(),
            self.validate_pid(),
        ]
        return all(validation)

    def validate_required_fields(self):
        required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        required_fields_in_dict = list(map(lambda req_field: getattr(self, req_field) != None, required_fields))
        match = all(required_fields_in_dict)
        return match

    def validate_byr(self):
        value = self.byr
        validation = [
            validate_by_min_max(value, 1920, 2002), 
            validate_by_regex(value, r"\d{4}")
            ]
        return all(validation)

    def validate_iyr(self):
        value = self.iyr
        validation = [
            validate_by_min_max(value, 2010, 2020),
            validate_by_regex(value, r"\d{4}")
            ]
        return all(validation)

    def validate_eyr(self):
        value = self.eyr
        validation = [
            validate_by_min_max(value, 2020, 2030),
            validate_by_regex(value, r"\d{4}")
            ]
        return all(validation)
    
    def validate_hgt(self):
        value = str(self.hgt)
        match = re.fullmatch(r"(\d+)(cm|in)", value)
        if match:
            groups = match.groups()
            unit = groups[1]
            amount = groups[0]
            if unit == "cm":
                return validate_by_min_max(amount, 150, 193)
            elif unit == "in":
                return validate_by_min_max(amount, 59, 76)
            else:
                return False
        else:
            return False

    def validate_hcl(self):
        value = self.hcl
        validation = validate_by_regex(value, r"#[0-9A-Fa-f]{6}")
        return validation

    def validate_ecl(self):
        value = self.ecl
        validation = validate_by_regex(value, r"amb|blu|brn|gry|grn|hzl|oth")
        return validation

    def validate_pid(self):
        value = self.pid
        validation = validate_by_regex(value, r"\d{9}")
        return validation


def part_one():

    valid = 0
    invalid = 0

    passports = load_passports()
        
    for passport in passports:

        validated = passport.validate_required_fields()
        if validated:
            valid += 1
        else:
            invalid += 1

    print(f"Valid: {valid}")
    print(f"Invalid: {invalid}")

    return valid

def part_two():

    valid = 0
    invalid = 0

    passports = load_passports()
        
    for passport in passports:

        validated = passport.validate()
        if validated:
            valid += 1
        else:
            invalid += 1

    print(f"Valid: {valid}")
    print(f"Invalid: {invalid}")

    return valid


if __name__ == "__main__":

    print("==== Part 1 ====")
    part_one()

    print("==== Part 2 ====")
    part_two()

