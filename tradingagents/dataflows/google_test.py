import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# 加载环境变量
load_dotenv(project_root / ".env", override=True)


def test_google_news_tool():
  """测试Google新闻工具"""
  try:
    print("🧪 测试Google新闻工具")
    print("=" * 50)

    from tradingagents.dataflows.google import get_google_news
    import logging
    logger = logging.getLogger("google_news")
    logger.info(
        f"[Google新闻] 开始获取新")

    print("✅ get_google_news函数导入成功")

    # 测试获取苹果公司新闻
    print("📰 获取NVDA公司新闻...")
    try:
      news = get_google_news(
          query="Nvidia NVDA stock",
          start_date="2026-01-15",
          end_date="2026-01-22"
      )
      if news and len(news) > 0:
        print("✅ Google新闻获取成功")
        print(f"   新闻长度: {len(news)} 字符")
        print(f"   新闻预览: {news[0]}...")
        return True
      else:
        print("⚠️ Google新闻获取成功但内容为空")
        return True  # 功能正常，只是没有内容

    except Exception as e:
      print(f"❌ Google新闻获取失败: {e}")
      return False

  except ImportError as e:
    print(f"❌ Google新闻工具导入失败: {e}")
    return False


from gnews import GNews


def getNewsData():
  google_news = GNews()
  pakistan_news = google_news.get_news('nvda')
  print(pakistan_news[0])
