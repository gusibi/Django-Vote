Django-Vote
===========

一个基于django的类似于hacker news 的基于用户投票的排名应用

说明
此应用符合以下要求:
1. 支持赞同反对票，使用openid登录:
2. 投票结果实时更新，所有用户无需刷新即可看到最新结果
3. 防止机器人恶意刷票
4. 一个用户只能投一次票



使用要求：
需要 python openid         http://pypi.python.org/pypi/python-openid/
     django_openid_auth    https://launchpad.net/django-openid-auth
UI使用的bootstrap
将vote文件夹放在和manage.py 同等级目录下， 修改setting.py 和 project url.py