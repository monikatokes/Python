countries = [('Belgium', 'F', '2018', 22.2), ('Bulgaria', 'F', '2018', 0), ('Czechia', 'F', '2018', 13.6),
                 ('Denmark', 'F', '2017', 35.6), ('Germany', 'F', '2017', 15.9), ('Greece', 'F', '2017', 43.2),
                 ('Spain', 'F', '2017', 25.5), ('France', 'F', '2017', 16.6), ('Italy', 'F', '2017', 13.4),
                 ('Hungary', 'F', '2017', 5.9), ('Poland', 'F', '2017', 0), ('Netherlands', 'F', '2017', 22.5),
                 ('Portugal', 'F', '2017', 19.1), ('Romania', 'F', '2017', 1.3), ('Slovenia', 'F', '2017', 15.4),
                 ('Sweden', 'F', '2017', 24.8), ('Finland', 'F', '2017', 26.3), ('Norway', 'F', '2017', 36.3),
                 ('Switzerland', 'F', '2017', 28.9), ('United Kingdom', 'F', '2017', 39),
                 ('Belgium', 'M', '2017', 26.8), ('Bulgaria', 'M', '2017', 0.75), ('Czechia', 'M', '2017', 23.9),
                 ('Denmark', 'M', '2017', 17.2), ('Germany', 'M', '2017', 16.2), ('Greece', 'M', '2017', 55.6),
                 ('Spain', 'M', '2017', 17.5), ('France', 'M', '2017', 16.5), ('Italy', 'M', '2017', 15.8),
                 ('Hungary', 'M', '2017', 21.2), ('Netherlands', 'M', '2017', 27.4)]


def group_data_by_name_year():
    country_by_name_2017 = {
        country: [sex, health_index]
        for (country, sex, year, health_index) in countries
        if year == '2017'
    }
    print(country_by_name_2017)
    print(country_by_name_2017.__len__())

    country_by_name_2018 = {
        country: [sex, health_index]
        for (country, sex, year, health_index) in countries
        if year == '2018'
    }
    print(country_by_name_2018)
    print(country_by_name_2018.__len__())


def group_data_germany():
    group_germany = {
        year: [sex, health_index]
        for (country, sex, year, health_index) in countries
        if country == 'Germany'
    }
    print(group_germany)
    print(len(group_germany))


def group_data_country_year():
    group_country_year = {
        country + '_' + year: [year, sex, health_index]
        for (country, sex, year, health_index) in countries
    }
    print(group_country_year)
    print(len(group_country_year))

    group_country_year_5 = {k: v for k, v in group_country_year.items() if v[2] > 5}
    print(group_country_year_5)
    print(len(group_country_year_5))

    group_country_year_5_f = {a: group_country_year_5.get(a) for a in group_country_year_5.keys() if group_country_year_5.get(a)[1] == 'F'}
    print(group_country_year_5_f)
    print(len(group_country_year_5_f))


def sets_operations():
    a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    b= {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

    c = a.union(b)
    print(c)

    c = a.intersection(b)
    print(c)

    c = a.difference(b)
    print(c)

    c = a.symmetric_difference(b)
    print(c)


if __name__ == '__main__':
    group_data_by_name_year()
    group_data_germany()
    group_data_country_year()
    sets_operations()
