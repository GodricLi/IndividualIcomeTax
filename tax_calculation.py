# coding=utf-8


def calculator(salary):
    """
    税后工资计算器:2019年新税率个人所得税计算器，各地区五险一金比例有差异
    """
    point = 5000
    yanglao_rate = 0.08
    hospital_rate = 0.02
    unemployment_rate = 0.005
    housing_money_rate = 0.12
    five_one_money = salary * (yanglao_rate + hospital_rate + unemployment_rate + housing_money_rate)
    housing_money = salary * housing_money_rate
    rest_money = salary - five_one_money - point
    res_money = salary - five_one_money
    if rest_money <= 0:
        tax_money = 0
        rest_money -= tax_money
    elif rest_money <= 1500:
        tax_money = rest_money * 0.03
        res_money -= tax_money
    elif 1500 < rest_money <= 4500:
        tax_money = rest_money * 0.1
        res_money -= (tax_money - 105)
    elif 4500 < rest_money <= 9000:
        tax_money = rest_money * 0.2
        res_money -= (tax_money - 555)
    elif 9000 < rest_money <= 35000:
        tax_money = rest_money * 0.25
        res_money -= (tax_money - 1005)
    elif 35000 < rest_money <= 55000:
        tax_money = rest_money * 0.3
        res_money -= (tax_money - 2755)
    elif 55000 < rest_money <= 80000:
        tax_money = rest_money * 0.35
        res_money -= (tax_money - 5505)
    else:
        tax_money = rest_money * 0.45
        res_money -= (tax_money - 13505)
    print('税前工资为：{0},税后工资为：{1},五险一金：{2},缴税：{3},住房公积金：{4}'.format(salary, res_money, five_one_money,
                                                                 tax_money, housing_money))


if __name__ == '__main__':
    # calculator(one_salary)
    salary_list = [7000, 8000, 10000, 14000, 15000, 16000, 18000, 25000, 80000, 100000]
    for one_salary in salary_list:
        calculator(one_salary)
