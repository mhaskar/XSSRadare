echo "[+] Installing python requirments"
python2 -m pip install selenium termcolor pyvirtualdisplay
sudo apt-get install xvfb
echo "[+] Installing Geckpdriver"
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz 
mkdir /opt/geckodriver && tar zxvf geckodriver-v0.26.0-linux64.tar.gz -C /opt/geckodriver
echo "[+] Cleaning up .."
rm geckodriver-v0.26.0-linux64.tar.gz
