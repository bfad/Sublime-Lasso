import subprocess, re
import sublime, sublime_plugin

class LassoCheckSyntaxCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        file_regex = "^Compiler error. ([^:])*: (.*?)line: (\\d+), col: (\\d+).*$"

        cmd  = ['/usr/bin/lassoc', self.window.active_view().file_name(), '-n', '-o', '/dev/null']
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = proc.communicate()[0].decode("utf-8") or "No Problems Found"

        self.window.run_command("exec", {"cmd": ["echo", data], "file_regex": file_regex})

        # Move cursor to the position of the error
        if data != "No Problems Found":
            line_col = re.compile("line: (\\d+), col: (\\d+).*$").findall(data)[0]
            row  = int(line_col[0]) - 1
            col  = int(line_col[1]) - 1
            view = self.window.active_view()

            view.sel().clear()
            view.sel().add(sublime.Region(view.text_point(row, col)))
            view.show(view.text_point(row, col))

    def is_enabled(self, **kwargs):
        return True