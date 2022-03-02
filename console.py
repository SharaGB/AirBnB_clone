#!/usr/bin/python3
"""
Module to write a class HBNBCommand
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter. """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """ Exit the program ."""
        return True

    def emptyline(self):
        """ Shouldn’t execute anything. """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
