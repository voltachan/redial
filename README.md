# OpenWRT 重新拨号（需要 PPPoE 上网）
## 使用指南
替换 `redial.py` 代码中的 IP 地址、用户名、密码，然后运行。
## 注意事项
1. **禁止**使用光猫的拨号模式，必须使用桥接模式。
2. 请**关闭**多拨或自行修改代码（加入虚拟出来的接口）。
3. ***请勿***将 `LAN`、  `WAN6` 或无线接口并入，会导致与路由器失去连接。
4. 不可用于梅林及其它私有路由器系统。
