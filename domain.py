from urllib.parse import urlparse

# Get domain name(exampl.com)


def get_domain(url):
    try:
        results = get_sub_domain_name(url).split('.')
        print('entered domain is ', results)
        return results[-2] + '.' + results[-1]
    except:
        return ''


# For getting subdomain
def get_sub_domain_name(url):
    try:
        print(urlparse(url).netloc)
        return urlparse(url).netloc
    except:
        return ''
