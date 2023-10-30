import gc,time

class Bane_Instances_Interface:

    @staticmethod
    def process_threaded(a, check_interval=0.1):
        while True:
            try:
                if a.done() == True:
                    try:
                        return a.result
                    except:
                        pass
                    try:
                        return a.counter
                    except:
                        return
                time.sleep(check_interval)
            except KeyboardInterrupt:
                a.stop = True
                try:
                    return a.result
                except:
                    pass
                try:
                    return a.counter
                except:
                    pass



    @staticmethod
    def get_current_instances(instance_type):
        active = []
        inactive = []
        b = list(gc.get_objects())
        for x in b:
            try:
                if "bane." + instance_type in x.__repr__():
                    try:
                        if x.done() == True:
                            inactive.append(x)
                        else:
                            active.append(x)
                    except:
                        pass
            except:
                pass
        return {"active": active, "inactive": inactive}

