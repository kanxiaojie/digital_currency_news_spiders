# -*- coding: utf-8 -*-
import sys
import logging
from datetime import datetime

from app.repository.article_repo import save

logger = logging.getLogger(__name__)
sys.setrecursionlimit(10000)

date = datetime.now().strftime("%Y-%m-%d")

base_directory_name = '/data/python/digital_currency_news_files/'


class Spider(object):
    def __init__(self):
        self.__directory_name = ''
        self.__full_directory_path = ''

    def banner(self, site_name):
        logger.info(site_name + ' spider is running...')

    def run(self):
        pass

    @staticmethod
    def save_to_repository(new_article):
        save(new_article.serialize())
