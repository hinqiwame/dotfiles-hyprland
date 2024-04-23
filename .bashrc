# NOTE: this file is not so important and may change after new install, but THIS IS THE ONLY SOLUTION TO USE MY NVIDIA (NOUVEAU) GPU INSTEAD OF INTEL INTEGRATED
#
# ~/.bashrc
#

# Let's fucking use my nvidia card, not Intel integrated one
export DRI_PRIME=1 # MOST IMPORTANT LINE (FORCES THE WHOLE SYSTEM TO USE NVIDIA GPU)

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# Created by `pipx` on 2024-04-13 13:54:25
export PATH="$PATH:/home/hinqiwame/.local/bin"

# User space
(cat ~/.cache/wal/sequences &)
pfetch
