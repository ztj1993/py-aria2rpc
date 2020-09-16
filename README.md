# Python Aria2 RPC 调用模块

### 说明
这是一个 aria2rpc 调用模块。

## 安装
```
pip install py-ztj-aria2rpc
```

### 使用
```
from ZtjAria2Rpc import Aria2Rpc

rpc = Aria2Rpc(uri='http://127.0.0.1:6800/rpc')
print(rpc.get_version())
```
