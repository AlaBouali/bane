<h1>MariaDB_Scanner Class</h1>

<p>Class that provides a static method for scanning MariaDB installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans MariaDB installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'mariadb' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of MariaDB to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>MariaDB_Scanner</code> class, call the <code>scan</code> method with the MariaDB version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import MariaDB_Scanner

# Scan MariaDB for vulnerabilities
mariadb_vulnerabilities = MariaDB_Scanner.scan(
    version="10.5.12",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("MariaDB Vulnerabilities:", mariadb_vulnerabilities)
</code></pre>
<h1>MongoDB_Scanner Class</h1>

<p>Class that provides a static method for scanning MongoDB installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans MongoDB installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'mongodb' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of MongoDB to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>MongoDB_Scanner</code> class, call the <code>scan</code> method with the MongoDB version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import MongoDB_Scanner

# Scan MongoDB for vulnerabilities
mongodb_vulnerabilities = MongoDB_Scanner.scan(
    version="4.4.12",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("MongoDB Vulnerabilities:", mongodb_vulnerabilities)
</code></pre>
<h1>Microsoft_SQL_Server_Scanner Class</h1>

<p>Class that provides a static method for scanning Microsoft SQL Server installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Microsoft SQL Server installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'microsoft' and 'sql_server' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Microsoft SQL Server to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Microsoft_SQL_Server_Scanner</code> class, call the <code>scan</code> method with the Microsoft SQL Server version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Microsoft_SQL_Server_Scanner

# Scan Microsoft SQL Server for vulnerabilities
microsoft_sql_server_vulnerabilities = Microsoft_SQL_Server_Scanner.scan(
    version="2019",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Microsoft SQL Server Vulnerabilities:", microsoft_sql_server_vulnerabilities)
</code></pre>
<h1>MySQL_MySQL_Scanner Class</h1>

<p>Class that provides a static method for scanning MySQL Server installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans MySQL Server installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'mysql' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of MySQL Server to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>MySQL_MySQL_Scanner</code> class, call the <code>scan</code> method with the MySQL Server version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import MySQL_MySQL_Scanner

# Scan MySQL Server for vulnerabilities
mysql_server_vulnerabilities = MySQL_MySQL_Scanner.scan(
    version="8.0.23",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("MySQL Server Vulnerabilities:", mysql_server_vulnerabilities)
</code></pre>
<h1>MySQL_Oracle_Scanner Class</h1>

<p>Class that provides a static method for scanning MySQL Server installations (Oracle variant) using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans MySQL Server installations (Oracle variant) for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'oracle' and 'mysql' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of MySQL Server (Oracle variant) to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>MySQL_Oracle_Scanner</code> class, call the <code>scan</code> method with the MySQL Server (Oracle variant) version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import MySQL_Oracle_Scanner

# Scan MySQL Server (Oracle variant) for vulnerabilities
mysql_oracle_server_vulnerabilities = MySQL_Oracle_Scanner.scan(
    version="8.0.23",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("MySQL Server (Oracle variant) Vulnerabilities:", mysql_oracle_server_vulnerabilities)
</code></pre>
<h1>PostgreSQL_Scanner Class</h1>

<p>Class that provides a static method for scanning PostgreSQL installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans PostgreSQL installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'postgresql' keyword.</p>

<ul>
    <li><code>version</code> (str): The version of PostgreSQL to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>PostgreSQL_Scanner</code> class, call the <code>scan</code> method with the PostgreSQL version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import PostgreSQL_Scanner

# Scan PostgreSQL for vulnerabilities
postgresql_vulnerabilities = PostgreSQL_Scanner.scan(
    version="13.4",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("PostgreSQL Vulnerabilities:", postgresql_vulnerabilities)
</code></pre>
<h1>Redis_Scanner Class</h1>

<p>Class that provides a static method for scanning Redis installations using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>Static method that scans Redis installations for known vulnerabilities based on the specified version. It internally uses the <code>Vulners_Search_Scanner</code> with the 'redislabs' and 'redis' keywords.</p>

<ul>
    <li><code>version</code> (str): The version of Redis to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the <code>Vulners_Search_Scanner</code>, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns the result of the vulnerability scan.</p>

<h2>Example Usage</h2>
<p>To use the <code>Redis_Scanner</code> class, call the <code>scan</code> method with the Redis version and any additional parameters needed for the <code>Vulners_Search_Scanner</code>. Here's an example:</p>

<pre><code>
from bane import Redis_Scanner

# Scan Redis for vulnerabilities
redis_vulnerabilities = Redis_Scanner.scan(
    version="6.2.5",
    http_proxies=["1.2.3.4:80"],
)

# Access the results
print("Redis Vulnerabilities:", redis_vulnerabilities)
</code></pre>
