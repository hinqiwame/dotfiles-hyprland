This subfolder contains a source and pre-compiled binary of my wallpaper creation tool called `methpaper`.

```bash
chmod +x methpaper && sudo cp methpaper /usr/local/bin
```

---

```sh
pyinstaller -F --onefile --clean --bootloader-ignore-signals methpaper.py
```
