from .utils import *

class RANDOM_GENERATOR:

    @staticmethod
    def get_random_ip():
        """
        this function was inspired by the scanning file in mirai's source code to returns a safe IP to bruteforce."""
        while True:
            ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
            ip=u'{}'.format(ip)
            ip_obj = ipaddress.IPv4Address(ip)

            # Check if the generated IP address is not in any of the specified ranges
            is_valid = True
            for network in Common_Variables.private_ip_ranges:
                if ip_obj in network:
                    is_valid = False
                    break

            if is_valid:
                return str(ip_obj)

    @staticmethod
    def get_safe_random_ip():
        while True:
            ip=ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
            ip=u'{}'.format(ip)
            ip_obj = ipaddress.IPv4Address(ip)

            # Check if the generated IP address is not in any of the specified ranges
            is_valid = True
            for network in Common_Variables.excluded_ip_ranges:
                if ip_obj in network:
                    is_valid = False
                    break

            if is_valid:
                return str(ip_obj)


    @staticmethod
    def generate_random_url():
        protocols = ["http", "https"]
        protocol = random.choice(protocols)
        domain = random.choice(Common_Variables.domains_list)
        return "{}://{}/".format(protocol,domain)


    @staticmethod
    def generate_random_phone_number(pattern):
        phone_number = ""
        for char in pattern:
            if char == "X":
                random_digit = str(random.randint(0, 9))
                phone_number += random_digit
            else:
                phone_number += char
        return phone_number

    @staticmethod
    def generate_random_html_input_color():
        # Generate random RGB values
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # Convert RGB to hexadecimal
        color_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)
        return color_hex


    @staticmethod
    def random_date(start_date, end_date):
        if start_date==end_date:
            return start_date
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date.strftime("%Y-%m-%d")

    @staticmethod
    def get_random_user_agent(browser_header=None,system_info=None,system_platform=None,operating_system=None,operating_system_name=None):
        if browser_header in ['', None]:
            browser_header = random.choice(Common_Variables.USER_AGENT_PARTS['browser_header'])
        if operating_system in ['', None]:
            operating_system = Common_Variables.USER_AGENT_PARTS['operating_system'][random.choice(list(Common_Variables.USER_AGENT_PARTS['operating_system'].keys()))]
        else:
            operating_system = Common_Variables.USER_AGENT_PARTS['operating_system'][operating_system]
        if operating_system_name in ['', None]:
            operating_system_name = random.choice(operating_system['name'])
        if system_info in ['', None]:
            system_info = operating_system_name
        if system_platform in ['', None]:
            system_platform = Common_Variables.USER_AGENT_PARTS['system_platform'][random.choice(list(Common_Variables.USER_AGENT_PARTS['system_platform'].keys()))]
        if 'browser_info' in system_platform and system_platform['browser_info']:
            browser = system_platform['browser_info']
            browser_string = random.choice(browser['name'])
            if 'ext_pre' in browser:
                browser_string = "%s; %s" % (random.choice(browser['ext_pre']), browser_string)
            system_info = "%s; %s" % (browser_string, system_info)
            if 'ext_post' in browser:
                system_info = "%s; %s" % (system_info, random.choice(browser['ext_post']))
        if 'ext' in operating_system and operating_system['ext']:
            system_info = "%s; %s" % (system_info, random.choice(operating_system['ext']))
        ua_string = "%s (%s)" % (browser_header, system_info)
        if 'name' in system_platform and system_platform['name']:
            ua_string = "%s %s" % (ua_string, random.choice(system_platform['name']))
        if 'details' in system_platform and system_platform['details']:
            ua_string = "%s (%s)" % (ua_string, random.choice(system_platform['details']) if len(system_platform['details']) > 1 else system_platform['details'][0] )
        if 'extensions' in system_platform and system_platform['extensions']:
            ua_string = "%s %s" % (ua_string, random.choice(system_platform['extensions']))
        return ua_string
    
    @staticmethod
    def update_user_agents_list(max_user_agents=20000):
        l=[]
        while True:
            a=RANDOM_GENERATOR.get_random_user_agent()
            if a not in Common_Variables.user_agents_list:
                l.append(a)
            if len(l)==max_user_agents:
                break
        Common_Variables.user_agents_list=l