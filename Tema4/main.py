from decimal import Decimal

def get_raw_data():
    description = ('Country', [
    '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ',
    '2019 '
    ])
    raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
    ]
    return description, raw_data


def prepare_dataset(desc, raw__data):
    final_dataset = dict()
    year_list = desc[1]

    for row in raw__data:
        country_code = row[0]
        coverage_list = row[1]

        coverages_year = list()
        for index in range(len(coverage_list)):
            coverage = coverage_list[index]
            year = year_list[index]
            if coverage != ": ":
                coverage = "".join([digit for digit in coverage if digit.isdigit()])

                coverages_year.append(
                    {
                        "year": year.strip(),
                        "coverage": int(coverage)
                    }
                )
        final_dataset[country_code] = coverages_year

    return final_dataset


def data_per_year(data, year):

    result_list = list()
    result_dict = dict()

    for key, values in data.items():
        for value in values:
            if value.get("year") == year:
                result_list.append((key, value.get("coverage")))

    result_dict[year] = result_list
    return result_dict


def data_per_country(data, country):

    result_list = list()
    result_dict = dict()

    country_rec = data.get(country)
    print(country_rec)
    for value in country_rec:
        result_list.append((value.get("year"), value.get("coverage")))

    result_dict[country] = result_list
    return result_dict


def average_data(data):
    coverage_sum = 0

    for key, values in data.items():
        for value in values:
            coverage_sum += value[1]

    return coverage_sum/len(values)


#Closures, Decorators
def uppercase(fnc):

    def wrapper(name):

        res = fnc(name)
        modified = res.upper()

        return modified
    return wrapper


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


def safe_divide(fnc):

    def wrapper(first, second):

        if second == 0:
            return "Division cannot be done"

        res = fnc(first, second)

        return res
    return wrapper


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


print_registry = []


def register(fnc):
    fnc.wrapped = True
    print_registry.append(fnc.__name__)
    return fnc


@register
def greet_second(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


def safe_addition(fnc):

    def wrapper(a, b):
        if a + b != Decimal(str(a)) + Decimal(str(b)):
            return "You will have floating point errors!"

    return wrapper


@safe_addition
def addition(a, b):
    return a + b


if __name__ == '__main__':
    description, raw_data = get_raw_data()
    prepared_data = prepare_dataset(description, raw_data)
    print(prepared_data)
    print(data_per_year(prepared_data, "2019"))
    data_prepared_by_country = data_per_country(prepared_data, "AT")
    print(data_prepared_by_country)
    print(average_data(data_prepared_by_country))
    print(greet("Monika"))
    print(divide(1, 3))
    print(addition(0.1, 0.2))
    print(say_goodbye("Julia"))
    print(print_registry)

