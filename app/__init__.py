"""
App模块初始化文件
"""
from fastapi import APIRouter

# 创建主路由（待实现各子路由后注册）
api_router = APIRouter(prefix="/api")

# 导入各子路由（待实现）
# from app.routers import auth, chat, teaching, research, news, skills, video, admin

# 注册子路由（待取消注释）
# api_router.include_router(auth.router, prefix="/auth", tags=["认证"])
# api_router.include_router(chat.router, prefix="/chat", tags=["对话"])
# api_router.include_router(teaching.router, prefix="/teaching", tags=["教学"])
# api_router.include_router(research.router, prefix="/research", tags=["科研"])
# api_router.include_router(news.router, prefix="/news", tags=["新闻"])
# api_router.include_router(skills.router, prefix="/skills", tags=["技能"])
# api_router.include_router(video.router, prefix="/video", tags=["视频"])
# api_router.include_router(admin.router, prefix="/admin", tags=["管理"])
