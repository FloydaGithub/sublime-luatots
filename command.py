import sublime
import sublime_plugin

from .luatots import luatots


class LuaToTsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get lines of replacement
        region = sublime.Region(0, self.view.size())
        self.view.unfold(region)

        # get characters of view
        content = self.view.substr(region)

        self.view.replace(edit, region, luatots(content))
