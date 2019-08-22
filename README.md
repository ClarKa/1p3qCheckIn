# 1p3qCheckIn

一亩三分地自动每日签到脚本。

目前只支持每日签到功能，后续会慢慢支持每日答题，现在正在收集题库。

脚本会从当前目录下的accounts.json来读取账号密码。

需要注意的是，一亩三分地会在前端直接吧密码加密，然后把加密后的密码发送到后端。我比较懒暂时没有去研究这个前端加密的算法，所以直接用chrome抓了登录时候的post request，然后从里面提取了加密之后密码复制粘贴到了accounts.json里面。

accounts.json的格式如下：

```json
[
    {
        "id": "用户名1",
        "password": "加密密码1"
    },
    {
        "id": "用户名2",
        "password": "加密密码2"
    }
]
```