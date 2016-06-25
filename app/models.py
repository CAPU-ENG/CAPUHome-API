#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: models.py
Author: huxuan <i(at)huxuan.org>
Description: Models for app.
"""
from app import db


group_user = db.Table(
    'group_user',
    db.Column('group_id', db.Integer, db.ForeignKey('groups.gid')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.uid'))
)


class User(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    birthday = db.Column(db.Date)
    student_id = db.Column(db.String(16))
    name = db.Column(db.String(16))
    tel = db.Column(db.String(16))
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32), nullable=False)
    gender = db.Column(db.Boolean, nullable=False)
    avatar = db.Column(db.String(32))
    intro = db.Column(db.Text)
    sig1 = db.Column(db.Text)
    sig2 = db.Column(db.Text)
    sig3 = db.Column(db.Text)
    hobby = db.Column(db.Text)
    qq = db.Column(db.String(16))
    mail = db.Column(db.String(64))
    wechat = db.Column(db.String(64))
    province = db.Column(db.String(8))
    registration_date = db.Column(db.Date)
    last_login_time = db.Column(db.DateTime)
    last_post_time = db.Column(db.DateTime)
    star = db.Column(db.Integer, default=1)
    num_featured = db.Column(db.Integer)
    num_post = db.Column(db.Integer, default=0)
    num_reply = db.Column(db.Integer, default=0)
    num_water = db.Column(db.Integer, default=0)
    num_sign = db.Column(db.Integer, default=0)
    current_board = db.Column(db.Integer)
    user_agent = db.Column(db.String(128))

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    threads = db.relationship('Thread', backref='author', lazy='dynamic')
    groups = db.relationship(
        'Group',
        backref=db.backref('users', lazy='dynamic'),
        secondary=group_user,
        lazy='dynamic'
    )


class Group(db.Model):
    __tablename__ = 'groups'

    gid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    uid = db.Column(db.Integer)
    created_date = db.Column(db.Date)
    deleted = db.Column(db.Boolean, default=False)


class Board(db.Model):
    __tablename__ = 'boards'

    bid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    invisible = db.Column(db.Boolean, default=False)


class Thread(db.Model):
    __tablename__ = 'threads'

    tid = db.Column(db.Integer, primary_key=True)
    author_uid = db.Column(db.Integer, db.ForeignKey('users.uid'))
    bid = db.Column(db.Integer)
    title = db.Column(db.String(64))
    replier_uid = db.Column(db.Integer)
    num_click = db.Column(db.Integer, default=0)
    num_reply = db.Column(db.Integer, default=0)
    featured = db.Column(db.Boolean, default=False)
    sticky = db.Column(db.Boolean, default=False)
    locked = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
    replied_at = db.Column(db.DateTime)


class Post(db.Model):
    __tablename__ = 'posts'

    pid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('users.uid'))
    bid = db.Column(db.Integer)
    tid = db.Column(db.Integer)
    title = db.Column(db.String(32))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    signature = db.Column(db.Text)
    user_agent = db.Column(db.String(128))
    ip = db.Column(db.String(64))
    parse_type = db.Column(db.String(16))


class Comment(db.Model):
    __tablename__ = 'comments'

    cid = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    content = db.Column(db.Text)
    time = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)


class Message(db.Model):
    __tablename__ = 'messages'

    mid = db.Column(db.Integer, primary_key=True)
    sender_uid = db.Column(db.Integer)
    receiver_uid = db.Column(db.Integer)
    content = db.Column(db.Text)
    time = db.Column(db.DateTime)
    is_read = db.Column(db.Boolean, default=False)
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
