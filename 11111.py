from pathlib import Path

p = Path("D:/PYCHARM/100test")
print(p)
b = p / "a/b/c/s/d"
b.mkdir(parents=True, exist_ok=True)
b = b / "fishc"
f=b.open("w")
f.write("I LOVE FISH")
f.close()
c= p/"a/b/c/s/d/newfishc.txt"
b.rename(c)

# c.unlink()
#
# c.parent.rmdir()
p.glob(".txt")
print(list(p.glob("*.txt")))