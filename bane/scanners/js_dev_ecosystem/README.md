<h1>Angular_Scanner Class</h1>

<p>Class that provides a static method for scanning AngularJS and Angular installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans AngularJS and Angular installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'angularjs' and 'angular' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of AngularJS or Angular to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Angular_Scanner</code> class, call the <code>scan</code> method with the AngularJS or Angular version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Angular_Scanner

# Scan AngularJS or Angular for vulnerabilities
angular_vulnerabilities = Angular_Scanner.scan(
    version="2.5.2",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Angular Vulnerabilities:", angular_vulnerabilities)
</code></pre>

<h1>AngularJS_Scanner Class</h1>

<p>Class that provides a static method for scanning AngularJS and Angular installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans AngularJS and Angular installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'angularjs' and 'angular' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of AngularJS or Angular to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>AngularJS_Scanner</code> class, call the <code>scan</code> method with the AngularJS or Angular version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import AngularJS_Scanner

# Scan AngularJS or Angular for vulnerabilities
angular_vulnerabilities = AngularJS_Scanner.scan(
    version="2.5.2",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Angular Vulnerabilities:", angular_vulnerabilities)
</code></pre>


<h1>NodeJS_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>NodeJS_Scanner</code> class is designed to scan Node.js installations for known vulnerabilities using the Vulners database. It provides a static method to perform the scanning process based on the specified Node.js version.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>This static method scans a Node.js installation for known vulnerabilities based on the specified version. It utilizes the Vulners database for vulnerability information. It takes the following parameters:</p>

<ul>
    <li><code>version</code> (str): The version of Node.js to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the Vulners_Search_Scanner, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns a list of vulnerabilities with their titles, descriptions, and links.</p>

<h2>Example Usage</h2>
<p>To use the <code>NodeJS_Scanner</code> class, call the <code>scan</code> method with the Node.js version and any additional parameters needed for the Vulners_Search_Scanner. Here's an example:</p>

<pre><code>
from bane import NodeJS_Scanner

#Scan Node.js for vulnerabilities
nodejs_vulnerabilities = NodeJS_Scanner.scan(
    version="14.17.6",
    http_proxies=["1.2.3.4:80"],
)

#Access the results
print("Node.js Vulnerabilities:", nodejs_vulnerabilities)
</code></pre>

<h1>NPMJS_Scanner Class</h1>

<p>Class that provides a static method for scanning npm packages using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans npm packages for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'npmjs' and 'npm' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of npm package to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>NPMJS_Scanner</code> class, call the <code>scan</code> method with the npm package version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import NPMJS_Scanner

# Scan npm package for vulnerabilities
npm_vulnerabilities = NPMJS_Scanner.scan(
    version="3.10.10",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("NPM Package Vulnerabilities:", npm_vulnerabilities)
</code></pre>



<h1>ReactJS_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>ReactJS_Scanner</code> class is designed to scan React.js installations for known vulnerabilities using the Vulners database. It provides a static method to perform the scanning process based on the specified React.js version.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>This static method scans a React.js installation for known vulnerabilities based on the specified version. It utilizes the Vulners database for vulnerability information specific to React.js. It takes the following parameters:</p>

<ul>
    <li><code>version</code> (str): The version of React.js to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the Vulners_Search_Scanner, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns a list of vulnerabilities with their titles, descriptions, and links.</p>

<h2>Example Usage</h2>
<p>To use the <code>ReactJS_Scanner</code> class, call the <code>scan</code> method with the React.js version and any additional parameters needed for the Vulners_Search_Scanner. Here's an example:</p>

<pre><code>
from bane import ReactJS_Scanner

#Scan React.js for vulnerabilities
reactjs_vulnerabilities = ReactJS_Scanner.scan(
    version="17.0.2",
    http_proxies=["1.2.3.4:80"],
)

#Access the results
print("React.js Vulnerabilities:", reactjs_vulnerabilities)
</code></pre>
