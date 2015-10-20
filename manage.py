#!/usr/bin/env python
# coding: utf-8
from flask import Flask
from flask.ext.script import Manager
from app.app import create_app

manager = Manager(create_app)

if __name__ == '__main__':
    manager.run()