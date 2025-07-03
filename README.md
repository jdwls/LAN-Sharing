# 局域网文件共享系统

## 项目简介

这是一个基于 Vue.js 前端和 Flask 后端的局域网文件共享系统，支持文件上传下载、预览、目录管理等功能。

## 功能特点

- 文件上传/下载
- 图片/文本/视频预览
- Office 文档预览(PDF/Word/Excel)
- 目录创建与管理
- 用户登录/注册

## 安装指南

### 前端(Vue)安装

1. 确保已安装 Node.js(>=12.x)
2. 进入前端目录：
   ```bash
   cd restvue003
   ```
3. 安装依赖：
   ```bash
   npm install
   ```

### 后端(Flask)安装

1. 确保已安装 Python(>=3.6)
2. 安装依赖：
   ```bash
   pip install flask flask-cors
   ```

## 运行说明

### 启动前端

```bash
cd restvue003
npm run s
```

访问地址：http://localhost:8080

### 启动后端

```bash
cd restFlask003
python index.py
```

后端默认运行在：http://localhost:5000

## 目录结构说明

### 前端(restvue003)

- `src/components/` - Vue 组件
  - 文件操作相关组件
  - 预览相关组件
  - 用户认证组件
- `src/store/` - Vuex 状态管理
- `public/` - 静态资源

### 后端(restFlask003)

- `module/funtion/` - 功能模块
  - `common/` - 通用工具
  - `see/` - 文件预览功能
  - `view/` - 视图路由
- `template/` - 模板文件
  - `UseSql/` - 数据库相关
  - `crt/` - SSL 证书

## 注意事项

1. 确保前后端同时运行
2. 首次使用需要创建用户
3. 文件上传大小限制可在后端配置
4. 视频预览需要浏览器支持相应格式

## 常见问题

Q: 无法预览 Office 文档？
A: 确保已安装 Microsoft Office 或兼容的阅读器

Q: 上传文件失败？
A: 检查后端存储目录权限

## 高级功能说明

### 聊天室功能
- 实时在线用户列表
- 支持WebSocket通信
- 用户状态实时更新

### SSL安全配置
- 项目已内置自签名证书(localhost.crt/localhost.key)
- 如需更换证书，请替换template/crt/目录下的文件
- 后端默认启用HTTPS

### API接口说明
- 文件操作API: /api/file/*
- 用户认证API: /api/auth/*
- 聊天室API: /api/chat/*
- 目录管理API: /api/dir/*

## 版本更新

### v0.1.1 更新内容：

1. 优化代码格式
2. 优化上传、下载相关内容
3. 优化 UI
4. 更新文档

### v0.1.2 (功能预告)：

1. 新增上传设置（支持1-5文件并行传输）
2. 新增多种格式在线预览支持
3. 实现上传页面实时预览功能
4. 完善聊天室功能
5. 优化SSL安全配置
