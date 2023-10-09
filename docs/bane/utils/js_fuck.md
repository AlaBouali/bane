<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport">
<meta content="pdoc 0.10.0" name="generator"/>
<title>bane.utils.js_fuck API documentation</title>
<meta content="" name="description"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/sanitize.min.css" integrity="sha256-PK9q560IAAa6WVRRh76LtCaI8pjTJ2z11v0miyNNjrs=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/typography.min.css" integrity="sha256-7l/o7C8jubJiy74VsKTidCy1yBkRtiUGbVkYBylBqUg=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/github.min.css" rel="stylesheet preload"/>
<style>:root{--highlight-color:#fe9}.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}h1:target,h2:target,h3:target,h4:target,h5:target,h6:target{background:var(--highlight-color);padding:.2em 0}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}dt:target .name{background:var(--highlight-color)}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}td{padding:0 .5em}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
<script crossorigin="" defer="" integrity="sha256-Uv3H6lx7dJmRfRvH8TH6kJD1TSK1aFcwgx+mdg3epi8=" src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js"></script>
<script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
</meta></head>
<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.utils.js_fuck</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">import re,random,sys

"""

I've edited this script to be compatible with python2.X/3.X 

"""

def get_dict(d):
    if  sys.version_info &lt; (3,0):
        return d.iteritems()
    else:
        return tuple(d.items())


"""
P.S: I didn't write the following class but i find it very useful to encode XSS payloads. I would like to thank the guy who did it, good job bro &lt;3
"""



class js_fuck(object):
    '''
    Encodes/Decodes Javascript using JSFuck 0.4.0
    (https://github.com/aemkei/jsfuck)

    Class variables:
    USE_CHAR_CODE   -- string used to indicate which keys in MAPPING will
                                           be encoded using their ASCII character code

    MIN                            -- int the position within MAPPING dictionary to start
                                          iterating from, for the final encoding pass

    MAX                          -- int the maximum value to iterate in MAPPING
                                         on the final encode

    SIMPLE                    -- dictionary of built-in Javascript types and values

    CONSTRUCTORS   -- dictionary of mostly Javascript data types

    MAPPING                -- dictionary of every character to be mapped and decoded

    GLOBAL                  -- string used to replace 'GLOBAL' value on final encode

    '''

    USE_CHAR_CODE = "USE_CHAR_CODE"

    MIN, MAX = 32, 126

    SIMPLE = {
        'false':      '![]',
        'true':       '!![]',
        'undefined':  '[][[]]',
        'NaN':        '+[![]]',
        'Infinity':   ('+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+'
                       '!+[]]+[+[]]+[+[]]+[+[]])')  # +"1e1000"
    }

    CONSTRUCTORS = {
        'Array':    '[]',
        'Number':   '(+[])',
        'String':   '([]+[])',
        'Boolean':  '(![])',
        'Function': '[]["fill"]',
        'RegExp':   'Function("return/"+false+"/")()'
    }

    MAPPING = {
        'a':   '(false+"")[1]',
        'b':   '([]["entries"]()+"")[2]',
        'c':   '([]["fill"]+"")[3]',
        'd':   '(undefined+"")[2]',
        'e':   '(true+"")[3]',
        'f':   '(false+"")[0]',
        'g':   '(false+[0]+String)[20]',
        'h':   '(+(101))["to"+String["name"]](21)[1]',
        'i':   '([false]+undefined)[10]',
        'j':   '([]["entries"]()+"")[3]',
        'k':   '(+(20))["to"+String["name"]](21)',
        'l':   '(false+"")[2]',
        'm':   '(Number+"")[11]',
        'n':   '(undefined+"")[1]',
        'o':   '(true+[]["fill"])[10]',
        'p':   '(+(211))["to"+String["name"]](31)[1]',
        'q':   '(+(212))["to"+String["name"]](31)[1]',
        'r':   '(true+"")[1]',
        's':   '(false+"")[3]',
        't':   '(true+"")[0]',
        'u':   '(undefined+"")[0]',
        'v':   '(+(31))["to"+String["name"]](32)',
        'w':   '(+(32))["to"+String["name"]](33)',
        'x':   '(+(101))["to"+String["name"]](34)[1]',
        'y':   '(NaN+[Infinity])[10]',
        'z':   '(+(35))["to"+String["name"]](36)',

        'A':   '(+[]+Array)[10]',
        'B':   '(+[]+Boolean)[10]',
        'C':   'Function("return escape")()(("")["italics"]())[2]',
        'D':   'Function("return escape")()([]["fill"])["slice"]("-1")',
        'E':   '(RegExp+"")[12]',
        'F':   '(+[]+Function)[10]',
        'G':   '(false+Function("return Date")()())[30]',
        'H':   USE_CHAR_CODE,
        'I':   '(Infinity+"")[0]',
        'J':   USE_CHAR_CODE,
        'K':   USE_CHAR_CODE,
        'L':   USE_CHAR_CODE,
        'M':   '(true+Function("return Date")()())[30]',
        'N':   '(NaN+"")[0]',
        'O':   '(NaN+Function("return{}")())[11]',
        'P':   USE_CHAR_CODE,
        'Q':   USE_CHAR_CODE,
        'R':   '(+[]+RegExp)[10]',
        'S':   '(+[]+String)[10]',
        'T':   '(NaN+Function("return Date")()())[30]',
        'U':   ('(NaN+Function("return{}")()["to"+String'
                '["name"]]["call"]())[11]'),
        'V':   USE_CHAR_CODE,
        'W':   USE_CHAR_CODE,
        'X':   USE_CHAR_CODE,
        'Y':   USE_CHAR_CODE,
        'Z':   USE_CHAR_CODE,

        ' ':   '(NaN+[]["fill"])[11]',
        '!':   USE_CHAR_CODE,
        '"':   '("")["fontcolor"]()[12]',
        '#':   USE_CHAR_CODE,
        '$':   USE_CHAR_CODE,
        '%':   'Function("return escape")()([]["fill"])[21]',
        '&amp;':   '("")["link"](0+")[10]',
        '\'':  USE_CHAR_CODE,
        '(':   '(undefined+[]["fill"])[22]',
        ')':   '([0]+false+[]["fill"])[20]',
        '*':   USE_CHAR_CODE,
        '+':   ('(+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]'
                '+[+!+[]]+[+[]]+[+[]])+[])[2]'),
        ',':   '([]["slice"]["call"](false+"")+"")[1]',
        '-':   '(+(.+[0000000001])+"")[2]',
        '.':   ('(+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+'
                '[]+!+[]]+[+[]])+[])[+!+[]]'),
        '/':   '(false+[0])["italics"]()[10]',
        ':':   '(RegExp()+"")[3]',
        ';':   '("")["link"](")[14]',
        '&lt;':   '("")["italics"]()[0]',
        '=':   '("")["fontcolor"]()[11]',
        '&gt;':   '("")["italics"]()[2]',
        '?':   '(RegExp()+"")[2]',
        '@':   USE_CHAR_CODE,
        '[':   '([]["entries"]()+"")[0]',
        '\\':  USE_CHAR_CODE,
        ']':   '([]["entries"]()+"")[22]',
        '^':   USE_CHAR_CODE,
        '_':   USE_CHAR_CODE,
        '`':   USE_CHAR_CODE,
        '{':   '(true+[]["fill"])[20]',
        '|':   USE_CHAR_CODE,
        '}':   '([]["fill"]+"")["slice"]("-1")',
        '~':   USE_CHAR_CODE
    }

    GLOBAL = 'Function("return this")()'

    def __init__(self, js=None):
        '''
        Checks if passed some Javascript and if so assigns an instance variable
        to that of the pass Javascript.

        Populates MAPPING dictionary with the keys corresponding encoded value.

        Keyword arguments:
        js -- string containing the encoded Javascript to be
              decoded (defualt None)

        '''
        if js:
            self.js = js

        self.__fillMissingDigits()
        self.__fillMissingChars()
        self.__replaceMap()
        self.__replaceStrings()

    def decode(self, js=None):
        '''
        Decodes JSFuck'd Javascript

        Keyword arguments:
        js -- string containing the JSFuck to be decoded (defualt None)

        Returns:
        js -- string of decoded Javascript

        '''
        if not js:
            js = self.js

        js = self.__mapping(js)

        # removes concatenation operators
        js = re.sub('\+(?!\+)', '', js)
        js = js.replace('++', '+')

        # check to see if source js is eval'd
        if '[][fill][constructor]' in js:
            js = self.uneval(js)

        self.js = js

        return js

    def encode(self, js=None, wrapWithEval=False, runInParentScope=False):
        '''
        Encodes vanilla Javascript to JSFuck obfuscated Javascript

        Keyword arguments:
        js                            -- string of unobfuscated Javascript

        wrapWithEval        -- boolean determines whether to wrap with an eval

        runInParentScope -- boolean determines whether to run in parents scope

        '''
        output = []

        if not js:
            js = self.js

            if not js:
                return ''

        regex = ''

        for i in self.SIMPLE:
            regex += i + '|'

        regex += '.'

        def inputReplacer(c):
            c = c.group()
            replacement = self.SIMPLE[c] if c in self.SIMPLE else False

            if replacement:
                output.append('[' + replacement + ']+[]')

            else:
                replacement = self.MAPPING[c] if c in self.MAPPING else False

                if replacement:
                    output.append(replacement)
                else:
                    replacement = (
                        '([]+[])[' + self.encode('constructor') + ']'
                        '[' + self.encode('fromCharCode') + ']'
                        '(' + self.encode(str(ord(c[0]))) + ')')

                    output.append(replacement)
                    self.MAPPING[c] = replacement

        re.sub(regex, inputReplacer, js)

        output = '+'.join(output)

        if re.search(r'^\d$', js):
            output += "+[]"

        if wrapWithEval:
            if runInParentScope:
                output = ('[][' + self.encode('fill') + ']'
                          '[' + self.encode('constructor') + ']'
                          '(' + self.encode('return eval') + ')()'
                          '(' + output + ')')

            else:
                output = ('[][' + self.encode('fill') + ']'
                          '[' + self.encode('constructor') + ']'
                          '(' + output + ')')

        self.js = output

        return output

    def uneval(self, js):
        '''
        Unevals a piece of Javascript wrapped with an encoded eval

        Keyword arguments:
        js -- string containing an eval wrapped string of Javascript

        Returns:
        js -- string with eval removed

        '''
        js = js.replace('[][fill][constructor](', '')
        js = js[:-2]

        ev = 'return eval)()('

        if ev in js:
            js = js[(js.find(ev) + len(ev)):]

        return js

    def __mapping(self, js):
        '''
        Iterates over MAPPING and replaces every value found with
        its corresponding key

        Keyword arguments:
        js -- string containing Javascript encoded with JSFuck

        Returns:
        js -- string of decoded Javascript

        '''
        for key, value in sorted(
                self.MAPPING.items(), key=lambda x: len(x[1]), reverse=True):
            js = js.replace(value, key)

        return js

    def __fillMissingDigits(self):
        '''
        Calculates 0-9's encoded value and adds it to MAPPING

        '''
        for number in range(10):
            output = '+[]'

            if number &gt; 0:
                output = '+!' + output

            for i in range(number - 1):
                output = '+!+[]' + output

            if number &gt; 1:
                output = output[1:]

            self.MAPPING[str(number)] = '[' + output + ']'

    def __fillMissingChars(self):
        '''
        Iterates over MAPPING and fills missing character values with a string
        containing their ascii value represented in hex

        '''
        for key in self.MAPPING:
            if self.MAPPING[key] == self.USE_CHAR_CODE:
                hexidec = hex(ord(key[0]))[2:]

                digit_search = re.findall(r'\d+', hexidec)
                letter_search = re.findall(r'[^\d+]', hexidec)

                digit = digit_search[0] if digit_search else ''
                letter = letter_search[0] if letter_search else ''

                string = ('Function("return unescape")()("%%"+(%s)+"%s")'
                          % (digit, letter))

                self.MAPPING[key] = string

    def __replaceMap(self):
        '''
        Iterates over MAPPING from MIN to MAX and replaces value with values
        found in CONSTRUCTORS and SIMPLE, as well as using digitalReplacer and
        numberReplacer to replace numeric values

        '''
        def replace(pattern, replacement):
            return re.sub(pattern, replacement, value, flags=re.I)

        def digitReplacer(x):
            return self.MAPPING[x.group(1)]

        def numberReplacer(y):
            values = list(y.group(1))
            head = int(values[0])
            output = '+[]'

            values.pop(0)

            if head &gt; 0:
                output = '+!' + output

            for i in range(1, head):
                output = '+!+[]' + output

            if head &gt; 1:
                output = output[1:]

            return re.sub(r'(\d)', digitReplacer, '+'.join([output] + values))

        for i in range(self.MIN, self.MAX + 1):
            character = chr(i)
            value = self.MAPPING[character]

            original = ''

            if not value:
                continue

            while value != original:
                original = value

                for key, val in get_dict(self.CONSTRUCTORS):
                    value = replace(r'\b' + key, val + '["constructor"]')

                for key, val in get_dict(self.SIMPLE):
                    value = replace(key, val)

            value = replace(r'(\d\d+)', numberReplacer)
            value = replace(r'\((\d)\)', digitReplacer)
            value = replace(r'\[(\d)\]', digitReplacer)

            value = replace(r'GLOBAL', self.GLOBAL)
            value = replace(r'\+""', '+[]')
            value = replace(r'""', '[]+[]')

            self.MAPPING[character] = value

    def __replaceStrings(self):
        '''
        Replaces strings added in __replaceMap with there encoded values

        '''
        regex = r'[^\[\]\(\)\!\+]'

        # determines if there are still characters to replace
        def findMissing():
            done = False
            # python 2 workaround for nonlocal
            findMissing.missing = {}

            for key, value in get_dict(self.MAPPING):
                if re.findall(regex, value):
                    findMissing.missing[key] = value
                    done = True

            return done

        def mappingReplacer(x):
            return '+'.join(list(x.group(1)))

        def valueReplacer(x):
            x = x.group()
            return x if x in findMissing.missing else self.MAPPING[x]

        for key in self.MAPPING:
            self.MAPPING[key] = re.sub(r'\"([^\"]+)\"', mappingReplacer,
                                       self.MAPPING[key], flags=re.I)

        while findMissing():
            for key in findMissing.missing:
                value = self.MAPPING[key]
                value = re.sub(regex, valueReplacer, value)

                self.MAPPING[key] = value
                findMissing.missing[key] = value</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.utils.js_fuck.get_dict"><code class="name flex">
<span>def <span class="ident">get_dict</span></span>(<span>d)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_dict(d):
    if  sys.version_info &lt; (3,0):
        return d.iteritems()
    else:
        return tuple(d.items())</code></pre>
</details>
</dd>
</dl>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="bane.utils.js_fuck.js_fuck"><code class="flex name class">
<span>class <span class="ident">js_fuck</span></span>
<span>(</span><span>js=None)</span>
</code></dt>
<dd>
<div class="desc"><p>Encodes/Decodes Javascript using JSFuck 0.4.0
(<a href="https://github.com/aemkei/jsfuck">https://github.com/aemkei/jsfuck</a>)</p>
<p>Class variables:
USE_CHAR_CODE
– string used to indicate which keys in MAPPING will
be encoded using their ASCII character code</p>
<p>MIN
– int the position within MAPPING dictionary to start
iterating from, for the final encoding pass</p>
<p>MAX
– int the maximum value to iterate in MAPPING
on the final encode</p>
<p>SIMPLE
– dictionary of built-in Javascript types and values</p>
<p>CONSTRUCTORS
– dictionary of mostly Javascript data types</p>
<p>MAPPING
– dictionary of every character to be mapped and decoded</p>
<p>GLOBAL
– string used to replace 'GLOBAL' value on final encode</p>
<p>Checks if passed some Javascript and if so assigns an instance variable
to that of the pass Javascript.</p>
<p>Populates MAPPING dictionary with the keys corresponding encoded value.</p>
<p>Keyword arguments:
js – string containing the encoded Javascript to be
decoded (defualt None)</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class js_fuck(object):
    '''
    Encodes/Decodes Javascript using JSFuck 0.4.0
    (https://github.com/aemkei/jsfuck)

    Class variables:
    USE_CHAR_CODE   -- string used to indicate which keys in MAPPING will
                                           be encoded using their ASCII character code

    MIN                            -- int the position within MAPPING dictionary to start
                                          iterating from, for the final encoding pass

    MAX                          -- int the maximum value to iterate in MAPPING
                                         on the final encode

    SIMPLE                    -- dictionary of built-in Javascript types and values

    CONSTRUCTORS   -- dictionary of mostly Javascript data types

    MAPPING                -- dictionary of every character to be mapped and decoded

    GLOBAL                  -- string used to replace 'GLOBAL' value on final encode

    '''

    USE_CHAR_CODE = "USE_CHAR_CODE"

    MIN, MAX = 32, 126

    SIMPLE = {
        'false':      '![]',
        'true':       '!![]',
        'undefined':  '[][[]]',
        'NaN':        '+[![]]',
        'Infinity':   ('+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+'
                       '!+[]]+[+[]]+[+[]]+[+[]])')  # +"1e1000"
    }

    CONSTRUCTORS = {
        'Array':    '[]',
        'Number':   '(+[])',
        'String':   '([]+[])',
        'Boolean':  '(![])',
        'Function': '[]["fill"]',
        'RegExp':   'Function("return/"+false+"/")()'
    }

    MAPPING = {
        'a':   '(false+"")[1]',
        'b':   '([]["entries"]()+"")[2]',
        'c':   '([]["fill"]+"")[3]',
        'd':   '(undefined+"")[2]',
        'e':   '(true+"")[3]',
        'f':   '(false+"")[0]',
        'g':   '(false+[0]+String)[20]',
        'h':   '(+(101))["to"+String["name"]](21)[1]',
        'i':   '([false]+undefined)[10]',
        'j':   '([]["entries"]()+"")[3]',
        'k':   '(+(20))["to"+String["name"]](21)',
        'l':   '(false+"")[2]',
        'm':   '(Number+"")[11]',
        'n':   '(undefined+"")[1]',
        'o':   '(true+[]["fill"])[10]',
        'p':   '(+(211))["to"+String["name"]](31)[1]',
        'q':   '(+(212))["to"+String["name"]](31)[1]',
        'r':   '(true+"")[1]',
        's':   '(false+"")[3]',
        't':   '(true+"")[0]',
        'u':   '(undefined+"")[0]',
        'v':   '(+(31))["to"+String["name"]](32)',
        'w':   '(+(32))["to"+String["name"]](33)',
        'x':   '(+(101))["to"+String["name"]](34)[1]',
        'y':   '(NaN+[Infinity])[10]',
        'z':   '(+(35))["to"+String["name"]](36)',

        'A':   '(+[]+Array)[10]',
        'B':   '(+[]+Boolean)[10]',
        'C':   'Function("return escape")()(("")["italics"]())[2]',
        'D':   'Function("return escape")()([]["fill"])["slice"]("-1")',
        'E':   '(RegExp+"")[12]',
        'F':   '(+[]+Function)[10]',
        'G':   '(false+Function("return Date")()())[30]',
        'H':   USE_CHAR_CODE,
        'I':   '(Infinity+"")[0]',
        'J':   USE_CHAR_CODE,
        'K':   USE_CHAR_CODE,
        'L':   USE_CHAR_CODE,
        'M':   '(true+Function("return Date")()())[30]',
        'N':   '(NaN+"")[0]',
        'O':   '(NaN+Function("return{}")())[11]',
        'P':   USE_CHAR_CODE,
        'Q':   USE_CHAR_CODE,
        'R':   '(+[]+RegExp)[10]',
        'S':   '(+[]+String)[10]',
        'T':   '(NaN+Function("return Date")()())[30]',
        'U':   ('(NaN+Function("return{}")()["to"+String'
                '["name"]]["call"]())[11]'),
        'V':   USE_CHAR_CODE,
        'W':   USE_CHAR_CODE,
        'X':   USE_CHAR_CODE,
        'Y':   USE_CHAR_CODE,
        'Z':   USE_CHAR_CODE,

        ' ':   '(NaN+[]["fill"])[11]',
        '!':   USE_CHAR_CODE,
        '"':   '("")["fontcolor"]()[12]',
        '#':   USE_CHAR_CODE,
        '$':   USE_CHAR_CODE,
        '%':   'Function("return escape")()([]["fill"])[21]',
        '&amp;':   '("")["link"](0+")[10]',
        '\'':  USE_CHAR_CODE,
        '(':   '(undefined+[]["fill"])[22]',
        ')':   '([0]+false+[]["fill"])[20]',
        '*':   USE_CHAR_CODE,
        '+':   ('(+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]'
                '+[+!+[]]+[+[]]+[+[]])+[])[2]'),
        ',':   '([]["slice"]["call"](false+"")+"")[1]',
        '-':   '(+(.+[0000000001])+"")[2]',
        '.':   ('(+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+'
                '[]+!+[]]+[+[]])+[])[+!+[]]'),
        '/':   '(false+[0])["italics"]()[10]',
        ':':   '(RegExp()+"")[3]',
        ';':   '("")["link"](")[14]',
        '&lt;':   '("")["italics"]()[0]',
        '=':   '("")["fontcolor"]()[11]',
        '&gt;':   '("")["italics"]()[2]',
        '?':   '(RegExp()+"")[2]',
        '@':   USE_CHAR_CODE,
        '[':   '([]["entries"]()+"")[0]',
        '\\':  USE_CHAR_CODE,
        ']':   '([]["entries"]()+"")[22]',
        '^':   USE_CHAR_CODE,
        '_':   USE_CHAR_CODE,
        '`':   USE_CHAR_CODE,
        '{':   '(true+[]["fill"])[20]',
        '|':   USE_CHAR_CODE,
        '}':   '([]["fill"]+"")["slice"]("-1")',
        '~':   USE_CHAR_CODE
    }

    GLOBAL = 'Function("return this")()'

    def __init__(self, js=None):
        '''
        Checks if passed some Javascript and if so assigns an instance variable
        to that of the pass Javascript.

        Populates MAPPING dictionary with the keys corresponding encoded value.

        Keyword arguments:
        js -- string containing the encoded Javascript to be
              decoded (defualt None)

        '''
        if js:
            self.js = js

        self.__fillMissingDigits()
        self.__fillMissingChars()
        self.__replaceMap()
        self.__replaceStrings()

    def decode(self, js=None):
        '''
        Decodes JSFuck'd Javascript

        Keyword arguments:
        js -- string containing the JSFuck to be decoded (defualt None)

        Returns:
        js -- string of decoded Javascript

        '''
        if not js:
            js = self.js

        js = self.__mapping(js)

        # removes concatenation operators
        js = re.sub('\+(?!\+)', '', js)
        js = js.replace('++', '+')

        # check to see if source js is eval'd
        if '[][fill][constructor]' in js:
            js = self.uneval(js)

        self.js = js

        return js

    def encode(self, js=None, wrapWithEval=False, runInParentScope=False):
        '''
        Encodes vanilla Javascript to JSFuck obfuscated Javascript

        Keyword arguments:
        js                            -- string of unobfuscated Javascript

        wrapWithEval        -- boolean determines whether to wrap with an eval

        runInParentScope -- boolean determines whether to run in parents scope

        '''
        output = []

        if not js:
            js = self.js

            if not js:
                return ''

        regex = ''

        for i in self.SIMPLE:
            regex += i + '|'

        regex += '.'

        def inputReplacer(c):
            c = c.group()
            replacement = self.SIMPLE[c] if c in self.SIMPLE else False

            if replacement:
                output.append('[' + replacement + ']+[]')

            else:
                replacement = self.MAPPING[c] if c in self.MAPPING else False

                if replacement:
                    output.append(replacement)
                else:
                    replacement = (
                        '([]+[])[' + self.encode('constructor') + ']'
                        '[' + self.encode('fromCharCode') + ']'
                        '(' + self.encode(str(ord(c[0]))) + ')')

                    output.append(replacement)
                    self.MAPPING[c] = replacement

        re.sub(regex, inputReplacer, js)

        output = '+'.join(output)

        if re.search(r'^\d$', js):
            output += "+[]"

        if wrapWithEval:
            if runInParentScope:
                output = ('[][' + self.encode('fill') + ']'
                          '[' + self.encode('constructor') + ']'
                          '(' + self.encode('return eval') + ')()'
                          '(' + output + ')')

            else:
                output = ('[][' + self.encode('fill') + ']'
                          '[' + self.encode('constructor') + ']'
                          '(' + output + ')')

        self.js = output

        return output

    def uneval(self, js):
        '''
        Unevals a piece of Javascript wrapped with an encoded eval

        Keyword arguments:
        js -- string containing an eval wrapped string of Javascript

        Returns:
        js -- string with eval removed

        '''
        js = js.replace('[][fill][constructor](', '')
        js = js[:-2]

        ev = 'return eval)()('

        if ev in js:
            js = js[(js.find(ev) + len(ev)):]

        return js

    def __mapping(self, js):
        '''
        Iterates over MAPPING and replaces every value found with
        its corresponding key

        Keyword arguments:
        js -- string containing Javascript encoded with JSFuck

        Returns:
        js -- string of decoded Javascript

        '''
        for key, value in sorted(
                self.MAPPING.items(), key=lambda x: len(x[1]), reverse=True):
            js = js.replace(value, key)

        return js

    def __fillMissingDigits(self):
        '''
        Calculates 0-9's encoded value and adds it to MAPPING

        '''
        for number in range(10):
            output = '+[]'

            if number &gt; 0:
                output = '+!' + output

            for i in range(number - 1):
                output = '+!+[]' + output

            if number &gt; 1:
                output = output[1:]

            self.MAPPING[str(number)] = '[' + output + ']'

    def __fillMissingChars(self):
        '''
        Iterates over MAPPING and fills missing character values with a string
        containing their ascii value represented in hex

        '''
        for key in self.MAPPING:
            if self.MAPPING[key] == self.USE_CHAR_CODE:
                hexidec = hex(ord(key[0]))[2:]

                digit_search = re.findall(r'\d+', hexidec)
                letter_search = re.findall(r'[^\d+]', hexidec)

                digit = digit_search[0] if digit_search else ''
                letter = letter_search[0] if letter_search else ''

                string = ('Function("return unescape")()("%%"+(%s)+"%s")'
                          % (digit, letter))

                self.MAPPING[key] = string

    def __replaceMap(self):
        '''
        Iterates over MAPPING from MIN to MAX and replaces value with values
        found in CONSTRUCTORS and SIMPLE, as well as using digitalReplacer and
        numberReplacer to replace numeric values

        '''
        def replace(pattern, replacement):
            return re.sub(pattern, replacement, value, flags=re.I)

        def digitReplacer(x):
            return self.MAPPING[x.group(1)]

        def numberReplacer(y):
            values = list(y.group(1))
            head = int(values[0])
            output = '+[]'

            values.pop(0)

            if head &gt; 0:
                output = '+!' + output

            for i in range(1, head):
                output = '+!+[]' + output

            if head &gt; 1:
                output = output[1:]

            return re.sub(r'(\d)', digitReplacer, '+'.join([output] + values))

        for i in range(self.MIN, self.MAX + 1):
            character = chr(i)
            value = self.MAPPING[character]

            original = ''

            if not value:
                continue

            while value != original:
                original = value

                for key, val in get_dict(self.CONSTRUCTORS):
                    value = replace(r'\b' + key, val + '["constructor"]')

                for key, val in get_dict(self.SIMPLE):
                    value = replace(key, val)

            value = replace(r'(\d\d+)', numberReplacer)
            value = replace(r'\((\d)\)', digitReplacer)
            value = replace(r'\[(\d)\]', digitReplacer)

            value = replace(r'GLOBAL', self.GLOBAL)
            value = replace(r'\+""', '+[]')
            value = replace(r'""', '[]+[]')

            self.MAPPING[character] = value

    def __replaceStrings(self):
        '''
        Replaces strings added in __replaceMap with there encoded values

        '''
        regex = r'[^\[\]\(\)\!\+]'

        # determines if there are still characters to replace
        def findMissing():
            done = False
            # python 2 workaround for nonlocal
            findMissing.missing = {}

            for key, value in get_dict(self.MAPPING):
                if re.findall(regex, value):
                    findMissing.missing[key] = value
                    done = True

            return done

        def mappingReplacer(x):
            return '+'.join(list(x.group(1)))

        def valueReplacer(x):
            x = x.group()
            return x if x in findMissing.missing else self.MAPPING[x]

        for key in self.MAPPING:
            self.MAPPING[key] = re.sub(r'\"([^\"]+)\"', mappingReplacer,
                                       self.MAPPING[key], flags=re.I)

        while findMissing():
            for key in findMissing.missing:
                value = self.MAPPING[key]
                value = re.sub(regex, valueReplacer, value)

                self.MAPPING[key] = value
                findMissing.missing[key] = value</code></pre>
</details>
<h3>Class variables</h3>
<dl>
<dt id="bane.utils.js_fuck.js_fuck.CONSTRUCTORS"><code class="name">var <span class="ident">CONSTRUCTORS</span></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt id="bane.utils.js_fuck.js_fuck.GLOBAL"><code class="name">var <span class="ident">GLOBAL</span></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt id="bane.utils.js_fuck.js_fuck.MAPPING"><code class="name">var <span class="ident">MAPPING</span></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt id="bane.utils.js_fuck.js_fuck.MAX"><code class="name">var <span class="ident">MAX</span></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt id="bane.utils.js_fuck.js_fuck.MIN"><code class="name">var <span class="ident">MIN</span></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt id="bane.utils.js_fuck.js_fuck.SIMPLE"><code class="name">var <span class="ident">SIMPLE</span></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt id="bane.utils.js_fuck.js_fuck.USE_CHAR_CODE"><code class="name">var <span class="ident">USE_CHAR_CODE</span></code></dt>
<dd>
<div class="desc"></div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="bane.utils.js_fuck.js_fuck.decode"><code class="name flex">
<span>def <span class="ident">decode</span></span>(<span>self, js=None)</span>
</code></dt>
<dd>
<div class="desc"><p>Decodes JSFuck'd Javascript</p>
<p>Keyword arguments:
js – string containing the JSFuck to be decoded (defualt None)</p>
<p>Returns:
js – string of decoded Javascript</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def decode(self, js=None):
    '''
    Decodes JSFuck'd Javascript

    Keyword arguments:
    js -- string containing the JSFuck to be decoded (defualt None)

    Returns:
    js -- string of decoded Javascript

    '''
    if not js:
        js = self.js

    js = self.__mapping(js)

    # removes concatenation operators
    js = re.sub('\+(?!\+)', '', js)
    js = js.replace('++', '+')

    # check to see if source js is eval'd
    if '[][fill][constructor]' in js:
        js = self.uneval(js)

    self.js = js

    return js</code></pre>
</details>
</dd>
<dt id="bane.utils.js_fuck.js_fuck.encode"><code class="name flex">
<span>def <span class="ident">encode</span></span>(<span>self, js=None, wrapWithEval=False, runInParentScope=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Encodes vanilla Javascript to JSFuck obfuscated Javascript</p>
<p>Keyword arguments:
js
– string of unobfuscated Javascript</p>
<p>wrapWithEval
– boolean determines whether to wrap with an eval</p>
<p>runInParentScope – boolean determines whether to run in parents scope</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def encode(self, js=None, wrapWithEval=False, runInParentScope=False):
    '''
    Encodes vanilla Javascript to JSFuck obfuscated Javascript

    Keyword arguments:
    js                            -- string of unobfuscated Javascript

    wrapWithEval        -- boolean determines whether to wrap with an eval

    runInParentScope -- boolean determines whether to run in parents scope

    '''
    output = []

    if not js:
        js = self.js

        if not js:
            return ''

    regex = ''

    for i in self.SIMPLE:
        regex += i + '|'

    regex += '.'

    def inputReplacer(c):
        c = c.group()
        replacement = self.SIMPLE[c] if c in self.SIMPLE else False

        if replacement:
            output.append('[' + replacement + ']+[]')

        else:
            replacement = self.MAPPING[c] if c in self.MAPPING else False

            if replacement:
                output.append(replacement)
            else:
                replacement = (
                    '([]+[])[' + self.encode('constructor') + ']'
                    '[' + self.encode('fromCharCode') + ']'
                    '(' + self.encode(str(ord(c[0]))) + ')')

                output.append(replacement)
                self.MAPPING[c] = replacement

    re.sub(regex, inputReplacer, js)

    output = '+'.join(output)

    if re.search(r'^\d$', js):
        output += "+[]"

    if wrapWithEval:
        if runInParentScope:
            output = ('[][' + self.encode('fill') + ']'
                      '[' + self.encode('constructor') + ']'
                      '(' + self.encode('return eval') + ')()'
                      '(' + output + ')')

        else:
            output = ('[][' + self.encode('fill') + ']'
                      '[' + self.encode('constructor') + ']'
                      '(' + output + ')')

    self.js = output

    return output</code></pre>
</details>
</dd>
<dt id="bane.utils.js_fuck.js_fuck.uneval"><code class="name flex">
<span>def <span class="ident">uneval</span></span>(<span>self, js)</span>
</code></dt>
<dd>
<div class="desc"><p>Unevals a piece of Javascript wrapped with an encoded eval</p>
<p>Keyword arguments:
js – string containing an eval wrapped string of Javascript</p>
<p>Returns:
js – string with eval removed</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def uneval(self, js):
    '''
    Unevals a piece of Javascript wrapped with an encoded eval

    Keyword arguments:
    js -- string containing an eval wrapped string of Javascript

    Returns:
    js -- string with eval removed

    '''
    js = js.replace('[][fill][constructor](', '')
    js = js[:-2]

    ev = 'return eval)()('

    if ev in js:
        js = js[(js.find(ev) + len(ev)):]

    return js</code></pre>
</details>
</dd>
</dl>
</dd>
</dl>
</section>
</article>
<nav id="sidebar">
<h1>Index</h1>
<div class="toc">
<ul></ul>
</div>
<ul id="index">
<li><h3>Super-module</h3>
<ul>
<li><code><a href="index.md" title="bane.utils">bane.utils</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a href="#bane.utils.js_fuck.get_dict" title="bane.utils.js_fuck.get_dict">get_dict</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a href="#bane.utils.js_fuck.js_fuck" title="bane.utils.js_fuck.js_fuck">js_fuck</a></code></h4>
<ul class="two-column">
<li><code><a href="#bane.utils.js_fuck.js_fuck.CONSTRUCTORS" title="bane.utils.js_fuck.js_fuck.CONSTRUCTORS">CONSTRUCTORS</a></code></li>
<li><code><a href="#bane.utils.js_fuck.js_fuck.GLOBAL" title="bane.utils.js_fuck.js_fuck.GLOBAL">GLOBAL</a></code></li>
<li><code><a href="#bane.utils.js_fuck.js_fuck.MAPPING" title="bane.utils.js_fuck.js_fuck.MAPPING">MAPPING</a></code></li>
<li><code><a href="#bane.utils.js_fuck.js_fuck.MAX" title="bane.utils.js_fuck.js_fuck.MAX">MAX</a></code></li>
<li><code><a href="#bane.utils.js_fuck.js_fuck.MIN" title="bane.utils.js_fuck.js_fuck.MIN">MIN</a></code></li>
<li><code><a href="#bane.utils.js_fuck.js_fuck.SIMPLE" title="bane.utils.js_fuck.js_fuck.SIMPLE">SIMPLE</a></code></li>
<li><code><a href="#bane.utils.js_fuck.js_fuck.USE_CHAR_CODE" title="bane.utils.js_fuck.js_fuck.USE_CHAR_CODE">USE_CHAR_CODE</a></code></li>
<li><code><a href="#bane.utils.js_fuck.js_fuck.decode" title="bane.utils.js_fuck.js_fuck.decode">decode</a></code></li>
<li><code><a href="#bane.utils.js_fuck.js_fuck.encode" title="bane.utils.js_fuck.js_fuck.encode">encode</a></code></li>
<li><code><a href="#bane.utils.js_fuck.js_fuck.uneval" title="bane.utils.js_fuck.js_fuck.uneval">uneval</a></code></li>
</ul>
</li>
</ul>
</li>
</ul>
</nav>
</main>
<footer id="footer">
<p>Generated by <a href="https://pdoc3.github.io/pdoc" title="pdoc: Python API documentation generator"><cite>pdoc</cite> 0.10.0</a>.</p>
</footer>
</body>
</html>