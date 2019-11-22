"""
    作者：lucky merry
    功能：计算BMR值
    日期：22／11／2019
    版本：v1.0
"""


def main():
    pass

    y_or_n = input('是否退出程序y/n:')

    while y_or_n != 'y':
        print('请输入一下信息，用空格分隔。')
        input_str = input('性别 体重(kg) 身高(cm) 年龄： ')
        # 使用到字符串内置函数 str.split()
        str_list = input_str.split(' ')

        try:
            gender = str_list[0]
            weight = float(str_list[1])
            height = float(str_list[2])
            age = int(str_list[3])

            if gender == '男':
                # 男性
                bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
            elif gender == '女':
                # 女性
                bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
            else:
                bmr = -1

            if bmr != -1:
                print('您的性别: {}, 体重: {}kg, 身高: {}cm, 年龄: {}'.format(gender, weight, height, age))
                print('您的基础代谢率: {}大卡'.format(bmr))
            else:
                print('不支持的性别：', gender)

        except ValueError:
            print('输入信息的格式不正确！参考：男 55 170 32')
        except IndexError:
            print('输入的信息过少！参考：男 55 170 32')
        except:
            print('程序异常！')

        # 输出空行
        print()
        y_or_n = input('是否退出程序y/n:')


if __name__ == '__main__':
    main()
