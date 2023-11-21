# Please open each folder to find its own documentation.

<ul>
<li><a href="https://github.com/AlaBouali/bane#installation">Installation</a></li>
<br>
<!-- Root Directory -->
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane">Home</a> </li>
<br>
<!-- bruteforce Directory -->
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/bruteforce"><b>Bruteforce:</b></a> </li>
  <br>
  <ul>
  <li><a href="https://github.com/AlaBouali/bane/tree/master/bane/bruteforce#Admin_Panel_Finder-class">Admin_Panel_Finder :</a> used to search for potential admin panel URLs on a website using a predefined list of extensions.</li>
  <li><a href="https://github.com/AlaBouali/bane/tree/master/bane/bruteforce#Decryptor-class">Decryptor :</a> used for performing various cryptographic hash decryption attempts.</li>
  <li><a href="https://github.com/AlaBouali/bane/tree/master/bane/bruteforce#Files_Manager_Finder-class">Files_Manager_Finder :</a> used to search for a filemanager on a website.</li>
  <li><a href="https://github.com/AlaBouali/bane/tree/master/bane/bruteforce#Force_Browsing-class">Force_Browsing :</a> used to perform force browsing on a website by attempting to access various URLs with different extensions.</li>
  <li><a href="https://github.com/AlaBouali/bane/tree/master/bane/bruteforce#HTTP_Auth_Bruteforce-class">HTTP_Auth_Bruteforce :</a> used to perform HTTP authentication bruteforce attacks on a website.</li>

<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/bruteforce#jwt_manager-class">JWT_Manager :</a> provides functionality for analyzing, encoding, decoding, and guessing secret keys for JSON Web Tokens (JWT). JWTs are widely used in web applications for secure data exchange and authentication.</li>


  <li><a href="https://github.com/AlaBouali/bane/tree/master/bane/bruteforce#Hydra-class">Hydra :</a> used for performing brute-force login attempts on various services, including SSH, Telnet, FTP, SMTP, MySQL, and WordPress. It takes a list of username-password combinations and tries to log in using different protocols. It reports success or failure for each combination.</li>
  <li><a href="https://github.com/AlaBouali/bane/tree/master/bane/bruteforce#Services_Login-class">Services_Login :</a> class provides a set of methods for performing various login/authentication attempts for different services, such as SMTP, Telnet, SSH, FTP, and MySQL. These methods check for successful login using the provided credentials and options.</li>
  <li><a href="https://github.com/AlaBouali/bane/tree/master/bane/bruteforce#Web_Login_Bruteforce-class">Web_Login_Bruteforce :</a> used for performing brute-force login attempts on web-based login forms. It takes a list of username-password combinations and tries to log in by filling out the login form. It reports success or failure for each combination.</li>
  </ul>
<br>
<!-- common Directory -->
<li><a href="https://github.com/AlaBouali/bane/blob/master/bane/common">Common_Variables :</a> used to store internal and necessary variables for bane to run including: more than 20k unique user-agents created on importation, valid lists legit values for many HTTP headers to choose from, various file types ( png , jpg , docx , pptx , html , php ... ) used to fill the forms and test of file upload vulnerabilities , ...</li>
<br>
<!-- cryptographers Directory -->
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/cryptographers"><b>Cryptographers:</b></a> </li>
 <br> <ul>
 <li><a href="https://github.com/AlaBouali/bane/tree/master/bane/cryptographers#BASE64-class">BASE64 :</a> provides methods for encoding and decoding data using Base64 encoding.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/cryptographers#CAESAR-class">CAESAR :</a> provides methods for encoding and decoding text using the Caesar cipher ( just for fun )</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/cryptographers#MD5-class">MD5 :</a> provides methods for generating and comparing MD-5 hash values for text and files.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/cryptographers#SHA1-class">SHA1 :</a> provides methods for generating and comparing SHA-1 hash values for text and files.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/cryptographers#SHA224-class">SHA224 :</a> provides methods for generating and comparing SHA-224 hash values for text and files.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/cryptographers#SHA256-class">SHA256 :</a> provides methods for generating and comparing SHA-256 hash values for text and files.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/cryptographers#SHA348-class">SHA384 :</a> provides methods for generating and comparing SHA-384 hash values for text and files.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/cryptographers#SHA512-class">SHA512 :</a> provides methods for generating and comparing SHA-512 hash values for text and files.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/cryptographers#XOR-class">XOR :</a> provides methods for generating and comparing XOR hash values for text and files.</li>
</ul>
<br>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos"><b>DDoS ( Distributed Denial-of-Service  ) :</b></a> </li>
  <br><ul>
 
<!-- ddos Directory -->
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos#HTTP_Puncher-class">HTTP_Puncher :</a> used for launching HTTP-based DDoS attacks on a target URL.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos#HTTP_Spam-class">HTTP_Spam :</a> used for launching HTTP-based DDoS attacks on a target URL by spamming each connection with a stream of requests unlike the previous one.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos#Proxies_Hammer-class">Proxies_Hammer :</a> used for launching low-rate HTTP POST requests through a list of proxy servers to a target URL.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos#Proxies_HTTP_Spam-class">Proxies_HTTP_Spam :</a> used for launching HTTP-based DDoS attacks on a target URL by spamming each connection with a stream of requests through proxies.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos#Proxies_Xerxes-class">Proxies_Xerxes :</a> used for performing a simple DDoS attack by sending NULL characters through a list of proxy servers.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos#Slow_Read-class">Slow_Read :</a> used to perform a slow reading attack on a target server. This attack sends normal HTTP requests but reads them slowly to keep the connection open for an extended period of time.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos#TCP_Flood-class">TCP_Flood :</a> used to perform a TCP flooding attack on a target server. This attack floods the target with a large number of TCP packets to overwhelm the server and disrupt its normal operations.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos#Tor_Hammer-class">Tor_Hammer :</a> used for launching low-rate HTTP POST requests through TOR to a target URL.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos#UDP_Flood-class">UDP_Flood :</a> used to perform a DDoS attack by flooding a target server with UDP (User Datagram Protocol) packets. UDP is a connectionless protocol, and this attack generates a large volume of UDP packets to overwhelm the target.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos#VSE_Flood-class">VSE_Flood :</a> used to perform a DDoS attack known as the Valve Source Engine Query (VSE) flood attack. The attack sends spoofed queries to Source Engine servers in an attempt to overwhelm them with traffic. This attack is often used in the gaming community to disrupt online game servers.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/ddos#Xerxes-class">Xerxes :</a> used to perform a DDoS attack using the Xerxes tool. This attack sends NULL characters to a target server to flood it with traffic. The tool is named after the ancient Persian king Xerxes I, known for his invasion of Greece.</li>
<br>
<!-- gather_info Directory -->
</ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/gather_info"><b>Information Gathering:</b></a> </li>
  <br><ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/gather_info#Domain_Info-class">Domain_Info :</a> provides methods for gathering information about a domain, including WHOIS data, domain information, and DNS resolution.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/gather_info#Dorking_Info-class">Dorking_Info :</a> provides a method for performing Google dork searches to find URLs related to a specific query.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/gather_info#IP_Info-class">IP_Info :</a> provides methods for gathering information related to IP addresses, including obtaining your own IP, geolocation information, reverse IP lookup, and Shodan reports.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/gather_info#Network_Info-class">Network_Info :</a> provides methods for network-related tasks, including retrieving local IP addresses, checking if a host is alive, performing TCP port scanning, and obtaining banners from network services.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/gather_info#Subdomain_Info-class">Subdomain_Info :</a> provides methods for extracting and analyzing subdomains associated with a given domain. It can fetch subdomains from sources like crt.sh and the Wayback Machine, allowing you to discover subdomains for a target domain.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/gather_info#URL_Info-class">URL_Info :</a> provides methods for performing security checks, deep inspection, and HTTP OPTIONS requests on a given URL. You can use these methods to analyze and gather information about a specific URL, such as its security status, response headers, and more.</li>
<br>
<!-- scanners Directory -->
</ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/botnet"><b>Botnet: creation , control and management with a scalable infrastructure :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/botnet#botnet_master-class">Botnet_Master :</a> used for managing botnet operations.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/botnet#Botnet_Scanner-class">Botnet_Scanner :</a> used for scanning safe IPs all over the internet with a word list to bruteforce various login protocols, including FTP, SSH, Telnet, SMTP, and MySQL. The scan results are saved to text files in the same directory.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/botnet#botnet_c_c_server-class">Botnet_C_C_Server :</a> used for managing a Command and Control (C&C) server for a botnet.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/botnet#botnet_malware_download_server-class">Botnet_Malware_Download_Server :</a> used for creating a server to download malware files from a specified folder while preventing path traversal vulnerabilities.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/botnet#botnet_reporting_server-class">Botnet_Reporting_Server :</a> used for creating a server to receive reports from the bots and store them in the database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/botnet#botnet_web_interface_server-class">Botnet_Web_Interface_Server :</a> used for creating a web interface server for managing the botnet.</li>
</ul>
<br>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/cms"><b>CMS's Vulnerability Scanner :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/cms#Drupal_Scanner-class">Drupal_Scanner :</a> used to scan a website for Drupal-related information and vulnerabilities. It checks the target URL for Drupal version, server information, subdomains, and possible vulnerabilities.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/cms#Joomla_Scanner-class">Joomla_Scanner :</a> used to scan a website for Joomla-related information and vulnerabilities. It checks the target URL for Joomla version, server information, subdomains, and possible vulnerabilities.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/cms#Magento_Scanner-class">Magento_Scanner :</a> used to scan a website for Magento-related information and vulnerabilities. It checks the target URL for Magento version, server information, subdomains, and possible vulnerabilities.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/cms#WordPress_Scanner-class">WordPress_Scanner :</a> used to scan a website for WordPress-related information and vulnerabilities. It checks the target URL for WordPress version, server information, subdomains, themes, plugins, and possible vulnerabilities.</li>
</ul>
<br>

<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/data_visualization_stack"><b>Data Visualization Stack :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/data_visualization_stack#elasticsearch_scanner-class">ElasticSearch_Scanner :</a> designed to scan an Elasticsearch server for information and vulnerabilities. It checks the target server for Elasticsearch version, performs a basic HTTP request, and retrieves relevant vulnerability information using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/data_visualization_stack#grafana_scanner-class">Grafana_Scanner :</a> designed to scan a Grafana server for information and vulnerabilities. It checks the target server for Grafana version, server information, subdomains, and possible vulnerabilities.</li>
<br>
</ul>

<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/databases"><b>Databases :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/databases#mariadb_scanner-class">MariaDB_Scanner :</a> provides a static method for scanning MariaDB installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/databases#mongodb_scanner-class">MongoDB_Scanner :</a> provides a static method for scanning MongoDB installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/databases#microsoft_sql_server_scanner-class">Microsoft_SQL_Server_Scanner :</a> provides a static method for scanning Microsoft SQL Server installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/databases#mysql_mysql_scanner-class">MySQL_MySQL_Scanner :</a> provides a static method for scanning MySQL Server installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/databases#mysql_oracle_scanner-class">MySQL_Oracle_Scanner :</a> provides a static method for scanning MySQL Server installations (Oracle variant) using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/databases#postgresql_scanner-class">PostgreSQL_Scanner :</a> provides a static method for scanning PostgreSQL installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/databases#redis_scanner-class">Redis_Scanner :</a> provides a static method for scanning Redis installations using the Vulners database.</li>
<br>
</ul>



<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/devops_project_management"><b>DevOps ( project management ) :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/devops_project_management#ansible_scanner-class">Ansible_Scanner :</a> provides a static method for scanning Ansible installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/devops_project_management#docker_scanner-class">Docker_Scanner :</a> provides a static method for scanning Docker installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/devops_project_management#git_scanner-class">Git_Scanner :</a> provides a static method for scanning Git installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/devops_project_management#jenkins_scanner-class">Jenkins_Scanner :</a> designed to perform application security testing on Jenkins sites. It scans for known vulnerabilities using the Vulners database and provides detailed information about the Jenkins site's configuration, versions, and potential exploits.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/devops_project_management#jira_scanner-class">Jira_Scanner :</a> designed for application security testing on Jira sites. It scans for vulnerabilities using the Vulners database and provides detailed information about the Jira site's configuration, versions, and potential exploits.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/devops_project_management#kubernetes_scanner-class">Kubernetes_Scanner :</a> provides a static method for scanning Kubernetes installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/devops_project_management#maven_scanner-class">Maven_Scanner :</a> provides a static method for scanning Maven installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/devops_project_management#puppet_scanner-class">Puppet_Scanner :</a> provides a static method for scanning Puppet installations using the Vulners database.</li>
<br>
</ul>


<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/erp_solutions"><b>ERP Solutions :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/erp_solutions#dolibarr_scanner-class">Dolibarr_Scanner :</a> designed to scan a Dolibarr server for information and vulnerabilities. It checks the target server for Dolibarr version, server information, subdomains, and possible vulnerabilities.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/erp_solutions#odoo_scanner-class">Odoo_scanner :</a> designed to scan a Odoo server for information and vulnerabilities. It checks the target server for Odoo version, server information, subdomains, and possible vulnerabilities.</li>
<br>
</ul>


<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/js_dev_ecosystem"><b>Javasript Development Eco-System :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/js_dev_ecosystem#angular_scanner-class">Angular_Scanner :</a> provides a static method for scanning Angular installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/js_dev_ecosystem#angularjs_scanner-class">AngularJS_Scanner :</a> provides a static method for scanning AngularJS installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/js_dev_ecosystem#nodejs_scanner-class">NodeJS_Scanner :</a> designed to scan Node.js installations for known vulnerabilities using the Vulners database. It provides a static method to perform the scanning process based on the specified Node.js version.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/js_dev_ecosystem#npmjs_scanner-class">NPMJS_Scanner :</a> provides a static method for scanning npm packages using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/js_dev_ecosystem#reactjs_scanner-class">ReactJS_Scanner :</a> designed to scan React.js installations for known vulnerabilities using the Vulners database. It provides a static method to perform the scanning process based on the specified React.js version.</li>
<br>
</ul>

<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/lms"><b>LMS's Vulnerability Scanner :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/lms#moodle_scanner-class">Moodle_Scanner :</a> used to scan a website for Moodle-related information and vulnerabilities. It checks the target URL for Moodle version, server information, subdomains, and possible vulnerabilities.</li>
<br>
</ul>


<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/mobile_dev"><b>Mobile Applications development Stack :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/mobile_dev#flutter_scanner-class">Flutter_Scanner :</a> provides a static method for scanning Flutter installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/mobile_dev#react_native_scanner-class">React_Native_Scanner :</a> provides a static method for scanning React Native installations using the Vulners database.</li>
<br>
</ul>




<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/network_protocols"><b>Network Discovery and Scanning:</b></a> </li>
  <br><ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/network_protocols#Chargen_Amplification_Scanner-class">Chargen_Amplification_Scanner :</a> used to calculate the amplification factor for a given Chargen server.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/network_protocols#DNS_Amplification_Scanner-class">DNS_Amplification_Scanner :</a> used to calculate the amplification factor for a given DNS server.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/network_protocols#Echo_Amplification_Scanner-class">Echo_Amplification_Scanner :</a> used to calculate the amplification factor for a given Echo server.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/network_protocols#Memcache_Amplification_Scanner-class">Memcache_Amplification_Scanner :</a> used to calculate the amplification factor for a given Memcache server.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/network_protocols#NTP_Amplification_Scanner-class">NTP_Amplification_Scanner :</a> used to calculate the amplification factor for a given NTP (Network Time Protocol) server.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/network_protocols#Ports_Scanner-class">Ports_Scanner :</a> used to scan a range of ports on a target IP address to check if they are open or closed.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners#SNMP_Amplification_Scanner-class">SNMP_Amplification_Scanner :</a> used to calculate the amplification factor for a given SNMP (Simple Network Management Protocol) server.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners#SSDP_Amplification_Scanner-class">SSDP_Amplification_Scanner :</a> used to calculate the amplification factor for a given SSDP (Simple Service Discovery Protocol) server.</li>
<br>
</ul>




<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/operating_systems"><b>Operating Systems :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/operating_systems#android_os_scanner-class">Android_OS_Scanner :</a> provides a static method for scanning Android OS installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/operating_systems#busybox_os_scanner-class">Busybox_OS_Scanner :</a> provides a static method for scanning Busybox OS installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/operating_systems#centos_scanner-class">CentOS_Scanner :</a> provides a static method for scanning CentOS installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/operating_systems#debian_os_scanner-class">Debian_OS_Scanner :</a> provides a static method for scanning Debian OS installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/operating_systems#freebsd_os_scanner-class">FreeBSD_OS_Scanner :</a> provides a static method for scanning FreeBSD OS installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/operating_systems#ios_scanner-class">IOS_Scanner :</a> provides a static method for scanning iOS installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/operating_systems#mac_os_scanner-class">Mac_OS_Scanner :</a> provides a static method for scanning macOS installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/operating_systems#ubuntu_os_scanner-class">Ubuntu_OS_Scanner :</a> provides a static method for scanning Ubuntu OS installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/operating_systems#windows_os_scanner-class">Windows_OS_Scanner :</a> provides a static method for scanning Windows OS installations using the Vulners database.</li>
<br>
</ul>





<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities"><b>Vulnerability Scanners:</b></a> </li>
  <br><ul>

<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#ADB_Exploit_Scanner-class">ADB_Exploit_Scanner :</a> used to scan for Android Debug Bridge (ADB) vulnerabilities on a target device.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#Backend_Technologies_Scanner-class">Backend_Technologies_Scanner :</a> used to scan web applications for information about the backend technologies and potential vulnerabilities associated with them.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#ClickJacking_Scanner-class">ClickJacking_Scanner :</a> used to scan a web page for Clickjacking protection headers and determine if Clickjacking is possible.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#CORS_Misconfiguration_Scanner-class">CORS_Misconfiguration_Scanner :</a> used to detect Cross-Origin Resource Sharing (CORS) misconfigurations in web applications.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#CRLF_Injection_Scanner-class">CRLF_Injection_Scanner :</a> used to detect potential CRLF (Carriage Return Line Feed) injection vulnerabilities in web applications.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#CSRF_Scanner-class">CSRF_Scanner :</a> used for scanning and detecting Cross-Site Request Forgery (CSRF) vulnerabilities on web pages. It provides methods to identify vulnerable forms and perform tests to check for CSRF vulnerabilities.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#Exposed_ENV_Scanner-class">Exposed_ENV_Scanner :</a> used for scanning and detecting exposed environment (".env") files on web servers. It provides methods to check if a specific path or multiple common paths lead to an exposed environment file.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#Exposed_Git_Scanner-class">Exposed_Git_Scanner :</a> used to scan for exposed Git repositories on web servers. It checks if a specific URL is an exposed Git repository and returns a boolean result.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#Exposed_Telnet_Scanner-class">Exposed_Telnet_Scanner :</a> used to scan for exposed an unauthenticated Telnet services on a remote host. It attempts to establish a Telnet connection to a specified host and port and returns a boolean result indicating whether the connection was successful or not.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#File_Upload_Scanner-class">File_Upload_Scanner :</a> used to scan web forms for potential file upload vulnerabilities. It searches for forms that allow file uploads, tests the file upload functionality, and reports potential issues such as unacceptable file extensions.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#Open_Redirect_Scanner-class">Open_Redirect_Scanner :</a> used to scan web forms for potential open redirect vulnerabilities. It detects and reports open redirect issues in web applications, helping security professionals identify and mitigate these risks.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#Path_Traversal_Scanner-class">Path_Traversal_Scanner :</a> used to scan web applications for Path Traversal vulnerabilities. It provides methods to check for directory traversal and file inclusion vulnerabilities in web pages.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#PHP_Unit_Exploit_Scanner-class">PHP_Unit_Exploit_Scanner :</a> used to detect vulnerabilities related to the PHP Unit exploit on a specified website URL.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#RCE_Scanner-class">RCE_Scanner :</a> used for scanning web forms for Remote Code / Command Execution (RCE) vulnerabilities using various payload injections.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#Shodan_Scanner-class">Shodan_Scanner :</a> designed to interact with the Shodan API and retrieve information about a specific IP address.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#Mixed_Content_Scanner-class">Mixed_Content_Scanner :</a> used to scan web pages for mixed content vulnerabilities, where HTTP content is loaded on an HTTPS page.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#SpringBoot_Actuator_Exploit_Scanner-class">SpringBoot_Actuator_Exploit_Scanner :</a> used to scan a Spring Boot application for vulnerabilities in the Actuator endpoints.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#SSRF_Scanner-class">SSRF_Scanner :</a> used for scanning web pages for Server-Side Request Forgery (SSRF) vulnerabilities.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#SSTI_Scanner-class">SSTI_Scanner :</a> used for scanning websites for Server-Side Template Injection (SSTI) vulnerabilities.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#Vulners_Search_Scanner-class">Vulners_Search_Scanner :</a> used to search for vulnerabilities in software using the Vulners API.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/vulnerabilities#XSS_Scanner-class">XSS_Scanner :</a> designed for systematically identifying and testing Cross-Site Scripting (XSS) vulnerabilities in web applications. This method allows users to spider through web pages, identify forms, and test them for XSS vulnerabilities. It provides flexibility to test multiple pages and payloads.</li>
<br>
<!-- Utils Directory -->
</ul>



<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_dev"><b>Web Development :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_dev#aspnet_dast_scanner-class">ASPNET_DAST_Scanner :</a> designed to perform dynamic application security testing (DAST) on ASP.NET sites. It scans for known vulnerabilities using the Vulners database and provides detailed information about the ASP.NET site's configuration, version, and potential exploits.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_dev#php_dast_scanner-class">PHP_DAST_Scanner :</a> designed to perform dynamic application security testing (DAST) on PHP sites. It scans for known vulnerabilities using the Vulners database and provides detailed information about the PHP site's configuration, version, and potential exploits.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_dev#ruby_dast_scanner-class">Ruby_DAST_Scanner :</a> designed to perform dynamic application security testing (DAST) on Ruby on Rails sites. It scans for known vulnerabilities using the Vulners database and provides detailed information about the Ruby on Rails site's configuration, versions, and potential exploits.</li>
<br>
</ul>




<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_servers"><b>Web Development Frameworks :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_dev_frameworks#django_scanner-class">Django_Scanner :</a> provides a static method for scanning Django installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_dev_frameworks#fastapi_scanner-class">FastAPI_Scanner :</a> provides a static method for scanning FastAPI installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_dev_frameworks#flask_scanner-class">Flask_Scanner :</a> provides a static method for scanning Flask installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_dev_frameworks#laravel_scanner-class">Laravel_Scanner :</a> provides a static method for scanning Laravel installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_dev_frameworks#spring_boot_scanner-class">Spring_Boot_Scanner :</a> provides a static method for scanning Spring Boot installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_dev_frameworks#spring_security_scanner-class">Spring_Security_Scanner :</a> provides a static method for scanning Spring Security installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_dev_frameworks#symfony_scanner-class">Symfony_Scanner :</a> provides a static method for scanning Symfony installations using the Vulners database.</li>
<br>
</ul>






<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_servers"><b>Web Servers :</b></a> </li>
 <br> <ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_servers#apache_coyote_server_scanner-class">Apache_Coyote_Server_Scanner :</a> provides a static method for scanning Apache Coyote Server installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_servers#apache_http_server_scanner-class">Apache_HTTP_Server_Scanner :</a> provides a static method for scanning Apache HTTP Server installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_servers#apache_tomcat_server_scanner-class">Apache_Tomcat_Server_Scanner :</a> provides a static method for scanning Apache Tomcat Server installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_servers#glassfish_server_scanner-class">GlassFish_Server_Scanner :</a> provides a static method for scanning GlassFish Server installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_servers#jetty_server_scanner-class">Jetty_Server_Scanner :</a> provides a static method for scanning Jetty Server installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_servers#microsoft_iis_server_scanner-class">Microsoft_IIS_Server_Scanner :</a> provides a static method for scanning Microsoft IIS Server installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_servers#nginx_server_scanner-class">Nginx_Server_Scanner :</a> provides a static method for scanning Nginx Server installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_servers#payara_server_scanner-class">Payara_Server_Scanner :</a> provides a static method for scanning Payara Server installations using the Vulners database.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/scanners/web_servers#windows_server_scanner-class">Windows_Server_Scanner :</a> provides a static method for scanning Windows Server installations using the Vulners database.</li>
<br>
</ul>











<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/pager"><b>Web Pages Analyzers:</b></a> </li>
  <br><ul>

<!-- Utils/pager Directory -->
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/pager#Cookies_Manager-class">Cookies_Manager :</a> provides methods for managing HTTP cookies.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/pager#FORMS_FILLER-class">FORMS_FILLER :</a> provides methods for filling HTML forms with data, including injecting payloads into form parameters.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/pager#FORMS_FINDER-class">FORMS_FINDER :</a> provides methods for extracting and parsing HTML forms from web pages. It offers methods for sorting inputs in forms and parsing forms from web pages. </li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/pager#FORM_FILE_UPLOAD-class">FORM_FILE_UPLOAD :</a> used for extracting and identifying file upload forms from HTML documents. It provides methods to retrieve these forms both from a list of dictionaries and from a URL with HTML content.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/pager#Pager_Interface-class">Pager_Interface :</a> provides various methods for web scraping and JavaScript code analysis.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/pager#RANDOM_GENERATOR-class">RANDOM_GENERATOR :</a> provides various static methods for generating random data, such as IP addresses, URLs, phone numbers, HTML input colors, and random dates.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/pager#LOGIN_FORM_FILLER-class">LOGIN_FORM_FILLER :</a> provides methods for working with login forms in web pages. It includes methods for getting a login form and setting its values for username and password.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/pager#URLS_Parser-class">URLS_Parser :</a> provides methods for parsing and extracting information from URLs and web page sources. It includes methods for converting URLs to form data and extracting links from the page source.</li>
</ul>
<br>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/proxer"><b>Useful Proxing Utilities:</b></a> </li>
  <br><ul>

<!-- Utils/proxer Directory -->
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/proxer#BurpSuite_Getter-class">BurpSuite_Getter :</a> provides a method for obtaining a Burp Suite proxy configuration. It includes a method for getting the Burp Suite proxy settings with optional host and port parameters.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/proxer#Proxies_Collector-class">Proxies_Collector :</a> used to collect and verify proxy information from various sources.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/proxer#Proxies_Interface-class">Proxies_Interface :</a> provides methods for loading, parsing, and converting proxy data for use in various applications.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/proxer#ProxyChecker-class">ProxyChecker :</a> responsible for checking the validity and functionality of proxy servers in a list. It can perform proxy checks using either socket-level connections or HTTP requests, depending on the configuration.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/proxer#Proxies_Getter-class">Proxies_Getter :</a> used to retrieve proxy sockets and proxy settings for various protocols.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils/proxer#Proxies_Parser-class">Proxies_Parser :</a> used to parse and handle proxy configurations and settings.</li>
</ul>
<br>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils"><b>Additional Useful Modules :</b></a></li>
  <br><ul>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils#Userful_Utilities-class">Userful_Utilities :</a> provides various utility methods for common tasks and operations.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils#Files_Interface-class">Files_Interface :</a> provides utility methods for working with files, including clearing, deleting, writing, and reading files. It also includes methods for creating and reading JSON files.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils#Bane_Instances_Interface-class">Bane_Instances_Interface :</a> provides utility methods for working with instances of other classes, especially those created for parallel processing.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils#Socket_Connection-class">Socket_Connection :</a> provides methods for creating and configuring socket connections.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils#Tor_Switch_Interface-class">Tor_Switch_Interface :</a> provides methods for switching IP addresses when using the Tor network. It allows for automatic IP switching with or without a password, depending on the Tor configuration and platform.</li>
<li><a href="https://github.com/AlaBouali/bane/tree/master/bane/utils#Update_Module_Interface-class">Update_Module_Interface :</a> provides methods for updating the "bane" module to a specified version or the latest version available.</li>
</ul>