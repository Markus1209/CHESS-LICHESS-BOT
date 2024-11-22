"""Starting point for lichess-bot."""
from lib.lichess_bot import start_program
from keep_alive import keep_alive
keep_alive()
if __name__ == "__main__":
    start_program()
