### python包管理

	
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





