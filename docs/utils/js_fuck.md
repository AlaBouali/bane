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

&#34;&#34;&#34;

I&#39;ve edited this script to be compatible with python2.X/3.X 

&#34;&#34;&#34;

def get_dict(d):
    if  sys.version_info &lt; (3,0):
        return d.iteritems()
    else:
        return tuple(d.items())


&#34;&#34;&#34;
P.S: I didn&#39;t write the following class but i find it very useful to encode XSS payloads. I would like to thank the guy who did it, good job bro &lt;3
&#34;&#34;&#34;



class js_fuck(object):
    &#39;&#39;&#39;
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

    GLOBAL                  -- string used to replace &#39;GLOBAL&#39; value on final encode

    &#39;&#39;&#39;

    USE_CHAR_CODE = &#34;USE_CHAR_CODE&#34;

    MIN, MAX = 32, 126

    SIMPLE = {
        &#39;false&#39;:      &#39;![]&#39;,
        &#39;true&#39;:       &#39;!![]&#39;,
        &#39;undefined&#39;:  &#39;[][[]]&#39;,
        &#39;NaN&#39;:        &#39;+[![]]&#39;,
        &#39;Infinity&#39;:   (&#39;+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+&#39;
                       &#39;!+[]]+[+[]]+[+[]]+[+[]])&#39;)  # +&#34;1e1000&#34;
    }

    CONSTRUCTORS = {
        &#39;Array&#39;:    &#39;[]&#39;,
        &#39;Number&#39;:   &#39;(+[])&#39;,
        &#39;String&#39;:   &#39;([]+[])&#39;,
        &#39;Boolean&#39;:  &#39;(![])&#39;,
        &#39;Function&#39;: &#39;[][&#34;fill&#34;]&#39;,
        &#39;RegExp&#39;:   &#39;Function(&#34;return/&#34;+false+&#34;/&#34;)()&#39;
    }

    MAPPING = {
        &#39;a&#39;:   &#39;(false+&#34;&#34;)[1]&#39;,
        &#39;b&#39;:   &#39;([][&#34;entries&#34;]()+&#34;&#34;)[2]&#39;,
        &#39;c&#39;:   &#39;([][&#34;fill&#34;]+&#34;&#34;)[3]&#39;,
        &#39;d&#39;:   &#39;(undefined+&#34;&#34;)[2]&#39;,
        &#39;e&#39;:   &#39;(true+&#34;&#34;)[3]&#39;,
        &#39;f&#39;:   &#39;(false+&#34;&#34;)[0]&#39;,
        &#39;g&#39;:   &#39;(false+[0]+String)[20]&#39;,
        &#39;h&#39;:   &#39;(+(101))[&#34;to&#34;+String[&#34;name&#34;]](21)[1]&#39;,
        &#39;i&#39;:   &#39;([false]+undefined)[10]&#39;,
        &#39;j&#39;:   &#39;([][&#34;entries&#34;]()+&#34;&#34;)[3]&#39;,
        &#39;k&#39;:   &#39;(+(20))[&#34;to&#34;+String[&#34;name&#34;]](21)&#39;,
        &#39;l&#39;:   &#39;(false+&#34;&#34;)[2]&#39;,
        &#39;m&#39;:   &#39;(Number+&#34;&#34;)[11]&#39;,
        &#39;n&#39;:   &#39;(undefined+&#34;&#34;)[1]&#39;,
        &#39;o&#39;:   &#39;(true+[][&#34;fill&#34;])[10]&#39;,
        &#39;p&#39;:   &#39;(+(211))[&#34;to&#34;+String[&#34;name&#34;]](31)[1]&#39;,
        &#39;q&#39;:   &#39;(+(212))[&#34;to&#34;+String[&#34;name&#34;]](31)[1]&#39;,
        &#39;r&#39;:   &#39;(true+&#34;&#34;)[1]&#39;,
        &#39;s&#39;:   &#39;(false+&#34;&#34;)[3]&#39;,
        &#39;t&#39;:   &#39;(true+&#34;&#34;)[0]&#39;,
        &#39;u&#39;:   &#39;(undefined+&#34;&#34;)[0]&#39;,
        &#39;v&#39;:   &#39;(+(31))[&#34;to&#34;+String[&#34;name&#34;]](32)&#39;,
        &#39;w&#39;:   &#39;(+(32))[&#34;to&#34;+String[&#34;name&#34;]](33)&#39;,
        &#39;x&#39;:   &#39;(+(101))[&#34;to&#34;+String[&#34;name&#34;]](34)[1]&#39;,
        &#39;y&#39;:   &#39;(NaN+[Infinity])[10]&#39;,
        &#39;z&#39;:   &#39;(+(35))[&#34;to&#34;+String[&#34;name&#34;]](36)&#39;,

        &#39;A&#39;:   &#39;(+[]+Array)[10]&#39;,
        &#39;B&#39;:   &#39;(+[]+Boolean)[10]&#39;,
        &#39;C&#39;:   &#39;Function(&#34;return escape&#34;)()((&#34;&#34;)[&#34;italics&#34;]())[2]&#39;,
        &#39;D&#39;:   &#39;Function(&#34;return escape&#34;)()([][&#34;fill&#34;])[&#34;slice&#34;](&#34;-1&#34;)&#39;,
        &#39;E&#39;:   &#39;(RegExp+&#34;&#34;)[12]&#39;,
        &#39;F&#39;:   &#39;(+[]+Function)[10]&#39;,
        &#39;G&#39;:   &#39;(false+Function(&#34;return Date&#34;)()())[30]&#39;,
        &#39;H&#39;:   USE_CHAR_CODE,
        &#39;I&#39;:   &#39;(Infinity+&#34;&#34;)[0]&#39;,
        &#39;J&#39;:   USE_CHAR_CODE,
        &#39;K&#39;:   USE_CHAR_CODE,
        &#39;L&#39;:   USE_CHAR_CODE,
        &#39;M&#39;:   &#39;(true+Function(&#34;return Date&#34;)()())[30]&#39;,
        &#39;N&#39;:   &#39;(NaN+&#34;&#34;)[0]&#39;,
        &#39;O&#39;:   &#39;(NaN+Function(&#34;return{}&#34;)())[11]&#39;,
        &#39;P&#39;:   USE_CHAR_CODE,
        &#39;Q&#39;:   USE_CHAR_CODE,
        &#39;R&#39;:   &#39;(+[]+RegExp)[10]&#39;,
        &#39;S&#39;:   &#39;(+[]+String)[10]&#39;,
        &#39;T&#39;:   &#39;(NaN+Function(&#34;return Date&#34;)()())[30]&#39;,
        &#39;U&#39;:   (&#39;(NaN+Function(&#34;return{}&#34;)()[&#34;to&#34;+String&#39;
                &#39;[&#34;name&#34;]][&#34;call&#34;]())[11]&#39;),
        &#39;V&#39;:   USE_CHAR_CODE,
        &#39;W&#39;:   USE_CHAR_CODE,
        &#39;X&#39;:   USE_CHAR_CODE,
        &#39;Y&#39;:   USE_CHAR_CODE,
        &#39;Z&#39;:   USE_CHAR_CODE,

        &#39; &#39;:   &#39;(NaN+[][&#34;fill&#34;])[11]&#39;,
        &#39;!&#39;:   USE_CHAR_CODE,
        &#39;&#34;&#39;:   &#39;(&#34;&#34;)[&#34;fontcolor&#34;]()[12]&#39;,
        &#39;#&#39;:   USE_CHAR_CODE,
        &#39;$&#39;:   USE_CHAR_CODE,
        &#39;%&#39;:   &#39;Function(&#34;return escape&#34;)()([][&#34;fill&#34;])[21]&#39;,
        &#39;&amp;&#39;:   &#39;(&#34;&#34;)[&#34;link&#34;](0+&#34;)[10]&#39;,
        &#39;\&#39;&#39;:  USE_CHAR_CODE,
        &#39;(&#39;:   &#39;(undefined+[][&#34;fill&#34;])[22]&#39;,
        &#39;)&#39;:   &#39;([0]+false+[][&#34;fill&#34;])[20]&#39;,
        &#39;*&#39;:   USE_CHAR_CODE,
        &#39;+&#39;:   (&#39;(+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]&#39;
                &#39;+[+!+[]]+[+[]]+[+[]])+[])[2]&#39;),
        &#39;,&#39;:   &#39;([][&#34;slice&#34;][&#34;call&#34;](false+&#34;&#34;)+&#34;&#34;)[1]&#39;,
        &#39;-&#39;:   &#39;(+(.+[0000000001])+&#34;&#34;)[2]&#39;,
        &#39;.&#39;:   (&#39;(+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+&#39;
                &#39;[]+!+[]]+[+[]])+[])[+!+[]]&#39;),
        &#39;/&#39;:   &#39;(false+[0])[&#34;italics&#34;]()[10]&#39;,
        &#39;:&#39;:   &#39;(RegExp()+&#34;&#34;)[3]&#39;,
        &#39;;&#39;:   &#39;(&#34;&#34;)[&#34;link&#34;](&#34;)[14]&#39;,
        &#39;&lt;&#39;:   &#39;(&#34;&#34;)[&#34;italics&#34;]()[0]&#39;,
        &#39;=&#39;:   &#39;(&#34;&#34;)[&#34;fontcolor&#34;]()[11]&#39;,
        &#39;&gt;&#39;:   &#39;(&#34;&#34;)[&#34;italics&#34;]()[2]&#39;,
        &#39;?&#39;:   &#39;(RegExp()+&#34;&#34;)[2]&#39;,
        &#39;@&#39;:   USE_CHAR_CODE,
        &#39;[&#39;:   &#39;([][&#34;entries&#34;]()+&#34;&#34;)[0]&#39;,
        &#39;\\&#39;:  USE_CHAR_CODE,
        &#39;]&#39;:   &#39;([][&#34;entries&#34;]()+&#34;&#34;)[22]&#39;,
        &#39;^&#39;:   USE_CHAR_CODE,
        &#39;_&#39;:   USE_CHAR_CODE,
        &#39;`&#39;:   USE_CHAR_CODE,
        &#39;{&#39;:   &#39;(true+[][&#34;fill&#34;])[20]&#39;,
        &#39;|&#39;:   USE_CHAR_CODE,
        &#39;}&#39;:   &#39;([][&#34;fill&#34;]+&#34;&#34;)[&#34;slice&#34;](&#34;-1&#34;)&#39;,
        &#39;~&#39;:   USE_CHAR_CODE
    }

    GLOBAL = &#39;Function(&#34;return this&#34;)()&#39;

    def __init__(self, js=None):
        &#39;&#39;&#39;
        Checks if passed some Javascript and if so assigns an instance variable
        to that of the pass Javascript.

        Populates MAPPING dictionary with the keys corresponding encoded value.

        Keyword arguments:
        js -- string containing the encoded Javascript to be
              decoded (defualt None)

        &#39;&#39;&#39;
        if js:
            self.js = js

        self.__fillMissingDigits()
        self.__fillMissingChars()
        self.__replaceMap()
        self.__replaceStrings()

    def decode(self, js=None):
        &#39;&#39;&#39;
        Decodes JSFuck&#39;d Javascript

        Keyword arguments:
        js -- string containing the JSFuck to be decoded (defualt None)

        Returns:
        js -- string of decoded Javascript

        &#39;&#39;&#39;
        if not js:
            js = self.js

        js = self.__mapping(js)

        # removes concatenation operators
        js = re.sub(&#39;\+(?!\+)&#39;, &#39;&#39;, js)
        js = js.replace(&#39;++&#39;, &#39;+&#39;)

        # check to see if source js is eval&#39;d
        if &#39;[][fill][constructor]&#39; in js:
            js = self.uneval(js)

        self.js = js

        return js

    def encode(self, js=None, wrapWithEval=False, runInParentScope=False):
        &#39;&#39;&#39;
        Encodes vanilla Javascript to JSFuck obfuscated Javascript

        Keyword arguments:
        js                            -- string of unobfuscated Javascript

        wrapWithEval        -- boolean determines whether to wrap with an eval

        runInParentScope -- boolean determines whether to run in parents scope

        &#39;&#39;&#39;
        output = []

        if not js:
            js = self.js

            if not js:
                return &#39;&#39;

        regex = &#39;&#39;

        for i in self.SIMPLE:
            regex += i + &#39;|&#39;

        regex += &#39;.&#39;

        def inputReplacer(c):
            c = c.group()
            replacement = self.SIMPLE[c] if c in self.SIMPLE else False

            if replacement:
                output.append(&#39;[&#39; + replacement + &#39;]+[]&#39;)

            else:
                replacement = self.MAPPING[c] if c in self.MAPPING else False

                if replacement:
                    output.append(replacement)
                else:
                    replacement = (
                        &#39;([]+[])[&#39; + self.encode(&#39;constructor&#39;) + &#39;]&#39;
                        &#39;[&#39; + self.encode(&#39;fromCharCode&#39;) + &#39;]&#39;
                        &#39;(&#39; + self.encode(str(ord(c[0]))) + &#39;)&#39;)

                    output.append(replacement)
                    self.MAPPING[c] = replacement

        re.sub(regex, inputReplacer, js)

        output = &#39;+&#39;.join(output)

        if re.search(r&#39;^\d$&#39;, js):
            output += &#34;+[]&#34;

        if wrapWithEval:
            if runInParentScope:
                output = (&#39;[][&#39; + self.encode(&#39;fill&#39;) + &#39;]&#39;
                          &#39;[&#39; + self.encode(&#39;constructor&#39;) + &#39;]&#39;
                          &#39;(&#39; + self.encode(&#39;return eval&#39;) + &#39;)()&#39;
                          &#39;(&#39; + output + &#39;)&#39;)

            else:
                output = (&#39;[][&#39; + self.encode(&#39;fill&#39;) + &#39;]&#39;
                          &#39;[&#39; + self.encode(&#39;constructor&#39;) + &#39;]&#39;
                          &#39;(&#39; + output + &#39;)&#39;)

        self.js = output

        return output

    def uneval(self, js):
        &#39;&#39;&#39;
        Unevals a piece of Javascript wrapped with an encoded eval

        Keyword arguments:
        js -- string containing an eval wrapped string of Javascript

        Returns:
        js -- string with eval removed

        &#39;&#39;&#39;
        js = js.replace(&#39;[][fill][constructor](&#39;, &#39;&#39;)
        js = js[:-2]

        ev = &#39;return eval)()(&#39;

        if ev in js:
            js = js[(js.find(ev) + len(ev)):]

        return js

    def __mapping(self, js):
        &#39;&#39;&#39;
        Iterates over MAPPING and replaces every value found with
        its corresponding key

        Keyword arguments:
        js -- string containing Javascript encoded with JSFuck

        Returns:
        js -- string of decoded Javascript

        &#39;&#39;&#39;
        for key, value in sorted(
                self.MAPPING.items(), key=lambda x: len(x[1]), reverse=True):
            js = js.replace(value, key)

        return js

    def __fillMissingDigits(self):
        &#39;&#39;&#39;
        Calculates 0-9&#39;s encoded value and adds it to MAPPING

        &#39;&#39;&#39;
        for number in range(10):
            output = &#39;+[]&#39;

            if number &gt; 0:
                output = &#39;+!&#39; + output

            for i in range(number - 1):
                output = &#39;+!+[]&#39; + output

            if number &gt; 1:
                output = output[1:]

            self.MAPPING[str(number)] = &#39;[&#39; + output + &#39;]&#39;

    def __fillMissingChars(self):
        &#39;&#39;&#39;
        Iterates over MAPPING and fills missing character values with a string
        containing their ascii value represented in hex

        &#39;&#39;&#39;
        for key in self.MAPPING:
            if self.MAPPING[key] == self.USE_CHAR_CODE:
                hexidec = hex(ord(key[0]))[2:]

                digit_search = re.findall(r&#39;\d+&#39;, hexidec)
                letter_search = re.findall(r&#39;[^\d+]&#39;, hexidec)

                digit = digit_search[0] if digit_search else &#39;&#39;
                letter = letter_search[0] if letter_search else &#39;&#39;

                string = (&#39;Function(&#34;return unescape&#34;)()(&#34;%%&#34;+(%s)+&#34;%s&#34;)&#39;
                          % (digit, letter))

                self.MAPPING[key] = string

    def __replaceMap(self):
        &#39;&#39;&#39;
        Iterates over MAPPING from MIN to MAX and replaces value with values
        found in CONSTRUCTORS and SIMPLE, as well as using digitalReplacer and
        numberReplacer to replace numeric values

        &#39;&#39;&#39;
        def replace(pattern, replacement):
            return re.sub(pattern, replacement, value, flags=re.I)

        def digitReplacer(x):
            return self.MAPPING[x.group(1)]

        def numberReplacer(y):
            values = list(y.group(1))
            head = int(values[0])
            output = &#39;+[]&#39;

            values.pop(0)

            if head &gt; 0:
                output = &#39;+!&#39; + output

            for i in range(1, head):
                output = &#39;+!+[]&#39; + output

            if head &gt; 1:
                output = output[1:]

            return re.sub(r&#39;(\d)&#39;, digitReplacer, &#39;+&#39;.join([output] + values))

        for i in range(self.MIN, self.MAX + 1):
            character = chr(i)
            value = self.MAPPING[character]

            original = &#39;&#39;

            if not value:
                continue

            while value != original:
                original = value

                for key, val in get_dict(self.CONSTRUCTORS):
                    value = replace(r&#39;\b&#39; + key, val + &#39;[&#34;constructor&#34;]&#39;)

                for key, val in get_dict(self.SIMPLE):
                    value = replace(key, val)

            value = replace(r&#39;(\d\d+)&#39;, numberReplacer)
            value = replace(r&#39;\((\d)\)&#39;, digitReplacer)
            value = replace(r&#39;\[(\d)\]&#39;, digitReplacer)

            value = replace(r&#39;GLOBAL&#39;, self.GLOBAL)
            value = replace(r&#39;\+&#34;&#34;&#39;, &#39;+[]&#39;)
            value = replace(r&#39;&#34;&#34;&#39;, &#39;[]+[]&#39;)

            self.MAPPING[character] = value

    def __replaceStrings(self):
        &#39;&#39;&#39;
        Replaces strings added in __replaceMap with there encoded values

        &#39;&#39;&#39;
        regex = r&#39;[^\[\]\(\)\!\+]&#39;

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
            return &#39;+&#39;.join(list(x.group(1)))

        def valueReplacer(x):
            x = x.group()
            return x if x in findMissing.missing else self.MAPPING[x]

        for key in self.MAPPING:
            self.MAPPING[key] = re.sub(r&#39;\&#34;([^\&#34;]+)\&#34;&#39;, mappingReplacer,
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
&ndash; string used to indicate which keys in MAPPING will
be encoded using their ASCII character code</p>
<p>MIN
&ndash; int the position within MAPPING dictionary to start
iterating from, for the final encoding pass</p>
<p>MAX
&ndash; int the maximum value to iterate in MAPPING
on the final encode</p>
<p>SIMPLE
&ndash; dictionary of built-in Javascript types and values</p>
<p>CONSTRUCTORS
&ndash; dictionary of mostly Javascript data types</p>
<p>MAPPING
&ndash; dictionary of every character to be mapped and decoded</p>
<p>GLOBAL
&ndash; string used to replace 'GLOBAL' value on final encode</p>
<p>Checks if passed some Javascript and if so assigns an instance variable
to that of the pass Javascript.</p>
<p>Populates MAPPING dictionary with the keys corresponding encoded value.</p>
<p>Keyword arguments:
js &ndash; string containing the encoded Javascript to be
decoded (defualt None)</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class js_fuck(object):
    &#39;&#39;&#39;
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

    GLOBAL                  -- string used to replace &#39;GLOBAL&#39; value on final encode

    &#39;&#39;&#39;

    USE_CHAR_CODE = &#34;USE_CHAR_CODE&#34;

    MIN, MAX = 32, 126

    SIMPLE = {
        &#39;false&#39;:      &#39;![]&#39;,
        &#39;true&#39;:       &#39;!![]&#39;,
        &#39;undefined&#39;:  &#39;[][[]]&#39;,
        &#39;NaN&#39;:        &#39;+[![]]&#39;,
        &#39;Infinity&#39;:   (&#39;+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+&#39;
                       &#39;!+[]]+[+[]]+[+[]]+[+[]])&#39;)  # +&#34;1e1000&#34;
    }

    CONSTRUCTORS = {
        &#39;Array&#39;:    &#39;[]&#39;,
        &#39;Number&#39;:   &#39;(+[])&#39;,
        &#39;String&#39;:   &#39;([]+[])&#39;,
        &#39;Boolean&#39;:  &#39;(![])&#39;,
        &#39;Function&#39;: &#39;[][&#34;fill&#34;]&#39;,
        &#39;RegExp&#39;:   &#39;Function(&#34;return/&#34;+false+&#34;/&#34;)()&#39;
    }

    MAPPING = {
        &#39;a&#39;:   &#39;(false+&#34;&#34;)[1]&#39;,
        &#39;b&#39;:   &#39;([][&#34;entries&#34;]()+&#34;&#34;)[2]&#39;,
        &#39;c&#39;:   &#39;([][&#34;fill&#34;]+&#34;&#34;)[3]&#39;,
        &#39;d&#39;:   &#39;(undefined+&#34;&#34;)[2]&#39;,
        &#39;e&#39;:   &#39;(true+&#34;&#34;)[3]&#39;,
        &#39;f&#39;:   &#39;(false+&#34;&#34;)[0]&#39;,
        &#39;g&#39;:   &#39;(false+[0]+String)[20]&#39;,
        &#39;h&#39;:   &#39;(+(101))[&#34;to&#34;+String[&#34;name&#34;]](21)[1]&#39;,
        &#39;i&#39;:   &#39;([false]+undefined)[10]&#39;,
        &#39;j&#39;:   &#39;([][&#34;entries&#34;]()+&#34;&#34;)[3]&#39;,
        &#39;k&#39;:   &#39;(+(20))[&#34;to&#34;+String[&#34;name&#34;]](21)&#39;,
        &#39;l&#39;:   &#39;(false+&#34;&#34;)[2]&#39;,
        &#39;m&#39;:   &#39;(Number+&#34;&#34;)[11]&#39;,
        &#39;n&#39;:   &#39;(undefined+&#34;&#34;)[1]&#39;,
        &#39;o&#39;:   &#39;(true+[][&#34;fill&#34;])[10]&#39;,
        &#39;p&#39;:   &#39;(+(211))[&#34;to&#34;+String[&#34;name&#34;]](31)[1]&#39;,
        &#39;q&#39;:   &#39;(+(212))[&#34;to&#34;+String[&#34;name&#34;]](31)[1]&#39;,
        &#39;r&#39;:   &#39;(true+&#34;&#34;)[1]&#39;,
        &#39;s&#39;:   &#39;(false+&#34;&#34;)[3]&#39;,
        &#39;t&#39;:   &#39;(true+&#34;&#34;)[0]&#39;,
        &#39;u&#39;:   &#39;(undefined+&#34;&#34;)[0]&#39;,
        &#39;v&#39;:   &#39;(+(31))[&#34;to&#34;+String[&#34;name&#34;]](32)&#39;,
        &#39;w&#39;:   &#39;(+(32))[&#34;to&#34;+String[&#34;name&#34;]](33)&#39;,
        &#39;x&#39;:   &#39;(+(101))[&#34;to&#34;+String[&#34;name&#34;]](34)[1]&#39;,
        &#39;y&#39;:   &#39;(NaN+[Infinity])[10]&#39;,
        &#39;z&#39;:   &#39;(+(35))[&#34;to&#34;+String[&#34;name&#34;]](36)&#39;,

        &#39;A&#39;:   &#39;(+[]+Array)[10]&#39;,
        &#39;B&#39;:   &#39;(+[]+Boolean)[10]&#39;,
        &#39;C&#39;:   &#39;Function(&#34;return escape&#34;)()((&#34;&#34;)[&#34;italics&#34;]())[2]&#39;,
        &#39;D&#39;:   &#39;Function(&#34;return escape&#34;)()([][&#34;fill&#34;])[&#34;slice&#34;](&#34;-1&#34;)&#39;,
        &#39;E&#39;:   &#39;(RegExp+&#34;&#34;)[12]&#39;,
        &#39;F&#39;:   &#39;(+[]+Function)[10]&#39;,
        &#39;G&#39;:   &#39;(false+Function(&#34;return Date&#34;)()())[30]&#39;,
        &#39;H&#39;:   USE_CHAR_CODE,
        &#39;I&#39;:   &#39;(Infinity+&#34;&#34;)[0]&#39;,
        &#39;J&#39;:   USE_CHAR_CODE,
        &#39;K&#39;:   USE_CHAR_CODE,
        &#39;L&#39;:   USE_CHAR_CODE,
        &#39;M&#39;:   &#39;(true+Function(&#34;return Date&#34;)()())[30]&#39;,
        &#39;N&#39;:   &#39;(NaN+&#34;&#34;)[0]&#39;,
        &#39;O&#39;:   &#39;(NaN+Function(&#34;return{}&#34;)())[11]&#39;,
        &#39;P&#39;:   USE_CHAR_CODE,
        &#39;Q&#39;:   USE_CHAR_CODE,
        &#39;R&#39;:   &#39;(+[]+RegExp)[10]&#39;,
        &#39;S&#39;:   &#39;(+[]+String)[10]&#39;,
        &#39;T&#39;:   &#39;(NaN+Function(&#34;return Date&#34;)()())[30]&#39;,
        &#39;U&#39;:   (&#39;(NaN+Function(&#34;return{}&#34;)()[&#34;to&#34;+String&#39;
                &#39;[&#34;name&#34;]][&#34;call&#34;]())[11]&#39;),
        &#39;V&#39;:   USE_CHAR_CODE,
        &#39;W&#39;:   USE_CHAR_CODE,
        &#39;X&#39;:   USE_CHAR_CODE,
        &#39;Y&#39;:   USE_CHAR_CODE,
        &#39;Z&#39;:   USE_CHAR_CODE,

        &#39; &#39;:   &#39;(NaN+[][&#34;fill&#34;])[11]&#39;,
        &#39;!&#39;:   USE_CHAR_CODE,
        &#39;&#34;&#39;:   &#39;(&#34;&#34;)[&#34;fontcolor&#34;]()[12]&#39;,
        &#39;#&#39;:   USE_CHAR_CODE,
        &#39;$&#39;:   USE_CHAR_CODE,
        &#39;%&#39;:   &#39;Function(&#34;return escape&#34;)()([][&#34;fill&#34;])[21]&#39;,
        &#39;&amp;&#39;:   &#39;(&#34;&#34;)[&#34;link&#34;](0+&#34;)[10]&#39;,
        &#39;\&#39;&#39;:  USE_CHAR_CODE,
        &#39;(&#39;:   &#39;(undefined+[][&#34;fill&#34;])[22]&#39;,
        &#39;)&#39;:   &#39;([0]+false+[][&#34;fill&#34;])[20]&#39;,
        &#39;*&#39;:   USE_CHAR_CODE,
        &#39;+&#39;:   (&#39;(+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]&#39;
                &#39;+[+!+[]]+[+[]]+[+[]])+[])[2]&#39;),
        &#39;,&#39;:   &#39;([][&#34;slice&#34;][&#34;call&#34;](false+&#34;&#34;)+&#34;&#34;)[1]&#39;,
        &#39;-&#39;:   &#39;(+(.+[0000000001])+&#34;&#34;)[2]&#39;,
        &#39;.&#39;:   (&#39;(+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+&#39;
                &#39;[]+!+[]]+[+[]])+[])[+!+[]]&#39;),
        &#39;/&#39;:   &#39;(false+[0])[&#34;italics&#34;]()[10]&#39;,
        &#39;:&#39;:   &#39;(RegExp()+&#34;&#34;)[3]&#39;,
        &#39;;&#39;:   &#39;(&#34;&#34;)[&#34;link&#34;](&#34;)[14]&#39;,
        &#39;&lt;&#39;:   &#39;(&#34;&#34;)[&#34;italics&#34;]()[0]&#39;,
        &#39;=&#39;:   &#39;(&#34;&#34;)[&#34;fontcolor&#34;]()[11]&#39;,
        &#39;&gt;&#39;:   &#39;(&#34;&#34;)[&#34;italics&#34;]()[2]&#39;,
        &#39;?&#39;:   &#39;(RegExp()+&#34;&#34;)[2]&#39;,
        &#39;@&#39;:   USE_CHAR_CODE,
        &#39;[&#39;:   &#39;([][&#34;entries&#34;]()+&#34;&#34;)[0]&#39;,
        &#39;\\&#39;:  USE_CHAR_CODE,
        &#39;]&#39;:   &#39;([][&#34;entries&#34;]()+&#34;&#34;)[22]&#39;,
        &#39;^&#39;:   USE_CHAR_CODE,
        &#39;_&#39;:   USE_CHAR_CODE,
        &#39;`&#39;:   USE_CHAR_CODE,
        &#39;{&#39;:   &#39;(true+[][&#34;fill&#34;])[20]&#39;,
        &#39;|&#39;:   USE_CHAR_CODE,
        &#39;}&#39;:   &#39;([][&#34;fill&#34;]+&#34;&#34;)[&#34;slice&#34;](&#34;-1&#34;)&#39;,
        &#39;~&#39;:   USE_CHAR_CODE
    }

    GLOBAL = &#39;Function(&#34;return this&#34;)()&#39;

    def __init__(self, js=None):
        &#39;&#39;&#39;
        Checks if passed some Javascript and if so assigns an instance variable
        to that of the pass Javascript.

        Populates MAPPING dictionary with the keys corresponding encoded value.

        Keyword arguments:
        js -- string containing the encoded Javascript to be
              decoded (defualt None)

        &#39;&#39;&#39;
        if js:
            self.js = js

        self.__fillMissingDigits()
        self.__fillMissingChars()
        self.__replaceMap()
        self.__replaceStrings()

    def decode(self, js=None):
        &#39;&#39;&#39;
        Decodes JSFuck&#39;d Javascript

        Keyword arguments:
        js -- string containing the JSFuck to be decoded (defualt None)

        Returns:
        js -- string of decoded Javascript

        &#39;&#39;&#39;
        if not js:
            js = self.js

        js = self.__mapping(js)

        # removes concatenation operators
        js = re.sub(&#39;\+(?!\+)&#39;, &#39;&#39;, js)
        js = js.replace(&#39;++&#39;, &#39;+&#39;)

        # check to see if source js is eval&#39;d
        if &#39;[][fill][constructor]&#39; in js:
            js = self.uneval(js)

        self.js = js

        return js

    def encode(self, js=None, wrapWithEval=False, runInParentScope=False):
        &#39;&#39;&#39;
        Encodes vanilla Javascript to JSFuck obfuscated Javascript

        Keyword arguments:
        js                            -- string of unobfuscated Javascript

        wrapWithEval        -- boolean determines whether to wrap with an eval

        runInParentScope -- boolean determines whether to run in parents scope

        &#39;&#39;&#39;
        output = []

        if not js:
            js = self.js

            if not js:
                return &#39;&#39;

        regex = &#39;&#39;

        for i in self.SIMPLE:
            regex += i + &#39;|&#39;

        regex += &#39;.&#39;

        def inputReplacer(c):
            c = c.group()
            replacement = self.SIMPLE[c] if c in self.SIMPLE else False

            if replacement:
                output.append(&#39;[&#39; + replacement + &#39;]+[]&#39;)

            else:
                replacement = self.MAPPING[c] if c in self.MAPPING else False

                if replacement:
                    output.append(replacement)
                else:
                    replacement = (
                        &#39;([]+[])[&#39; + self.encode(&#39;constructor&#39;) + &#39;]&#39;
                        &#39;[&#39; + self.encode(&#39;fromCharCode&#39;) + &#39;]&#39;
                        &#39;(&#39; + self.encode(str(ord(c[0]))) + &#39;)&#39;)

                    output.append(replacement)
                    self.MAPPING[c] = replacement

        re.sub(regex, inputReplacer, js)

        output = &#39;+&#39;.join(output)

        if re.search(r&#39;^\d$&#39;, js):
            output += &#34;+[]&#34;

        if wrapWithEval:
            if runInParentScope:
                output = (&#39;[][&#39; + self.encode(&#39;fill&#39;) + &#39;]&#39;
                          &#39;[&#39; + self.encode(&#39;constructor&#39;) + &#39;]&#39;
                          &#39;(&#39; + self.encode(&#39;return eval&#39;) + &#39;)()&#39;
                          &#39;(&#39; + output + &#39;)&#39;)

            else:
                output = (&#39;[][&#39; + self.encode(&#39;fill&#39;) + &#39;]&#39;
                          &#39;[&#39; + self.encode(&#39;constructor&#39;) + &#39;]&#39;
                          &#39;(&#39; + output + &#39;)&#39;)

        self.js = output

        return output

    def uneval(self, js):
        &#39;&#39;&#39;
        Unevals a piece of Javascript wrapped with an encoded eval

        Keyword arguments:
        js -- string containing an eval wrapped string of Javascript

        Returns:
        js -- string with eval removed

        &#39;&#39;&#39;
        js = js.replace(&#39;[][fill][constructor](&#39;, &#39;&#39;)
        js = js[:-2]

        ev = &#39;return eval)()(&#39;

        if ev in js:
            js = js[(js.find(ev) + len(ev)):]

        return js

    def __mapping(self, js):
        &#39;&#39;&#39;
        Iterates over MAPPING and replaces every value found with
        its corresponding key

        Keyword arguments:
        js -- string containing Javascript encoded with JSFuck

        Returns:
        js -- string of decoded Javascript

        &#39;&#39;&#39;
        for key, value in sorted(
                self.MAPPING.items(), key=lambda x: len(x[1]), reverse=True):
            js = js.replace(value, key)

        return js

    def __fillMissingDigits(self):
        &#39;&#39;&#39;
        Calculates 0-9&#39;s encoded value and adds it to MAPPING

        &#39;&#39;&#39;
        for number in range(10):
            output = &#39;+[]&#39;

            if number &gt; 0:
                output = &#39;+!&#39; + output

            for i in range(number - 1):
                output = &#39;+!+[]&#39; + output

            if number &gt; 1:
                output = output[1:]

            self.MAPPING[str(number)] = &#39;[&#39; + output + &#39;]&#39;

    def __fillMissingChars(self):
        &#39;&#39;&#39;
        Iterates over MAPPING and fills missing character values with a string
        containing their ascii value represented in hex

        &#39;&#39;&#39;
        for key in self.MAPPING:
            if self.MAPPING[key] == self.USE_CHAR_CODE:
                hexidec = hex(ord(key[0]))[2:]

                digit_search = re.findall(r&#39;\d+&#39;, hexidec)
                letter_search = re.findall(r&#39;[^\d+]&#39;, hexidec)

                digit = digit_search[0] if digit_search else &#39;&#39;
                letter = letter_search[0] if letter_search else &#39;&#39;

                string = (&#39;Function(&#34;return unescape&#34;)()(&#34;%%&#34;+(%s)+&#34;%s&#34;)&#39;
                          % (digit, letter))

                self.MAPPING[key] = string

    def __replaceMap(self):
        &#39;&#39;&#39;
        Iterates over MAPPING from MIN to MAX and replaces value with values
        found in CONSTRUCTORS and SIMPLE, as well as using digitalReplacer and
        numberReplacer to replace numeric values

        &#39;&#39;&#39;
        def replace(pattern, replacement):
            return re.sub(pattern, replacement, value, flags=re.I)

        def digitReplacer(x):
            return self.MAPPING[x.group(1)]

        def numberReplacer(y):
            values = list(y.group(1))
            head = int(values[0])
            output = &#39;+[]&#39;

            values.pop(0)

            if head &gt; 0:
                output = &#39;+!&#39; + output

            for i in range(1, head):
                output = &#39;+!+[]&#39; + output

            if head &gt; 1:
                output = output[1:]

            return re.sub(r&#39;(\d)&#39;, digitReplacer, &#39;+&#39;.join([output] + values))

        for i in range(self.MIN, self.MAX + 1):
            character = chr(i)
            value = self.MAPPING[character]

            original = &#39;&#39;

            if not value:
                continue

            while value != original:
                original = value

                for key, val in get_dict(self.CONSTRUCTORS):
                    value = replace(r&#39;\b&#39; + key, val + &#39;[&#34;constructor&#34;]&#39;)

                for key, val in get_dict(self.SIMPLE):
                    value = replace(key, val)

            value = replace(r&#39;(\d\d+)&#39;, numberReplacer)
            value = replace(r&#39;\((\d)\)&#39;, digitReplacer)
            value = replace(r&#39;\[(\d)\]&#39;, digitReplacer)

            value = replace(r&#39;GLOBAL&#39;, self.GLOBAL)
            value = replace(r&#39;\+&#34;&#34;&#39;, &#39;+[]&#39;)
            value = replace(r&#39;&#34;&#34;&#39;, &#39;[]+[]&#39;)

            self.MAPPING[character] = value

    def __replaceStrings(self):
        &#39;&#39;&#39;
        Replaces strings added in __replaceMap with there encoded values

        &#39;&#39;&#39;
        regex = r&#39;[^\[\]\(\)\!\+]&#39;

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
            return &#39;+&#39;.join(list(x.group(1)))

        def valueReplacer(x):
            x = x.group()
            return x if x in findMissing.missing else self.MAPPING[x]

        for key in self.MAPPING:
            self.MAPPING[key] = re.sub(r&#39;\&#34;([^\&#34;]+)\&#34;&#39;, mappingReplacer,
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
js &ndash; string containing the JSFuck to be decoded (defualt None)</p>
<p>Returns:
js &ndash; string of decoded Javascript</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def decode(self, js=None):
    &#39;&#39;&#39;
    Decodes JSFuck&#39;d Javascript

    Keyword arguments:
    js -- string containing the JSFuck to be decoded (defualt None)

    Returns:
    js -- string of decoded Javascript

    &#39;&#39;&#39;
    if not js:
        js = self.js

    js = self.__mapping(js)

    # removes concatenation operators
    js = re.sub(&#39;\+(?!\+)&#39;, &#39;&#39;, js)
    js = js.replace(&#39;++&#39;, &#39;+&#39;)

    # check to see if source js is eval&#39;d
    if &#39;[][fill][constructor]&#39; in js:
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
&ndash; string of unobfuscated Javascript</p>
<p>wrapWithEval
&ndash; boolean determines whether to wrap with an eval</p>
<p>runInParentScope &ndash; boolean determines whether to run in parents scope</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def encode(self, js=None, wrapWithEval=False, runInParentScope=False):
    &#39;&#39;&#39;
    Encodes vanilla Javascript to JSFuck obfuscated Javascript

    Keyword arguments:
    js                            -- string of unobfuscated Javascript

    wrapWithEval        -- boolean determines whether to wrap with an eval

    runInParentScope -- boolean determines whether to run in parents scope

    &#39;&#39;&#39;
    output = []

    if not js:
        js = self.js

        if not js:
            return &#39;&#39;

    regex = &#39;&#39;

    for i in self.SIMPLE:
        regex += i + &#39;|&#39;

    regex += &#39;.&#39;

    def inputReplacer(c):
        c = c.group()
        replacement = self.SIMPLE[c] if c in self.SIMPLE else False

        if replacement:
            output.append(&#39;[&#39; + replacement + &#39;]+[]&#39;)

        else:
            replacement = self.MAPPING[c] if c in self.MAPPING else False

            if replacement:
                output.append(replacement)
            else:
                replacement = (
                    &#39;([]+[])[&#39; + self.encode(&#39;constructor&#39;) + &#39;]&#39;
                    &#39;[&#39; + self.encode(&#39;fromCharCode&#39;) + &#39;]&#39;
                    &#39;(&#39; + self.encode(str(ord(c[0]))) + &#39;)&#39;)

                output.append(replacement)
                self.MAPPING[c] = replacement

    re.sub(regex, inputReplacer, js)

    output = &#39;+&#39;.join(output)

    if re.search(r&#39;^\d$&#39;, js):
        output += &#34;+[]&#34;

    if wrapWithEval:
        if runInParentScope:
            output = (&#39;[][&#39; + self.encode(&#39;fill&#39;) + &#39;]&#39;
                      &#39;[&#39; + self.encode(&#39;constructor&#39;) + &#39;]&#39;
                      &#39;(&#39; + self.encode(&#39;return eval&#39;) + &#39;)()&#39;
                      &#39;(&#39; + output + &#39;)&#39;)

        else:
            output = (&#39;[][&#39; + self.encode(&#39;fill&#39;) + &#39;]&#39;
                      &#39;[&#39; + self.encode(&#39;constructor&#39;) + &#39;]&#39;
                      &#39;(&#39; + output + &#39;)&#39;)

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
js &ndash; string containing an eval wrapped string of Javascript</p>
<p>Returns:
js &ndash; string with eval removed</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def uneval(self, js):
    &#39;&#39;&#39;
    Unevals a piece of Javascript wrapped with an encoded eval

    Keyword arguments:
    js -- string containing an eval wrapped string of Javascript

    Returns:
    js -- string with eval removed

    &#39;&#39;&#39;
    js = js.replace(&#39;[][fill][constructor](&#39;, &#39;&#39;)
    js = js[:-2]

    ev = &#39;return eval)()(&#39;

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
<li><code><a title="bane.utils" href="index.md">bane.utils</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.utils.js_fuck.get_dict" href="#bane.utils.js_fuck.get_dict">get_dict</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="bane.utils.js_fuck.js_fuck" href="#bane.utils.js_fuck.js_fuck">js_fuck</a></code></h4>
<ul class="two-column">
<li><code><a title="bane.utils.js_fuck.js_fuck.CONSTRUCTORS" href="#bane.utils.js_fuck.js_fuck.CONSTRUCTORS">CONSTRUCTORS</a></code></li>
<li><code><a title="bane.utils.js_fuck.js_fuck.GLOBAL" href="#bane.utils.js_fuck.js_fuck.GLOBAL">GLOBAL</a></code></li>
<li><code><a title="bane.utils.js_fuck.js_fuck.MAPPING" href="#bane.utils.js_fuck.js_fuck.MAPPING">MAPPING</a></code></li>
<li><code><a title="bane.utils.js_fuck.js_fuck.MAX" href="#bane.utils.js_fuck.js_fuck.MAX">MAX</a></code></li>
<li><code><a title="bane.utils.js_fuck.js_fuck.MIN" href="#bane.utils.js_fuck.js_fuck.MIN">MIN</a></code></li>
<li><code><a title="bane.utils.js_fuck.js_fuck.SIMPLE" href="#bane.utils.js_fuck.js_fuck.SIMPLE">SIMPLE</a></code></li>
<li><code><a title="bane.utils.js_fuck.js_fuck.USE_CHAR_CODE" href="#bane.utils.js_fuck.js_fuck.USE_CHAR_CODE">USE_CHAR_CODE</a></code></li>
<li><code><a title="bane.utils.js_fuck.js_fuck.decode" href="#bane.utils.js_fuck.js_fuck.decode">decode</a></code></li>
<li><code><a title="bane.utils.js_fuck.js_fuck.encode" href="#bane.utils.js_fuck.js_fuck.encode">encode</a></code></li>
<li><code><a title="bane.utils.js_fuck.js_fuck.uneval" href="#bane.utils.js_fuck.js_fuck.uneval">uneval</a></code></li>
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