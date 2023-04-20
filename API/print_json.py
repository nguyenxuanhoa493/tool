
import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter


def PJ(data):
    json_str = json.dumps(data, indent=4, sort_keys=True,ensure_ascii=False).encode('utf8')
    print(highlight(json_str, JsonLexer(), TerminalFormatter()))