from bs4 import BeautifulSoup
from logic.cache import url_fetch


def parse_members_from_url(page_url):
    # member_addresses = []
    members = []
    page = url_fetch(page_url)
    soup = BeautifulSoup(page, features="html.parser")

    member_blocks = soup.find_all('div', {'class': 'mn-row-inner Rank1'})

    for member_block in member_blocks:

        # PARSE MEMBER NAME
        member_name = ""
        member_name_find = member_block.find_all('a', {'class': 'mn-main-heading'})
        if len(member_name_find) > 0:
            member_name = member_name_find[0].text.strip()

        # PARSE MEMBER PHONE
        member_phone = ''
        member_phone_find = member_block.find_all('span', {'class': 'mn-sub-heading'})
        if len(member_phone_find) > 0:
            member_phone = member_phone_find[0].text.strip()

        # PARSE MEMBER ADDRESS
        member_address = ''
        member_address_block = member_block.find_all('div', {'class': 'mn-block mn-address'})
        if len(member_address_block) > 0:

            member_street = ''
            member_street_find = member_address_block[0].find_all('span', {'class': 'mn-street'})
            if len(member_street_find) > 0:
                member_street = member_street_find[0].text.strip()

            member_city = ''
            member_city_find = member_address_block[0].find_all('span', {'class': 'mn-city'})
            if len(member_city_find) > 0:
                member_city = member_city_find[0].text.strip()

            member_state = ''
            member_state_find = member_address_block[0].find_all('span', {'class': 'mn-state'})
            if len(member_state_find) > 0:
                member_state = member_state_find[0].text.strip()

            member_zip = ''
            member_zip_find = member_address_block[0].find_all('span', {'class': 'mn-zip'})
            if len(member_zip_find) > 0:
                member_zip = member_zip_find[0].text.strip()

            # Construct Member Address (e.g. "PO Box 358, Nixa, MO 65714")
            member_address = member_street + ' ' + member_city + ' ' + member_state + ' ' + member_zip

        # PARSE MEMBER WEBSITE
        member_website = ""
        member_website_find = member_block.find_all('div', {'class': 'mn-block mn-listing-website'})
        if len(member_website_find) > 0:
            member_website = member_website_find[0].text.strip()

        member = [member_name, member_phone, member_address, member_website]
        members.append(member)

    return members

    """
    <!-- SAMPLE HTML -->
    <div class="mn-row-inner Rank1">
        <div class="mn-col-1-5 mn-directory-list-item" contacttype="2">
            <div class="mn-block mn-img-placeholder"></div>
        </div>
        <div class="mn-col-4-5">
            <div class="mn-block mn-listing-title">
                    <a class="mn-main-heading" href="//business.springfieldchamber.com/directory/Details/logic-forte-708107">Logic Forte</a>
                <span>
                    <span class="mn-divider-pipe"> | </span>
                    <span class="mn-sub-heading"><a href="tel:4177202325">(417) 720-2325</a></span>
                </span>
            </div>
            <div class="mn-block mn-listing-address">
                <div class="mn-text"><div class="mn-block mn-address">
                    <span class="mn-street">PO Box 358,</span>

                    <span class="mn-city">Nixa,</span>
                    <span class="mn-state">MO</span>
                    <span class="mn-zip">65714</span></div>
                </div>
            </div>
            <div class="mn-block mn-listing-website">
                <div class="mn-text"><a href="http://logicforte.com/about/our-office/">logicforte.com/about/our-office/</a></div>
            </div>
            <div class="mn-block mn-action">
                <a class="mn-button" href="//business.springfieldchamber.com/directory/Details/logic-forte-708107">Learn More</a>
            </div>
        </div>
    </div>
    """


def save_members_to_file(members, file):
    with open(file, 'w') as f:
        for member in members:

            member_name = member[0]
            member_phone = member[1]
            member_address = member[2]
            member_website = member[3]

            # Remove all pipes before writing to unescaped pipe-delimited CSV file
            member_name = member_name.replace("|", "")
            member_phone = member_phone.replace("|", "")
            member_address = member_address.replace("|", "")
            member_website = member_website.replace("|", "")

            f.write("%s|%s|%s|%s\n" % (member_name, member_phone, member_address, member_website))


def fetch_members():
    base_url = 'https://business.springfieldchamber.com/directory/FindStartsWith?term='
    pages = ('%23', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

    members = []
    for page in pages:
        url = base_url + page
        print("Parsing Member Page: " + url)
        page_addresses = parse_members_from_url(url)
        for page_address in page_addresses:
            members.append(page_address)

    return members


# Fetch all members (name, phone, address, url)
members = fetch_members()

# Save all members to a data file
file = 'members.dat'
save_members_to_file(members, file)

print("DONE")
