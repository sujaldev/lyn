![Banner](https://user-images.githubusercontent.com/75830554/200155641-e8d936b2-5deb-427f-b6a3-c1621f381aae.png)

# Lyn

A programming language to create mathematical animations (but not limited to mathematics).

## HackCBS 5.0

This project was developed within less than 24 hours at a hackathon - our excuse for the garbage code (lies we tell
ourselves to go to sleep). Our team name was vormir:

- [Divyansh Kartik](https://github.com/DivKC)
- [Sujal Singh](https://github.com/sujaldev)
- [Surya Singh](https://github.com/Surya-sin)
- [Uday Sharma](https://github.com/usyntest)

Credits to Divyansh who made the banner visible on top of this readme and came up with this awesome name (Lyn and
Lynium) and also made one cool presentation present in this repository in the docs folder.

## Demo

<div align=center>
  <video src="https://github.com/sujaldev/lyn/assets/75830554/7fa48761-d513-4c40-a4f7-962e8a860354" width=500 autoplay>
</div>

Run `demo.py`.

## Run instructions

```bash
git clone https://github.com/sujaldev/lyn
cd lyn

# please refer to Skia and SDL2 documentation
# to get help specific to your platform
pip install -r requirements.txt  

cd src/
export PYTHONPATH='.' # or use absolute paths

cd parser
python parser.py
```
