GitHub Actions使用模板
===

<p align="center">
    <img src="https://img.shields.io/badge/Created on-2022.09-green"/>
    <img src="https://img.shields.io/badge/Python-3.7-blue"/>
    <img src="https://img.shields.io/badge/Last commit-Dec.-yellow"/>
    <img src="https://img.shields.io/badge/Repo size-35.8kb-red"/>
</p>

# 1. 实现功能
+ 定时执行特定任务
+ 通过 `SERVERCHAN`推送简单的运行结果到微信
+ 由 `github actions` 每日`x`点定时运行

# 2. 使用方法
1. Fork [此仓库项目](https://github.com/) > 点击右上角fork按钮即可，欢迎点`star`~
2. 本地调试请修改`config.py`文件
3. 远端调试请在`github项目 - Settings - Secrets - Actions`中配置config文件中需要的相关ID
4. fork后必须修改一下文件，才能执行定时任务, 可修改 `README.MD`, 添加一个空格+1
5. 更新`Secrets`后，必须重新提交代码才会生效


## 3. 配置`.github/main.yml`

- **更改执行时间** [crontab 表达式在线测试](https://crontab.guru/)
```yml
    # 语法同crontab，具体可百度，为美区时间，加8小时为中国时间
    - cron: '0 0 * * *'
```

- **更改env**
```yml
    # DEFAULT_MAC_LIST为config中配置的名称
    # secrets.DEFAULT_MAC_LIST为github actions中配置的名称
    - name: Working
    env:
        DEFAULT_MAC_LIST: ${{ secrets.DEFAULT_MAC_LIST }}
        DEFAULT_WSKEY: ${{ secrets.DEFAULT_WSKEY }}
        SERVERCHAN_SECRETKEY: ${{ secrets.SERVERCHAN_SECRETKEY }}
    run: python main.py #>JDCloud_Bot.log
```



# N. Log

+ 2021-09-22  
首次提交代码 1
