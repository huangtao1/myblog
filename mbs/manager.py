# -*- coding:utf-8 -*-
# Created by mark.huang on 2019/6/25
from base import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
import os

app = create_app(os.getenv('MBS_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command('shell', Shell(make_shell_context))
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
