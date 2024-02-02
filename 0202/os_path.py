
from pathlib import Path
import os


# __file__ 是 Python 中的一个内置变量，表示当前执行的脚本文件的路径
# 以创建一个 Path 对象。
# Path对象赋值给变量 path_prefix， path_prefix 可以用于构建文件路径，例如拼接或者子目录

''' path 对象 解析
path 对象是 pathlib 模块中的一个类，用于处理文件路径。它提供了许多方法和属性，用于操作和检查文件路径。下面是一些常用的 Path 对象可调用的参数：
.resolve()：解析路径中的符号链接并返回绝对路径。
.exists()：检查路径是否存在。
.is_file()：检查路径是否是一个文件。
.is_dir()：检查路径是否是一个目录。
.name：获取路径的文件名（包括扩展名）。
.stem：获取路径的文件名（不包括扩展名）。
.suffix：获取路径的文件扩展名。
.parent：获取路径的父目录。
.parts：将路径拆分为各个部分，并以元组形式返回。
.joinpath(*args)：连接路径的各个部分。
.glob(pattern)：返回与指定模式匹配的所有路径。
.mkdir(mode=0o777, parents=False, exist_ok=False)：创建目录。
.rename(target)：重命名路径。
.unlink()：删除路径。
.stat()：返回路径的文件状态信息。
'''



path = Path(os.path.dirname(__file__))
print(path)

# 路径拼接，可以使用 / 进行直接拼接
path1 = str( path / Path("npz/1.npz") )

print("name: ")
print(path.parent)


 
