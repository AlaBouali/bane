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
