from dragonfly import Dictation, AppContext, Text, Key, IntegerRef, Function
from breathe import Breathe, CommandContext

from my_commands.core.gnome import notify

context = CommandContext("terminal")

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = context,
    mapping = {
        'git diff': Text('git diff'),
        'git status': Text('git diff'),
        'git commit minus a m <text>': Text('git commit -am "%(text)s"\n'),
        'git commit minus m <text>': Text('git commit -m "%(text)s"\n'),
        'git <text>': Function(lambda text: notify('unrecognized git command:', str(text))),
    },
    extras = [
        IntegerRef("n", 1, 20, default=1),
        Dictation("text", default=""),
    ]
)
