# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:
# FIXME:qt6
# pylint: disable=missing-module-docstring,import-error,wildcard-import,unused-wildcard-import
# flake8: noqa

from qutebrowser.qt import machinery


if machinery.USE_PYQT5:
    from PyQt5.QtSql import *
elif machinery.USE_PYQT6:
    from PyQt6.QtSql import *
elif machinery.USE_PYSIDE2:
    from PySide2.QtSql import *
elif machinery.USE_PYSIDE6:
    from PySide6.QtSql import *