This subfolder contains a source and pre-compiled binary of my cryptocurrency price fetch tool called `crypto`.

```sh
chmod +x crypto && sudo cp crypto /usr/local/bin
```

---

```sh
pyinstaller -F --onefile --clean --bootloader-ignore-signals crypto.py 
```
