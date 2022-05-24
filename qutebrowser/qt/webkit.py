# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:
# FIXME:qt6
# pylint: disable=missing-module-docstring,wildcard-import
# flake8: noqa

from qutebrowser.qt import machinery


if machinery.USE_PYQT5:
    from PyQt5.QtWebKit import *
elif machinery.USE_PYQT6:
    raise machinery.Unavailable()
elif machinery.USE_PYSIDE2:
    raise machinery.Unavailable()
elif machinery.USE_PYSIDE6:
    raise machinery.Unavailable()
else:
    raise machinery.UnknownWrapper()