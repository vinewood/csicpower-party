# 中船党校AI智能业务系统

> **China State Shipbuilding Corporation (CSSC) Party School AI Intelligent Business Platform**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com)

---

## 📋 项目简介

中船党校AI智能业务系统是为中国船舶集团有限公司党校量身打造的智能化业务平台。系统采用**零编译技术栈**，集成AI大模型能力，为党校的教学、科研、信息管理工作提供全方位智能支持。

### 核心定位

- **用户规模**：40人（讲师20人 + 研究员15人 + 领导5人）
- **核心目标**：提升教学科研效率，实现AI能力深度业务化
- **技术策略**：零编译、快速迭代、低成本维护

---

## 🎯 核心功能模块

系统包含六大功能模块，覆盖党校核心业务场景：

### 1️⃣ 教学工作台
对标 aizke 搜索界面设计
- 📝 课程设计与管理系统
- 🎯 课件智能生成（AI辅助）
- 🎥 音视频分析工具（转录+摘要+思维导图）
- 📊 教学经验萃取
- 🎓 AI互动课堂

### 2️⃣ 科研工作台
对标 AMiner + 维普学术平台
- 📊 课题选题助手（AI推荐研究方向）
- 📚 文献检索与管理（集成AMiner API）
- 📝 论文润色/翻译/校对（集成gpt_academic引擎）
- 📈 研究动态追踪
- 🗂️ 科研项目空间

### 3️⃣ 信息导航台
RSS新闻聚合 + AI摘要
- 📰 多源新闻订阅（新华网、人民网、国资委等）
- 🤖 AI自动摘要每条新闻
- 📅 每日要点简报生成
- 📤 支持导出PDF和分享

### 4️⃣ 技能中心
对标青泥AI技能广场
- 🧩 预置20+科研/教学/通用技能
- 🔧 自定义技能创建
- ⭐ 技能评分与使用统计
- 📌 个人技能空间管理

### 5️⃣ 视频分析工具
对标dwsh.cn用户体验
- 📁 拖拽上传视频文件
- 🎤 自动转录（语音→文本）
- 🧠 自动生成思维导图
- 📝 结构化笔记提取
- 📄 支持导出多种格式

### 6️⃣ 系统管理后台
- 👥 用户与角色管理
- 🤖 AI模型配置（单模/多模对比）
- 📊 用量统计与Token消耗监控
- 📢 系统公告管理
- 🔧 RSS订阅源管理

---

## 🛠️ 技术栈

### 核心设计理念：**零编译、快速迭代**

```
传统路线（❌）                    推荐路线（✅）
━━━━━━━━━━━━━━━━━━━━━━━    ━━━━━━━━━━━━━━━━━━━━━━━━━━
React/Vue + Webpack/Vite    Jinja2模板 + Alpine.js + CDN
npm install (500MB+)        零依赖安装
修改代码 → 编译 → 刷新       修改代码 → 直接刷新
TypeScript 编译              纯JavaScript（无编译）
CSS Module/PostCSS          Tailwind CSS CDN（即时生效）
```

### 技术选型

| 层级 | 技术 | 引入方式 | 说明 |
|------|------|---------|------|
| **后端框架** | Python 3.12 + FastAPI | pip install | AI生态母语，异步SSE支持 |
| **模板引擎** | Jinja2 | FastAPI内置 | 服务端渲染，无需前端编译 |
| **前端交互** | Alpine.js 3.x | CDN | Vue风格语法，零编译 |
| **CSS框架** | Tailwind CSS | CDN | 实用优先，即时生效 |
| **组件库** | Flowbite | CDN | 基于Tailwind的组件库 |
| **图表** | ECharts | CDN | 数据可视化 |
| **思维导图** | simple-mind-map | CDN | 音视频分析结果展示 |
| **Markdown** | marked.js | CDN | AI输出渲染 |
| **数据库** | MySQL 8.0 | SQLAlchemy | ORM + 迁移 |
| **任务队列** | Celery + Redis | pip install | 异步任务处理 |
| **AI网关** | 阿里云百炼 | SDK | Qwen全系 + RAG知识库 |

### 为什么选择"零编译"路线？

✅ **开发效率高**：修改模板→刷新浏览器，无需等待编译  
✅ **学习成本低**：只需懂Python + HTML，无需学习React/Vue  
✅ **维护成本低**：不依赖Node.js生态，避免依赖地狱  
✅ **部署简单**：无需构建步骤，直接部署Python应用  

---

## 📁 项目结构

```
csicpower-party/
│
├── main.py                      # FastAPI应用入口
├── config.py                    # 全局配置文件
├── requirements.txt             # Python依赖（< 20个包）
├── .env.example                 # 环境变量示例
│
├── app/                        # 应用核心代码
│   ├── __init__.py
│   ├── auth.py                 # JWT认证中间件
│   ├── dependencies.py         # 依赖注入（get_current_user）
│   ├── models.py               # SQLAlchemy模型定义
│   ├── schemas.py              # Pydantic数据校验
│   │
│   ├── routers/                # API路由模块
│   │   ├── auth_router.py     # 登录/注册/Token刷新
│   │   ├── chat_router.py     # 对话SSE流式接口
│   │   ├── teaching_router.py  # 教学管理API
│   │   ├── research_router.py # 科研管理API
│   │   ├── news_router.py     # 新闻聚合API
│   │   ├── skill_router.py    # 技能中心API
│   │   ├── video_router.py    # 视频分析API
│   │   └── admin_router.py    # 系统管理API
│   │
│   ├── integrations/           # 外部服务集成
│   │   ├── bailian_client.py  # 阿里云百炼MaaS
│   │   ├── deepseek_client.py  # DeepSeek API
│   │   ├── rss_fetcher.py     # RSSHub + Miniflux桥接
│   │   ├── video_processor.py # 视频转录引擎
│   │   └── academic_tools.py  # gpt_academic核心函数
│   │
│   └── tasks/                  # Celery异步任务
│       ├── news_crawler.py     # 定时抓取新闻
│       └── video_transcribe.py # 异步视频转录
│
├── templates/                  # Jinja2模板（零编译前端）
│   ├── base.html               # 基础布局模板
│   │
│   ├── public/                 # 公开页面
│   │   ├── landing.html        # 登录前介绍页
│   │   └── login.html          # 登录页
│   │
│   ├── workspace/              # 主工作区模板
│   │   ├── teaching.html       # 教学工作台
│   │   ├── research.html       # 科研工作台
│   │   ├── news.html           # 信息导航台
│   │   ├── skills.html         # 技能中心
│   │   ├── video.html          # 视频分析工具
│   │   └── admin.html         # 管理后台
│   │
│   └── components/             # 可复用模板片段
│       ├── topbar.html         # 顶部导航栏
│       ├── model_switcher.html # 模型切换组件
│       ├── chat_panel.html     # 聊天面板
│       └── footer.html         # 页脚
│
├── static/                     # 静态文件
│   ├── css/
│   │   └── custom.css        # 少量自定义样式
│   └── js/
│       ├── chat.js             # SSE聊天流式处理
│       ├── workspace.js        # 工作台交互逻辑
│       └── utils.js            # 工具函数
│
├── docker/                     # Docker部署配置
│   ├── docker-compose.yml      # 服务编排
│   ├── Dockerfile             # 主应用镜像
│   ├── nginx.conf             # 反向代理配置
│   └── .dockerignore         # Docker构建忽略文件
│
├── alembic/                   # 数据库迁移
│   └── versions/              # 迁移脚本目录
│
├── tests/                      # 测试用例
│   ├── test_auth.py
│   ├── test_chat.py
│   └── ...
│
├── docs/                       # 项目文档
│   ├── API.md                 # API接口文档
│   ├── DEPLOYMENT.md         # 部署指南
│   ├── DEVELOPMENT.md        # 开发指南
│   └── CHANGELOG.md          # 版本更新日志
│
├── scripts/                    # 运维脚本
│   ├── deploy.sh              # 一键部署脚本
│   ├── backup.sh              # 数据备份脚本
│   └── init_db.py            # 数据库初始化
│
├── .gitignore                  # Git忽略文件
├── LICENSE                     # 开源许可证
└── README.md                  # 项目说明文档（本文件）
```

---

## 🚀 快速开始

### 环境要求

- Python 3.12+
- MySQL 8.0+
- Redis 7.0+
- Git

### 1. 克隆项目

```bash
git clone https://github.com/vinewood/csicpower-party.git
cd csicpower-party
```

### 2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

**核心依赖（仅15个包）**：

```txt
fastapi==0.115.0
uvicorn[standard]==0.34.0
jinja2==3.1.5
sqlalchemy==2.0.38
alembic==1.14.0
celery==5.3.6
redis==5.2.1
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
aiohttp==3.11.11
alibabacloud-bailian==1.0.0
pymysql==1.2.1
python-multipart==0.0.20
itsdangerous==2.2.0
python-dotenv==1.0.0
```

### 4. 配置环境变量

```bash
cp .env.example .env
```

编辑 `.env` 文件，配置以下变量：

```env
# 数据库配置
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/csic_ai

# Redis配置
REDIS_URL=redis://localhost:6379

# 阿里云百炼API
BAILIAN_API_KEY=your_api_key_here
BAILIAN_WORKSPACE_ID=your_workspace_id

# DeepSeek API（备用）
DEEPSEEK_API_KEY=your_api_key_here

# JWT配置
JWT_SECRET_KEY=your_secret_key_here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# 应用配置
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

### 5. 初始化数据库

```bash
# 创建数据库
mysql -u root -p -e "CREATE DATABASE csic_ai CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# 运行迁移
alembic upgrade head

# 初始化基础数据（可选）
python scripts/init_db.py
```

### 6. 启动应用

#### 开发模式

```bash
# 启动FastAPI应用（自动重载）
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 启动Celery_worker（新终端）
celery -A app.tasks worker -l info

# 启动Celery_beat（新终端，可选）
celery -A app.tasks beat -l info
```

访问 `http://localhost:8000` 查看应用。

#### 生产模式（Docker）

```bash
# 构建并启动所有服务
docker-compose -f docker/docker-compose.yml up -d

# 查看日志
docker-compose -f docker/docker-compose.yml logs -f

# 停止服务
docker-compose -f docker/docker-compose.yml down
```

---

## 📊 核心功能详解

### AI模型切换器（全局组件）

系统支持**单模型模式**和**多模型对比模式**：

- **单模型模式**：选择单个AI模型进行对话（Qwen-Max/DeepSeek等）
- **多模型对比模式**：同时调用2-4个模型，并排显示回答，方便对比选择

模型切换器在所有页面可见，用户可随时切换。

### 多租户数据隔离

系统采用 `user_id` 隔离策略：

- 每个用户只能看到自己的对话、项目、技能
- 数据库层面通过 `user_id` 外键实现隔离
- 支持角色权限控制（讲师/研究员/领导/管理员）

### 个性化工作空间

每个用户可以：

- **设置默认工作台**：登录后自动跳转到指定模块
- **调整功能卡片**：拖拽排序，显示/隐藏特定功能
- **固定快捷入口**：将常用项目/技能固定在顶栏

---

## 🌐 外部服务集成

系统集成了多个开源工具和商业API，通过**API桥接**方式实现，不改造第三方代码：

| 服务 | 类型 | 用途 |
|------|------|------|
| **阿里云百炼** | 商业API | 模型服务 + RAG知识库 + Agent平台 |
| **DeepSeek** | 商业API | 备用模型源 |
| **AMiner** | 商业API | 学术文献检索 |
| **RSSHub** | 开源 | RSS订阅源生成 |
| **Miniflux** | 开源 | RSS阅读器 |
| **gpt_academic** | 开源 | 论文解析/润色/翻译引擎 |
| **simple-mind-map** | 开源 | 思维导图渲染库 |

### 集成策略

```
┌─────────────────────────────────────────┐
│        统一前端（Jinja2 + Alpine.js）    │
├─────────────────────────────────────────┤
│        统一API网关（FastAPI）            │
│  ├─ 认证中间件（JWT Token）            │
│  ├─ 路由分发                          │
│  └─ 响应格式化                        │
├─────────────────────────────────────────┤
│        外部服务层（独立部署）            │
│  ├─ 阿里云百炼 API                   │
│  ├─ DeepSeek API                     │
│  ├─ RSSHub (Docker)                  │
│  ├─ Miniflux (Docker)                │
│  └─ gpt_academic (Python模块)         │
└─────────────────────────────────────────┘
```

---

## 📦 部署指南

### 方案A：单机Docker部署（推荐）

适合40人规模，成本低，维护简单。

#### 服务器配置

- **云服务商**：阿里云ECS
- **实例规格**：8C16G
- **操作系统**：Ubuntu 22.04 LTS
- **存储**：100GB SSD云盘

#### 部署步骤

1. **安装Docker和Docker Compose**

```bash
curl -fsSL https://get.docker.com | sh
apt-get install -y docker-compose-plugin
```

2. **克隆项目**

```bash
git clone https://github.com/vinewood/csicpower-party.git
cd csicpower-party
```

3. **配置环境变量**

```bash
cp .env.example .env
# 编辑 .env 填入生产环境配置
```

4. **启动服务**

```bash
docker compose -f docker/docker-compose.yml up -d
```

5. **配置Nginx反向代理（可选）**

已包含在生产配置中，自动配置SSL证书。

#### 成本估算

| 项目 | 配置 | 年费用 |
|------|------|--------|
| 阿里云ECS | 8C16G | ¥4,800 |
| 阿里云RDS MySQL | 2C4G 40GB | ¥1,200 |
| 阿里云Redis | 256MB标准版 | ¥600 |
| 阿里云OSS | 40GB标准存储 | ¥200 |
| 阿里云百炼API | Qwen-Turbo为主 | ¥3,000 |
| 域名 + SSL | .cn域名 | ¥200 |
| **首年总计** | | **¥16,500** |
| **次年运营** | | **¥8,800/年** |
| **人均首年（40人）** | | **¥413** |

### 方案B：本地部署

适合内网环境，不依赖公网。

```bash
# 安装MySQL和Redis
apt-get install -y mysql-server redis-server

# 按照"快速开始"步骤启动应用
# 配置内网Nginx反向代理
```

---

## 👥 用户角色与权限

| 角色 | 人数 | 默认工作台 | 可访问模块 |
|------|------|-----------|-----------|
| **讲师** | ~20 | 教学工作台 | 教学+技能+视频+新闻 |
| **研究员** | ~15 | 科研工作台 | 科研+技能+视频+新闻 |
| **领导** | ~5 | 信息导航台 | 新闻+技能 |
| **管理员** | ~2 | 系统管理 | 全部模块 |

### 权限控制

- **数据隔离**：用户只能访问自己的数据
- **功能授权**：不同角色看到不同的功能模块
- **操作审计**：关键操作记录日志

---

## 🧪 开发指南

### 代码规范

- **Python**：遵循PEP 8规范，使用Black格式化
- **HTML/Jinja2**：缩进2空格，语义化标签
- **JavaScript**：ES6+语法，Alpine.js组件化
- **Git提交**：遵循Conventional Commits规范

### 开发流程

1. **创建功能分支**

```bash
git checkout -b feature/功能名称
```

2. **开发并测试**

```bash
# 启动开发服务器
uvicorn main:app --reload

# 运行测试
pytest tests/
```

3. **提交代码**

```bash
git add .
git commit -m "feat: 添加XX功能"
git push origin feature/功能名称
```

4. **创建Pull Request**

在GitHub上创建PR，描述功能变更和测试结果。

### 调试技巧

- **FastAPI自动文档**：访问 `http://localhost:8000/docs`
- **SQLAlchemy日志**：设置 `echo=True` 查看SQL语句
- **Alpine.js调试**：浏览器控制台输入 `Alpine.debug = true`

---

## 📈 开发路线图

### Phase 1：MVP核心功能（第1-4周）

- [x] 项目骨架搭建
- [x] 用户认证系统（JWT）
- [x] 登录页和介绍页
- [ ] 教学工作台（基础版）
- [ ] 单模型聊天功能
- [ ] 技能中心（预置10个技能）

### Phase 2：业务工作台（第5-8周）

- [ ] 科研工作台（选题+文献）
- [ ] 多模型对比功能
- [ ] 信息导航台（RSS聚合）
- [ ] 视频分析工具（转录+摘要）

### Phase 3：完善与优化（第9-12周）

- [ ] 个性化定制功能
- [ ] 管理后台
- [ ] 性能优化
- [ ] 安全加固
- [ ] 用户培训文档

### Phase 4：上线与迭代（第13周+）

- [ ] 生产环境部署
- [ ] 用户验收测试
- [ ] 收集反馈并迭代
- [ ] 新增功能模块

---

## 🤝 贡献指南

我们欢迎任何形式的贡献！

### 如何贡献

1. **Fork项目**到你的GitHub账号
2. **创建功能分支**
3. **提交代码**并添加测试
4. **创建Pull Request**

### 贡献类型

- 🐛 **Bug修复**
- ✨ **新功能开发**
- 📝 **文档改进**
- 🎨 **UI/UX优化**
- ⚡ **性能优化**
- 🔒 **安全加固**

---

## 📄 许可证

本项目采用 **MIT License** 开源许可证。

详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

本项目集成了多个优秀的开源工具，特此致谢：

- [LobeChat](https://github.com/lobehub/lobe-chat) - 多模型聊天界面参考
- [gpt_academic](https://github.com/binary-husky/gpt_academic) - 学术论文处理引擎
- [RSSHub](https://github.com/DIYgod/RSSHub) - RSS订阅源生成
- [Miniflux](https://github.com/miniflux/v2) - 自托管RSS阅读器
- [simple-mind-map](https://github.com/wanglin2/mind-map) - 思维导图库
- [Alpine.js](https://alpinejs.dev) - 零编译前端框架
- [Tailwind CSS](https://tailwindcss.com) - CSS框架
- [FastAPI](https://fastapi.tiangolo.com) - 现代Python Web框架

---

## 📞 联系方式

- **项目负责人**：[Your Name]
- **Email**：your.email@example.com
- **GitHub Issues**：[提交问题](https://github.com/vinewood/csicpower-party/issues)

---

## 📚 相关文档

- [API接口文档](docs/API.md)
- [部署指南](docs/DEPLOYMENT.md)
- [开发指南](docs/DEVELOPMENT.md)
- [版本更新日志](docs/CHANGELOG.md)

---

<div align="center">

**⚓ 为中船党校赋能，让AI助力教学科研！**

Made with ❤️ by [Your Team]

</div>
