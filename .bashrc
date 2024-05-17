#
# ~/.bashrc
#

# Let's fucking use my nvidia card, not Intel integrated one
export DRI_PRIME=1 # Swith to 0 render everything on Intel GPU for playing games like Dota 2 or Buckshot Roulette (vulkan-intel needs to be installed)

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# Created by `pipx` on 2024-04-13 13:54:25
export PATH="$PATH:/home/hinqiwame/.local/bin"
#export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nouveau_icd.json
#export VK_LAYER_PATH=/usr/share/vulkan/explicit_layer.d

# User space
(cat ~/.cache/wal/sequences &)
pfetch
