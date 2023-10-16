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
            headers={"User-Agent": random.choice(ua)},
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


def webcams(count=10, by={"country": "us"}, timeout=10):
    a = 0
    f = {}
    x = 1
    if by:
        key = list(by.keys())[0]
        if key not in ["country", "tag", "city", "timezone", "type"]:
            raise Exception(
                "Your search must be in one of these categories: country, city, timezone, type, tag"
            )
        value = by[key].lower()
        if "country" in by:
            if by["country"].lower() not in [
                "af",
                "ax",
                "al",
                "dz",
                "as",
                "ad",
                "ao",
                "ai",
                "aq",
                "ag",
                "ar",
                "am",
                "aw",
                "au",
                "at",
                "az",
                "bs",
                "bh",
                "bd",
                "bb",
                "by",
                "be",
                "bz",
                "bj",
                "bm",
                "bt",
                "bo",
                "bq",
                "ba",
                "bw",
                "br",
                "io",
                "bn",
                "bg",
                "bf",
                "bi",
                "cv",
                "kh",
                "cm",
                "ca",
                "ky",
                "cf",
                "td",
                "cl",
                "cn",
                "cx",
                "cc",
                "co",
                "km",
                "cd",
                "cg",
                "ck",
                "cr",
                "ci",
                "hr",
                "cu",
                "cw",
                "cy",
                "cz",
                "dk",
                "dj",
                "dm",
                "do",
                "ec",
                "eg",
                "sv",
                "gq",
                "er",
                "ee",
                "sz",
                "et",
                "fk",
                "fo",
                "fj",
                "fi",
                "fr",
                "gf",
                "pf",
                "tf",
                "ga",
                "gm",
                "ge",
                "de",
                "gh",
                "gi",
                "gr",
                "gl",
                "gd",
                "gp",
                "gu",
                "gt",
                "gg",
                "gn",
                "gw",
                "gy",
                "ht",
                "hm",
                "va",
                "hn",
                "hk",
                "hu",
                "is",
                "in",
                "id",
                "ir",
                "iq",
                "ie",
                "im",
                "il",
                "it",
                "jm",
                "jp",
                "je",
                "jo",
                "kz",
                "ke",
                "ki",
                "kp",
                "kr",
                "kw",
                "kg",
                "la",
                "lv",
                "lb",
                "ls",
                "lr",
                "ly",
                "li",
                "lt",
                "lu",
                "mo",
                "mk",
                "mg",
                "mw",
                "my",
                "mv",
                "ml",
                "mt",
                "mh",
                "mq",
                "mr",
                "mu",
                "yt",
                "mx",
                "fm",
                "md",
                "mc",
                "mn",
                "me",
                "ms",
                "ma",
                "mz",
                "mm",
                "na",
                "nr",
                "np",
                "nl",
                "nc",
                "nz",
                "ni",
                "ne",
                "ng",
                "nu",
                "nf",
                "mp",
                "no",
                "om",
                "pk",
                "pw",
                "ps",
                "pa",
                "pg",
                "py",
                "pe",
                "ph",
                "pn",
                "pl",
                "pt",
                "pr",
                "qa",
                "re",
                "ro",
                "ru",
                "rw",
                "bl",
                "sh",
                "kn",
                "lc",
                "mf",
                "pm",
                "vc",
                "ws",
                "sm",
                "st",
                "sa",
                "sn",
                "rs",
                "sc",
                "sl",
                "sg",
                "sx",
                "sk",
                "si",
                "sb",
                "so",
                "za",
                "gs",
                "ss",
                "es",
                "lk",
                "sd",
                "sr",
                "se",
                "ch",
                "sy",
                "tw",
                "tj",
                "tz",
                "th",
                "tl",
                "tg",
                "tk",
                "to",
                "tt",
                "tn",
                "tr",
                "tm",
                "tc",
                "tv",
                "ug",
                "ua",
                "ae",
                "gb",
                "us",
                "uy",
                "uz",
                "vu",
                "ve",
                "vn",
                "vg",
                "vi",
                "wf",
                "ye",
                "zm",
                "zw",
            ]:
                raise Exception("Unexisting Country code")
        url = "https://www.insecam.org/en/by{}/{}/?page=".format(key, value)
    else:
        url = "https://www.insecam.org/en/byrating/?page="
    while True:
        try:
            soup = BeautifulSoup(
                requests.Session().get(
                    url + str(x),
                    headers={"User-Agent": random.choice(ua)},
                    timeout=timeout,
                ).text,
                "html.parser",
            )
            fi = soup.findAll("img", {"class": "thumbnail-item__img img-responsive"})
            for i in fi:
                j = HTMLParser.HTMLParser().unescape(i["src"])
                o = HTMLParser.HTMLParser().unescape(i["title"])
                f.update({j: o})
            if (len(fi) == 0) or (a == len(f)):
                break
            a = len(f)
        except Exception as e:
            break
        if len(f) >= int(count):
            break
        x += 1
    return {k: f[k] for k in list(f.keys())[: int(count)]}
