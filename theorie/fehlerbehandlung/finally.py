try: 
    f = open("test.txt", "w")
    f.write("Hallo Welt!")
except Exception:
    pass
finally: 
    f.close()