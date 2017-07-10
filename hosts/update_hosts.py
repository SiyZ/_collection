import os
from platform import uname


def main():
    basedir = os.path.abspath(os.path.dirname(__file__))

    (system_version, hostname, _, _, _, _) = uname()
    hosts_head = '''127.0.0.1   localhost
127.0.1.1   {hostname}

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters\n\n'''.format(hostname=hostname)
    if system_version.lower() == 'windows':
        host_path = os.path.join(os.environ.get('SYSTEMROOT'), 'System32', 'drivers', 'etc', 'hosts')
        hosts_head = ''
    else:
        host_path = os.path.join('/', 'etc', 'hosts')

    try:
        os.rename(host_path, '{}.bak'.format(host_path))
    except Exception as e:
        print(e)

    with open(os.path.join(basedir, 'hosts'), 'r') as fr:
        with open(host_path, 'w') as fw:
            fw.write(hosts_head)
            for line in fr:
                fw.write(line)

    if system_version.lower() == 'windows':
        os.system('IPCONFIG /FLUSHDNS')


if __name__ == '__main__':
    main()
