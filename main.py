"""
中船党校AI智能业务系统 - 主应用入口
China State Shipbuilding Corporation (CSSC) Party School AI Platform
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import os

# 创建FastAPI应用实例
app = FastAPI(
    title="中船党校AI智能业务系统",
    description="为党校教学科研工作提供AI能力支持",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应限制具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 配置静态文件目录
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# 配置模板目录
templates_dir = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))

# ============ 路由导入（待实现）============
# from app.routers import auth_router, chat_router, teaching_router
# from app.routers import research_router, news_router, skill_router
# from app.routers import video_router, admin_router

# 注册路由（待取消注释）
# app.include_router(auth_router.router, prefix="/api/auth", tags=["认证"])
# app.include_router(chat_router.router, prefix="/api/chat", tags=["对话"])
# app.include_router(teaching_router.router, prefix="/api/teaching", tags=["教学"])
# app.include_router(research_router.router, prefix="/api/research", tags=["科研"])
# app.include_router(news_router.router, prefix="/api/news", tags=["新闻"])
# app.include_router(skill_router.router, prefix="/api/skills", tags=["技能"])
# app.include_router(video_router.router, prefix="/api/video", tags=["视频"])
# app.include_router(admin_router.router, prefix="/api/admin", tags=["管理"])

# ============ 根路由（临时占位）============
@app.get("/")
async def root():
    """根路由 - 返回欢迎信息"""
    return {
        "message": "中船党校AI智能业务系统 API",
        "version": "1.0.0",
        "status": "under_development",
        "docs": "/api/docs"
    }

@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy"}

# ============ 应用启动事件 ============
@app.on_event("startup")
async def startup_event():
    """应用启动时执行"""
    print("🚀 中船党校AI系统启动中...")

@app.on_event("shutdown")
async def shutdown_event():
    """应用关闭时执行"""
    print("🛑 中船党校AI系统关闭")

# ============ 主程序入口 ============
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # 开发模式自动重载
        log_level="info"
    )
