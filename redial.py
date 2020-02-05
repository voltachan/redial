import requests
import time
def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()
    return ""
s=requests.session()
headers={
    'Referer': 'http://路由器的 IP 地址/cgi-bin/luci/admin/network/network',
    }
s.post("http://路由器的 IP 地址/cgi-bin/luci/",{"luci_username":"root","luci_password":"你的密码"},headers=headers)
cookies=s.cookies.get_dict()
tmp=s.get("http://路由器的 IP 地址/cgi-bin/luci/admin/network/network",headers=headers,cookies=cookies).text
token={'token':getmidstring(tmp,'name="token" value="','" />')}
s.post("http://路由器的 IP 地址/cgi-bin/luci/admin/network/iface_shutdown/wan",token,headers=headers,cookies=cookies)
time.sleep(1)
s.post("http://路由器的 IP 地址/cgi-bin/luci/admin/network/iface_reconnect/wan",token,headers=headers,cookies=cookies)
print("Successful\n")
