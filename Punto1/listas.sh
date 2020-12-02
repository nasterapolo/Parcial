
Firewall-cmd --zone=public--change-interface=eth1 --permanent

firewall-cmd --zone=public --list-all
firewall-cmd --zone=dmz --list-all

firewall-cmd --zone=dmz --add-rich-rule 'rule family="ipv4" source address=192.168.0.37 accept' --permanent

firewall-cmd --zone="public" --add-forward-port=port=80:proto=tcp:toport=8080:toaddr=192.168.0.38 --permanent
firewall-cmd --zone=public--change-interface=eth1 --permanent

firewall-cmd --zone=public --add-interface=eth1 --permanent