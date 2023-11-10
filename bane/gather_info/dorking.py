import googlesearch,random,time
from ..common.payloads import *

class Dorking_Info:

    @staticmethod
    def google(
        q,
        max_results=100,
        language="en",
        start_from=1,
        stop_on=None,
        top_level_domain="com",
        pause=2,
        user_agent=None,
        **kwargs
    ):
        started_at=time.time()
        if user_agent==None:
            user_agent=random.choice(Common_Variables.user_agents_list)
        j = []
        j += googlesearch.search(
            q,
            num=max_results,
            lang=language,
            start=start_from,
            stop=stop_on,
            tld=top_level_domain,
            pause=pause,
            user_agent=user_agent,
            **kwargs
        )
        l = []
        for x in j:
            if x not in l:
                l.append(x)
        return {'result':l,'start_date':started_at,'end_date':time.time()}

