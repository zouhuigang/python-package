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
