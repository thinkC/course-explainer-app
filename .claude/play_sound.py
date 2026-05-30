import os
import subprocess

sound_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sounds', 'notification.mp3')

try:
    # Convert Linux WSL path to Windows path (e.g. /home/user/... -> \\wsl$\Ubuntu\home\user\...)
    win_path = subprocess.check_output(['wslpath', '-w', sound_path], text=True).strip()

    ps_command = f'''
    Add-Type -AssemblyName presentationCore
    $mediaPlayer = New-Object System.Windows.Media.MediaPlayer
    $mediaPlayer.Open([uri]::new("{win_path}"))
    $mediaPlayer.Play()
    Start-Sleep -Milliseconds 5000
    $mediaPlayer.Close()
    '''

    subprocess.run(
        ['powershell.exe', '-WindowStyle', 'Hidden', '-Command', ps_command],
        timeout=7
    )
except Exception:
    pass
