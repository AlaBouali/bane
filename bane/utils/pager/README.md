<h1>Cookies_Manager Class</h1>

<h2>Class Overview</h2>
<p>The <code>Cookies_Manager</code> class is part of the "bane" module and provides methods for managing HTTP cookies.</p>

<h2>Method <code>scan</code></h2>
<pre><code>def scan(cookies: str, cook: str) -&gt; str</code></pre>
<p>The <code>scan</code> method is used to update and set HTTP cookies. It takes the following parameters:</p>

<ul>
    <li><code>cookies</code> (str): A string representing the existing cookies in the format "name1=value1; name2=value2; ...".</li>
    <li><code>cook</code> (str): A string representing new cookies in the same format as the <code>cookies</code> parameter.</li>
</ul>

<p>The method combines and updates the provided cookies and returns a new cookie string.</p>

<h2>Example Usage</h2>
<p>Here's an example of using the <code>scan</code> method from the <code>Cookies_Manager</code> class:</p>

<pre><code>
#Import the Cookies_Manager class
from bane.Cookies_Manager import Cookies_Manager

#Existing cookies
existing_cookies = "user=John; session=12345;"

#New cookies to be added or updated
new_cookies = "session=67890; role=admin;"

#Use the scan method to update and set cookies
result_cookies = Cookies_Manager.scan(existing_cookies, new_cookies)

#The result_cookies now contains the updated cookies
print("Updated Cookies:", result_cookies)
</code></pre>
</p>
<h1>FORM_FILE_UPLOAD Class</h1>

<h2>Class Overview</h2>
<p>The <code>FORM_FILE_UPLOAD</code> class is used for extracting and identifying file upload forms from HTML documents. It provides methods to retrieve these forms both from a list of dictionaries and from a URL with HTML content.</p>

<h2>Methods</h2>

<h3><code>get_upload_form(a: List[Dict]) -&gt; List[Dict]</code></h3>
<p>The <code>get_upload_form</code> method retrieves file upload forms from a list of dictionaries containing HTML form data. It takes the following parameter:</p>

<ul>
    <li><code>a</code> (List[Dict]): A list of dictionaries, where each dictionary represents an HTML form containing input elements.</li>
</ul>

<p>The method scans the input elements within each form dictionary and returns a list of dictionaries that represent file upload forms found within the provided list.</p>

<h3><code>get_upload_form_text(url: str, text: str) -&gt; List[Dict]</code></h3>
<p>The <code>get_upload_form_text</code> method retrieves file upload forms from HTML content fetched from a URL. It takes the following parameters:</p>

<ul>
    <li><code>url</code> (str): The URL from which the HTML content is fetched.</li>
    <li><code>text</code> (str): The HTML content as a string.</li>
</ul>

<p>The method utilizes the <code>FORMS_FINDER.forms_parser_text</code method to parse the HTML content and then scans for file upload forms within the parsed data. It returns a list of dictionaries representing file upload forms found in the HTML content.</p>

<h2>Example Usage</h2>
<p>Here are examples of how to use the methods from the <code>FORM_FILE_UPLOAD</code> class:</p>

<p>Using <code>get_upload_form</code> to extract file upload forms from a list of form dictionaries:</p>

<pre><code>
#Import the FORM_FILE_UPLOAD class
from bane import FORM_FILE_UPLOAD

#Sample list of form dictionaries
form_data = [
    {
        "inputs": [
            {"type": "text"},
            {"type": "file"},
        ]
        #Other form data...
    },
    #Other form dictionaries...
]

#Get file upload forms from the list
file_upload_forms = FORM_FILE_UPLOAD.get_upload_form(form_data)

#Print the identified file upload forms
for form in file_upload_forms:
    print("File Upload Form:", form)
</code></pre>

<p>Using <code>get_upload_form_text</code to fetch and extract file upload forms from HTML content:</p>

<pre><code>
#Import the FORM_FILE_UPLOAD class
from your_module import FORM_FILE_UPLOAD

#URL and HTML content as strings
url = "https://example.com/upload"
html_content = "<html>...</html>"

#Get file upload forms from HTML content
file_upload_forms = FORM_FILE_UPLOAD.get_upload_form_text(url, html_content)

#Print the identified file upload forms
for form in file_upload_forms:
    print("File Upload Form:", form)
</code></pre>
</p>
<h1>FORMS_FILLER Class</h1>

<h2>Class Overview</h2>
<p>The <code>FORMS_FILLER</code> class is part of the "bane" module and provides methods for filling HTML forms with data, including injecting payloads into form parameters. It offers two main methods: <code>set_up_injection</code> and <code>form_filler</code>.</p>

<h2>Methods</h2>

<h3><code>set_up_injection</code></h3>
<pre><code>def set_up_injection(
    url: str,
    form_index: int,
    parameter: str,
    payload: str,
    cookie: str,
    user_agent: str,
    proxy: dict,
    timeout: int,
    auto_fill: int,
    file_extension: str = "png",
    email_extension: str = '@gmail.com',
    phone_pattern: str = 'XXX-XXX-XXXX',
    dont_change: dict = {},
    number: Tuple[int, int] = (1, 9),
    leave_empty: list = [],
    dont_send: list = [],
    mime_type: str = None,
    predefined_inputs: dict = {},
    headers: dict = {}
) -&gt; Tuple[dict, dict, dict, int]</code></pre>
<p>The <code>set_up_injection</code> method prepares form data for payload injection. It performs the following tasks:</p>

<ul>
    <li>Fetches HTML content from a URL.</li>
    <li>Parses form data from the HTML content based on the provided form index.</li>
    <li>Sets up HTTP headers, cookies, and other parameters for making a request.</li>
    <li>Uses the <code>form_filler</code> method to inject payloads into the form parameters.</li>
</ul>

<p>It returns a tuple containing the modified form data, HTTP headers, proxy settings, and the timeout value.</p>

<h3><code>form_filler</code></h3>
<pre><code>def form_filler(
    form: dict,
    param: str,
    payload: str,
    file_extension: str = "png",
    email_extension: str = '@gmail.com',
    phone_pattern: str = 'XXX-XXX-XXXX',
    dont_change: dict = {},
    number: Tuple[int, int] = (1, 9),
    auto_fill: int = 10,
    leave_empty: list = [],
    dont_send: list = [],
    mime_type: str = None,
    predefined_inputs: dict = {}
) -&gt; dict</code></pre>
<p>The <code>form_filler</code> method injects payloads and data into the specified form. It takes the following parameters:</p>

<ul>
    <li><code>form</code> (dict): A dictionary representing an HTML form with input elements.</li>
    <li><code>param</code> (str): The parameter name to inject payloads into.</li>
    <li><code>payload</code> (str): The payload data to inject into the specified parameter.</li>
</ul>

<p>This method updates the form with injected data and returns the modified form dictionary.</p>

<h2>Example Usage</h2>
<p>Here's an example of using the <code>FORMS_FILLER</code> methods:</p>

<p>Using <code>set_up_injection</code> to prepare form data for payload injection:</p>

<pre><code>
#Import the FORMS_FILLER class
from bane import FORMS_FILLER

#Define injection parameters
url = "https://example.com/form"
form_index = 0
parameter = "username"
payload = "malicious_payload"
cookie = "session=12345"
user_agent = "CustomUserAgent"
proxy = {"http": "http://proxy_server:8080"}
timeout = 10
auto_fill = 5

#Prepare form data for injection
result_data, headers, proxy_settings, request_timeout = FORMS_FILLER.set_up_injection(
    url, form_index, parameter, payload, cookie, user_agent, proxy, timeout, auto_fill
)

#Now, you can use the result_data, headers, proxy_settings, and request_timeout for making a request.
</code></pre>

<p>Using <code>form_filler</code> to inject payloads into a form:</p>

<pre><code>
#Import the FORMS_FILLER class
from bane import FORMS_FILLER

#Sample form data as a dictionary
form_data = {
    "inputs": [
        {"name": "username", "type": "text"},
        {"name": "password", "type": "password"},
        #Other form input elements...
    ],
    #Other form data...
}

#Define injection parameters
param = "username"
payload = "malicious_payload"
file_extension = "png"
email_extension = "@evil.com"
phone_pattern = "XXX-XXX-XXXX"
dont_change = {"password": "secure_password"}
number = (1, 9)
auto_fill = 5
leave_empty = ["email"]
dont_send = ["hidden_field"]
mime_type = "application/pdf"
predefined_inputs = {"country": "USA"}

#Inject payloads into the form
result_form = FORMS_FILLER.form_filler(
    form_data, param, payload, file_extension, email_extension, phone_pattern, dont_change,
    number, auto_fill, leave_empty, dont_send, mime_type, predefined_inputs
)

#The result_form now contains the modified form data with injected payloads.
</code></pre>
</p>
<h1>FORMS_FINDER Class</h1>

<h2>Class Overview</h2>
<p>The <code>FORMS_FINDER</code> class is part of the "bane" module and provides methods for extracting and parsing HTML forms from web pages. It offers methods for sorting inputs in forms and parsing forms from web pages.</p>

<h2>Methods</h2>

<h3><code>sort_inputs</code></h3>
<pre><code>def sort_inputs(inputs: List[dict]) -&gt; List[dict]</code></pre>
<p>The <code>sort_inputs</code> method takes a list of input dictionaries and sorts them based on their type. It groups radio and checkbox inputs with the same name together and returns a sorted list of input dictionaries.</p>

<h3><code>forms_parser</code></h3>
<pre><code>def forms_parser(
    u: str,
    html_comments: bool = False,
    user_agent: str = None,
    timeout: int = 10,
    bypass: bool = False,
    proxy: dict = None,
    cookie: str = None,
    include_links: bool = True,
    headers: dict = {}
) -&gt; List[dict]</code></pre>
<p>The <code>forms_parser</code> method extracts and parses forms from a web page specified by the URL <code>u</code>. It returns a list of dictionaries, each representing a form with detailed information, including form inputs, action URL, method, and more.</p>

<h3><code>forms_parser_text</code></h3>
<pre><code>def forms_parser_text(
    u: str,
    text: str,
    html_comments: bool = False,
    include_links: bool = True
) -&gt; List[dict]</code></pre>
<p>The <code>forms_parser_text</code> method extracts and parses forms from the provided HTML <code>text</code>. It returns a list of dictionaries, each representing a form with detailed information, including form inputs, action URL, method, and more.</p>

<h2>Example Usage</h2>
<p>Here's an example of using the <code>FORMS_FINDER</code> methods:</p>

<p>Using <code>sort_inputs</code> to sort input elements in a list:</p>

<pre><code>
#Import the FORMS_FINDER class
from your_module import FORMS_FINDER

#Sample list of input dictionaries
input_list = [
    {"name": "username", "type": "text"},
    {"name": "password", "type": "password"},
    {"name": "remember_me", "type": "checkbox"},
    {"name": "gender", "type": "radio"},
    #Other input dictionaries...
]

#Sort the input elements
sorted_inputs = FORMS_FINDER.sort_inputs(input_list)

#The sorted_inputs list now contains grouped radio and checkbox inputs.
</code></pre>

<p>Using <code>forms_parser</code> to extract and parse forms from a web page:</p>

<pre><code>
#Import the FORMS_FINDER class
from bane import FORMS_FINDER

#Define parsing parameters
url = "https://example.com/form-page"
html_comments = False
user_agent = "CustomUserAgent"
timeout = 10
bypass = False
proxy = {"http": "http://proxy_server:8080"}
cookie = "session=12345"
include_links = True
headers = {"Custom-Header": "Value"}

#Extract and parse forms from the web page
form_data = FORMS_FINDER.forms_parser(
    url, html_comments, user_agent, timeout, bypass, proxy, cookie, include_links, headers
)

#The form_data list now contains detailed information about forms on the web page.
</code></pre>

<p>Using <code>forms_parser_text</code> to extract and parse forms from HTML text:</p>

<pre><code>
#Import the FORMS_FINDER class
from bane import FORMS_FINDER

#Define HTML text content
html_text = "..."
html_comments = False
include_links = True

#Extract and parse forms from HTML text
form_data = FORMS_FINDER.forms_parser_text(html_text, html_comments, include_links)

#The form_data list now contains detailed information about forms in the HTML text.
</code></pre>
</p>

<h1>Pager_Interface Class</h1>

<h2>Class Overview</h2>
<p>The <code>Pager_Interface</code> class is part of the "bane" module and provides various methods for web scraping and JavaScript code analysis.</p>

<h2>Methods</h2>

<h3><code>spider_url(base_url, include_links=False, include_id=False, max_pages=5, timeout=15, cookie=None, user_agent=None, proxy=None, headers={}, parse_forms=False, only_urls=True)</code></h3>
<p>This method scrapes web pages, starting from a base URL, and collects URLs. It supports the following parameters:</p>
<ul>
    <li><code>base_url</code> (str): The starting URL for web scraping.</li>
    <li><code>include_links</code> (bool): Include links in the collected data (default is False).</li>
    <li><code>include_id</code> (bool): Include HTML element IDs in the collected data (default is False).</li>
    <li><code>max_pages</code> (int): Maximum number of pages to scrape (default is 5).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 15).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>proxy</code> (dict): Dictionary of HTTP proxies, e.g., {"http":"http://1.2.3.4:80", "https":"http://1.2.3.4:80"}</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>parse_forms</code> (bool): Parse HTML forms on the web pages (default is False).</li>
    <li><code>only_urls</code> (bool): Collect only URLs (default is True).</li>
</ul>

<h3><code>extract_urls_from_js(js_content, base_url)</code></h3>
<p>This method extracts URLs from JavaScript code. It takes the following parameters:</p>
<ul>
    <li><code>js_content</code> (str): JavaScript code to extract URLs from.</li>
    <li><code>base_url</code> (str): The base URL to resolve relative URLs.</li>
</ul>

<h3><code>fetch_url(u, user_agent=None, timeout=10, proxy=None, cookie=None, headers={})</code></h3>
<p>This method fetches the content of a URL. It supports the following parameters:</p>
<ul>
    <li><code>u</code> (str): The URL to fetch.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for the request.</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>proxy</code> (dict): Dictionary of HTTP proxies for the request.</li>
    <li><code>cookie</code> (str): Custom cookies to include in the request.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
</ul>

<h3><code>readable_js_code(code)</code></h3>
<p>This method beautifies JavaScript code for better readability. It takes the following parameter:</p>
<ul>
    <li><code>code</code> (str): JavaScript code to beautify.</li>
</ul>

<h3><code>examine_js_code(u, user_agent=None, timeout=10, proxy=None, cookie=None, headers={})</code></h3>
<p>This method examines JavaScript code on a web page, searching for secrets. It supports the following parameters:</p>
<ul>
    <li><code>u</code> (str): The URL of the web page to examine.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>proxy</code> (dict): Dictionary of HTTP proxies for the request.</li>
    <li><code>cookie</code> (str): Custom cookies to include in the request.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
</ul>

<h3><code>extract_secrets_from_text(js_content)</code></h3>
<p>This method extracts secrets from JavaScript code. It takes the following parameter:</p>
<ul>
    <li><code>js_content</code> (str): JavaScript code to extract secrets from.</li>
</ul>

<h2>Example Usage</h2>
<p>Here's an example of how to use the <code>Pager_Interface</code> class:</p>

<pre><code>
from bane import Pager_Interface


#Scrape web pages and collect URLs
base_url = "https://example.com"
collected_urls = Pager_Interface.spider_url(
    base_url,
    include_links=True,
    include_id=True,
    max_pages=5,
    timeout=15,
    cookie="custom_cookie",
    user_agent="custom_user_agent",
    proxy={"http": "http://1.2.3.4:80", "https": "http://1.2.3.4:80"},
    headers={"Custom-Header": "Value"},
    parse_forms=True,
    only_urls=True
)

#Extract URLs from JavaScript code
js_content = "Your JavaScript code here"
base_url = "https://example.com"
js_urls = Pager_Interface.extract_urls_from_js(js_content, base_url)

#Fetch the content of a URL
url_to_fetch = "https://example.com/page"
fetched_content = Pager_Interface.fetch_url(
    url_to_fetch,
    user_agent="custom_user_agent",
    timeout=10,
    proxy={"http": "http://1.2.3.4:80", "https": "http://1.2.3.4:80"},
    cookie="custom_cookie",
    headers={"Custom-Header": "Value"}
)

#Beautify JavaScript code
beautified_code = Pager_Interface.readable_js_code(js_content)

#Examine JavaScript code for secrets
url_to_examine = "https://example.com/page"
secrets = Pager_Interface.examine_js_code(
    url_to_examine,
    user_agent="custom_user_agent",
    timeout=10,
    proxy={"http": "http://1.2.3.4:80", "https": "http://1.2.3.4:80"},
    cookie="custom_cookie",
    headers={"Custom-Header": "Value"}
)

#Extract secrets from JavaScript code
js_code = "Your JavaScript code here"
secrets = Pager_Interface.extract_secrets_from_text(js_code)
</code></pre>
<h1>RANDOM_GENERATOR Class</h1>

<h2>Class Overview</h2>
<p>The <code>RANDOM_GENERATOR</code> class provides various static methods for generating random data, such as IP addresses, URLs, phone numbers, HTML input colors, and random dates.</p>

<h2>Methods</h2>

<h3><code>get_random_ip()</code></h3>
<p>This method generates a random IPv4 address that is not in any of the specified private IP address ranges. It has no parameters and returns a safe IP address for brute force.</p>

<h3><code>get_safe_random_ip()</code></h3>
<p>This method generates a random IPv4 address that is not in any of the specified excluded IP address ranges. It has no parameters and returns a safe IP address.</p>

<h3><code>generate_random_url()</code></h3>
<p>This method generates a random URL with a random protocol (http or https) and a random domain from a predefined list. It has no parameters and returns the generated URL.</p>

<h3><code>generate_random_phone_number(pattern)</code></h3>
<p>This method generates a random phone number based on a given pattern. The pattern should contain 'X' characters, which will be replaced with random digits. It takes the following parameter:</p>
<ul>
    <li><code>pattern</code> (str): The pattern for the phone number, e.g., "XXX-XXX-XXXX".</li>
</ul>

<h3><code>generate_random_html_input_color()</code></h3>
<p>This method generates a random HTML input color in hexadecimal format (e.g., #RRGGBB). It has no parameters and returns the generated color.</p>

<h3><code>random_date(start_date, end_date)</code></h3>
<p>This method generates a random date between the specified start and end dates. It takes the following parameters:</p>
<ul>
    <li><code>start_date</code> (str): The start date in the format "YYYY-MM-DD".</li>
    <li><code>end_date</code> (str): The end date in the format "YYYY-MM-DD".</li>
</ul>

<h2>Example Usage</h2>
<p>Here's an example of how to use the <code>RANDOM_GENERATOR</code> class methods:</p>

<pre><code>
from bane import RANDOM_GENERATOR

#Generate a random IP address
random_ip = RANDOM_GENERATOR.get_random_ip()

#Generate a safe random IP address
safe_random_ip = RANDOM_GENERATOR.get_safe_random_ip()

#Generate a random URL
random_url = RANDOM_GENERATOR.generate_random_url()

#Generate a random phone number with a pattern
phone_pattern = "XXX-XXX-XXXX"
random_phone_number = RANDOM_GENERATOR.generate_random_phone_number(phone_pattern)

#Generate a random HTML input color
random_color = RANDOM_GENERATOR.generate_random_html_input_color()

#Generate a random date between two dates
start_date = "2023-01-01"
end_date = "2023-12-31"
random_date = RANDOM_GENERATOR.random_date(start_date, end_date)
</code></pre>
<h1>LOGIN_FORM_FILLER Class</h1>

<h2>Class Overview</h2>
<p>The <code>LOGIN_FORM_FILLER</code> class is part of the "bane" module and provides methods for working with login forms in web pages. It includes methods for getting a login form and setting its values for username and password.</p>

<h2>Methods</h2>

<h3><code>get_login_form(url, text)</code></h3>
<p>This method retrieves the login form from a web page based on the URL and the HTML content. It searches for a form that contains an input field with the type "password" and returns the form data. It takes the following parameters:</p>
<ul>
    <li><code>url</code> (str): The URL of the web page containing the login form.</li>
    <li><code>text</code> (str): The HTML content of the web page.</li>
</ul>

<h3><code>set_login_form(url, text, username, password)</code></h3>
<p>This method sets the values for the login form's username and password fields. It uses the information obtained from the <code>get_login_form</code> method to identify the form and its input fields. It returns a list containing a dictionary of input names and their values, along with the form's action URL. It takes the following parameters:</p>
<ul>
    <li><code>url</code> (str): The URL of the web page containing the login form.</li>
    <li><code>text</code> (str): The HTML content of the web page.</li>
    <li><code>username</code> (str): The username to be filled in the login form.</li>
    <li><code>password</code> (str): The password to be filled in the login form.</li>
</ul>

<h2>Example Usage</h2>
<p>Here's an example of how to use the <code>LOGIN_FORM_FILLER</code> class methods:</p>

<pre><code>
from bane import LOGIN_FORM_FILLER

#URL and HTML content of the web page
web_page_url = "https://example.com/login"
web_page_html = """
&lt;html&gt;
    &lt;form action=&quot;/login&quot; method=&quot;post&quot;&gt;
        &lt;input type=&quot;text&quot; name=&quot;username&quot; value=&quot;&quot;&gt;
        &lt;input type=&quot;password&quot; name=&quot;password&quot; value=&quot;&quot;&gt;
        &lt;input type=&quot;submit&quot; value=&quot;Login&quot;&gt;
    &lt;/form&gt;
&lt;/html&gt;
"""

#Get the login form from the web page
login_form_data = LOGIN_FORM_FILLER.get_login_form(web_page_url, web_page_html)

#Set the login form values for username and password
username_value = "your_username"
password_value = "your_password"
form_data, form_action = LOGIN_FORM_FILLER.set_login_form(
    web_page_url, web_page_html, username_value, password_value
)

#Now you can use the form_data and form_action to submit the login form
print("Form Data:", form_data)
print("Form Action:", form_action)
</code></pre>
