"""
    作者：叶美倩
    日期：20／11／2019
    功能：用递归函数绘制分形树
    版本：v1.0
"""
import turtle


def draw_branch(branch_length):
    """
    绘制分形树
    :return:
    """

    if branch_length > 5:
        # 绘制右侧树枝
        if branch_length > 25:
            turtle.color('brown')
        else:
            turtle.color('green')
        turtle.forward(branch_length)
        print('向前 ', branch_length)
        turtle.right(20)
        print('右转1 20')
        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(40)
        print('左转 40')
        draw_branch(branch_length - 15)

        # 返回之前的树枝
        turtle.right(20)
        print('右转2 20')
        if branch_length > 25:
            turtle.color('brown')
        else:
            turtle.color('green')
        turtle.backward(branch_length)
        print('向后 ', branch_length)



def main():
    """
    主函数
    :return:
    """
    turtle.color('brown')

    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    branch_length = 100

    draw_branch(branch_length)

    turtle.exitonclick()


if __name__ == '__main__':
    main()

