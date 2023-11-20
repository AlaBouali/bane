<h1>Ansible_Scanner Class</h1>

<p>Class that provides a static method for scanning Ansible installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans an Ansible installation for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'ansible' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Ansible to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Ansible_Scanner</code> class, call the <code>scan</code> method with the Ansible version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Ansible_Scanner

# Scan Ansible for vulnerabilities
ansible_vulnerabilities = Ansible_Scanner.scan(
    version="2.10.10",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Ansible Vulnerabilities:", ansible_vulnerabilities)
</code></pre>

<h1>Docker_Scanner Class</h1>

<p>Class that provides a static method for scanning Docker installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans a Docker installation for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'docker' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Docker to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Docker_Scanner</code> class, call the <code>scan</code> method with the Docker version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Docker_Scanner

# Scan Docker for vulnerabilities
docker_vulnerabilities = Docker_Scanner.scan(
    version="20.10.8",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Docker Vulnerabilities:", docker_vulnerabilities)
</code></pre>

<h1>Git_Scanner Class</h1>

<p>Class that provides a static method for scanning Git installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans a Git installation for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'git' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Git to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Git_Scanner</code> class, call the <code>scan</code> method with the Git version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Git_Scanner

# Scan Git for vulnerabilities
git_vulnerabilities = Git_Scanner.scan(
    version="2.33.0",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Git Vulnerabilities:", git_vulnerabilities)
</code></pre>


<h1>Jenkins_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Jenkins_Scanner</code> class is designed to perform application security testing on Jenkins sites. It scans for known vulnerabilities using the Vulners database and provides detailed information about the Jenkins site's configuration, versions, and potential exploits.</p>

<h2>Static Methods</h2>

<h3><code>scan(u, user_agent=None, cookie=None, timeout=10, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method initiates a scan on the provided Jenkins site. It takes various parameters for customization and returns a comprehensive report on the site's security posture. The parameters are similar to those used in other scanner classes.</p>

<p>The method returns a detailed report containing information about the site's URL, domain, IP, server details, operating system, backend technology, Jenkins version, vulnerabilities, and more.</p>

<h2>Example Usage</h2>
<p>To use the <code>Jenkins_Scanner</code> class, call the <code>scan</code> method with the URL of the Jenkins site and any additional parameters needed for the scan. Here's an example:</p>

<pre><code>
from bane import Jenkins_Scanner

#Scan Jenkins site for vulnerabilities
jenkins_scan_result = Jenkins_Scanner.scan(
    u="https://jenkins.example.com",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    cookie="your_cookie_string",
    timeout=15,
    logs=True,
    crt_timeout=120,
    wayback_timeout=120,
    subdomain_check_timeout=10,
    max_wayback_urls=10,
    subdomains_only=True,
    headers={"Custom-Header": "header_value"},
    http_proxies=["http://proxy1:8080", "http://proxy2:8080"],
    socks4_proxies=["socks4://proxy3:1080"],
    socks5_proxies=["socks5://proxy4:1080"]
)

#Access the scan results
print("Jenkins Scan Results:", jenkins_scan_result)
</code></pre>

<h1>Jira_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Jira_Scanner</code> class is designed for application security testing on Jira sites. It scans for vulnerabilities using the Vulners database and provides detailed information about the Jira site's configuration, versions, and potential exploits.</p>

<h2>Static Methods</h2>

<h3><code>scan(u, user_agent=None, cookie=None, timeout=10, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method initiates a scan on the provided Jira site. It takes various parameters for customization and returns a comprehensive report on the site's security posture. The parameters are similar to those used in other scanner classes.</p>

<p>The method returns a detailed report containing information about the site's URL, domain, IP, server details, operating system, backend technology, Jira version, vulnerabilities, and more.</p>

<h2>Example Usage</h2>
<p>To use the <code>Jira_Scanner</code> class, call the <code>scan</code> method with the URL of the Jira site and any additional parameters needed for the scan. Here's an example:</p>

<pre><code>
from bane import Jira_Scanner

#Scan Jira site for vulnerabilities
jira_scan_result = Jira_Scanner.scan(
    u="https://jira.example.com",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    cookie="your_cookie_string",
    timeout=15,
    logs=True,
    crt_timeout=120,
    wayback_timeout=120,
    subdomain_check_timeout=10,
    max_wayback_urls=10,
    subdomains_only=True,
    headers={"Custom-Header": "header_value"},
    http_proxies=["http://proxy1:8080", "http://proxy2:8080"],
    socks4_proxies=["socks4://proxy3:1080"],
    socks5_proxies=["socks5://proxy4:1080"]
)

#Access the scan results
print("Jira Scan Results:", jira_scan_result)
</code></pre>
<h1>Kubernetes_Scanner Class</h1>

<p>Class that provides a static method for scanning Kubernetes installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans a Kubernetes installation for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'kubernetes' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Kubernetes to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Kubernetes_Scanner</code> class, call the <code>scan</code> method with the Kubernetes version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Kubernetes_Scanner

# Scan Kubernetes for vulnerabilities
kubernetes_vulnerabilities = Kubernetes_Scanner.scan(
    version="1.22.1",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Kubernetes Vulnerabilities:", kubernetes_vulnerabilities)
</code></pre>

<h1>Maven_Scanner Class</h1>

<p>Class that provides a static method for scanning Maven installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans a Maven installation for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'maven' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Maven to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Maven_Scanner</code> class, call the <code>scan</code> method with the Maven version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Maven_Scanner

# Scan Maven for vulnerabilities
maven_vulnerabilities = Maven_Scanner.scan(
    version="3.8.4",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Maven Vulnerabilities:", maven_vulnerabilities)
</code></pre>

<h1>Puppet_Scanner Class</h1>

<p>Class that provides a static method for scanning Puppet installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans a Puppet installation for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'puppet' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of Puppet to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Puppet_Scanner</code> class, call the <code>scan</code> method with the Puppet version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Puppet_Scanner

# Scan Puppet for vulnerabilities
puppet_vulnerabilities = Puppet_Scanner.scan(
    version="7.13.0",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Puppet Vulnerabilities:", puppet_vulnerabilities)
</code></pre>
