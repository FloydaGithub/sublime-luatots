#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

import re

# [comment by Floyda] filePath = sys.argv[1]
# [comment by Floyda] # filePath = "ActivityCtrl"
# [comment by Floyda] # 检查是否为Unity转cc
# [comment by Floyda] isU2cc = '-u2cc' in sys.argv

# [comment by Floyda] with open(filePath + ".lua", "r") as f:
# [comment by Floyda]     print filePath
# [comment by Floyda]     file = f.read()
# [comment by Floyda]     className = filePath
# [comment by Floyda]     if className:
# [comment by Floyda]         print "export class", className

# [comment by Floyda]         # 块注释
# [comment by Floyda]         content = re.sub(r"--\[\[((.*\n)*?.*?)\]\]", "/*\\1*/", file)
# [comment by Floyda]         # 类
# [comment by Floyda]         content = re.sub(r"\b(.*) = \{\}\nlocal this = \1\n", "export class " + className + "{\n", content)
# [comment by Floyda]         content = re.sub(r"" + className + "\.", "this.", content)
# [comment by Floyda]         # 局部变量
# [comment by Floyda]         content = re.sub(r"[\t|\s]local(.*=)", "\tlet\\1", content)
# [comment by Floyda]         # 成员变量
# [comment by Floyda]         content = re.sub(r"\blocal m_(.*)", "private _\\1", content)
# [comment by Floyda]         content = re.sub(r"([^(private)]) m_(\w+)", "\\1this._\\2", content)
# [comment by Floyda]         if isU2cc:
# [comment by Floyda]             content = re.sub(r"_transform", "node", content)
# [comment by Floyda]         # 整体缩进
# [comment by Floyda]         content = re.sub(r"\n", "\n\t", content)
# [comment by Floyda]         # 类结束
# [comment by Floyda]         content = content + "\n}"
# [comment by Floyda]         # 符号
# [comment by Floyda]         content = re.sub(r"\n\t*\band\b", "&&", content)
# [comment by Floyda]         content = re.sub(r"\sand\s", " && ", content)
# [comment by Floyda]         content = re.sub(r"\n\t*\bor\b", "||", content)
# [comment by Floyda]         content = re.sub(r"\sor\s", " || ", content)
# [comment by Floyda]         content = re.sub(r"\bnot ", "!", content)
# [comment by Floyda]         content = re.sub(r"\.\.", "+", content)
# [comment by Floyda]         content = re.sub(r"~=", "!=", content)
# [comment by Floyda]         content = re.sub(r"#((\w|\.)*)", "\\1.length", content)
# [comment by Floyda]         # for if
# [comment by Floyda]         content = re.sub(r"\bfor (\w)( = \d),\s*(.*)\s*do", "for (let \\1\\2; \\1 < \\3; ++\\1) {", content)
# [comment by Floyda]         content = re.sub(r"\bif((.*\n)*?.*?)then", "if (\\1) {", content)
# [comment by Floyda]         content = re.sub(r"\belseif(.*)then", "} else if (\\1) {", content)
# [comment by Floyda]         content = re.sub(r"\belse(\t*)\n", "} else {\n", content)
# [comment by Floyda]         content = re.sub(r"--(.*\n)", "//\\1", content)
# [comment by Floyda]         content = re.sub(r"\bend\s*\n", "}\n", content)
# [comment by Floyda]         # 函数
# [comment by Floyda]         content = re.sub(r"\bfunction " + className + r"[\.|:](.*)", "\\1 {", content)
# [comment by Floyda]         content = re.sub(r"\bfunction this[\.|:](.*)", "\\1 {", content)
# [comment by Floyda]         content = re.sub(r"(\bfunction\(.*\))(.*)\n", "\\1{\\2\n", content)
# [comment by Floyda]         content = re.sub(r"end(,|\)|\s.*)", "}\\1", content)
# [comment by Floyda]         content = re.sub(r"New(\(\) {)", "constructor\\1", content)
# [comment by Floyda]         content = re.sub(r"string\.gsub\((.*?), (.*?), (.*)\)", "\\1.replace(\\2, \\3)", content)
# [comment by Floyda]         content = re.sub(r"string\.find\((.*),([^\)]*)\)", "\\1.includes(\\2)", content)
# [comment by Floyda]         content = re.sub(r"[\t|\s]log\(", "console.log(", content)

# [comment by Floyda]         if isU2cc:
# [comment by Floyda]             content = re.sub(r":GetComponent", ".getComponent", content)
# [comment by Floyda]             content = re.sub(r"'UILabel'", "cc.Label", content)
# [comment by Floyda]             content = re.sub(r"\.text = ", ".string = ", content)
# [comment by Floyda]             content = re.sub(r"'UIScrollView'", "cc.ScrollView", content)
# [comment by Floyda]             content = re.sub(r"\.gameObject", "", content)
# [comment by Floyda]             content = re.sub(r"\.transform", "", content)
# [comment by Floyda]             content = re.sub(r":Find\(\"(.*)\"", ":Find('\\1'",content)
# [comment by Floyda]             content = re.sub(r"(\w+(\.\w+)*?):Find\(('\w+(\/\w+)+')\)", "cc.find(\\3, \\1)", content)
# [comment by Floyda]             content = re.sub(r"(\w+(\.\w+)*?):Find\(('.*')\)", "\\1.getChildByName(\\3)", content)
# [comment by Floyda]             content = re.sub(r":SetActive\((.*)\)", ".active = \\1", content)
# [comment by Floyda]             content = re.sub(r"\.activeSelf", ".active", content)
# [comment by Floyda]             content = re.sub(r":GetChild\((.*)\)", ".children[\\1]", content)
# [comment by Floyda]             # 自用
# [comment by Floyda]             content = re.sub(r"Util.ClearChild\((.*)\)", "\\1.removeAllChildren()", content)
# [comment by Floyda]             content = re.sub(r"NGUITools.AddChild", "Utils.addChild", content)
# [comment by Floyda]             content = re.sub(r"\w(.*):AddClick\((.*),(.*this\.(\w+))\)", 'Utils.addClickEvent(\\2, this.node, \'' + className + '\', \'\\4\')', content)
# [comment by Floyda]             content = re.sub(r"\btonumber\(", "Number(", content)
# [comment by Floyda]             content = re.sub(r"\btostring\(", "String(", content)
# [comment by Floyda]             content = re.sub(r"LuaTableManager\.AddTable", "DataTable.loadTable", content)
# [comment by Floyda]             content = re.sub(r"\blog(\(.*\))", "console.log\\1", content)
# [comment by Floyda]             content = re.sub(r"\bUI_SystemPrompt.Open_Prompt_\d", "cc.vv.alert", content)

# [comment by Floyda]         # nil 转 null
# [comment by Floyda]         content = re.sub(r"nil", "null", content)

# [comment by Floyda]         with open(filePath + ".ts", "w") as f:
# [comment by Floyda]             f.write(content)


def luatots(content):
    content = re.sub(r"--\[\[((.*\n)*?.*?)\]\]", "/*\\1*/", content)
    content = re.sub(r"--", "// ", content)
    # and/or/not/../~=/#
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
    # for if
    # [comment by Floyda] content = re.sub(r"\bfor\s+(\w+)(\s*= \d),\s*(.*)\s*do", "for (let \\1\\2; \\1 <= \\3; ++\\1) {", content)
    # content = re.sub(r"\bfor\s+([a..zA..Z0..9])\s*=\s*([a..zA..Z0..9])\s*,\s*([a..zA..Z0..9])\s+do", "for (\\1= ) {", content)
    content = re.sub(r"\bfor\s+(\w+)\s*=\s*(\w+),\s*(\w+)\s*do",
                     "for (var \\1 = \\2; \\1 <= \\3; ++\\1) {", content)
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

    content = re.sub(r"\bprint\b", "console.log", content)

    return content
