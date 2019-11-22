'''
功能：人民币 美元 汇率兑换
4.0 将汇率兑换功能封装成函数
'''


def main():
    # 汇率
    USD_VS_CNY = 6.77

    # 带单位的货币输入
    currency_str_value = input('请输入带单位的货币金额: ')

    # 获取货币单位
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        # 如果输入的是人民币
        exchange_rate = 1 / USD_VS_CNY

    elif unit == 'USD':
        exchange_rate = USD_VS_CNY

    else:
        exchange_rate = -1


    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])

        # 使用lambda定义函数
        convert_currency2 = lambda x, y: x * y
        # 调用函数
        out_money = convert_currency2(in_money,exchange_rate)
        print('兑换后的货币值： ', out_money)
    else:
        print('不支持改种货币')


if __name__ == '__main__':
    main()
