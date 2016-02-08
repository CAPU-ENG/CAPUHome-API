#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: models.py
Author: huxuan <i(at)huxuan.org>
Description: Models for app.
"""
from app import db


class User(db.Model):
    __tablename__ = 'users'

    # new segments
    uid = db.Column(db.Integer, primary_key=True)
    birthday = db.Column(db.Date)
    student_id = db.Column(db.String(16))
    name = db.Column(db.String(16))
    tel = db.Column(db.String(16))

    # existing segments
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32), nullable=False)
    # token temporarily not included
    # tokentime temporarily not included
    gender = db.Column(db.Boolean, nullable=False)  # was `sex`
    avatar = db.Column(db.String(32))
    intro = db.Column(db.Text)
    sig1 = db.Column(db.Text)
    sig2 = db.Column(db.Text)
    sig3 = db.Column(db.Text)
    hobby = db.Column(db.Text)
    qq = db.Column(db.String(16))
    mail = db.Column(db.String(64))
    wechat = db.Column(db.String(64))
    province = db.Column(db.String(8))  # was `place`
    registration_date = db.Column(db.Date)  # was `regdate`
    last_login_time = db.Column(db.DateTime)  # was `lastdate`
    last_post_time = db.Column(db.DateTime)  # was `lastpost`
    star = db.Column(db.Integer, default=1)
    # score temporarily not included
    num_post = db.Column(db.Integer, unsigned=True)  # was `post`
    num_reply = db.Column(db.Integer, unsigned=True)  # was `reply`
    num_water = db.Column(db.Integer, unsigned=True)  # was `water`
    num_sign = db.Column(db.Integer, unsigned=True)  # was `sign`
    # rights temporarily not included
    # newmsy temporarily not included
    # extr temporarily not included
    current_board = db.Column(db.Integer)  # was `nowboard`
    user_agent = db.Column(db.String(128))  # was `onlinetype`
    # logininfo temporarily not included
    # code temporarily not included
    # other2 3 4 5 6 temporarily not included


class Group(db.Model):
    __tablename__ = 'groups'

    gid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    leader_uid = db.Column(db.Integer)
    created_date = db.Column(db.Date)
    deleted = db.Column(db.Boolean, default=False)


class Board(db.Model):
    __tablename__ = 'boards'

    bid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)  # was `bbstitle`
    invisible = db.Column(db.Boolean, default=False)  # was `hide`


class Threads(db.Model):
    __tablename__ = 'threads'

    tid = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.Integer)
    title = db.Column(db.String)
    content = db.Column(db.Text)
    author_uid = db.Column(db.Integer)  # was `author`
    replyer_uid = db.Column(db.Integer)  # was `replyer`
    num_click = db.Column(db.Integer, default=0)  # was `click`
    num_reply = db.Column(db.Integer, default=0)  # was `reply`
    # gesture temporarily not included
    good = db.Column(db.Boolean, default=False)  # was `extr`
    sticky = db.Column(db.Boolean, default=False)  # was `top`
    created_at = db.Column(db.DateTime)  # was `postdate`
    replied_at = db.Column(db.DateTime)  # was `timestamp`


class Post(db.Model):
    __tablename__ = 'posts'

    pid = db.Column(db.Integer, primary_key=True)  # was `fid`
    bid = db.Column(db.Integer)
    tid = db.Column(db.Integer)
    title = db.Column(db.String(32))
    uid = db.Column(db.Integer)  # was `author`
    content = db.Column(db.Text)  # was `text`
    # ishtml temporarily not included
    # attachs temporarily not included
    created_at = db.Column(db.DateTime)  # was `replytime`
    updated_at = db.Column(db.DateTime)  # was `updatetime`
    signature = db.Column(db.Text)
    user_agent = db.Column(db.String(128))  # was `type`
    ip = db.Column(db.String(64))
    # lzl temporarily not included


class Comment(db.Model):
    __tablename__ = 'comments'

    cid = db.Column(db.Integer, primary_key=True)  # was `id`
    pid = db.Column(db.Integer)  # was `fid`
    uid = db.Column(db.Integer)  # was `author`
    content = db.Column(db.Text)  # was `text`
    time = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)  # was `visible`


class Message(db.Model):
    __tablename__ = 'messages'

    mid = db.Column(db.Integer, primary_key=True)
    sender_uid = db.Column(db.Integer)
    receiver_uid = db.Column(db.Integer)
    content = db.Column(db.Text)
    time = db.Column(db.DateTime)
    is_read = db.Column(db.Boolean, default=False)
    # ruser, rmsg, rbid, rtid, rpid deleted
    sender_deleted = db.Column(db.Boolean, default=False)
    receiver_deleted = db.Column(db.Boolean, default=False)


class Notification(db.Model):
    __tablename__ = 'notifications'

    nid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    ntype = db.Column(db.Integer)
    # Type of the notification: reply, at or quote
    pid = db.Column(db.Integer)
    cid = db.Column(db.Integer)
    is_read = db.Column(db.Boolean, default=False)


group_user = db.Table(
    'group_user',
    db.Column('group_id', db.Integer, db.ForeignKey('group.gid')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.uid'))
)
