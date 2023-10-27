import cgi, requests, os, random, re, hashlib, urllib, sys, json, gc,socket,socks
from bane.cryptographers import *
from bane.utils import *
if sys.version_info < (3, 0):
    import HTMLParser
else:
    import html.parser as HTMLParser
import bs4
from bs4 import BeautifulSoup
from bane.common import *
from bane.utils.pager import crawl








def escape_html(s):
    """
    function to return escaped html string
    """
    return cgi.escape(s, quote=True)


def unescape_html(s):
    """
    function to return unescaped html string
    """
    return HTMLParser.HTMLParser().unescape(s).encode("utf-8")



def youtube_search(q, proxy=None, timeout=10):
    """
    this function is for searching on youtub and returning a links of related videos."""
    q = q.replace(" ", "+")
    u = "https://www.youtube.com/results"
    params = {"search_query": q}
    l = []
    try:
        r = requests.Session().get(
            u,
            params,
            headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
            proxies=proxy,
            timeout=timeout,
        ).text
        soup = BeautifulSoup(r, "html.parser")
        yt = soup.find_all(attrs={"class": "yt-uix-tile-link"})
        for vi in yt:
            try:
                vi = "https://www.youtube.com" + str(vi["href"])
                if vi not in l:
                    l.append(vi)
            except Exception as ex:
                pass
    except Exception as e:
        pass
    return l

def generate_human_poc(data):
    if "is_url" not in data:
        raise ValueError("The 'is_url' key is missing in the input data")

    if data["is_url"]:
        # If is_url is True, generate a URL
        url = data.get("action", "")
        if not url:
            raise ValueError("Missing 'action' key for URL generation")
        
        query_parameters = []
        for input_field in data.get("inputs", []):
            name = input_field.get("name", "")
            value = input_field.get("value", "")
            query_parameters.append("{}={}".format(name,value))
        
        if query_parameters:
            url += "?" + "&".join(query_parameters)

        return url

    else:
        # If is_url is False, generate an HTML form
        form_id = data.get("id", "")
        form_method = data.get("method", "post")
        form_action = data.get("action", "")
        form_enctype = data.get("enctype", "application/x-www-form-urlencoded")

        inputs = ""
        for input_field in data.get("inputs", []):
            name = input_field.get("name", "")
            value = input_field.get("value", "")
            input_type = input_field.get("type", "text")
            required = "required" if input_field.get("required", False) else ""
            input_element = "<input type='{}' name='{}' value='{}' {}>".format(input_type,name,value,required)
            inputs += input_element

        html_form = """
        <form id='{}' method='{}' action='{}' enctype='{}'>
            {}
        </form>
        """.format(form_id,form_method,form_action,form_enctype,inputs)
        return html_form



