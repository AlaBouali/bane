<h1>Flutter_Scanner Class</h1>

<p>Class that provides a static method for scanning Flutter installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Flutter installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'flutter' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Flutter to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Flutter_Scanner</code> class, call the <code>scan</code> method with the Flutter version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Flutter_Scanner

# Scan Flutter for vulnerabilities
flutter_vulnerabilities = Flutter_Scanner.scan(
    version="2.8.1",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Flutter Vulnerabilities:", flutter_vulnerabilities)
</code></pre>

<h1>React_Native_Scanner Class</h1>

<p>Class that provides a static method for scanning React Native installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans React Native installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'facebook' and 'react-native' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of React Native to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>React_Native_Scanner</code> class, call the <code>scan</code> method with the React Native version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import React_Native_Scanner

# Scan React Native for vulnerabilities
react_native_vulnerabilities = React_Native_Scanner.scan(
    version="0.66.3",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("React Native Vulnerabilities:", react_native_vulnerabilities)
</code></pre>
