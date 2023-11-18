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
