#!/usr/bin/python3
import sys
assert sys.version_info[0] == 3

from pandocfilters import toJSONFilter, RawBlock
import re

def minted_filter(key, value, frmat, meta):
    """ Modifing codeblock

    Args:
        key   => type of pandoc object. In json its key is "t"
        value => contents of pandoc object. In json its key is "c"
        frmat => target output format
        meta  => document metadata
    """

    # if frmat != "latex" or key != "CodeBlock":
    if key != "CodeBlock":
        return

    [[_, classes, _], contents] = value

    if len(classes) > 0:
        splt_cls = classes[0].split(":")
        title    = splt_cls[1] if len(splt_cls) >= 2 else ""
        lang     = splt_cls[0]
    else:
        title    = ""
        lang     = "text"

    title = re.sub(r"_", "\\_", title)
    lang  = re.sub(r"_", "\\_", lang)

    replaced = """\
\\begin{{spacing}}{{1.0}} {title}\n\
\\begin{{mdframed}}\n\
\\begin{{minted}}[breaklines, linenos]{{{lang}}}\n\
{contents}\n\
\\end{{minted}}\n\
\\end{{mdframed}}\n\
\\end{{spacing}}""".format(title=title, lang=lang, contents=contents)

    return [RawBlock(frmat, replaced)]

if __name__ == "__main__":
    toJSONFilter(minted_filter)
