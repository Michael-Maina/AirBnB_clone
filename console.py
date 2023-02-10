#!/usr/bin/python3
"""Entry point for the command interpreter """
import cmd
import re
import ast
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def type_parser(arg):
    """Check data type of arg and cast it"""
    if arg.isalpha():
        pass
    elif arg.isdigit():
        arg = int(arg)
    else:
        arg = float(arg)
    return arg


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB program"""

    prompt = '(hbnb) '

    __classes = {"BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"}

    def default(self, arg):
        """
        Parses different inputs and matches them to the corresponding methods
        """
        method_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "update": self.do_update,
            "destroy": self.do_destroy,
            "count": self.do_count
        }

        match = re.search(r"\.", arg)
        if match is not None:
            input_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            print("Input_list: {}".format(input_list))
            input_list[1] = re.sub('[",]+', '', input_list[1])
            match = re.search(r"\((.*?)\)", input_list[1])

            if match is not None:
                cmd_list = [input_list[1][:match.span()[0]],
                            match.group()[1:-1]]
                print("Cmd_list: {}".format(cmd_list))
                if cmd_list[0] in method_dict.keys():
                    arguments = input_list[0] + " " + cmd_list[1]
                    print("Arguments: {}".format(arguments))
                    return method_dict[cmd_list[0]](arguments)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_emptyline(self):
        """Executes nothing when no command is passed to the interpreter"""
        pass

    def do_EOF(self, arg):
        """EOF(end_of_file) command to exit the interpreter"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the interpreter"""
        return True

    def do_create(self, arg):
        """
        Creates a new instance of a class, saves it and prints the id
        """
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        else:
            if not line[0] in self.__classes:
                print("** class doesn't exist **")
            else:
                new_inst = eval(line[0])()
                new_inst.save()
                print("{}".format(new_inst.id))

    def help_create(self):
        """Help output for the create command"""
        print("Creates a new instance of a class, saves it and prints the id")
        print()
