


██████╗ ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
██╔══██╗██╔════╝████╗  ██║██║   ██║████╗ ████║
██║  ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
██║  ██║██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
██████╔╝███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝


A Simple Domain Enumeration Script


Denum is a simple tool using Python3 libraries to automate the searching of DNS records, whois records and reverse DNS records for a domain and its associated IP.

### Installation and Use 

To install and run Denum do the following:
`git clone https://github.com/nothing0x00/denum.git
cd denum
pip3 install -r requirements.txt
python3 denum.py -t [domain name]`

All searches need to use the root domain name for information gathering, rather than subdomains, and domain names are formatted without the protocol (http, https, etc). For example:

`python3 denum.py -t google.com`
