#!/usr/bin/env python
# coding: utf-8

"""
Gettext. Translation system.
"""

import os
import locale
import gettext

from Paths import TRANSLATION_DIR

APP_NAME = "guicavane"


def configure_gettext():
    """ Configures gettext and returns the
    gettext to be used. """

    langs = []

    lc, _ = locale.getdefaultlocale()
    if lc:
        langs.append(lc)

    language = os.environ.get("LANGUAGE", None)
    if language:
        langs += language.split(":")

    gettext.bindtextdomain(APP_NAME, TRANSLATION_DIR)
    gettext.textdomain(APP_NAME)

    lang = gettext.translation(APP_NAME, TRANSLATION_DIR,
                               languages=langs, fallback=True)

    return lang.gettext

gettext = configure_gettext()
