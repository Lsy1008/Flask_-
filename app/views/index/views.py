from flask import render_template

from app.models.models import News
from . import index_blu
from app import db


@index_blu.route("/index")
@index_blu.route("/")
def index():
    # 1. 查询点击排行的前6个数据
    news = db.session.query(News).order_by(News.clicks.desc()).limit(6)  # 从news数据表中查询点击最高的6个数据
    
    return render_template("index/index.html", news=news)
