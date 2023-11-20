<h1>Apache_Coyote_Server_Scanner Class</h1>

<p>Class that provides a static method for scanning Apache Coyote Server installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Apache Coyote Server installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'apache' and 'coyote_http_connector' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Apache Coyote Server to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Apache_Coyote_Server_Scanner</code> class, call the <code>scan</code> method with the Apache Coyote Server version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Apache_Coyote_Server_Scanner

# Scan Apache Coyote Server for vulnerabilities
apache_coyote_server_vulnerabilities = Apache_Coyote_Server_Scanner.scan(
    version="9.0.50",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Apache Coyote Server Vulnerabilities:", apache_coyote_server_vulnerabilities)
</code></pre>
<h1>Apache_HTTP_Server_Scanner Class</h1>

<p>Class that provides a static method for scanning Apache HTTP Server installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Apache HTTP Server installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'apache' and 'http_server' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Apache HTTP Server to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Apache_HTTP_Server_Scanner</code> class, call the <code>scan</code> method with the Apache HTTP Server version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Apache_HTTP_Server_Scanner

# Scan Apache HTTP Server for vulnerabilities
apache_http_server_vulnerabilities = Apache_HTTP_Server_Scanner.scan(
    version="2.4.51",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Apache HTTP Server Vulnerabilities:", apache_http_server_vulnerabilities)
</code></pre>
<h1>Apache_Tomcat_Server_Scanner Class</h1>

<p>Class that provides a static method for scanning Apache Tomcat Server installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Apache Tomcat Server installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'apache' and 'tomcat' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Apache Tomcat Server to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Apache_Tomcat_Server_Scanner</code> class, call the <code>scan</code> method with the Apache Tomcat Server version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Apache_Tomcat_Server_Scanner

# Scan Apache Tomcat Server for vulnerabilities
apache_tomcat_server_vulnerabilities = Apache_Tomcat_Server_Scanner.scan(
    version="9.0.53",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Apache Tomcat Server Vulnerabilities:", apache_tomcat_server_vulnerabilities)
</code></pre>
<h1>GlassFish_Server_Scanner Class</h1>

<p>Class that provides a static method for scanning GlassFish Server installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans GlassFish Server installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'oracle' and 'glassfish_server' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of GlassFish Server to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>GlassFish_Server_Scanner</code> class, call the <code>scan</code> method with the GlassFish Server version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import GlassFish_Server_Scanner

# Scan GlassFish Server for vulnerabilities
glassfish_server_vulnerabilities = GlassFish_Server_Scanner.scan(
    version="5.0.1",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("GlassFish Server Vulnerabilities:", glassfish_server_vulnerabilities)
</code></pre>
<h1>Jetty_Server_Scanner Class</h1>

<p>Class that provides a static method for scanning Jetty Server installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Jetty Server installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'eclipse' and 'jetty' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Jetty Server to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Jetty_Server_Scanner</code> class, call the <code>scan</code> method with the Jetty Server version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Jetty_Server_Scanner

# Scan Jetty Server for vulnerabilities
jetty_server_vulnerabilities = Jetty_Server_Scanner.scan(
    version="9.4.42",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Jetty Server Vulnerabilities:", jetty_server_vulnerabilities)
</code></pre>
<h1>Microsoft_IIS_Server_Scanner Class</h1>

<p>Class that provides a static method for scanning Microsoft IIS Server installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Microsoft IIS Server installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'microsoft' and 'iis' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Microsoft IIS Server to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Microsoft_IIS_Server_Scanner</code> class, call the <code>scan</code> method with the Microsoft IIS Server version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Microsoft_IIS_Server_Scanner

# Scan Microsoft IIS Server for vulnerabilities
microsoft_iis_server_vulnerabilities = Microsoft_IIS_Server_Scanner.scan(
    version="10.0",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Microsoft IIS Server Vulnerabilities:", microsoft_iis_server_vulnerabilities)
</code></pre>

<h1>Nginx_Server_Scanner Class</h1>

<p>Class that provides a static method for scanning Nginx Server installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Nginx Server installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'nginx' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Nginx Server to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Nginx_Server_Scanner</code> class, call the <code>scan</code> method with the Nginx Server version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Nginx_Server_Scanner

# Scan Nginx Server for vulnerabilities
nginx_server_vulnerabilities = Nginx_Server_Scanner.scan(
    version="1.21.1",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Nginx Server Vulnerabilities:", nginx_server_vulnerabilities)
</code></pre>
<h1>Payara_Server_Scanner Class</h1>

<p>Class that provides a static method for scanning Payara Server installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Payara Server installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'payara' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Payara Server to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Payara_Server_Scanner</code> class, call the <code>scan</code> method with the Payara Server version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Payara_Server_Scanner

# Scan Payara Server for vulnerabilities
payara_server_vulnerabilities = Payara_Server_Scanner.scan(
    version="5.2021.5",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Payara Server Vulnerabilities:", payara_server_vulnerabilities)
</code></pre>
<h1>Windows_Server_Scanner Class</h1>

<p>Class that provides a static method for scanning Windows Server installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Windows Server installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'microsoft' and 'windows_server' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Windows Server to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Windows_Server_Scanner</code> class, call the <code>scan</code> method with the Windows Server version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Windows_Server_Scanner

# Scan Windows Server for vulnerabilities
windows_server_vulnerabilities = Windows_Server_Scanner.scan(
    version="2019",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Windows Server Vulnerabilities:", windows_server_vulnerabilities)
</code></pre>
