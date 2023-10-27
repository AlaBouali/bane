from .utils import *

class RANDOM_GENERATOR:

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


