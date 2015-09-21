#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: models.py
Author: huxuan <i(at)huxuan.org>
Description: Models for app.
"""
from app import db


class User(db.Model):
    __tablename__ = 'userinfo'

    # new segments
    uid = db.Column(db.Integer, primary_key=True)
    birthday = db.Column(db.DateTime)
    student_id = db.Column(db.String(16))
    name = db.Column(db.String(16))
    tel = db.Column(db.String(16))

    # existing segments
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32), nullable=False)
    # token temporarily not included
    # tokentime temporarily not included
    gender = db.Column(db.Boolean, nullable=False)  # was `sex`
    icon = db.Column(db.Text)
    intro = db.Column(db.Text)
    sig1 = db.Column(db.Text)
    sig2 = db.Column(db.Text)
    sig3 = db.Column(db.Text)
    hobby = db.Column(db.Text)
    qq = db.Column(db.String(16))
    mail = db.Column(db.String(64))
    province = db.Column(db.String(8))  # was `place`
    registration_date = db.Column(db.DateTime)  # was `regdate`
    last_login_date = db.Column(db.DateTime)  # was `lastdate`
    last_login_ip = db.Column(db.DateTime)  # was `lastip`
    star = db.Column(db.Integer)
    # score temporarily not included
    post_num = db.Column(db.Integer, unsigned=True)  # was `post`
    reply_num = db.Column(db.Integer, unsigned=True)  # was `reply`
    water_num = db.Column(db.Integer, unsigned=True)  # was `water`
    sign_num = db.Column(db.Integer, unsigned=True)  # was `sign`
    # rights temporarily not included
    # newmsy temporarily not included
    # extr temporarily not included
    last_post_time = db.Column(db.DateTime)  # was `lastpost`
    current_board = db.Column(db.Integer)  # was `nowboard`
    user_agent = db.Column(db.String(128))  # was `onlinetype`
    # logininfo temporarily not included
    # code temporarily not included
    # other2 3 4 5 6 temporarily not included


class Board(db.Model):
    __tablename__ = 'boardinfo'

    bid = db.Column(db.Integer, primary_key=True)
    board_name = db.Column(db.String(32), unique=True)  # was `name`
    board_title = db.Column(db.String(32), unique=True)  # was `bbstitle`
    invisible = db.Column(db.Boolean, default=False)  # was `hide`
    m1 = db.Column(db.Integer)
    m2 = db.Column(db.Integer)
    m3 = db.Column(db.Integer)
    m4 = db.Column(db.Integer)
    # need temporarily not included


class Comments(db.Model):
    __tablename__ = 'comments'

    cid = db.Column(db.Integer, primary_key=True)  # was `id`
    pid = db.Column(db.Integer)  # was `fid`
    author_uid = db.Column(db.Integer)  # was `author`
    content = db.Column(db.Text)  # was `text`
    time = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)  # was `visible`

    pid = db.relationship('Posts', backref='pid', lazy='dynamic')
    author_uid = db.relationship('User', backref='uid', lazy='dynamic')


class Messages(db.Model):
    __tablename__ = 'messages'

    mid = db.Column(db.Integer, primary_key=True)
    sender_uid = db.Column(db.Integer)
    receiver_uid = db.Column(db.Integer)
    content = db.Column(db.Text)
    time = db.Column(db.DateTime)
    is_read = db.Column(db.Boolean, default=False)
    # ruser, rmsg, rbid, rtid, rpid deleted

    sender_uid = db.relationship('User', backref='uid', lazy='dynamic')
    receiver_uid = db.relationship('User', backref='uid', lazy='dynamic')


class Posts(db.Model):
    __tablename__ = 'posts'

    pid = db.Column(db.Integer, primary_key=True)  # was `fid`
    bid = db.Column(db.Integer)
    tid = db.Column(db.Integer)
    title = db.Column(db.String(32))
    author_uid = db.Column(db.Integer)  # was `author`
    content = db.Column(db.Text)  # was `text`
    # ishtml temporarily not included
    # attachs temporarily not included
    created_at = db.Column(db.DateTime)  # was `replytime`
    updated_at = db.Column(db.DateTime)  # was `updatetime`
    signature = db.Column(db.Text)
    user_agent = db.Column(db.String(128))  # was `type`
    ip = db.Column(db.String(64))
    # lzl temporarily not included

    bid = db.relationship('Board', backref='bid', lazy='dynamic')
    tid = db.relationship('Threads', backref='tid', lazy='dynamic')
    author_uid = db.relationship('User', backref='uid', lazy='dynamic')


class Sign(db.Model):
    __tablename__ = 'sign'

    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    minute = db.Column(db.Integer)
    second = db.Column(db.Integer)
    weekday = db.Column(db.Integer)  # was `week`
    uid = db.Column(db.Integer)  # was `username`

    uid = db.relationship('User', backref='uid', lazy='dynamic')


class Threads(db.Model):
    __tablename__ = 'threads'

    tid = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.Integer)
    title = db.Column(db.String(32))
    author_uid = db.Column(db.Integer)  # was `author`
    replyer_uid = db.Column(db.Integer)  # was `replyer`
    clicks = db.Column(db.Integer, default=0)  # was `click`
    reply_num = db.Column(db.Integer, default=0)  # was `reply`
    # gesture temporarily not included
    good = db.Column(db.Boolean, default=False)  # was `extr`
    sticky = db.Column(db.Boolean, default=False)  # was `top`
    created_at = db.Column(db.DateTime)  # was `postdate`
    replied_at = db.Column(db.DateTime)  # was `timestamp`

    bid = db.relationship('Board', backref='bid', lazy='dynamic')
    author_uid = db.relationship('User', backref='uid', lazy='dynamic')
    replyer_uid = db.relationship('User', backref='uid', lazy='dynamic')


class Group(db.Model):
    __tablename__ = 'group'

    gid = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(32), unique=True)


class Group_User(db.Model):
    __tablename__ = 'group_user'

    gid = db.Column(db.Integer)
    uid = db.Column(db.Integer)

    gid = db.relationship('Group', backref='gid', lazy='dynamic')
    uid = db.relationship('User', backref='uid', lazy='dynamic')
