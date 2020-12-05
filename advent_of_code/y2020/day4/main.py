import re


def year_parse(start, end):
    year_pattern = re.compile(r'^(\d{4})$')

    def valid_year(year_str):
        matches = year_pattern.match(year_str)
        if matches is None:
            return False
        year = int(matches[0])
        return (year >= start) and (year <= end)

    return valid_year


def height_parse():
    height_pattern = re.compile(r'^(\d*)(in|cm)$')

    def valid_height(height_str):
        matches = height_pattern.match(height_str)
        if matches is None:
            return False
        height, unit = matches.groups()
        height = int(height)

        if unit == 'in':
            return (height >= 59) and (height <= 76)
        elif unit == 'cm':
            return (height >= 150) and (height <= 193)
        else:
            return False

    return valid_height


def hair_parse():
    hair_pattern = re.compile(r'^(#[0-9a-f]{6})$')

    def valid_hair(hair_str):
        matches = hair_pattern.match(hair_str)
        return matches is not None

    return valid_hair


def eye_parse():
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def valid_eyes(eye_str):
        return eye_str in valid_eye_colors

    return valid_eyes


def pass_parse():
    pass_pattern = re.compile(r'^(\d{9})$')

    def valid_pass(pass_str):
        return pass_pattern.match(pass_str) is not None

    return valid_pass


PASSPORT_FIELDS = {'byr': {'field_name': 'Birth Year', 'parse': year_parse(1920, 2002)},
                   'iyr': {'field_name': 'Issue Year', 'parse': year_parse(2010, 2020)},
                   'eyr': {'field_name': 'Expiration Year', 'parse': year_parse(2020, 2030)},
                   'hgt': {'field_name': 'Height', 'parse': height_parse()},
                   'hcl': {'field_name': 'Hair Color', 'parse': hair_parse()},
                   'ecl': {'field_name': 'Eye Color', 'parse': eye_parse()},
                   'pid': {'field_name': 'Passport ID', 'parse': pass_parse()},
                   # 'cid': {'field_name': 'Country ID'},
                   }


def get_passports(input_data):
    return [ind.rstrip() for ind in input_data.split('\n\n')]


def parse_passport(passport):
    fields = {}
    for line in passport.split('\n'):
        for field in line.split(' '):
            key, value = field.split(':')
            fields[key] = value
    return fields


def passport_valid_fields(fields):
    return all([k in fields for k in PASSPORT_FIELDS.keys()])


def passport_valid(passport):
    if not passport_valid_fields(passport):
        return False

    for key, params in PASSPORT_FIELDS.items():
        parser = params['parse']
        if not parser(passport[key]):
            return False

    return True


def part1(input_data):
    passport_list = [parse_passport(passp) for passp in get_passports(input_data)]
    return sum([passport_valid_fields(passp) for passp in passport_list])


def part2(input_data):
    passport_list = [parse_passport(passp) for passp in get_passports(input_data)]
    return sum([passport_valid(passp) for passp in passport_list])


if __name__ == '__main__':
    with open('./advent_of_code/y2020/day4/input.txt') as f:
        input_data = f.read()

    print(f'Part 1: {part1(input_data)}')

    print(f'Part 2: {part2(input_data)}')
