import gc

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

