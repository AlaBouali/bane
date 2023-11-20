<h1>Django_Scanner Class</h1>

<p>Class that provides a static method for scanning Django installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Django installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'django' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Django to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Django_Scanner</code> class, call the <code>scan</code> method with the Django version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Django_Scanner

# Scan Django for vulnerabilities
django_vulnerabilities = Django_Scanner.scan(
    version="3.2.5",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Django Vulnerabilities:", django_vulnerabilities)
</code></pre>
<h1>FastAPI_Scanner Class</h1>

<p>Class that provides a static method for scanning FastAPI installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans FastAPI installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'fastapi' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of FastAPI to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>FastAPI_Scanner</code> class, call the <code>scan</code> method with the FastAPI version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import FastAPI_Scanner

# Scan FastAPI for vulnerabilities
fastapi_vulnerabilities = FastAPI_Scanner.scan(
    version="0.68.0",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("FastAPI Vulnerabilities:", fastapi_vulnerabilities)
</code></pre>
<h1>Flask_Scanner Class</h1>

<p>Class that provides a static method for scanning Flask installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Flask installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'flask' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Flask to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Flask_Scanner</code> class, call the <code>scan</code> method with the Flask version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Flask_Scanner

# Scan Flask for vulnerabilities
flask_vulnerabilities = Flask_Scanner.scan(
    version="2.0.1",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Flask Vulnerabilities:", flask_vulnerabilities)
</code></pre>
<h1>Laravel_Scanner Class</h1>

<p>Class that provides a static method for scanning Laravel installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Laravel installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'laravel' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Laravel to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Laravel_Scanner</code> class, call the <code>scan</code> method with the Laravel version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Laravel_Scanner

# Scan Laravel for vulnerabilities
laravel_vulnerabilities = Laravel_Scanner.scan(
    version="8.0.0",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Laravel Vulnerabilities:", laravel_vulnerabilities)
</code></pre>
<h1>Spring_Boot_Scanner Class</h1>

<p>Class that provides a static method for scanning Spring Boot installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Spring Boot installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'spring_boot' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Spring Boot to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Spring_Boot_Scanner</code> class, call the <code>scan</code> method with the Spring Boot version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Spring_Boot_Scanner

# Scan Spring Boot for vulnerabilities
spring_boot_vulnerabilities = Spring_Boot_Scanner.scan(
    version="2.5.3",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Spring Boot Vulnerabilities:", spring_boot_vulnerabilities)
</code></pre>
<h1>Spring_Security_Scanner Class</h1>

<p>Class that provides a static method for scanning Spring Security installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Spring Security installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'spring_security' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Spring Security to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Spring_Security_Scanner</code> class, call the <code>scan</code> method with the Spring Security version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Spring_Security_Scanner

# Scan Spring Security for vulnerabilities
spring_security_vulnerabilities = Spring_Security_Scanner.scan(
    version="5.5.0",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Spring Security Vulnerabilities:", spring_security_vulnerabilities)
</code></pre>
<h1>Symfony_Scanner Class</h1>

<p>Class that provides a static method for scanning Symfony installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Symfony installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'symfony' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Symfony to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Symfony_Scanner</code> class, call the <code>scan</code> method with the Symfony version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Symfony
