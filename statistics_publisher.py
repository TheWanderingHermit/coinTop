import curses

class statistics_publisher :
    def __init__( self ) :
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad( True )

        # kill the curses application
        # curses.nobreak()
        # curses.echo()
        # self.stdscr.keypad( False )
        # curses.endwin()
