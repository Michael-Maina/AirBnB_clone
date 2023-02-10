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


def dict_parser(arg):
    """
    Checks if argument passed to update method is a dictionary
    """
    ;


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
