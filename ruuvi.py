from ruuvitag import RuuviTag

while True:
    for tag in RuuviTag.scan():
        print(tag)
