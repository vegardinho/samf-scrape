import mechanicalsoup as ms
import keyring

BROWSER = ms.Browser()
ACCOUNTS = ["landsverk.vegard@gmail.com"]
URL = "https://medlem.samfundet.no/"


def main():
    for ACC in ACCOUNTS:
        # find_event()
        log_in(ACC)

def get_site(url):
    login_page = BROWSER.get(URL)
    return login_page.soup


def find_event():
    site = get_site("https://www.samfundet.no/arrangement/2830-svommebasseng-storsalen")
    print(site.prettify())

    #TODO: hvis ikke html for knapp eksisterer: exit

    buy_btn = login_html.find("div", class_="purchase-button")
    print(buy_btn)

def log_in(email):
    site = get_site(URL)
    form = site.select("form")[0]

    pswd = keyring.get_password("Samfundet", email)

    form.find(id="username")["value"] = email
    form.find(id="password")["value"] = pswd

    new_page = BROWSER.submit(form, URL)

    print(new_page.soup.prettify())


if __name__ == '__main__':
    main()
