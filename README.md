# aqua-monitor

Add Github permissions:
1. Create key: ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
2. See key: cat ~/.ssh/id_rsa.pub
3. Install copy utility: sudo apt install xclip
4. Copy to clipboard: xclip -sel clip < ~/.ssh/id_rsa.pub
5. Go to GitHub → Settings → SSH and GPG keys
6. Click New SSH Key, paste it in, and save.
7. Test connection: ssh -T git@github.com

==============================================


