
# Lab 1. Знайомство з Ubuntu

Рекомендовані ресурси: https://vnav.mit.edu/labs/lab1/


## Task 1 

Встановіть убунту довільним чином (людям з встановленим лінуксом співчуваю): 
- [WSL (***найпростіший варіант***)](https://github.com/davendiy/sage-labs2025) --
встановлюєте на свій любімий віндовс лінуксове ядро і використовуєте його, як звичайну програму.

- [встановлення паралельно з Windows як dual boot](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/)
-- для тих, хто не боїться випадково знищити всі свої дані (обовʼязково робіть бекапи)

- [запуск у віртуальній машині](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview)
-- не для макбуків на M серії
- [підняття свого сервера на AWS (***оптимальний варіант***)](https://www.geeksforgeeks.org/devops/create-ubuntu-server-on-aws-ec2-instance/)
-- якраз побудете трошки в ролі DevOps (насправді там все просто, можете зробить свій VPN [сервер](https://www.youtube.com/watch?v=pwV2p-NReUg&t=685s) і відчувать себе хацкером)
- [прошивка звичайної разбері через SD карту](https://documentation.ubuntu.com/core/tutorials/try-pre-built-images/use-raspberry-pi-imager/index.html)
-- для людей з богатої сімʼї, в кого є лишні 3к гривень
- [прошивка raspberry pi CM4 на EMMC, використовуючи usbboot (***найкращий варіант***)](https://docs.kubesail.com/guides/pibox/rpiboot/)
-- для людей з богатої сімʼї, в кого є лишні 6к+ гривень, бо їх тупо нема 


Підключіться до інтернету та оновіть систему: 

```
sudo apt-get update 
sudo apt-get upgrade
```

Встановіть довільний текстовий редактор (або користуйтесь вбудованими `vim` або `nano`): 

[Neovim](https://neovim.io/):
```shell
sudo apt install neovim
```

[Helix](https://helix-editor.com/):
```shell
sudo add-apt-repository ppa:maveonair/helix-editor
sudo apt update
sudo apt install helix
```


Встановіть [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install)
або використовуйте [virtual environment](https://docs.python.org/3/library/venv.html): 

```shell
mkdir test_project && cd test_project 
python3 -m venv venv 
source venv/bin/activate
which pip
```



## Task 2

Створіть свій репозиторій на Github (інструкція для самих маленьких
[тут](https://github.com/davendiy/programming2023-course1/blob/main/materials/Github_pull_requests_230915_153422.pdf)).

Налаштуйте підключення з Ubuntu машини до Github (в кого вже налаштовано -- пропустіть.
Детальна інструкція [ось](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)):

- Cтворіть новий ssh ключ (воно запропонує обрати шлях для результуючого файлу і придумать пароль -- не забудьте його).
Має створитись публічний і приватний ключ. ***Приватний ключ (тобто без розширення .pub) не даємо нікому***.

```shell
ssh-keygen -t ed25519 -C "your_email@example.com"
```

- Запустіть ssh агент, щоб можна було приєднатись до Github. Вкажіть папку, куди зберегло результуючий файл з ключем

```shell
eval `ssh-agent -s `
ssh-add ~/.ssh/
```

- Додайте публічний ключ до свого акаунту
(інструкція [тут](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)).
Щоб скопіювати публічний ключ можна прочитати його вміст: 

```
cat ~/.ssh/github.pub
```


## Task 3

Склонуйте свій репозиторій і поставте необхідні пакети: 
```shell
git clone git@github.com:davendiy/vnav-knu2025.git
cd vnav-knu2025/ 
python3 -m venv venv
source venv/bin/activate
pip install numpy scipy pandas matplotlib pymavlink
```

Створіть файл `requirements.txt` і закомітьте його з наступним вмістом: 
```shell
pip freeze > requirements.txt
git add requirements.txt 
git commit -m 'added requirements'
```

Встановіть neofetch і закомітьте файл з виводом цієї програми: 
```
sudo apt install neofetch
neofetch > neofetch-output
```


Створіть shell скрипт (з розширенням .sh) і додайте в нього усі використані команди. Використовуйте обраний
термінальний редактор. Зробіть його виконувальним і перевірте чи відтворює він все завдання Task 3: 
```sh
touch task3.sh
vi task3.sh

# add some commands to it, then :q for exit 

chmod +x task3.sh
cd ..           # cd from your repo directory
mkdir tmp/      # test script in a temporary directory
cd tmp/
../<your-repo>/task3.sh    # run task.sh in the tmp/ directory 
```

Перенаправте вивід скрипта в файл `task3-output`.

Запуште скрипт `task3.sh` разом з файлами `requirements.txt`, `neofetch-output`, `task3-output` на свій гітхаб.

