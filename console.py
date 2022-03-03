#!/usr/bin/python3
"""
Module to write a class HBNBCommand
"""
import cmd
import models
from shlex import split as split
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Command interpreter. """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program. """
        return True

    def do_EOF(self, line):
        """ Exit the program ."""
        return True

    def emptyline(self):
        """ Shouldn’t execute anything. """
        return cmd.Cmd.emptyline(self)

    def do_create(self, line):
        """ Create a new instance of BaseModel. """
        if not line:
            print("** class name missing **")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, line):
        """ Prints the string representation of an instance. """
        splitline = split(line)
        if not splitline:
            print(" class name missing ")
        elif splitline[0] != 'BaseModel':
            print(" class doesn't exist ")
        elif len(splitline) < 2:
            print(" instance id missing ")
        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print(" no instance found ")
            else:
                print(models.storage.all()[new_instance])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id. """
        splitline = split(line)
        if not splitline:
            print(" class name missing ")
        elif splitline[0] != 'BaseModel':
            print(" class doesn't exist ")
        elif len(splitline) < 2:
            print(" instance id missing ")
        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print(" no instance found ")
            else:
                del models.storage.all()[new_instance]
                models.storage.save()

    def do_all(self, line):
        """ Print a representation of all instance based
        or not in the class name. """
        list = []
        list2 = []
        if not line or line == 'BaseModel':
            for key, value in models.storage.all().items():
                list.append(value.str())
            print(list)
            for item in list:
                list2.append(str(item))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
