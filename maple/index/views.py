#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: index.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 02:21:04
# *************************************************************************
from flask import (render_template, redirect, url_for, make_response)
from flask.views import MethodView
from maple.extensions import cache
from maple.blog.models import Blog
from maple.question.models import Question
from .models import Notice


class IndexView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        blogs = Blog.query.limit(7)
        questions = Question.query.filter_by(is_private=False).limit(7)
        notice = Notice.query.first()
        data = {
            'blogs': blogs,
            'questions': questions,
            'notice': notice,
        }
        return render_template('index/index.html', **data)


class RainView(MethodView):
    def get(self):
        response = make_response(redirect(url_for('index.index')))
        response.delete_cookie('welcome')
        return response


class AboutView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return render_template('index/about.html')


class ResumeView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return render_template('index/resume.html')


class FriendView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return render_template('index/friends.html')
