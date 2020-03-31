# af-test
**Installation local** <br/>
pip install selenium <br/>
Installera Faker: pip install Faker <br/>
Put webdriver in PATH <br/>
<br/>
**Installation on Linux VM** <br/>
sudo apt-get update <br/>
sudo apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4 <br/>
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add <br/>
sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list <br/>
sudo apt-get -y update <br/>
sudo apt-get -y install google-chrome-stable <br/>
wget -N https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip -P ~/ <br/>
unzip ~/chromedriver_linux64.zip -d ~/ <br/>
rm ~/chromedriver_linux64.zip <br/>
sudo mv -f ~/chromedriver /usr/local/bin/chromedriver <br/>
sudo chown root:root /usr/local/bin/chromedriver <br/>
sudo chmod 0755 /usr/local/bin/chromedriver <br/>
pip install selenium <br/>
Put webdriver in PATH <br/>
