import subprocess
import sublime, sublime_plugin

class LassoCheckSyntaxCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        file_regex = "^Parser error. ([^:])*: (.*?)line: (\\d+), col: (\\d+).*$"

        cmd  = ['/usr/bin/lassoc', self.window.active_view().file_name(), '-n', '-o', '/dev/null']
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = proc.communicate()[0].decode("utf-8") or "No Problems Found"

        self.window.run_command("exec", {"cmd": ["echo", data], "file_regex": file_regex})

    def is_enabled(self, **kwargs):
        return True