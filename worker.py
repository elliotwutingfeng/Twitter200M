import tldextract
from collections import Counter

# In Python 3.14+, multiprocessing.Pool workers cannot import functions
# defined in a Jupyter notebook (__main__), so this function must live
# in a separate .py module.


def count_email_providers(shard):
    c = Counter()
    for email_address in shard:
        c.update({tldextract.extract(email_address).fqdn: 1})
    return c
