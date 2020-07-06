import os
import time

pkgs = ["alacritty", "bat", "neofetch", "fzf", "cava", "nss", "mkcert", "bashtop", "neovim", "vim", "atom", "cmatrix", "brave-bin", "keepassxc"]
aurPkgs = ["hyper", "cool-retro-term-git", "spotify-tui", "scrcpy", "qrcp", "motrix", "spicetify-cli", "pipes.sh"]

print("Start of installation...")

pkgsCmd = "sudo pacman -S"
aurPkgsCmd = "yay -S"

time.sleep(1)

for repo in range(len(pkgs)):
    pkgsCmd += " " + str(pkgs[repo]) + " "

for aurRepo in range(len(aurPkgs)):
    aurPkgsCmd += " " + str(aurPkgs[aurRepo]) + " "
 
os.system(str(pkgsCmd))
os.system(str(aurPkgsCmd))