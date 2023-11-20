<h1>Android_OS_Scanner Class</h1>

<p>Class that provides a static method for scanning Android OS installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Android OS installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'google' and 'android' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Android OS to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Android_OS_Scanner</code> class, call the <code>scan</code> method with the Android OS version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Android_OS_Scanner

# Scan Android OS for vulnerabilities
android_os_vulnerabilities = Android_OS_Scanner.scan(
    version="12.0",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Android OS Vulnerabilities:", android_os_vulnerabilities)
</code></pre>
<h1>Busybox_OS_Scanner Class</h1>

<p>Class that provides a static method for scanning Busybox OS installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Busybox OS installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'busybox' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Busybox OS to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Busybox_OS_Scanner</code> class, call the <code>scan</code> method with the Busybox OS version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Busybox_OS_Scanner

# Scan Busybox OS for vulnerabilities
busybox_os_vulnerabilities = Busybox_OS_Scanner.scan(
    version="1.33.1",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Busybox OS Vulnerabilities:", busybox_os_vulnerabilities)
</code></pre>
<h1>CentOs_Scanner Class</h1>

<p>Class that provides a static method for scanning CentOS installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans CentOS installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'centos' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of CentOS to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>CentOs_Scanner</code> class, call the <code>scan</code> method with the CentOS version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import CentOs_Scanner

# Scan CentOS for vulnerabilities
centos_vulnerabilities = CentOs_Scanner.scan(
    version="7.9.2009",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("CentOS Vulnerabilities:", debian_os_vulnerabilities)
</code></pre>


<h1>Debian_OS_Scanner Class</h1>

<p>Class that provides a static method for scanning Debian OS installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Debian OS installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'debian' and 'debian_linux' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Debian OS to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Debian_OS_Scanner</code> class, call the <code>scan</code> method with the Debian OS version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Debian_OS_Scanner

# Scan Debian OS for vulnerabilities
debian_os_vulnerabilities = Debian_OS_Scanner.scan(
    version="10.11",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Debian OS Vulnerabilities:", debian_os_vulnerabilities)
</code></pre>

<h1>FreeBSD_OS_Scanner Class</h1>

<p>Class that provides a static method for scanning FreeBSD OS installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans FreeBSD OS installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'freebsd' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of FreeBSD OS to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>FreeBSD_OS_Scanner</code> class, call the <code>scan</code> method with the FreeBSD OS version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import FreeBSD_OS_Scanner

# Scan FreeBSD OS for vulnerabilities
freebsd_os_vulnerabilities = FreeBSD_OS_Scanner.scan(
    version="12.2",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("FreeBSD OS Vulnerabilities:", freebsd_os_vulnerabilities)
</code></pre>
<h1>IOS_Scanner Class</h1>

<p>Class that provides a static method for scanning iOS installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans iOS installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'apple' and 'iphone_os' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of iOS to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>IOS_Scanner</code> class, call the <code>scan</code> method with the iOS version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import IOS_Scanner

# Scan iOS for vulnerabilities
ios_vulnerabilities = IOS_Scanner.scan(
    version="15.0",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("iOS Vulnerabilities:", ios_vulnerabilities)
</code></pre>
<h1>Mac_OS_Scanner Class</h1>

<p>Class that provides a static method for scanning macOS installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans macOS installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'apple' and 'macos' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of macOS to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Mac_OS_Scanner</code> class, call the <code>scan</code> method with the macOS version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Mac_OS_Scanner

# Scan macOS for vulnerabilities
mac_os_vulnerabilities = Mac_OS_Scanner.scan(
    version="12.0",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("macOS Vulnerabilities:", mac_os_vulnerabilities)
</code></pre>
<h1>Ubuntu_OS_Scanner Class</h1>

<p>Class that provides a static method for scanning Ubuntu OS installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Ubuntu OS installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'canonical' and 'ubuntu_linux' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Ubuntu OS to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Ubuntu_OS_Scanner</code> class, call the <code>scan</code> method with the Ubuntu OS version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Ubuntu_OS_Scanner

# Scan Ubuntu OS for vulnerabilities
ubuntu_os_vulnerabilities = Ubuntu_OS_Scanner.scan(
    version="20.04.3",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Ubuntu OS Vulnerabilities:", ubuntu_os_vulnerabilities)
</code></pre>
<h1>Windows_OS_Scanner Class</h1>

<p>Class that provides a static method for scanning Windows OS installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Windows OS installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'microsoft' and 'windows' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Windows OS to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Windows_OS_Scanner</code> class, call the <code>scan</code> method with the Windows OS version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Windows_OS_Scanner

# Scan Windows OS for vulnerabilities
windows_os_vulnerabilities = Windows_OS_Scanner.scan(
    version="10.0.19043",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Windows OS Vulnerabilities:", windows_os_vulnerabilities)
</code></pre>
