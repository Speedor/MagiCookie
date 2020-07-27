# MagiCookie
[Magi](https://magi.com/) AI 机器学习搜索引擎 逆向生成 cookie 

[Magi 是什么？](https://www.peak-labs.com/docs/zh/magi/intro)

javaScrpit、java、python 生成算法代码已 push，go、node、php等其他语言自翻译。

#### Magi cookie 思路重点：

- cookie 二次请求校验
- 绕过前端 F12 防 debug 死循环 
- 防 debug  死循环间隔调用
- 破解 Cookie 生成逻辑方法
- 防止本地调试检测代码是否 format
- 控制流平坦化（符号执行脚本）
- 混淆代码调试分析

PS：[magi_js_formate_compress.html](https://github.com/Speedor/MagiCookie/blob/master/magi_js_formate_compress.html) 为 js 压缩修正后代码，可正常调试分析