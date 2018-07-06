### python包管理

包，模块，方法的区别：

	包-->可以理解成文件夹
	模块-->可以理解成文件
	方法-->可以理解成在文件中的方法


与golang的对比:

	package main
	import(
		"github.com/zouhuigang/package/zhttp"
	)
	func main(){
		 zhttp.GET(`http://wwww.baidu.com`)
	}
	
导入一个名为为zhttp的golang包，然后这个包里面的所有公共方法都能使用，没有模块的概念。


python:

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	__author__ = 'zouhuigang'
	from zhttp.post import Post

	s =Post('http://www.baidu.com')
	print(s)

意思是，从包(zhttp)中找到模块(post.py),然后导入其中的方法Post，也可以这样导入:

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	__author__ = 'zouhuigang'
	from zhttp import post

	s =post.Post('http://www.baidu.com')
	print(s)
	
意思是，从包(zhttp)导入模块(post.py),然后模块.方法来使用。
	
然后打开命令行，切换到当前目录，输入

	cd python-package/zhttp
	pip install .

查看已安装的包:

	pip freeze

可以看到最后面有个包:

	zhttp==0.1

测试是否成功:

	cd example
	python main.py

### 上传到py官网(https://pypi.org/)

1.安装

	 pip install twine

2.生成package 

	python setup.py sdist bdist_wheel


注册：

	$ twine register dist/zhttp-0.1.tar.gz
	$ twine register dist/zhttp-0.1-py2-none-any.whl

上传:

	twine register dist/


卸载/安装

	pip uninstall zhttp
	pip install zhttp


查看安装的包:

	import zhttp
	dir(zhttp)




