from flask import Flask  # 导入包

app = Flask(__name__)  # 创建一个Web应用


@app.route('/')  # 定义路由(Views)，可以理解为定义页面的URL
def index():
    return "这是用Python + Flask 搞出来的。"  # 渲染页面


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)  # 运行，指定监听地址为 127.0.0.1:8080

'''
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''