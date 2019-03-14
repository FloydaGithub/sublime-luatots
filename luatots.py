#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

import re


def luatots(content):
    # comment
    content = re.sub(r"--\[\[((.*\n)*?.*?)\]\]", "/*\\1*/", content)
    content = re.sub(r"--", "// ", content)
    # and / or / not / .. / ~= / #
    content = re.sub(r"\n\t*\band\b", "&&", content)
    content = re.sub(r"\sand\s", " && ", content)
    content = re.sub(r"\n\t*\bor\b", "||", content)
    content = re.sub(r"\sor\s", " || ", content)
    content = re.sub(r"\bnot ", "!", content)
    content = re.sub(r"\.\.", "+", content)
    content = re.sub(r"~=", "!=", content)
    content = re.sub(r"#((\w|\.)*)", "\\1.length", content)
    # if / then / else
    content = re.sub(r"\bif\b", " if (", content)
    content = re.sub(r"\bthen\b", " ) {", content)
    content = re.sub(r"\belse\b", "} else {", content)
    content = re.sub(r"\bend\b", "}", content)
    content = re.sub(r"\belseif", "} else if (", content)
    # for
    content = re.sub(r"\bfor\s+(\w+)\s*=\s*(\w+),\s*(\w+)\s*do",
                     "for (var \\1 = \\2; \\1 <= \\3; ++\\1) {", content)
    # for ipairs
    content = re.sub(r"\bfor\s+(\w+)\s*,(\w+)\s+in\s+ipairs\((\w+)\)\s*do",
                     "for (var \\1 in \\3) {\n\tlet \\2 = \\3[\\1]\n", content)
    # for pairs
    content = re.sub(r"\bfor\s+(\w+)\s*,(\w+)\s+in\s+pairs\((\w+)\)\s*do",
                     "for (var \\1 in \\3) {\n\tlet \\2 = \\3[\\1]\n", content)
    # nil -> null
    content = re.sub(r"\bnil\b", " null ", content)
    # : -> .
    content = re.sub(r"\b\:\b", ".", content)
    # self -> this
    content = re.sub(r"\bself\b", "this", content)
    # local -> let
    content = re.sub(r"\blocal\s", "let ", content)
    # print -> console.log
    content = re.sub(r"\bprint\b", "console.log", content)

    return content
