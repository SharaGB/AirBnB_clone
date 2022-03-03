#!/usr/bin/python3
"""
Module to write a class HBNBCommand
"""
import cmd
from xxlimited import new
import models
from shlex import split as split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

new_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'Amenity': Amenity, 'Place': Place, 'City': City,
               'Review': Review}


class HBNBCommand(cmd.Cmd):
    """ Command interpreter. """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """ Exit the program."""
        return True

    def emptyline(self):
        """ Shouldn’t execute anything. """
        return cmd.Cmd.emptyline(self)

    def do_create(self, line):
        """ Create a new instance of BaseModel. """
        splitline = split(line)
        if not splitline:
            print("** class name missing **")
        elif splitline[0] not in new_classes:
            print("** class doesn't exist **")
        else:
            new_instance = new_classes[splitline[0]]()
        print(new_instance.id)
        new_instance.save()

    def do_show(self, line):
        """ Prints the string representation of an instance. """
        splitline = split(line)
        if not splitline:
            print("** class name missing **")
            return False
        elif splitline[0] not in new_classes:
            print("** class doesn't exist **")
        elif len(splitline) < 2:
            print("** instance id missing **")
        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[new_instance])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id. """
        splitline = split(line)
        if not splitline:
            print("** class name missing **")
            return False
        elif splitline[0] not in new_classes:
            print("** class doesn't exist **")
        elif len(splitline) < 2:
            print("** instance id missing **")
        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[new_instance]
                models.storage.save()

    def do_all(self, line):
        """ Print a representation of all instance based
        or not in the class name. """
        str_list = []
        if not line:
            for new_instance in models.storage.all().values():
                str_list.append(str(new_instance))
        else:
            splitline = split(line)
            if splitline[0] in new_classes:
                for key, value in models.storage.all().items():
                    if value.__class__.__name__ == splitline[0]:
                        str_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return False
        print(str_list)

    def do_update(self, line):
        """ Updates an instance based on the class name and id
                by adding or updating attribute. """
        splitline = split(line)
        if not splitline:
            print("** class name missing **")
        elif splitline[0] not in new_classes:
            print("** class doesn't exist **")
        elif len(splitline) < 2:
            print("** instance id missing **")
        elif len(splitline) < 3:
            print("** attribute name missing **")
        elif len(splitline) < 4:
            print("** value missing **")
        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print("** no instance found **")
            else:
                setattr(models.storage.all()[new_instance],
                        splitline[2], splitline[3])
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
