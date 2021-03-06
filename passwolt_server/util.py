"""
Utilities
"""


import colorama
import json
import os
import textwrap

from os.path import expanduser


colorama.init()    # needed for Windows OS -_-


STYLE = {
    'blue': colorama.Fore.LIGHTBLUE_EX,
    'cyan': colorama.Fore.LIGHTCYAN_EX,
    'green': colorama.Fore.LIGHTGREEN_EX,
    'red': colorama.Fore.LIGHTRED_EX,
    'yellow': colorama.Fore.LIGHTYELLOW_EX,
    'endc': colorama.Style.RESET_ALL,
    'bold': colorama.Style.BRIGHT
}
PASSWOLT_METADATA_DIR = os.path.join(expanduser("~"), ".passwolt")
SERVER_CONFIG_PATH = os.path.join(PASSWOLT_METADATA_DIR, "server.json")


def display(text, dedent=True, style=None, end_char=None):
    """
    Handles linux and windows command prompt display
    """
    start = ''
    end = ''
    if style:
        start = ''.join(map(lambda x: STYLE[x], style))
        end   = STYLE['endc']
    if dedent:
        text = textwrap.dedent(text)
    if end_char:
        print(f'{start}{text}{end}', end=end_char)
    else:
        print(f'{start}{text}{end}')


class Question(object):
    """
    Ask a Question.
    """
    def __init__(self, text, choices=None, default_choice=None, style=None):
        self._text = text
        style = style or {}
        self._text_style = style.pop('text', [])
        self._text_style = ''.join(map(lambda x: STYLE[x], self._text_style))
        self._choices = choices
        self._default_choice = default_choice
        if self._choices:
            assert self._default_choice in self._choices
            self._choices_style = style.pop('choices', [])
            self._choices_style = ''.join(
                map(lambda x: STYLE[x], self._choices_style)
            )
            self._default_choice_style = style.pop('default_choice', ['bold'])
            self._default_choice_style = ''.join(
                map(lambda x: STYLE[x], self._default_choice_style)
            )

        # At last, construct the question!
        self._ques = self._create_ques()

    def _create_ques(self):
        ques = f'{self._text_style}{self._text}{STYLE["endc"]}'
        if not self._choices:
            return ques

        self._choices.remove(self._default_choice)
        choices = (
            f'[{self._default_choice_style}{self._default_choice}{STYLE["endc"]}'
            f' | '
            f'{" | ".join(map(lambda x: self._choices_style + x + STYLE["endc"], self._choices))}]'
        )
        ques = f'{ques} {choices}'
        return ques

    def __str__(self):
        return self._ques

    def prompt(self):
        display(self._ques, end_char=' ')
        ans = input()
        if not ans:
            ans = self._default_choice
        return ans


def store_config(data):
    """
    Store the config file
    """
    if not os.path.exists(SERVER_CONFIG_PATH):
        # Create the necessary directories
        pdir = os.path.dirname(SERVER_CONFIG_PATH)
        os.makedirs(pdir)
    with open(SERVER_CONFIG_PATH, 'w') as f:
        json.dump(data, f)
