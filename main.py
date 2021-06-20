import mechanicalsoup as ms
import keyring

BROWSER = ms.Browser()
ACCOUNTS = ["landsverk.vegard@gmail.com"]
URL = "https://www.samfundet.no/arrangement/2830-svommebasseng-storsalen"


def main():
    for ACC in ACCOUNTS:
        find_event()
        # log_in(ACC)

def find_event():

    #TODO: hvis ikke html for knapp eksisterer: exit

    buy_btn = site.find("div", class_="purchase-button")
    print(buy_btn)

def log_in(email):
    site = BROWSER.get("https://medlem.samfundet.no/").soup
    form = site.select("form")[0]

    pswd = keyring.get_password("Samfundet", email)

    form.find(id="username")["value"] = email
    form.find(id="password")["value"] = pswd

    new_page = BROWSER.submit(form, URL)

    print(new_page.soup.prettify())


if __name__ == '__main__':
    main()
