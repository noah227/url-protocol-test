# -*- coding: utf-8 -*-
# CREATED: 2024/12/19
# AUTHOR : NOAH YOUNG
# EMAIL  : noah227@foxmail.com
import os


def gen():
    print("curdir: ", os.path.dirname(__file__))

    if not os.path.exists("./dist"):
        os.mkdir("./dist")

    regName = "tt-test"
    execPath = os.path.join(os.path.dirname(__file__), "dist\\main.exe")
    execPath = execPath.replace("\\", "\\\\")

    with open("./template.reg", "r", encoding="utf8") as f:
        content = f.read()
        content = content.replace("@name", regName).replace("@execPath", rf"{execPath}")
        with open("./dist/url-protocol-test.reg", "w", encoding="utf8") as f2:
            f2.write(content)
            print(" Info ".center(40, "-"))
            print("Double click generated reg file to register protocol")
            print(f"Open your browser and visit {regName}://hello to test")
    pass


if __name__ == "__main__":
    gen()
