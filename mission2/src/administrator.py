from src.member import Member

seg_string = """
Removed player
=============="""


class Administrator:
    def __init__(self):
        self.member_dict = {}
    
    def update(self, args):
        for member_name, day in args:
            if member_name not in self.member_dict:
                self.member_dict[member_name] = Member(member_name)
            self.member_dict[member_name].attend(day)
        for member in self.member_dict.values():
            member.update()

    def print_result(self):
        for member in self.member_dict.values():
            print(member)

        print(seg_string)

        for member in self.member_dict.values():
            if member.is_removable_member():
                print(member.name)